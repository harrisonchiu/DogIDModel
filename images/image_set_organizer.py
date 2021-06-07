#!/usr/bin/python3
"""Organize the images and annotations by training and validation.

Creates a folder structure to organize the images and the annotations
to prepare for training for the model.

Must be in the same directory as annotations, images, and lists
to create the training_set and validation_set folders in that directory
where annotation, images, and lists are the extracted files of its .tar
Example:
$ ls
annotations/ images/ image_set_organizer.py train_list validation_list

Folder structure:
training_set/validation_set  # folders
    breed_id-breed1  # folder
        image1.jpg
        annotation1
        image2.jpeg
        annotation2
      ...
    breed_id-breed2  # folder
        image1.jpeg
        annotation1
        image2.jpg
        annotation2
        ...
    ...
"""

import os
import shutil

CURRENT_DIR = os.getcwd()
TRAINING_SET_DIR = os.path.join(CURRENT_DIR, "training_set")
VALIDATION_SET_DIR = os.path.join(CURRENT_DIR, "validation_set")

def organize_tsinghua_set(set_list, directory):
    """Organize images and annotations to their set (training or validation)
    as described by the list
    """

    f = open(set_list, "r")
    organized_dog_dirs = f.read().splitlines()
    number_of_images = 0

    if not os.path.exists(directory):
        os.mkdir(directory)

    for dog_dir in organized_dog_dirs:
        # Extract information from the list
        dog_dir = dog_dir.strip().split("/")
        category_name = dog_dir[-2]
        image_name = dog_dir[-1]
        annotation_name = image_name + ".xml"

        # Rename folders to have breed name first
        new_category_name = category_name.split("-")[-1] + "-" + category_name.split("-")[-2]

        # Folder location where images and annotations will be organized to
        destination_dir = os.path.join(directory, new_category_name)

        # Directories of specific image and annotation from the tsinghua dataset
        image_dir = os.path.join(CURRENT_DIR, "images", category_name, image_name)
        annotation_dir = os.path.join(CURRENT_DIR, "annotations", category_name, annotation_name)

        if not os.path.exists(destination_dir):
            os.mkdir(destination_dir)

        # Copy the images and annotations to the category folder, organizing them.
        shutil.copyfile(image_dir, os.path.join(destination_dir, image_name))
        shutil.copyfile(annotation_dir, os.path.join(destination_dir, annotation_name))

        number_of_images += 1

    # Manually counted instead of len(set_list) to ensure correct number of files
    print("Number of images organized:", number_of_images)


organize_tsinghua_set("train_list", TRAINING_SET_DIR)
organize_tsinghua_set("validation_list", VALIDATION_SET_DIR)