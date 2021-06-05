def parse_annotations(xml_file: str):
    """Parses the annotation file and returns the bounding boxes and breed names
    May use annotations to crop to only have the dog

    https://stackoverflow.com/questions/53317592/reading-pascal-voc-annotations-in-python
    
    In the Tsinghua dataset, there is only one dog and one body bounding box per image
    unlike the Stanford dataset
    """

    root = ET.parse(xml_file).getroot()

    for boxes in root.iter("object"):
        breed_id = root.find("folder").text  # unused
        breed_name = root.find("object").find("name").text

        # Finds the bounding box coordinates of the dog within the image
        xmin = int(boxes.find("bodybndbox/xmin").text)
        xmax = int(boxes.find("bodybndbox/xmax").text)
        ymin = int(boxes.find("bodybndbox/ymin").text)
        ymax = int(boxes.find("bodybndbox/ymax").text)

        bounding_box = np.array([xmin, ymin, xmax, ymax], dtype=np.uint16)
        return bounding_box, breed_name


def load_data(image_set_dir, image_width, image_height, number_of_files):
    """Loads image data and breed names from directory"""

    # Arrays to store images and its class
    index = 0
    image_data = np.empty((number_of_files, image_width, image_height, 3), dtype=np.uint8)
    breed_ids = np.empty(number_of_files, dtype=np.uint8)

    # Iterates the files as (with the help of sorted()):
    # breedId1_dogId1
    # breedId1_dogId1.jpg
    # breedId1_dogId2
    # breedId1_dogId2.jpg
    # ...
    # breedId120_dogIdX.jpg
    for breed_folder in sorted(os.listdir(image_set_dir)):
        for file in sorted(os.listdir(os.path.join(image_set_dir, breed_folder))):
            if index >= number_of_files:
                break

            file_path = os.path.join(image_set_dir, breed_folder, file)

            if file_path.endswith(".jpg") or file_path.endswith(".jpeg"):
                image = cv2.imread(file_path)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = cv2.resize(image, (image_width, image_height))

                image_data[index] = image
                breed_ids[index] = int(breed_folder[-3:])
                index += 1
 
    return image_data, breed_ids

# There are 65228 training images
image_data_train, breed_ids_train = load_data(TRAINING_SET_DIR, IMAGE_WIDTH, IMAGE_HEIGHT, 32614)

print(f"Training images: {len(image_data_train)}")


def image_view(images, labels):
    """Displays a 3x3 subplot of randomly selected images"""

    fig, ax = plt.subplots(3, 3, figsize=(12, 12))

    for i in range(3):
        for j in range(3):
            # Selects a random image and displays it
            index = random.randint(0, len(images) - 1)
            ax[i, j].imshow(images[index])

            # Displays the breed's name as the title
            ax[i, j].set_title(f"Breed: {labels[index]}")

    plt.show()


image_view(image_data_train, breed_ids_train)
