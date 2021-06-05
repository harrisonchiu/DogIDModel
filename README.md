# DogID

## Feel free to edit/add to this

### Coding Style
Follow Google's Python Style Guide (basically the same as PEP8): https://google.github.io/styleguide/pyguide.html \
For bracket programming languages, use `K&R (One True Brace Style variant)`.

Exceptions to Google's Python Style Guide:
- Singular inline comments should be above the code
  - Yes: `# Descriptive inline comment with punctuations.`\ `if variable_one:`
  - No: `if variable_one:  # Descriptive inline comment with punctuations.`
- Character line limit is 100 instead of 80
- TODO comments should be above its related section and the name is not necessary
  - Example: `# TODO Change this to this.`\ `def some_function():`
- Type annotation optional for all but can be done for hard to understand code\
- No abbreviations except for `min, max, dir, id`\

| Abbreviation  | Exploded Name | Description |
| ------------- | ------------- | ----------- |
| min           | minimum       |             |
| max           | maximum       |             |
| dir           | directory     |             |
| id            | identity      | don't use id as verb |


### Dataset
20,580 pictures of 120 dog species with its bounding box\
http://vision.stanford.edu/aditya86/ImageNetDogs/

### Part 1
Create a model that:
- detects dog(s) in an image and draw a box around them (object detection)
- detects the species of the dog(s) identified from above

Problems:
- Some raw images are rotated 90 degrees, all images should have dogs in normal positions and orientations
- 

### Part 2
idk, maybe host a heroku site where this will run or a dogid app (not an iOS app tho)
