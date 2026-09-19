import utilidadesS1

# lista de al menos 10 registros, cada uno un diccionario
personas = [
    {"nombre": "Ana",     "edad": 34, "provincia": "Pichincha",  "ingreso": 1200.0},
    {"nombre": "Luis",    "edad": 45, "provincia": "Guayas",     "ingreso": 950.0},
    {"nombre": "María",   "edad": 29, "provincia": "Azuay",      "ingreso": 1500.0},
    {"nombre": "Carlos",  "edad": 52, "provincia": "Pichincha",  "ingreso": 2100.0},
    {"nombre": "Sofía",   "edad": 38, "provincia": "Manabí",     "ingreso": 880.0},
    {"nombre": "Jorge",   "edad": 61, "provincia": "Guayas",     "ingreso": 1750.0},
    {"nombre": "Valeria", "edad": 26, "provincia": "Azuay",      "ingreso": 1020.0},
    {"nombre": "Diego",   "edad": 43, "provincia": "Pichincha",  "ingreso": 1380.0},
    {"nombre": "Elena",   "edad": 33, "provincia": "Manabí",     "ingreso": 500.0},
    {"nombre": "Miguel",  "edad": 22, "provincia": "Guayas",     "ingreso": 300.0},
]

# ------------------------------------------------------------
# 1. Promedio de ingreso de todas las personas
# ------------------------------------------------------------

ingresos = [persona["ingreso"] for persona in personas]
promedio_ingreso = utilidadesS1.promedio(ingresos)

if promedio_ingreso is None:
    print("Promedio de ingreso: no hay datos para calcular.")
else:
    ingresos = [persona["ingreso"] for persona in personas]
    promedio_ingreso = utilidadesS1.promedio(ingresos)
    print(f"Promedio de ingreso: ${promedio_ingreso:.2f}")


# ------------------------------------------------------------
# 2. Frecuencias por provincia
# ------------------------------------------------------------

provincias = [persona["provincia"] for persona in personas]
frecuencias_provincia = utilidadesS1.contar_frecuencias(provincias)
print("\nPersonas por provincia:")
if not frecuencias_provincia:
    print("  No hay datos.")
else:
    for provincia, cantidad in frecuencias_provincia.items():
        print(f"  {provincia}: {cantidad}")


# ------------------------------------------------------------
# 3. Clasificacion de ingreso de cada persona
# ------------------------------------------------------------

print("\nClasificación de ingreso por persona:")
if not personas:
    print("  No hay personas registradas.")
else:
    for persona in personas:
        categoria = utilidadesS1.clasificar_ingreso(persona["ingreso"])
        print(f"  {persona['nombre']}: {categoria}")


# ------------------------------------------------------------
# RETO EXTRA: resumen de edades (minimo, maximo, promedio)
# ------------------------------------------------------------
resumen_edades = utilidadesS1.resumen(personas)
if resumen_edades["promedio"] is None:
    print("\nResumen de edades: no hay edades válidas.")
else:
    print(f"\nResumen de edades: {resumen_edades}")


