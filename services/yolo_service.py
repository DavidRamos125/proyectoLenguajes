from ultralytics import YOLO

class YoloService:

    _instance = None
    _model = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(YoloService, cls).__new__(cls)
            print("Cargando modelo YOLO...")
            cls._model = YOLO("services/model.pt")

        return cls._instance

    @property
    def model(self):
        return self._model

    def detect(self, image):

        return self.model(image)