import pandas as pd
from rapidfuzz.distance import Levenshtein


class MunicipioMatcher:

    def __init__(self):

        # Leer CSV con coordenadas
        self.df = pd.read_csv(
            r"data\municipios_colombia_coords.csv",
            encoding="utf-8-sig"
        )

        # Lista normalizada
        self.municipios = []

        for _, row in self.df.iterrows():

            ciudad = str(row["CIUDAD"]).strip()
            departamento = str(row["DEPARTAMENTO"]).strip()

            lat = row["LAT"]
            lng = row["LNG"]

            self.municipios.append({

                # Original
                "ciudad_original": ciudad,
                "departamento": departamento,

                # Coordenadas
                "lat": lat,
                "lng": lng,

                # Normalizado
                "ciudad": ciudad.upper()
            })


    def buscar(self, texto, tolerancia=0.30):

        """
        Busca el municipio más parecido
        usando distancia Levenshtein.

        tolerancia=0.30
        permite hasta 30% de error.
        """

        texto = texto.upper().strip()

        mejor_match = None
        mejor_score = 999999

        for municipio in self.municipios:

            ciudad = municipio["ciudad"]

            # Distancia Levenshtein
            distancia = Levenshtein.distance(
                texto,
                ciudad
            )

            # Error relativo
            error = distancia / max(
                len(texto),
                len(ciudad)
            )

            # Mejor coincidencia
            if error < mejor_score:

                mejor_score = error
                mejor_match = municipio

        # Coincidencia válida
        if mejor_score <= tolerancia:

            resultado = pd.DataFrame([{

                "CIUDAD":
                    mejor_match["ciudad_original"],

                "DEPARTAMENTO":
                    mejor_match["departamento"],

                "LAT": 
                    mejor_match["lat"], 

                "LNG": 
                    mejor_match["lng"]
            }])
            return resultado

        return  pd.DataFrame([{

            "CIUDAD": "COLOMBIA",
            "DEPARTAMENTO": " ",
            "LAT": 4.5709,
            "LNG": -74.2973
        }])

