import cv2
import numpy as np
def viewImage(image):
    cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
    cv2.imshow('Display', image)
    cv2.destroyAllWindows()


green = np.uint8([[[0, 255, 0]]])
green_hsv = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print(green_hsv)
cam = cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FPS, 60) # Частота кадров
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 600) # Ширина кадров в видеопотоке.
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # Высота кадров в видеопотоке.
while True:
    ret, image = cam.read()
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    green_low = np.array([45, 100, 50])
    green_high = np.array([75, 255, 255])
    curr_mask = cv2.inRange(hsv_img, green_low, green_high)
    hsv_img[curr_mask > 0] = ([75, 255, 200])
    ## converting the HSV image to Gray inorder to be able to apply
    ## contouring
    RGB_again = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)
    gray = cv2.cvtColor(RGB_again, cv2.COLOR_RGB2GRAY)
    ret, threshold = cv2.threshold(gray, 90, 255, 0)
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0, 0, 255), 3)
    #viewImage(image)
    cv2.imshow("camera", image)
    if cv2.waitKey(10) == 27: # Клавиша Esc
        break
cam.release()
cv2.destroyAllWindows()
