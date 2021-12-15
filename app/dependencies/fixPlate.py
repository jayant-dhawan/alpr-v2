import cv2

def convertToBinary(img):
    image = cv2.resize(img, (333, 75))
    # img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, img_binary = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    img_erode = cv2.erode(img_binary, (3,3))
    img_dilate = cv2.dilate(img_erode, (3,3), iterations=1)

    return img_dilate