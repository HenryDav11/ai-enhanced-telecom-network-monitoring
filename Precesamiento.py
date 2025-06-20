import pandas as pd
from sklearn.preprocessing import StandardScaler
from tabulate import tabulate
from sklearn.preprocessing import LabelEncoder

#PREPARACIÓN DE LOS DATOS

#IMPORTACIÓN DE LAS DATASETS
df_train=pd.read_csv("UNSW_NB15_training-set.csv")
df_test=pd.read_csv("UNSW_NB15_testing-set.csv")

#1. Verificación de valorees nulos

##def verificar_nulos(df,nombre):
    #null_values = df.isnull().sum.reset_index()
    #null_values.colums={"variable","valores nulos"}
    #print(f"Valores nulos en {nombre}:")
    ##print(df.isnull().sum())
    #print(tabulate(null_values, headers="keys", tablefmt="pretty"))
    ##print("-"*50)
    #exportar a excel
    #null_values.to_excel(f"valores_nulos_{nombre}:")

##verificar_nulos(df_train,"Training")
##verificar_nulos(df_test, "Test")

columnas_a_eliminar=["id"]
df_train=df_train.drop(columns=columnas_a_eliminar, errors="ignore")
df_test=df_test.drop(columns=columnas_a_eliminar, errors="ignore")
print(df_train.columns)
print(df_test.columns)

#conversion de variables categórcas a numéricas
labelencoder=LabelEncoder()
#tipo de ataque 
"""df_train["attack_cat"]=labelencoder.fit_transform(df_train["attack_cat"])
df_test["attack_cat"]=labelencoder.fit_transform(df_test["attack_cat"])

categorias=dict(zip(labelencoder.classes_, labelencoder.transform(labelencoder.classes_)))
print("conversion de attack_cat:")
for categoria, valor in categorias.items():
    print(f"{categoria}: {valor}")"""

###
columnas_categoricas=df_train.select_dtypes(include=["object"]).columns #train y test tienen las mismas categorias; por lo que basta con encontrar las categorias de uno de los dos

label_encoders={}
for col in columnas_categoricas:
    le=LabelEncoder()
    df_train[col]= le.fit_transform(df_train[col].astype(str)) #fit_transform ajusta y convierte
    df_test[col]=le.transform(df_test[col].astype(str)) #transform usa la conversion anterior
    label_encoders[col]=le
    
for col, le in label_encoders.items():
    print(f"\n Conversion de {col}:")
    print(dict(zip(le.classes_, le.transform(le.clasess_))))
    