import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


# =========================
# CARGAR CSV
# =========================

df = pd.read_csv(
    "municipios_colombia.csv",
    encoding="utf-8-sig"
)


# =========================
# CONFIGURAR GEOCODER
# =========================

geolocator = Nominatim(
    user_agent="dash_leaflet_colombia"
)

geocode = RateLimiter(
    geolocator.geocode,
    min_delay_seconds=1
)


# =========================
# LISTAS DE COORDENADAS
# =========================

latitudes = []
longitudes = []


# =========================
# BUSCAR COORDENADAS
# =========================

for _, row in df.iterrows():

    ciudad = str(row["CIUDAD"]).strip()
    departamento = str(row["DEPARTAMENTO"]).strip()

    query = f"{ciudad}, {departamento}, Colombia"

    print(f"Buscando: {query}")

    try:

        location = geocode(query)

        if location:

            latitudes.append(location.latitude)
            longitudes.append(location.longitude)

            print(
                f"OK -> {location.latitude}, {location.longitude}"
            )

        else:

            latitudes.append(None)
            longitudes.append(None)

            print("No encontrado")

    except Exception as e:

        latitudes.append(None)
        longitudes.append(None)

        print(e)


# =========================
# AÑADIR COLUMNAS
# =========================

df["LAT"] = latitudes
df["LNG"] = longitudes


# =========================
# GUARDAR CSV
# =========================

df.to_csv(
    "municipios_colombia_coords.csv",
    index=False,
    encoding="utf-8-sig"
)


print("\nCSV generado correctamente")
