    #Crear diccionario con datos de persona
informacion_personal = {"Nombre": "Alina", "Edad": 23, "Ciudad": "Guayaquil", "Profesión": "Economista"}

    # Acceder a la clave ciudad y reemplazarla
informacion_personal["Ciudad"]="Ambato"

    # Agregar la clave-valor profesión
informacion_personal["Profesión"]="Economista Agrícola"

    # Verificar si la clave teléfono está en el diccionario.Caso contario agregarla
if "Teléfono" not in informacion_personal:
    informacion_personal["Teléfono"]="0980457893"

    # Eliminar la clave edad
del(informacion_personal["Edad"])

    # Imprimir el diccionario

print(informacion_personal)


