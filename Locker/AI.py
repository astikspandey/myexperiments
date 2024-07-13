
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Load and preprocess the MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the pixel values to be between 0 and 1
x_train, x_test = x_train / 255.0, x_test / 255.0

# Define the model architecture
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),        # Flatten the 28x28 images into 1D vectors
    layers.Dense(128, activation='relu'),        # Fully connected layer with 128 units and ReLU activation
    layers.Dropout(0.2),                         # Dropout layer to prevent overfitting
    layers.Dense(10, activation='softmax')       # Output layer with 10 units (one for each digit) and softmax activation
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5)

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'\nTest accuracy: {test_acc}')

# Make predictions
predictions = model.predict(x_test)

# Function to plot the first 5 test images, their predicted labels, and the true labels
def plot_predictions(images, labels, predictions):
    plt.figure(figsize=(10, 5))
    for i in range(5):
        plt.subplot(1, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(images[i], cmap=plt.cm.binary)
        predicted_label = tf.argmax(predictions[i])
        true_label = labels[i]
        if predicted_label == true_label:
            color = 'blue'
        else:
            color = 'red'
        plt.xlabel(f'{predicted_label.numpy()} ({true_label})', color=color)
    plt.show()

# Plot the predictions for the first 5 test images
plot_predictions(x_test, y_test, predictions)