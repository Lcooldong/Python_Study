import threading
import time
def run(n):
    for i in range(10):
        time.sleep(0.1)
    print(f'[{n} done]')

players = ['one', 'two', 'three']

for player in players:
    threading.Thread(target=run, args=(player, )).start()