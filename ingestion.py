import pandas as pd

# Creamos un dataset manual para el MVP
data = {
    'id_cliente': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'nombre': ['Juan Perez', 'Maria Garcia', 'Alex Smith', 'Elena Rossi', 'Klaus Muller',
               'Lucia Sanz', 'Robert Brown', 'Ana White', 'Marc Dubois', 'Sonia Lee'],
    'edad': [25, 45, 31, 55, 67, 22, 40, 38, 29, 51],
    'saldo_cuenta': [1200.50, 15000.00, 2500.75, 45000.00, 89000.00, 800.00, 12000.40, 5600.00, 3100.20, 22000.00],
    'nivel_riesgo': ['Bajo', 'Medio', 'Bajo', 'Alto', 'Alto', 'Bajo', 'Medio', 'Medio', 'Bajo', 'Medio']
}

df = pd.DataFrame(data)
df.to_csv('datos_reales.csv', index=False)
print("Archivo 'datos_reales.csv' creado con éxito.")