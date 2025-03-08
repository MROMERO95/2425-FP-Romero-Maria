# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Guayaquil, Quito, Cuenca

ciudades =["Guayaquil", "Quito","Cuenca"]

# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 29}
        ]
    ],
    [   # Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 16}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 17}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 16}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 16}
        ]
    ],
    [   # Cuenca
        [   # Semana 1
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 17}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 16}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 16}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 16}
        ]
    ]
]
print("")

print(" Ejemplo bucles anidados ")

# Recorrer cada ciudad en la lista temperaturas


for i in range(len(temperaturas)):
    print(f"\n{ciudades[i]}")  # Imprime el nombre de la ciudad

# Inciar el contador del número de semanas
    semana_num = 1

    # Recorrer cada semana en la ciudad
    for semana in temperaturas[i]:
        suma = 0
        for dia in semana:
            suma += dia['temp']
        print(f"El promedio de la semana {semana_num} es: {round(suma / 7, 2)}°C")

        semana_num += 1  # Incrementar el número de semana después de cada semana

print("")
print("Fin del programa")