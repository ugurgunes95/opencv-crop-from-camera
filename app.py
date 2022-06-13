import cv2
import numpy as np

points = []


def cizgi(event, x, y, flag, params):
    global isClicked
    global points

    if event == cv2.EVENT_LBUTTONDOWN:
        isClicked = True
        points.append((x, y))
    if event == cv2.EVENT_LBUTTONUP:
        isClicked = False

    if len(points) > 1 and isClicked:
        pt1 = (points[-2][0], points[-2][1])
        pt2 = (points[-1][0], points[-1][1])

        cv2.line(img, pt1, pt2, (0, 0, 255), 2)


def save_image(img):

    mask = np.zeros(img.shape, dtype=np.uint8)

    roi_corners = np.array(points)

    channel_count = img.shape[2]

    ignore_mask_color = (255,)*channel_count
    cv2.fillPoly(mask, np.array(
        [roi_corners], dtype=np.int32), ignore_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    cv2.imwrite('kirpilan.png', masked_image)


cv2.namedWindow('window')
cv2.setMouseCallback("window", cizgi)

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
