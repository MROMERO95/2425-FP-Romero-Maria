# Ejemplo de Escritura en Archivos en Python usando write() y writelines()

# Definimos el nombre del archivo
datos_personales = "mynotes.txt"

# Modo de apertura: "w" para escritura (write)
archivo_escritura = open(datos_personales, "w")

# Método write(): escribir una línea a la vez
archivo_escritura.write("Linea 1: Mis nombres son Maria Ismenia\n")
archivo_escritura.write("Linea 2: Mis apellidos son Romero Davila \n")
archivo_escritura.write("Linea 3: Resido en la ciudad de Guayaquil.\n")
archivo_escritura.write("Linea 4: Lugar de nacimiento: El Empalme,Guayas.\n")

# Cierre del archivo de escritura
archivo_escritura.close()


# Abrir el archivo para lectura
archivo_lectura = open(datos_personales, "r")

# Leer el contenido del libro línea por línea con readline
archivo_lectura.seek(0)  # Reiniciamos el cursor al principio del archivo
linea_1 = archivo_lectura.readline()
linea_2 = archivo_lectura.readline()
linea_3 = archivo_lectura.readline()
linea_4 = archivo_lectura.readline()

print("\nContenido línea por línea usando readline():")
print(linea_1.strip())  # strip() para eliminar el salto de línea
print(linea_2.strip())
print(linea_3.strip())
print(linea_4.strip())


# Cierre del archivo de lectura
archivo_lectura.close()




