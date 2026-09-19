from fastapi import FastAPI, HTTPException
import pandas as pd

# Creamos la aplicacion de FastAPI. El titulo aparece en /docs
app = FastAPI(title="Mi analisis como API")

# El dataset se carga UNA sola vez al arrancar el servidor, no en cada peticion.
# Esto es importante: si lo cargaramos dentro de cada funcion, seria muy lento,
# porque leeria el CSV completo cada vez que alguien llama a un endpoint.
#
# Dataset: tips.csv (propinas de un restaurante), cargado directo desde GitHub:
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

@app.get("/resumen")
def resumen():
    """Devuelve numero de filas, columnas y tipo de dato de cada columna (como df.info() pero en JSON)."""
    return {
        "filas": len(df),
        "columnas": list(df.columns),
        # dtypes normalmente no es serializable a JSON directamente,
        # por eso lo convertimos primero a texto con .astype(str)
        "tipos": df.dtypes.astype(str).to_dict()
    }


@app.get("/estadisticas/{columna}")
def estadisticas(columna: str):
    """Devuelve media, mediana, minimo, maximo y desviacion estandar de una columna numerica."""
    # si la columna no existe en el dataframe, respondemos con error 404
    if columna not in df.columns:
        raise HTTPException(status_code=404, detail=f"La columna '{columna}' no existe")

    s = df[columna]

    # si la columna existe pero no es numerica (ej. "sex", "day"), tambien avisamos
    # porque mean(), median(), etc. no tienen sentido sobre texto
    if not pd.api.types.is_numeric_dtype(s):
        raise HTTPException(status_code=400, detail=f"La columna '{columna}' no es numérica")

    return {
        "media": s.mean(),
        "mediana": s.median(),
        "min": s.min(),
        "max": s.max(),
        "std": s.std()
    }


@app.get("/filtrar")
def filtrar(columna: str, valor: str, n: int = 10):
    """Devuelve las primeras n filas cuyo valor en 'columna' sea igual a 'valor'."""
    # primero validamos que la columna exista, igual que en /estadisticas
    if columna not in df.columns:
        raise HTTPException(status_code=404, detail=f"La columna '{columna}' no existe")

    # filtramos el dataframe: dejamos solo las filas donde esa columna
    # (convertida a texto con astype(str), porque "valor" siempre llega como string
    # desde la URL) sea igual al valor pedido
    filtrado = df[df[columna].astype(str) == valor]

    # tomamos solo las primeras n filas del resultado filtrado
    resultado = filtrado.head(n)

    # to_dict(orient="records") convierte el DataFrame en una lista de diccionarios,
    # que es el formato que FastAPI puede devolver directamente como JSON
    return {
        "total_encontradas": len(filtrado),
        "mostrando": len(resultado),
        "datos": resultado.to_dict(orient="records")
    }

@app.get("/promedios")
def promedios():
    """Identifica las columnas numericas y devuelve el promedio de cada una completa."""
    # select_dtypes filtra solo las columnas numericas (ignora texto como "day", "sex", etc.)
    columnas_numericas = df.select_dtypes(include="number").columns.tolist()

    resultado = {}
    for columna in columnas_numericas:
        promedio = df[columna].mean()
        resultado[columna] = round(promedio, 2)

    return resultado