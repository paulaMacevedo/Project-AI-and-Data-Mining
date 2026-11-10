import pandas as pd

demographic = pd.read_csv("Demographic.csv")
blood = pd.read_csv("BloodTest.csv")
triage = pd.read_csv("Triage.csv")
icd = pd.read_csv("ICD_chapter.csv")
print(demographic.head())


#show columns of the table
print (demographic.columns)

#print number of raws and columns
print(demographic.shape)

#show general information of the data
demographic.info()

#number of off data in each column
print(demographic.isnull().sum())

# show different tipes of income
print(demographic["admission_type"].value_counts())

# Explore blood data
print("\n BLOOD TEST")
print(blood.shape)
blood.info()
print(blood.head())

# Explore Triage data
print("\n TRIAGE ")
print(triage.shape)
triage.info()
print(triage.head())

# Explore diagnosis
print("\n ICD CHAPTER")
print(icd.shape)
icd.info()
print(icd.head())

# Merge demographic data with blood test results
datos = pd.merge(demographic, blood, on="hadm_id")

# Add triage information
datos = pd.merge(datos, triage, on="hadm_id")

# Add diagnosis information
datos = pd.merge(datos, icd, on="hadm_id")

# Check the merged dataset
print("\n DATOS UNIDOS ")
print(datos.shape)
print(datos.head())

# Count the number of patients for each diagnosis
print("\n DISTRIBUCIÓN DE DIAGNÓSTICOS ")

print(datos["ICD chapter"].value_counts())

# Check for duplicate hospitalization IDs
print("\n IDENTIFICADORES DUPLICADOS ")

print(datos["hadm_id"].duplicated().sum())

import matplotlib.pyplot as plt

# Count the number of patients for each diagnosis
diagnosticos = datos["ICD chapter"].value_counts()

# Create the bar chart
plt.bar(diagnosticos.index, diagnosticos.values)

# Add the chart title and axis labels
plt.title("Distribution of ICD Chapters")
plt.xlabel("ICD Chapter")
plt.ylabel("Number of patients")

# Adjust the layout to prevent labels from being cut off
plt.tight_layout()

# Save the chart as an image
plt.savefig("diagnosticos.png", dpi=300)

# Close the chart
plt.close()