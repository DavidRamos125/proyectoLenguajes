import pandas as pd
import re


with open(
    "data.txt",
    "r",
    encoding="utf-8"
) as f:

    lines = f.readlines()


data = []


for line in lines:

    line = line.strip()

    # Ignorar basura
    if (
        not line or
        "©Concesión" in line or
        "ORGANISMOS DE TRÁNSITO" in line or
        "SWA_MT002" in line or
        "DIVIPO" in line
    ):
        continue

    try:

        # Buscar estado
        estado_match = re.search(
            r"(ACTIVO|INACTIVO)$",
            line
        )

        if not estado_match:
            continue

        estado = estado_match.group(1)

        # Quitar estado
        line = line[:estado_match.start()].strip()

        # Buscar departamento
        dept_match = re.search(
            r"([A-Z][a-z]+(?:\s(?:del|de|y)\s[A-Z][a-z]+)*(?:\s[A-Z][a-z]+)*)$",
            line
        )

        if not dept_match:
            continue

        departamento = dept_match.group(1)

        # Quitar departamento
        line = line[:dept_match.start()].strip()

        # Separar tokens
        tokens = line.split()

        divipo = tokens[0]

        # Detectar NIT opcional
        nit = ""

        if len(tokens) > 1 and re.match(r"^\d+$", tokens[1]):
            nit = tokens[1]
            tokens = tokens[2:]
        else:
            tokens = tokens[1:]

        # Buscar categoría
        categoria_index = None

        for i, token in enumerate(tokens):

            if token in ["A", "B"]:
                categoria_index = i
                break

        if categoria_index is None:
            continue

        categoria = tokens[categoria_index]

        # Ciudad = todo después de categoría
        ciudad = " ".join(tokens[categoria_index + 1:])

        # Organismo = todo antes de categoría
        organismo = " ".join(tokens[:categoria_index])

        data.append({

            "DIVIPO": divipo,
            "NIT": nit,
            "ORGANISMO": organismo,
            "CATEGORIA": categoria,
            "CIUDAD": ciudad,
            "DEPARTAMENTO": departamento,
            "ESTADO": estado
        })

    except Exception as e:

        print("Error procesando línea:")
        print(line)
        print(e)
        print("-" * 50)


# Crear DataFrame
df = pd.DataFrame(data)


# Guardar CSV
df.to_csv(
    "organismos_transito.csv",
    index=False,
    encoding="utf-8-sig"
)

print(df.head())

print("\nCSV generado correctamente.")
