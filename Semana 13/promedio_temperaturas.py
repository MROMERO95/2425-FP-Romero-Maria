def temperatura_promedio(temp_ciudades):
    # Diccionario para almacenar los promedios de cada ciudad
    promedios_ciudad = {}

    # Iteramos sobre cada ciudad y sus datos de temperatura
    for ciudad, semanas_data in temp_ciudades.items():
        total_temperaturas = 0
        dias_totales = 0

        # Iteramos sobre cada semana de temperaturas
        for semana in semanas_data:
            total_temperaturas += sum(semana)  # Sumar las temperaturas de la semana
            dias_totales += len(semana)  # Contar los días de la semana (siempre 7 días)

        # Calcular el promedio de temperaturas de la ciudad
        promedio_ciudad = total_temperaturas / dias_totales
        promedios_ciudad[ciudad] = promedio_ciudad

    return promedios_ciudad


# Datos de las ciudades y temperaturas
temp_ciudades = {
    "Guayaquil": [
        [30, 30, 30, 30, 31, 30, 30],
        [29, 29, 28, 30, 29, 29, 30],
        [30, 30, 30, 29, 29, 28, 30],
        [30, 30, 29, 30, 30, 30, 29]
    ],
    "Quito": [
        [17, 18, 17, 17, 18, 18, 16],
        [17, 17, 16, 17, 17, 17, 17],
        [17, 17, 17, 17, 16, 15, 16],
        [17, 17, 17, 17, 16, 16, 16]
    ],
    "Cuenca": [
        [16, 16, 17, 16, 15, 15, 17],
        [16, 16, 16, 15, 16, 16, 16],
        [16, 16, 17, 16, 17, 17, 16],
        [17, 16, 16, 15, 16, 16, 16]
    ]
}

print("Temperatura promedio de tres ciudades")
print(" ")

# Calcular los promedios
promedios_resultado = temperatura_promedio(temp_ciudades)

# Mostrar los resultados
for ciudad, promedio in promedios_resultado.items():
    print(f"La temperatura promedio en {ciudad} es: {promedio:.2f}°C")
