from __future__ import annotations
from PIL import Image
from io import BytesIO
import numpy as np

from app.dependencies.main import readPlate

def load_image_into_numpy_array(data):
    return np.array(Image.open(BytesIO(data)))

def readPlateNumber(img) -> str:
    image = load_image_into_numpy_array(img)
    return readPlate(image)
