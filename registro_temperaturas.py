# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Loja
        [   # Semana 1
            {"dia": "Lunes", "temp": 25},
            {"dia": "Martes", "temp": 28},
            {"dia": "Miércoles", "temp": 26},
            {"dia": "Jueves", "temp": 24},
            {"dia": "Viernes", "temp": 27},
            {"dia": "Sábado", "temp": 23},
            {"dia": "Domingo", "temp": 22}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 24},
            {"dia": "Martes", "temp": 27},
            {"dia": "Miércoles", "temp": 26},
            {"dia": "Jueves", "temp": 25},
            {"dia": "Viernes", "temp": 26},
            {"dia": "Sábado", "temp": 22},
            {"dia": "Domingo", "temp": 21}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 26},
            {"dia": "Martes", "temp": 29},
            {"dia": "Miércoles", "temp": 28},
            {"dia": "Jueves", "temp": 27},
            {"dia": "Viernes", "temp": 28},
            {"dia": "Sábado", "temp": 24},
            {"dia": "Domingo", "temp": 23}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 23},
            {"dia": "Martes", "temp": 26},
            {"dia": "Miércoles", "temp": 25},
            {"dia": "Jueves", "temp": 24},
            {"dia": "Viernes", "temp": 27},
            {"dia": "Sábado", "temp": 22},
            {"dia": "Domingo", "temp": 21}
        ]
    ],
    [   # Zamora
        # ... (Datos de temperatura para Zamora)
    ],
    [   # Cuenca
        # ... (Datos de temperatura para Cuenca)
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad, semanas in enumerate(temperaturas, 1):
    print(f"\nCiudad {ciudad}:")
    for semana, dias in enumerate(semanas, 1):
        suma_temperaturas = sum(dia['temp'] for dia in dias)
        promedio_semana = suma_temperaturas / len(dias)
        print(f"Semana {semana}: Promedio = {promedio_semana:.2f}°C")

# Promedio temperaturas 1 ciudad Loja
def calcular_temperatura_promedio_loja(temperaturas):
    # Inicializar una lista para almacenar las temperaturas diarias de Loja durante todas las semanas.
    temperaturas_loja = []

    # Recorrer las semanas.
    for semana in temperaturas:
        # Filtrar las temperaturas de Loja para la semana actual.
        temperaturas_semana_loja = [dia["temp"] for dia in semana if dia["dia"] == "Lunes"]

        # Agregar las temperaturas de Loja a la lista.
        temperaturas_loja.extend(temperaturas_semana_loja)

    # Calcular y devolver la temperatura promedio de Loja.
    promedio_loja = sum(temperaturas_loja) / len(temperaturas_loja)
    return promedio_loja

# Ejemplo de uso con los datos proporcionados.
temperaturas = [
    # Loja
    [
        {"dia": "Lunes", "temp": 25},
        {"dia": "Martes", "temp": 28},
        {"dia": "Miércoles", "temp": 26},
        {"dia": "Jueves", "temp": 24},
        {"dia": "Viernes", "temp": 27},
        {"dia": "Sábado", "temp": 23},
        {"dia": "Domingo", "temp": 22}
    ],
    [
        {"dia": "Lunes", "temp": 24},
        {"dia": "Martes", "temp": 27},
        {"dia": "Miércoles", "temp": 26},
        {"dia": "Jueves", "temp": 25},
        {"dia": "Viernes", "temp": 26},
        {"dia": "Sábado", "temp": 22},
        {"dia": "Domingo", "temp": 21}
    ],
    [
        {"dia": "Lunes", "temp": 26},
        {"dia": "Martes", "temp": 29},
        {"dia": "Miércoles", "temp": 28},
        {"dia": "Jueves", "temp": 27},
        {"dia": "Viernes", "temp": 28},
        {"dia": "Sábado", "temp": 24},
        {"dia": "Domingo", "temp": 23}
    ],
    [
        {"dia": "Lunes", "temp": 23},
        {"dia": "Martes", "temp": 26},
        {"dia": "Miércoles", "temp": 25},
        {"dia": "Jueves", "temp": 24},
        {"dia": "Viernes", "temp": 27},
        {"dia": "Sábado", "temp": 22},
        {"dia": "Domingo", "temp": 21}
    ]
]

temperatura_promedio_loja = calcular_temperatura_promedio_loja(temperaturas)
print(f"La temperatura promedio en Loja es: {temperatura_promedio_loja} grados Celsius.")

