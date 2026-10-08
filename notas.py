
alumnos = [
    {"nombre": "Ana", "nota": 8.5},
    {"nombre": "Luis", "nota": 4.0},
    {"nombre": "Marta", "nota": 7.0},
    {"nombre": "Pablo", "nota": 3.5},
    {"nombre": "Sara", "nota": 9.0},
]
aprobado = 0
suspendido = 0
nota_total = 0
for alumno in alumnos:
    if alumno["nota"] >= 5:
        print (f"{alumno["nombre"].upper()}, {alumno["nota"]}, aprobado")
        aprobado += 1
        nota_total += alumno["nota"]
    else:
        print (f"{alumno["nombre"].upper()}, {alumno["nota"]},suspendido")
        suspendido += 1
        nota_total += alumno["nota"]

nota_media = round((nota_total / len(alumnos)),2)

print(f"la cantidad de alumnos es {len(alumnos)}, los alumnos aprobados son {aprobado}, los alumnos suspendidos son {suspendido} y, la nota media del grupo es {nota_media}")

def calcular_media(alumnos):
    """Calcula la nota media de una lista de alumnos.

    Args:
        alumnos (list[dict]): Lista de diccionarios donde cada diccionario
            representa a un alumno y contiene al menos la clave 'nota' (int o float).

    Returns:
        float | int: La media aritmética de las notas. Devuelve 0 si la lista
        está vacía.
    """
    nota = 0
    if len(alumnos) == 0:
        return 0

    for alumno in alumnos:
        nota += alumno["nota"]
    return nota / len(alumnos)  

print (f"nota media: {calcular_media(alumnos)}")

alumnos_inicial = [
    {"nombre": "Ana", "nota": 9.0},
    {"nombre": "Carlos", "nota": 8.0},
    {"nombre": "Elena", "nota": 8.0},
    {"nombre": "David", "nota": 4.5},
    {"nombre": "Beatriz", "nota": 2.5},
]

# Caso 2: Una persona con nota 5.0 (1 aprobado, 0 suspendidos, media 5.0)
alumnos_un_alumno = [{"nombre": "Laura", "nota": 5.0}]

# Caso 3: Lista vacía (0 alumnos, 0 aprobados, 0 suspendidos, media 0)
alumnos_vacia = []

print (f"nota media alumnos lista incial: {calcular_media(alumnos_inicial)}")
print (f"nota media alumno con nota 5.0: {calcular_media(alumnos_un_alumno)}")
print (f"nota media lista vacía: {calcular_media(alumnos_vacia)}")

