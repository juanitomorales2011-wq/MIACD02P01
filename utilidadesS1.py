def promedio(valores: list) -> float:   #Para lograr el reto, el try/except tuvieron que ser introducidos 
    #en la funcion promedio, ya que en esta se realiza el promedio de los ingresos y no habia validación
    #si se ingresaba strings
    """
    Devuelve el promedio de una lista de numeros; None si la lista esta vacia.
    Ignora los valores que no se puedan interpretar como numero.
    """
    # si la lista esta vacia, no hay nada que promediar
    if not valores:
        return None

    valores_numericos = []
    for valor in valores:
        try:
            # float(valor) intenta convertir cada elemento a numero.
            # si ya es un int o float, esto no cambia nada.
            # si es un texto no numerico (ej. "abc"), lanza ValueError.
            valores_numericos.append(float(valor))
        except (ValueError, TypeError):
            # TypeError cubre casos como None o listas dentro de la lista
            print(f"Advertencia: el valor '{valor}' no es numérico y fue ignorado.")
            continue

    # try/except extra: por si al calcular sum()/len() ocurriera algun problema
    # inesperado (ej. que valores_numericos quedara vacia tras filtrar)
    try:
        if not valores_numericos:
            return None
        return sum(valores_numericos) / len(valores_numericos)
    except ZeroDivisionError:
        return None


def contar_frecuencias(valores: list) -> dict:
    """Devuelve un diccionario con cuantas veces aparece cada elemento de la lista."""
    # si la lista esta vacia, devolvemos un diccionario vacio directamente
    if not valores:
        return {}

    frecuencias = {}
    try:
        for valor in valores:
            # .get(valor, 0) busca el valor en el diccionario; si no existe todavia,
            # devuelve 0 como valor por defecto. Luego le sumamos 1 y lo guardamos.
            frecuencias[valor] = frecuencias.get(valor, 0) + 1
    except TypeError:
        # TypeError ocurriria si algun elemento no es "hasheable" (ej. una lista como valor)
        print("Advertencia: algún valor no se pudo usar como clave y fue ignorado.")

    return frecuencias


def clasificar_ingreso(ingreso: float) -> str:
    """
    Clasifica un ingreso en 'bajo', 'medio' o 'alto'.

    Umbrales definidos:
    - bajo: menos de 460
    - medio: entre 460 y 999 (inclusive)
    - alto: 1000 o mas

    Si el valor recibido no se puede interpretar como numero, devuelve
    'valor invalido' en vez de detener el programa.
    """
    # si el ingreso viene vacio (None, "" o similar), lo tratamos como invalido
    if not ingreso and ingreso != 0:
        return "valor invalido"

    try:
        # float(ingreso) intenta convertir el valor a numero decimal.
        # si ingreso ya es un numero, esto no cambia nada; si es un texto
        # como "abc", lanza ValueError y pasamos al except.
        ingreso = float(ingreso)
    except (ValueError, TypeError):
        return "valor invalido"

    if ingreso < 460:
        return "bajo"
    elif ingreso <= 999:
        return "medio"
    else:
        return "alto"


def resumen(registros: list) -> dict:
    """
    Devuelve un diccionario con minimo, maximo y promedio de la edad
    de una lista de registros. Ignora los registros cuya edad no sea numérica.
    """
    # si la lista de registros esta vacia, no hay nada que resumir
    if not registros:
        return {"minimo": None, "maximo": None, "promedio": None}

    edades = []
    for registro in registros:
        try:
            # float(...) intenta convertir la edad a numero.
            # si el registro ya trae un int o float, esto no cambia nada.
            # si trae un texto no numerico (ej. "treinta"), lanza ValueError.
            edad = float(registro["edad"])
            edades.append(edad)
        except (ValueError, TypeError, KeyError):
            # KeyError cubre el caso de que el registro ni siquiera tenga la clave "edad"
            print(f"Advertencia: edad inválida en el registro {registro}, fue ignorado.")
            continue

    # try/except extra: protegemos min()/max() por si edades quedara vacia tras filtrar
    try:
        if not edades:
            return {"minimo": None, "maximo": None, "promedio": None}

        return {
            "minimo": min(edades),
            "maximo": max(edades),
            "promedio": promedio(edades)   # reutilizamos la funcion promedio() de arriba
        }
    except ValueError:
        # ValueError ocurriria si min()/max() reciben una lista vacia
        return {"minimo": None, "maximo": None, "promedio": None}


# ------------------------------------------------------------
# Pruebas rapidas de las funciones (solo se ejecutan si corremos
# este archivo directamente con "python utilidadesS1.py", no cuando
# se importa desde main.py)
# ------------------------------------------------------------
if __name__ == "__main__":
    # pruebas de promedio()
    assert promedio([10, 20, 30]) == 20
    assert promedio([]) is None

    # pruebas de contar_frecuencias()
    assert contar_frecuencias(["a", "b", "a", "c", "a"]) == {"a": 3, "b": 1, "c": 1}
    assert contar_frecuencias([]) == {}

    # pruebas de clasificar_ingreso()
    assert clasificar_ingreso(300) == "bajo"
    assert clasificar_ingreso(460) == "medio"
    assert clasificar_ingreso(999) == "medio"
    assert clasificar_ingreso(1000) == "alto"
    assert clasificar_ingreso("no es un numero") == "valor invalido"

    # pruebas de resumen()
    registros_prueba = [{"edad": 20}, {"edad": 30}, {"edad": 40}]
    resultado = resumen(registros_prueba)
    assert resultado == {"minimo": 20, "maximo": 40, "promedio": 30}
    assert resumen([]) == {"minimo": None, "maximo": None, "promedio": None}

    print("Todas las pruebas pasaron correctamente.")