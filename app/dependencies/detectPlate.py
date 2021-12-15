import cv2

def extract_plate(img):
    plate_img = img.copy()
    
    plate_cascade = cv2.CascadeClassifier('./app/dependencies/indian_license_plate.xml')

    plate_rect = plate_cascade.detectMultiScale(plate_img, scaleFactor = 1.21, minNeighbors = 7)

    if(not any(map(len, plate_rect))): return [], []

    for (x,y,w,h) in plate_rect:
        # a,b = (int(0.02*img.shape[0]), int(0.025*img.shape[1]))
        # plate = plate_img[y+a:y+h-a, x+b:x+w-b, :]
        plate = plate_img[y:y+h, x:x+w]
        cv2.rectangle(plate_img, (x,y), (x+w, y+h), (51,51,255), 3)
    
    return plate_img, plate
