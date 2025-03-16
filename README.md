# Handwritten-Digit-Recognition-with-TensorFlow
This project implements a neural network model using TensorFlow and Keras to classify handwritten digits from the MNIST dataset. The model is a simple feedforward neural network trained on 60,000 28x28 grayscale images of handwritten digits (0-9) and evaluated on 10,000 test images.
# Handwritten Digit Recognition with TensorFlow

## Project Overview
This project demonstrates how to build and train a neural network model using TensorFlow and Keras to recognize handwritten digits from the MNIST dataset. The MNIST dataset consists of 60,000 28x28 grayscale images of handwritten digits (0-9) used for training, and 10,000 images used for testing. The model architecture is a simple feedforward neural network with one hidden layer.

## Objective
The goal of this project is to create a neural network that can correctly classify handwritten digits. The project involves:
- Loading and preprocessing the MNIST dataset.
- Defining and training a neural network model.
- Evaluating the model's performance on unseen test data.

## Technologies Used
- **TensorFlow**: An open-source framework for machine learning and deep learning.
- **Keras**: High-level neural network API, running on top of TensorFlow.
- **Matplotlib**: Used for visualizing the training images.

## Files in the Repository
- `digit_recognition.py`: The main Python script containing the code for loading data, building, training, and evaluating the neural network.
- `README.md`: This file, which explains the project and how to use it.

## Steps to Run the Project

### 1. Clone the Repository
To get started, clone the repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/Handwritten-Digit-Recognition.git
##2. Install Dependencies
You need to install the required dependencies to run the project. You can use pip to install them:

##pip install -r requirements.txt

Here is the content of the requirements.txt file:

##tensorflow==2.12.0
##matplotlib==3.7.0

##3. Run the Script

To run the project, execute the following command in your terminal:

python digit_recognition.py
This will:

Load the MNIST dataset.
Preprocess the images (normalize them to a range of 0-1).
Build a neural network model.
Train the model for 5 epochs.
Evaluate the model on the test data and display the accuracy.

##4. Output

The script will output the test accuracy of the trained model, which is a measure of how well the model performs on unseen data.
##Test accuracy: 0.9812
