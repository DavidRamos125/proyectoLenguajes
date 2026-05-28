import cv2
import numpy as np

from sklearn.cluster import KMeans


class ColorService:
    
    def rgb_to_name(self, r, g, b):

        rgb = np.uint8([[[r, g, b]]])

        hsv = cv2.cvtColor(
            rgb,
            cv2.COLOR_RGB2HSV
        )

        h, s, v = hsv[0][0]

        # Negro
        if v < 50:
            return "Negro"

        # Blanco
        if s < 40 and v > 200:
            return "Blanco"

        # Amarillo
        if 20 <= h <= 35:
            return "Amarillo"

        # Verde
        if 36 <= h <= 85:
            return "Verde"

        # Azul
        if 90 <= h <= 130:
            return "Azul"

        # Rojo
        if h <= 10 or h >= 170:
            return "Rojo"

        return "Desconocido"

    def detect_dominant_colors(
        self,
        image,
        k=2
    ):

        # convertir BGR → RGB
        image = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2RGB
        )

        pixels = image.reshape((-1, 3))

        kmeans = KMeans(
            n_clusters=k,
            random_state=42,
            n_init='auto'
        )

        kmeans.fit(pixels)

        colors = kmeans.cluster_centers_

        labels = kmeans.labels_

        counts = np.bincount(labels)

        total = np.sum(counts)

        sorted_indices = np.argsort(counts)[::-1]

        result = []

        for idx in sorted_indices:

            color = colors[idx]

            r, g, b = color

            color_name = self.rgb_to_name(r, g, b)

            percent = (counts[idx] / total) * 100

            result.append({
                "color": color_name,
                "percent": round(percent, 2)
            })

        return result
    def detect_type(self, colors):

        if not colors:
            return "DESCONOCIDO"

        first = colors[0]

        second = colors[1] if len(colors) > 1 else None

        first_color = first["color"]
        first_percent = first["percent"]

        second_color = second["color"] if second else None
        second_percent = second["percent"] if second else 0

        # ANTIGUOS Y CLASICOS
        # ambos colores similares
        if (
            (
                (first_color == "Blanco" and second_color == "Azul") or
                (first_color == "Azul" and second_color == "Blanco")
            )
            and abs(first_percent - second_percent) < 36
        ):
            return "ANTIGUOS Y CLASICOS"

        # PARTICULAR
        if first_color == "Amarillo":
            return "PARTICULAR"

        # SERVICIO PUBLICO
        if first_color == "Blanco":
            return "SERVICIO PUBLICO"

        # DIPLOMATICOS
        if first_color == "Azul":
            return "DIPLOMATICOS, CONSULARES Y DE MISIONES ESPECIALES"

        # REMOLQUE
        if first_color == "Verde":
            return "REMOLQUE O SEMIRREMOLQUE"

        # CARGA ESPECIAL
        if first_color == "Rojo":
            return "CARGA ESPECIAL"

        return "DESCONOCIDO"