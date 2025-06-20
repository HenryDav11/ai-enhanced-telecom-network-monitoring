#Se va a fusionar los modelos Random Forest y una red neuronal MLP

from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
#dataset
df_train = pd.read_csv("UNSW_NB15_TRAIN_FINAL.csv")
df_test = pd.read_csv("UNSW_NB15_TEST_FINAL.csv")
x_train =df_train.drop(columns=["label"])
y_train= df_train["label"]
x_test=df_test.drop(columns=["label"])
y_test=df_test["label"]
#Modelos base
modelo_rf=RandomForestClassifier(random_state=42)
modelo_mlp=MLPClassifier(hidden_layer_sizes=(100,), max_iter=300, random_state=42)

#ensamblaje por votación de mayoría

modelo_ensemble=VotingClassifier(estimators=[
    ('rf', modelo_rf),
    ('mlp', modelo_mlp)
],voting='hard')
modelo_ensemble.fit(x_train, y_train)

#entrenamiento del nuevo modelo
modelo_ensemble.fit(x_train,y_train)

#predicción con los datos de test
y_pred_ensemble=modelo_ensemble.predict(x_test)
#Evaluación
print("Resultados obtenidos ")
print("Accuracy:", round(accuracy_score(y_test, y_pred_ensemble),4))
print("Reporte de clasificación:")
print(classification_report(y_test, y_pred_ensemble, target_names=["Normal", "Ataque"]))
print("Matriz de confusión:")
print(confusion_matrix(y_test, y_pred_ensemble))
#---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------
# Validación cruzada para evaluar generalización del modelo ensamblado
# ---------------------------------------------------------------
from sklearn.model_selection import cross_val_score

print("\nResultados de Validación Cruzada (5 folds):")
cv_scores = cross_val_score(modelo_ensemble, x_train, y_train, cv=5, scoring='accuracy')
print(f"Accuracy promedio: {cv_scores.mean():.4f}")
print(f"Desviación estándar: {cv_scores.std():.4f}")