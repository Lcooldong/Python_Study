# from PIL import image 아직 사용 x
import pytesseract
import cv2


def ocr_tesseract():
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    img = cv2.imread('images/text.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # text = pytesseract.image_to_string(img)


    # all letters   전체 다
    # x, y, width, height   (좌측 하단이 0,0 )

    # hImg, wImg, _ = img.shape
    # boxes = pytesseract.image_to_boxes(img)
    # for b in boxes.splitlines():
    #     # print(b)
    #     b = b.split(' ')    # 리스트로 만들기
    #     print(b)
    #     x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    #     cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (0, 0, 255), 2)
    #     cv2.putText(img, b[0], (x, hImg-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)


    # Words     단어

    # hImg, wImg,_ = img.shape
    # datas = pytesseract.image_to_data(img)
    # for x, d in enumerate(datas.splitlines()):
    #     if x != 0:
    #         d = d.split()    # 리스트로 만들기
    #         print(d)
    #         if len(d) == 12:
    #             x, y, w, h = int(d[6]), int(d[7]), int(d[8]), int(d[9])
    #             cv2.rectangle(img, (x, y), (w+x, h+y), (0, 255, 0), 2)
    #             cv2.putText(img, d[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 255, 50), 2)

    # digits    숫자들

    # hImg, wImg, _ = img.shape
    # cong = r'--oem 3 --psm 6 outputbase digits'
    # datas = pytesseract.image_to_data(img, config=cong)
    # for x, d in enumerate(datas.splitlines()):
    #     if x != 0:
    #         d = d.split()  # 리스트로 만들기
    #         print(d)
    #         if len(d) == 12:
    #             x, y, w, h = int(d[6]), int(d[7]), int(d[8]), int(d[9])
    #             cv2.rectangle(img, (x, y), (w + x, h + y), (255, 0, 0), 2)
    #             cv2.putText(img, d[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 50, 50), 2)


    # each digits   숫자 각각

    # hImg, wImg,_ = img.shape
    # cong = r'--oem 3 --psm 6 outputbase digits'
    # boxes = pytesseract.image_to_boxes(img, config=cong)
    # for b in boxes.splitlines():
    #     # print(b)
    #     b = b.split(' ')    # 리스트로 만들기
    #     print(b)
    #     x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    #     cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (0, 0, 255), 2)
    #     cv2.putText(img, b[0], (x, hImg-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)


    # digits    문자만 ???

    # hImg, wImg, _ = img.shape
    # cong = r'--oem 3 --psm 6 outputbase digits'
    # datas = pytesseract.image_to_data(img, config=cong)
    # for x, d in enumerate(datas.splitlines()):
    #     if x != 0:
    #         d = d.split()  # 리스트로 만들기
    #         print(d)
    #         if len(d) == 12:
    #             x, y, w, h = int(d[6]), int(d[7]), int(d[8]), int(d[9])
    #             cv2.rectangle(img, (x, y), (w + x, h + y), (255, 0, 0), 2)
    #             cv2.putText(img, d[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 50, 50), 2)


    # print(text)
    cv2.imshow('Result', img)
    cv2.waitKey(0)