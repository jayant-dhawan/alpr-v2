REPLACE = { letter: str(index) for index, letter in enumerate('oizeasgtb') }

def alphaToLeet(word: str):
    letters = [ REPLACE.get(l, l) for l in word.lower() ]
    return ''.join(letters).upper()

def fixPlateNumber(plate: str):
    plate = plate.strip()
    plate = ''.join(e for e in plate if e.isalnum())
    if (len(plate) >= 10):
        return plate[0: 2] + alphaToLeet(plate[2: 4]) + plate[4:-4] + alphaToLeet(plate[-4:])
    if (len(plate) == 9):
        return plate[0: 2] + alphaToLeet(plate[2: 3]) + plate[3:-4] + alphaToLeet(plate[-4:])
    else: return plate