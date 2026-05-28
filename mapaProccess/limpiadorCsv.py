import pandas as pd


# Leer CSV original
df = pd.read_csv(
    "organismos_transito.csv",
    encoding="utf-8-sig"
)


# Seleccionar solo ciudad y departamento
df_filtrado = df[[
    "CIUDAD",
    "DEPARTAMENTO"
]].copy()


# Limpiar espacios
df_filtrado["CIUDAD"] = (
    df_filtrado["CIUDAD"]
    .astype(str)
    .str.strip()
)

df_filtrado["DEPARTAMENTO"] = (
    df_filtrado["DEPARTAMENTO"]
    .astype(str)
    .str.strip()
)


# Eliminar filas vacías
df_filtrado = df_filtrado[
    (df_filtrado["CIUDAD"] != "") &
    (df_filtrado["DEPARTAMENTO"] != "")
]


# Eliminar duplicados
df_filtrado = df_filtrado.drop_duplicates()


# Ordenar alfabéticamente
df_filtrado = df_filtrado.sort_values(
    by=["DEPARTAMENTO", "CIUDAD"]
)


# Reiniciar índices
df_filtrado = df_filtrado.reset_index(drop=True)


# Guardar CSV final
df_filtrado.to_csv(
    "municipios_colombia.csv",
    index=False,
    encoding="utf-8-sig"
)


print(df_filtrado.head(20))

print("\nCSV filtrado generado correctamente.")

