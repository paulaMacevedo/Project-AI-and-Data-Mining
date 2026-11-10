import pandas as pd

demographic = pd.read_csv("Demographic.csv")
blood = pd.read_csv("BloodTest.csv")
triage = pd.read_csv("Triage.csv")
icd = pd.read_csv("ICD_chapter.csv")
print(demographic.head())


#mostrar las columnas de la tabla
print (demographic.columns)

#mostrar cuantas filas y cuantass columnas tenemos
print(demographic.shape)

#ver información general de los datos
demographic.info()

#contar los valores ausentes de cada columna
print(demographic.isnull().sum())

# Ver los diferentes tipos de ingreso
print(demographic["admission_type"].value_counts())

# Exploramos los análisis de sangre
print("\n===== BLOOD TEST =====")
print(blood.shape)
blood.info()
print(blood.head())

# Exploramos los datos de triaje
print("\n===== TRIAGE =====")
print(triage.shape)
triage.info()
print(triage.head())

# Exploramos los diagnósticos
print("\n===== ICD CHAPTER =====")
print(icd.shape)
icd.info()
print(icd.head())


# Unimos los datos demográficos con los análisis
datos = pd.merge(demographic, blood, on="hadm_id")

# Añadimos la información de triaje
datos = pd.merge(datos, triage, on="hadm_id")

# Añadimos el diagnóstico
datos = pd.merge(datos, icd, on="hadm_id")

# Comprobamos el resultado
print("\n===== DATOS UNIDOS =====")
print(datos.shape)
print(datos.head())

# Ver cuántos pacientes hay de cada diagnóstico
print("\n===== DISTRIBUCIÓN DE DIAGNÓSTICOS =====")

print(datos["ICD chapter"].value_counts())
# Comprobar si hay hospitalizaciones duplicadas
print("\n===== IDENTIFICADORES DUPLICADOS =====")

print(datos["hadm_id"].duplicated().sum())

import matplotlib.pyplot as plt

# Contamos los pacientes de cada diagnóstico
diagnosticos = datos["ICD chapter"].value_counts()

# Creamos el gráfico
plt.bar(diagnosticos.index, diagnosticos.values)

# Añadimos título y nombres de los ejes
plt.title("Distribution of ICD Chapters")
plt.xlabel("ICD Chapter")
plt.ylabel("Number of patients")

# Ajustamos el gráfico para que no se corte nada
plt.tight_layout()

# Guardamos el gráfico como imagen
plt.savefig("diagnosticos.png", dpi=300)

# Cerramos el gráfico
plt.close()