import tensorflow as tf

# Loading dataset
mnist = tf.keras.datasets.mnist
(X_train,y_train),(X_test,y_test) = mnist.load_data()

#Scaling data to 0 to 1
#X_train = tf.keras.utils.normalize(X_train, axis=1)
#X_test = tf.keras.utils.normalize(X_test, axis=1)


model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
# Create layer
model.add(tf.keras.layers.Dense(128, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=3)
val_loss, val_acc = model.evaluate(X_test, y_test)
print(val_acc)

