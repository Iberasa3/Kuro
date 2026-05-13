import pandas as pd
from sdv.metadata import Metadata
from sdv.single_table import GaussianCopulaSynthesizer

# 1. Ingestión: Cargamos los datos "reales" 
real_data = pd.read_csv('datos_reales.csv')

# 2. Metadatos: El sistema detecta qué es cada columna [cite: 37, 40]
metadata = Metadata.detect_from_dataframe(data=real_data)

# 3. Entrenamiento: El modelo aprende las estadísticas y correlaciones [cite: 42]
# Usamos GaussianCopula porque es ideal para el MVP 
synthesizer = GaussianCopulaSynthesizer(metadata)
synthesizer.fit(real_data)

# 4. Generación: Creamos 100 nuevos registros sintéticos [cite: 44]
synthetic_data = synthesizer.sample(num_rows=100)

# 5. Guardado
synthetic_data.to_csv('datos_sinteticos.csv', index=False)

print("¡Éxito! Se han generado 100 registros sintéticos en 'datos_sinteticos.csv'.")
print(synthetic_data.head()) # Muestra las primeras filas para verificar