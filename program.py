import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
import matplotlib.pyplot as plt
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from tensorflow.keras.metrics import SparseCategoricalAccuracy
# Load and prepare the MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
print(x_train.shape) # Output: (60000, 28, 28)
print(x_test.shape) # Output: (10000, 28, 28)
print(y_train.shape) # Output: (60000,)
print(y_test.shape) # Output: (10000,)
plt.imshow(x_train[59999], cmap="gray") # Display the first training imageplt.show()
# Build the model
model = Sequential([
 Flatten(input_shape=(28, 28)),
 Dense(128, activation='relu'),
 Dense(10, activation='softmax')
])
# Compile the model
model.compile(optimizer=Adam(),
 loss=SparseCategoricalCrossentropy(),
 metrics=[SparseCategoricalAccuracy()])
# Train the model
model.fit(x_train, y_train, epochs=5)
# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'\nTest accuracy: {test_acc}')
