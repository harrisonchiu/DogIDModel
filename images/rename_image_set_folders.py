#!/usr/bin/python3
"""Renames the folders in training_set/ and validation_set/ directories
so that they can be sorted alphabetically instead of by breed id

Example: n*-dog_breed_name/ -> dog_breed_name-n*/
"""

import os
import sys

CURRENT_DIR = os.getcwd()
TRAINING_SET_DIR = os.path.join(CURRENT_DIR, "training_set")
VALIDATION_SET_DIR = os.path.join(CURRENT_DIR, "validation_set")

def rename_folders(directory):
    for breed_folder in os.listdir(directory):
        breed_id = breed_folder[:breed_folder.find("-")]
        breed_name = breed_folder[breed_folder.find("-") + 1:]
        breed_folder = os.path.join(directory, breed_folder)

        if os.path.exists(breed_folder) and breed_id[0] == "n" and breed_id[1].isdigit():
            os.rename(breed_folder, os.path.join(directory, breed_name + "-" + breed_id))

# rename_folders(TRAINING_SET_DIR)
# rename_folders(VALIDATION_SET_DIR)

def output_stanford_breed_names():
    f = open("stanford_breeds", "w")

    breed_folders = sorted([breed_folder.lower() for breed_folder in os.listdir(TRAINING_SET_DIR)])

    for breed_folder in breed_folders:
        f.write(breed_folder[:breed_folder.find("n02") - 1].lower() + "\n")

    f.close()

output_stanford_breed_names()
