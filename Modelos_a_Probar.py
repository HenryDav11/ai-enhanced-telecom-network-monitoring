from sklearn.linear_model import LogisticRegression
from sklearn.tree  import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

import pandas as pd

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import warnings

warnings.filterwarnings("ignore")
#########Carga de datos pra realizar la coparación entre los modelos 
df_train = pd.read_csv("UNSW_NB15_TRAIN_FINAL.csv")
df_test = pd.read_csv("UNSW_NB15_TEST_FINAL.csv")

##############################################################################
x_train =df_train.drop(columns=["label"])
y_train= df_train["label"]
x_test=df_test.drop(columns=["label"])
y_test=df_test["label"]
#####definición de los modelos que se van a evaluar

modelos={
    "Regresión Logística": LogisticRegression(max_iter=1000),
    #"Arbol de Decisión": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    
    "SVM": SVC(),
    "KNN": KNeighborsClassifier()
}

####Evaluación de cada modelo
for nombre, modelo in modelos.items():
    print(f"\n Modelo: {nombre}")
    modelo.fit(x_train, y_train)
    y_pred = modelo.predict(x_test)
    
    print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))
    print("Reporte de clasificación:")
    print(classification_report(y_test, y_pred, target_names={"Normal","Ataque"}))
    print("Matriz de confusión:")
    print(confusion_matrix(y_test, y_pred))
    

