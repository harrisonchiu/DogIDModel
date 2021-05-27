#!/usr/bin/python3
"""Organize the images by training and validation images.

Creates a folder structure to organize the images and the annotations
to prepare for training for the model.

Must be in the same directory as annotation, images, and lists
to create the training_set and validation_set folders in that directory
where annotation, images, and lists are the extracted files of its .tar
Example:
$ ls
annotation lists images image_set_organizer.py

Folder structure:
training_set/validation_set  # folders
    breed_id-breed1  # folder
        image1.jpg
        annotation1
        image2.jpg
        annotation2
      ...
    breed_id-breed2  # folder
        image1.jpg
        annotation1
        image2.jpg
        annotation2
        ...
    ...
"""

import os
import shutil

import scipy.io as sp

CURRENT_DIR = os.getcwd()
TRAINING_SET_DIR = "training_set"
VALIDATION_SET_DIR = "validation_set"


def organize_training_set():
    """Organize images and annotations for the training set."""

    # Get the list of training images and their respective annotations and breed id (1 to 120).
    training_data = sp.loadmat("lists/train_list.mat")
    training_images = training_data["file_list"]
    training_annotation = training_data["annotation_list"]
    training_labels = training_data["labels"]

    # Counter for number of training images and annotations
    number_of_training_images = 0

    # Make the training dir.
    if not os.path.exists(TRAINING_SET_DIR):
        os.mkdir(TRAINING_SET_DIR)

    for i in range(len(training_images)):
        # Extract the class category, image name, annotation name from mat file.
        category = str(training_images[i][0][0]).split("/")[0]
        image = str(training_images[i][0][0]).split("/")[1]
        annotation = str(training_annotation[i][0][0]).split("/")[1]

        # Find image and annotation dir from the extracted data above.
        category_dir = CURRENT_DIR + "/" + TRAINING_SET_DIR + "/" + category + "/"
        images_dir = CURRENT_DIR + "/images/Images/" + category + "/" + image
        annotation_dir = CURRENT_DIR + "/annotation/Annotation/" + category + "/" + annotation

        # Create the category folder to organize the images and annotations by dog breed.
        if not os.path.exists(category_dir):
            os.mkdir(category_dir)

        # Copy the images and annotations to the category folder, organizing them.
        shutil.copyfile(images_dir, category_dir + "/" + image)
        shutil.copyfile(annotation_dir, category_dir + "/" + annotation)

        # Count the number of training images to ensure all training images are copied
        number_of_training_images += 1

    print("Number of training images:", number_of_training_images)


def organize_validation_set():
    """Organize images and annotations for the validation set."""

    # Get the list of training images and their respective annotations and breed id (1 to 120).
    validation_data = sp.loadmat("lists/test_list.mat")
    validation_images = validation_data["file_list"]
    validation_annotation = validation_data["annotation_list"]
    validation_labels = validation_data["labels"]

    # Counter for number of validation images and annotations
    number_of_validation_images = 0

    # Make the training dir.
    if not os.path.exists(VALIDATION_SET_DIR):
        os.mkdir(VALIDATION_SET_DIR)

    for i in range(len(validation_images)):
        # Extract the class category, image name, annotation name from mat file.
        category = str(validation_images[i][0][0]).split("/")[0]
        image = str(validation_images[i][0][0]).split("/")[1]
        annotation = str(validation_annotation[i][0][0]).split("/")[1]

        # Find image and annotation dir from the extracted data above.
        category_dir = CURRENT_DIR + "/" + VALIDATION_SET_DIR + "/" + category + "/"
        images_dir = CURRENT_DIR + "/images/Images/" + category + "/" + image
        annotation_dir = CURRENT_DIR + "/annotation/Annotation/" + category + "/" + annotation

        # Create the category folder to organize the images and annotations by dog breed.
        if not os.path.exists(category_dir):
            os.mkdir(category_dir)

        # Copy the images and annotations to the category folder, organizing them.
        shutil.copyfile(images_dir, category_dir + "/" + image)
        shutil.copyfile(annotation_dir, category_dir + "/" + annotation)

        # Count the number of validation images to ensure all validation images are copied
        number_of_validation_images += 1

    print("Number of validation images:", number_of_validation_images)


if __name__ == "__main__":
    organize_training_set()
    organize_validation_set()
