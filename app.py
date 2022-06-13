import cv2
import numpy as np


def save_image(img):
    pass


cap = cv2.VideoCapture(0)

while True:
    key = cv2.waitKey(1)

    if cap.isOpened():
        ret, img = cap.read()

    cv2.imshow("window", img)

    if key & 0xFF == ord('q'):
        break

    # kesilecek alan seçildikten sonra s tuşuna basılınca seçilen kısmı kaydedip kamerayı tekrar açıyoruz.
    if key == ord('s'):
        save_image(img)
        cap = cv2.VideoCapture(0)

    # c tuşuna basılınca yeni frame gelmesini önlemek için kamerayı kapatıyoruz.
    if key == ord('c'):
        cap.release()

cap.release()
cv2.destroyAllWindows()
