import tensorflow as tf
import pandas as pd
import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


iris = load_iris()

X = iris.data
y = iris.target

print("Primeiras features (X):")
print(X[:5])

print("\nPrimeiros rótulos (y):")
print(y[:5])

print("\nClasses:", iris.target_names)


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

print("\nFormato do treino:", X_train.shape)
print("Formato do teste:", X_test.shape)


scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("\nPrimeiras amostras normalizadas (X_train):")
print(X_train[:5])


model = Sequential()

model.add(Dense(10, input_shape=(4,), activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(3, activation="softmax"))

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()


history = model.fit(
    X_train,
    y_train,
    validation_data=(X_test, y_test),
    epochs=50,
    batch_size=8,
    verbose=1
)


loss, accuracy = model.evaluate(X_test, y_test, verbose=0)

print("\nResultado no conjunto de teste:")
print(f"Loss (Erro): {loss:.4f}")
print(f"Acurácia: {accuracy * 100:.2f}%")


y_pred = model.predict(X_test)

y_pred_classes = np.argmax(y_pred, axis=1)

print("\nPrimeiras previsões:", y_pred_classes[:10])
print("Valores reais:", y_test[:10])

print("\nExemplo de previsão em nomes:")

for i in range(5):
    print(
        f"Entrada: {X_test[i]} -> "
        f"Previsto: {iris.target_names[y_pred_classes[i]]}, "
        f"Real: {iris.target_names[y_test[i]]}"
    )