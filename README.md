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

| Abbreviation  | Exploded Name | Description and Notes |
| ------------- | ------------- | --------------------- |
| min           | minimum       |                       |
| max           | maximum       |                       |
| dir           | directory     |                       |
| id            | identity      | don't use id as verb  |


### Models Tested So Far
Format is `training // validation` in 4 decimals for Final Accuracy and Final Loss

| Base Pretrained Model  | Final Accuracy   | Final Loss          | Epochs | Batchsize | Learning Rate |
| ---------------------- | ---------------- | ------------------- | ------ | --------- | ------------- | 
| Inception V3           | 0.7719 // 0.8117 |  0.7154 // 0.6062   | 5      | 16        | 0.0001        |
| VGG16                  | 0.6715 // 0.5127 | 1.1107 // 1.8994    | 30     | 32        | 0.001         |
| EfficientNetB5         | 0.8688 // 0.8690 |  0.3810 // 0.4286   | 5      | 24        | 0.001         |
