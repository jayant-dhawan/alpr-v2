import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/app/.apt/usr/bin/tesseract'

def readLicensePlate(img):
    return pytesseract.image_to_string(img, lang='eng', config='tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ -psm 7')