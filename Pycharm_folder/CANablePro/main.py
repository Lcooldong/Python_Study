import serial
import time
import threading
import queue


class SerialHandler:
    def __init__(self, port, baudrate=115200, timeout=1, parity='N', eol=b'\n'):
        self.port = port
        self.baud_rate = baudrate
        self.timeout = timeout
        self.parity = parity
        self.eol = eol  # 줄 끝 terminator (bytes). 장치가 '\r'만 쓰면 b'\r'로 설정.
        self.serial = None

        # 큐 생성
        self.write_queue = queue.Queue()
        self.read_queue = queue.Queue()

        # 스레드 관련
        self.read_thread = None
        self.write_thread = None
        self.monitor_thread = None
        self.running = False
        self.monitor_running = False

        self.num = 0
        self._lock = threading.Lock()

    def connect(self):
        """Serial 포트 열기 (성공하면 True 반환)"""
        try:
            self.serial = serial.Serial(
                port=self.port,
                baudrate=self.baud_rate,
                timeout=self.timeout,
                parity=self.parity,
                stopbits=1,
                bytesize=8
            )
            # 연결되면 버퍼 비움
            try:
                self.serial.reset_input_buffer()
            except Exception:
                pass
            print(f"[INFO] Connected to {self.port} at {self.baud_rate} baud")
            return True
        except serial.SerialException as e:
            print(f"[ERROR] Serial connection failed: {e}")
            self.serial = None
            return False

    def disconnect(self):
        """Serial 포트 닫기"""
        try:
            if self.serial and self.serial.is_open:
                self.serial.close()
                print("[INFO] Serial port closed")
        except Exception as e:
            print("[ERROR] disconnect error:", e)
        finally:
            self.serial = None

    def read_loop(self):
        """수신 스레드"""
        while self.running:
            if self.serial and self.serial.is_open:
                try:
                    raw = self.serial.read_until(b"\r")
                    if raw.endswith(b"\r"):
                        raw = raw[:-1]
                    msg = raw.decode('utf-8', errors="ignore")
                    if msg:
                        self.read_queue.put(msg)
                except Exception as e:
                    print(f"[ERROR] Read error: {e}")
            time.sleep(0.01)

    def write_loop(self):
        """송신 스레드"""
        while self.running:
            try:
                msg = self.write_queue.get(timeout=0.1)  # 큐에서 꺼내오기
                if not self.running:
                    break
                if self.serial and self.serial.is_open:
                    with self._lock:
                        if isinstance(msg, str):
                            out = msg.encode()
                        else:
                            out = msg
                        try:
                            self.serial.write(out)
                            # flush 가능하면 flush
                            try:
                                self.serial.flush()
                            except Exception:
                                pass
                            print(f"[TX] {out!r}")
                        except Exception as e:
                            print(f"[ERROR] Serial write failed: {e}")
                else:
                    print("[WARN] Write requested but serial not open. Dropping or requeueing.")
                    # 필요 시 재큐하거나 드롭. 여기선 드롭.
            except queue.Empty:
                continue
            except Exception as e:
                print(f"[ERROR] Write loop exception: {e}")
                time.sleep(0.1)

    def monitor_loop(self):
        """1초마다 연결 상태 확인 및(선택) 재연결 시도"""
        while self.monitor_running:
            self.num += 1
            connected = bool(self.serial and self.serial.is_open)
            if connected:
                print(f"[{self.num}][MONITOR] {self.port} connected")
            else:
                print(f"[{self.num}][MONITOR] {self.port} disconnected - trying to reconnect...")
                # 자동 재연결 시도 (간단히 한 번 시도)
                try:
                    self.connect()
                except Exception:
                    pass
            time.sleep(1)

    def start_monitor(self):
        if not self.monitor_running:
            self.monitor_running = True
            self.monitor_thread = threading.Thread(target=self.monitor_loop, daemon=True)
            self.monitor_thread.start()
            print("[INFO] Monitor started")

    def stop_monitor(self):
        if self.monitor_running:
            self.monitor_running = False
            if self.monitor_thread:
                self.monitor_thread.join()
            print("[INFO] Monitor stopped")

    def begin(self):
        """스레드 시작"""
        if not self.running:
            # 최초 연결 시도
            self.connect()
            self.running = True
            # 읽기, 쓰기 스레드 시작
            self.read_thread = threading.Thread(target=self.read_loop, daemon=True, name="SerialRead")
            self.write_thread = threading.Thread(target=self.write_loop, daemon=True, name="SerialWrite")
            self.read_thread.start()
            self.write_thread.start()
            print("[INFO] Serial threads started")

    def stop(self):
        """스레드 종료"""
        if self.running:
            self.running = False
            # join with timeout to avoid blocking forever
            if self.read_thread:
                self.read_thread.join(timeout=1.0)
            if self.write_thread:
                self.write_thread.join(timeout=1.0)
            if self.monitor_thread:
                self.monitor_thread.join(timeout=1.0)
            self.disconnect()
            print("[INFO] Serial threads stopped")

    def restart(self):
        """스레드 재시작"""
        print("[INFO] Restarting serial threads...")
        self.stop()
        time.sleep(0.5)
        self.begin()

    def write(self, data):
        """쓰기 요청 (비동기, 큐에 저장) - str 또는 bytes 허용"""
        self.write_queue.put(data)

    def get_received(self):
        """수신 데이터 가져오기 (non-blocking)"""
        try:
            return self.read_queue.get_nowait()
        except queue.Empty:
            return None

    def get_latest_received(self):
        """큐에 쌓인 데이터 중 가장 마지막 데이터만 반환 (없으면 None)"""
        latest = None
        while True:
            try:
                latest = self.read_queue.get_nowait()
            except queue.Empty:
                break
        return latest


class CanablePro:
    def __init__(self, handler):
        self.handler = handler

    def start(self):
        self.handler.write("S6\r")
        self.handler.write("Y2\r")
        self.handler.write("O\r")
        print("[CANablePro] CAN started")

    def reconnect(self):
        print("[CANablePro] Reconnecting...")
        self.handler.restart()
        time.sleep(0.5)
        self.start()

    def send_can_message(self, can_id, data):
        frame = f"T{can_id}{len(data)}{data}\r"
        self.handler.write(frame)
        print(f"[CANablePro] Sent: {frame.strip()}")

    def read(self):
        msg = self.handler.get_received()
        if msg:
            print("[CAN RX]", msg)
        return msg

    def read_latest(self):
        msg = self.handler.get_latest_received()
        if msg:
            print("[CAN RX - LATEST]", msg)
        return msg


if __name__ == "__main__":
    print("Start UART Program")

    # 만약 장치가 '\r'만 보낸다면 eol=b'\r'로 설정
    Serial = SerialHandler("COM3", 115200, timeout=1, parity='N', eol=b'\n')
    Serial.begin()

    can = CanablePro(Serial)
    # 장치 초기 명령은 포트가 열리고 안정화된 후에 보내는게 좋음
    time.sleep(0.2)
    can.start()

    time.sleep(1)

    print("=== CAN Terminal ===")
    print("Commands:")
    print("  can start")
    print("  can read")
    print("  can write <id> <msg>")
    print("  can reconnect")
    print("  monitor on/off")
    print("  quit")

    try:
        while True:
            cmd = input("Command > ").strip()
            if cmd == "can start":
                can.start()
            elif cmd == "can read":
                data = can.read()
                if not data:
                    print("No data in buffer")
            elif cmd == "can read latest":
                data = can.read_latest()
                if not data:
                    print("No data in buffer")
            elif cmd.startswith("can write"):
                parts = cmd.split()
                if len(parts) >= 3:
                    can_id = parts[2]
                    msg = "".join(parts[3:]) if len(parts) > 3 else ""
                    can.send_can_message(can_id, msg)
                else:
                    print("Usage: can write <id> <msg>")
            elif cmd == "can reconnect":
                can.reconnect()
            elif cmd == "monitor on":
                Serial.start_monitor()
            elif cmd == "monitor off":
                Serial.stop_monitor()
            elif cmd == "quit":
                break
            else:
                print("Unknown command")

    except KeyboardInterrupt:
        pass
    finally:
        Serial.stop()
