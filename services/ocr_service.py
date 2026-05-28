import easyocr
import re


class OCRService:

    def __init__(self):

        print("Inicializando EasyOCR...")
        self.reader = easyocr.Reader(
            ['es'],
            gpu=False
        )

    def read_text(self, processed_image):

        results = self.reader.readtext(
            processed_image,

            detail=1,
            paragraph=False,

            # Más precisión
            decoder='beamsearch',
            beamWidth=10,

            # Umbrales de detección
            text_threshold=0.7,
            low_text=0.4,
            link_threshold=0.4,

            # Solo caracteres válidos para placas
            allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        )

        detected_text = ""

        for detection in results:

            text = detection[1]

            detected_text += text + " "

        return detected_text.strip()

    def clean_plate_text(self, text):
        # eliminar espacios
        text = text.replace(" ", "")
        # mayúsculas
        text = text.upper()
        # solo letras y números
        text = re.sub(r'[^A-Z0-9]', '', text)
        return text
    
    def validate_plate(self, text):

        text = self.clean_plate_text(text)

        patterns = [
            # NNN123 - vehículo particular
            (r'.*?([A-Z]{3}[0-9]{3})(.*)$', "CARRO"),

            # AA1234 - diplomático
            (r'.*?([A-Z]{2}[0-9]{4})(.*)$', "CARRO DIPLOMATICO"),

            # R12345 - remolque
            (r'.*?(R[0-9]{5})(.*)$', "REMOLQUE / SEMIREMOLQUE"),

            # T1234 - carga especial
            (r'.*?(T[0-9]{4})(.*)$', "CARGA ESPECIAL"),

            # AAA12A - moto
            (r'.*?([A-Z]{3}[0-9]{2}[A-Z])(.*)$', "MOTOCICLETA"),

            # 344AAA - motocarguero
            (r'.*?([0-9]{3}[A-Z]{3})(.*)$', "MOTOCARGUERO"),
        ]

        for pattern, plate_type in patterns:

            match = re.match(pattern, text)

            if match:

                plate = match.group(1)

                # lo restante después de la placa
                origin = match.group(2).strip()

                # limpiar basura típica OCR
                origin = re.sub(r'[^A-Z\s]', '', origin)
                origin = origin.strip()

                if origin == "":
                    origin = "COLOMBIA"

                return (
                    "\nPLACA:" + plate +
                    "\nORIGEN:" + origin +
                    "\nTIPO DE PLACA:" + plate_type
                )

        return (
            "\nPLACA:" + text +
            "\nORIGEN: COLOMBIA" +
            "\nTIPO DE PLACA :Desconocido"
        )