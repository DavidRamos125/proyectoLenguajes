import cv2


class GrayScale:

    def to_grayscale(self, image):

    # Convertir a escala de grises
        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )
        return gray