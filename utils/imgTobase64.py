import cv2
import base64
import numpy as np


def toBase64(image):
    _, buffer = cv2.imencode(
        '.jpg',
        image
    )
    jpg_as_text = base64.b64encode(
        buffer
    ).decode('utf-8')
    return (
        f"data:image/jpeg;base64,{jpg_as_text}"
    )

def toImg(base64_string):

    # separar metadata del contenido
    header, encoded = base64_string.split(",")

    # decodificar base64
    image_data = base64.b64decode(encoded)

    # convertir a numpy array
    np_array = np.frombuffer(image_data, np.uint8)

    # convertir a imagen OpenCV
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

    return image