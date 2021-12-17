import pytesseract
from app.core.config import settings

pytesseract.pytesseract.tesseract_cmd = settings.TESSERACT_PATH

def readLicensePlate(img):
    return pytesseract.image_to_string(img, lang='eng', config='-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 7 --oem 3')