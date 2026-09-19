def clasificar_gasto(monto, limite_menor=5, limite_mayor=50):
    """Clasifica un monto en 'menor', 'medio' o 'mayor' según dos límites configurables."""
    # limite_menor y limite_mayor tienen valores por defecto (5 y 50),
    # pero se pueden cambiar al llamar la función: clasificar_gasto(30, limite_mayor=25).
    if monto < limite_menor:
        return "menor"
    elif monto <= limite_mayor:
        # aquí ya sabemos que monto >= limite_menor; con "<=" incluimos el límite superior
        return "medio"
    else:
        return "mayor"


def total_por(lista, clave):
    """Suma el 'monto' de una lista de diccionarios agrupando por la clave indicada."""
    totales = {}  # diccionario acumulador: {valor_de_la_clave: suma_de_montos}
    for elemento in lista:
        valor_clave = elemento[clave]  # ej: la categoría o la fecha de este gasto
        # totales.get(valor_clave, 0) devuelve el total acumulado hasta ahora,
        # o 0 si es la primera vez que aparece ese valor de clave.
        totales[valor_clave] = totales.get(valor_clave, 0) + elemento["monto"]
    return totales


def resumen(numeros):
    """Devuelve una tupla (minimo, maximo, promedio, mediana) de una lista de números."""
    ordenados = sorted(numeros)  # ordenamos de menor a mayor para poder calcular la mediana
    n = len(ordenados)

    minimo = ordenados[0]        # el primer elemento de la lista ordenada
    maximo = ordenados[-1]       # el último elemento de la lista ordenada
    promedio = sum(ordenados) / n

    mitad = n // 2  # posición central (división entera)
    if n % 2 == 1:
        # cantidad impar de elementos: la mediana es exactamente el elemento del medio
        mediana = ordenados[mitad]
    else:
        # cantidad par de elementos: la mediana es el promedio de los dos elementos centrales
        mediana = (ordenados[mitad - 1] + ordenados[mitad]) / 2

    return (minimo, maximo, promedio, mediana)


def a_float(texto):
    """Convierte un texto a float manejando coma decimal, símbolo '$' y errores, sin lanzar excepciones."""
    try:
        # quitamos espacios al inicio/fin y el símbolo "$" (por si viene como "$ 12.50")
        limpio = texto.strip().replace("$", "").strip()
        # cambiamos la coma decimal por punto (por si viene como "12,50")
        limpio = limpio.replace(",", ".")
        return float(limpio)
    except (ValueError, AttributeError):
        # ValueError: el texto no se puede convertir a número (ej: "abc" o "")
        # AttributeError: "texto" no es un string y no tiene .strip() (ej: None)
        return None


def limpiar_montos(lista_textos):
    """Convierte una lista de textos con a_float y devuelve (valores_ok, textos_fallidos)."""
    valores_ok = []        # aquí van los números que sí se pudieron convertir
    textos_fallidos = []   # aquí van los textos originales que no se pudieron convertir
    for texto in lista_textos:
        valor = a_float(texto)
        if valor is None:
            # a_float devuelve None cuando falla, así que guardamos el texto original
            textos_fallidos.append(texto)
        else:
            valores_ok.append(valor)
    return valores_ok, textos_fallidos