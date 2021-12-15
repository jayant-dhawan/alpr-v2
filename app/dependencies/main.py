import cv2
from app.dependencies.detectPlate import extract_plate
from app.dependencies.readLicensePlate import readLicensePlate
from app.dependencies.fixPlate import convertToBinary


def readPlate(img) -> str:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, plate = extract_plate(gray)
    if (plate.any()):
        fixed_plate = convertToBinary(plate)
        plateNo = readLicensePlate(fixed_plate)

        return ''.join(e for e in plateNo if e.isalnum())
    else:
        return ''
