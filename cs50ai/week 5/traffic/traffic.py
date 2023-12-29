import cv2
import numpy as np
import os
import sys
import tensorflow as tf

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    images, labels = [], []

    # get all subdirs under data_dir with their paths
    subdir_list = sorted(
        [(f.name, f.path) for f in os.scandir(data_dir) if f.is_dir()]
    )

    for cat_name, cat_path in subdir_list:
        # Get all files under subdir
        for file in os.listdir(cat_path):
            file_path = os.path.join(data_dir, cat_name, file)

            img = cv2.imread(file_path)
            img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))

            # print(img.shape)
            # cv2.imshow(file_path,img)

            images.append(img)
            labels.append(int(cat_name))

    return (images, labels)


def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    model = tf.keras.Sequential([

        #################### Convolutional layer ####################

        # Convolutional layer 1. Learn 32 filters using a 3x3 kernel
        tf.keras.layers.Conv2D(
            32,
            kernel_size=(3, 3),
            activation="relu",
            input_shape=(IMG_WIDTH, IMG_HEIGHT, 3),
            name='conv_1'
        ),

        # BatchNormalization layer 1
        tf.keras.layers.BatchNormalization(name='norm_1'),

        # Max-pooling layer, using 2x2 pool size
        tf.keras.layers.MaxPooling2D(
            pool_size=(2, 2),
            name='max_pool'
        ),

        # Dropout 1 to prevent overfitting
        tf.keras.layers.Dropout(0.1, name='dropout_1'),

        # Convolutional layer 2. Learn 64 filters using a 3x3 kernel
        tf.keras.layers.Conv2D(
            64,
            kernel_size=(3, 3),
            activation="relu",
            name='conv_2'
        ),

        # BatchNormalization layer 2
        tf.keras.layers.BatchNormalization(name='norm_2'),

        # Average pooling layer, using 2x2 pool size
        tf.keras.layers.AveragePooling2D(
            pool_size=(2, 2),
            name='average_pool'
        ),

        # Dropout 2 to prevent overfitting
        tf.keras.layers.Dropout(0.1, name='dropout_2'),

        # Flatten units
        tf.keras.layers.Flatten(),

        #################### Hidden Layer ####################

        # Add 1st hidden layer with dropout
        tf.keras.layers.Dense(128, activation="relu", name='hidden_1'),
        tf.keras.layers.Dropout(0.1, name='dropout_3'),

        # Add 2nd hidden layer with dropout
        tf.keras.layers.Dense(256, activation="relu", name='hidden_2'),
        tf.keras.layers.Dropout(0.2, name='dropout_4'),

        #################### Output Layer ####################

        # Add an output layer with output units for all NUM_CATEGORIES
        tf.keras.layers.Dense(
            NUM_CATEGORIES,
            activation='softmax',
            name='output'
        )
    ])

    # compile model with adam optimizer
    model.compile(
        optimizer=tf.keras.optimizers.Adam(),
        loss=tf.keras.losses.CategoricalCrossentropy(),
        metrics=['accuracy']
    )

    # saving model
    # tf.keras.utils.plot_model(model, to_file='model.png', show_shapes=True)

    return model


if __name__ == "__main__":
    main()
