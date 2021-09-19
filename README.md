# DogID

### Breed classification only model comparison branch
Testing branch for different pretrained image classification models.
Detailed results are saved on Drive. Summary results displayed below.\
Code to recreate the model will only be for 1 chosen model in **Conclusions** is in `breed_classifier.ipynb` and `breed_classifier.py`.

### Models Tested So Far
Final Accuracy and loss format is `training // validation` to 4 decimals.

| Base Pretrained Model         | Final Accuracy   | Final Loss       | Epochs            | Batchsize | Learning Rate | Training |
| ----------------------------- | ---------------- | -----------------| ----------------- | --------- | ------------- | -------- |
| Own model**                   | 0.6969 // 0.7234 | 1.3452 // 2.3012 | 10                | 16        | 0.001         | Own model|
| Inception V3                  | 0.7719 // 0.8117 | 0.7154 // 0.6062 | 5                 | 16        | 0.0001        | Top only |
| VGG16                         | 0.6715 // 0.5127 | 1.1107 // 1.8994 | 30                | 32        | 0.001         | Top only |
| EfficientNetB5-GAP            | 0.8688 // 0.8690 | 0.3810 // 0.4286 | 5                 | 24        | 0.001         | Top only |
| EfficientNetB5-FC             | 0.6210 // 0.5702 | 1.6619 // 2.0661 | 15                | 24        | 0.001         | Top only |
| EfficientNetV2M               | 0.8675 // 0.8870 | 0.3830 // 0.3937 | 20                | 24        | 0.001         | Top only |
| EfficientNetV2B3              | 0.8235 // 0.7243 | 0.5267 // 0.9531 | 1603/2038 in 10th | 32        | 0.001         | All      |
| EfficientNetB5-NoisyStudent-1 | 0.8662 //        | 0.3871 //        | 450/2038 in 4th   | 32        | 0.001         | Top only |
| EfficientNetB5-NoisyStudent-2 | 0.8947 // 0.8850 | 0.2875 // 0.4049 | 15                | 24        | 0.001         | Top only |
| EfficientNetB5-NoisyStudent-3 | 0.8818 // 0.8920 | 0.3361 // 0.3631 | 8                 | 24        | 0.001         | Top only |
| EfficientNetB0                | 0.8780 // 0.7832 | 0.4945 // 0.8960 | 10                | 24        | 0.001         | All      |
| EfficientNetB0-NoisyStudent   | 0.8081 // 0.7957 | 0.5753 // 0.6998 | 10                | 24        | 0.001         | Top only |
| EfficientNetB1-NoisyStudent   | 0.8330 // 0.8210 | 0.4933 // 0.8210 | 10                | 24        | 0.001         | Top only |
| EfficientNetV2B0              | 0.8747 // 0.8079 | 0.3667 // 0.6724 | 10                | 24        | 0.001         | All      |

**Our own model was based on VGG16 architecture which are composed of multiple blocks of
many Convolutional 2D layers, followed by MaxPooling and Dropout layers.

### Notes
- VGG16, InceptionV3, ResNet (not recorded) performed poorly, so their variants will not be used.
- The EfficientNet model family performed the best.
    - B5 variant was chosen because the input size `456x456` is the closest resolution to the majority of our training images. Larger resolutions offered in B6 and B7 is hypothesized to have little improvements while having a longer training time.
    - B5 with global average pooling performed better than fully connected layers.
        - See https://arxiv.org/pdf/1312.4400.pdf Section 3.2 for Global average pooling as a classifier replacing fully connected layers.
    - B5 with NoisyStudent weights (with the same classifying layers as its counterpart: EfficientNetB5-GAP) performed very slightly better than it. May consider using this. If batch normalization is added in the GAP layers, it loses ~3% accuracy in first 2 epochs.
- EfficientNetV2-M (pretrained on ImageNet1K) trained much faster (approximately 35 minutes to V1's 50 minutes). But, it offered little improvement and a much larger model size: 230 MB to V1's 110 MB.
    - Performed the worst in terms of model memory size because it trains all layers.
    - If the entire model is to be trained, only EfficientNetV2-B3 or lower can be done; EfficientNetV2-S requires more than 12 VRAM.
- EfficientNetB5-NoisyStudent-2 is the second trial of the NoisyStudent model, trained at 15 epochs.
    - Overfit past at 5-10th epoch
    - Highest accuracy at 0.8947
- EfficientNetB5-NoisyStudent-3 is the third trial of the NoisyStudent model, trained at 8 epochs, the peak in EfficientNetB5-NoisyStudent-2
    - Highest validation accuracy at 0.8920 and lowest validation loss at 0.3631
    - Likely no further improvements of the NoisyStudent model
- EfficientNetB5 models are too large to be efficiently run on mobile devices
- EfficientNetB1 and B0 variants have small model sizes at around ~25 MB, making them ideal for mobile use
    - Similar accuracy between them, so EfficientNetB1 is used with NoisyStudent


### Conclusions
**19 September 2021**
- EfficientNetB5 could not efficiently run on mobile devices because of its large 100+ MB size
- EfficientNetB1-NoisyStudent had similar size to EfficientNetB0-NoisyStudent at ~25 MB, but with slightly better accuracy
- EfficientNetB1-NoisyStudent chosen for small model size to efficiently run on mobile devices (the purpose of this model is to run in Android app) while maintaining decent accuracy at 0.8330.

**22 June 2021**
- Improved EfficientNetB5-NoisyStudent-2 by retraining up to its peak epoch (8th epoch).
- Chosen for highest validation accuracy and lowest validation loss.
- Has a decent model size: ~130MB.

**21 June 2021**
- Chose EfficientNetB5-NoisyStudent-2 for highest accuracy while still have a decent size: ~130MB.


### TODO
- Train EfficientNetV2-B3 with 30+? epochs. Train on colab because local GPU does not have enough ram.
    - Done only for 10 epochs so far with peak accuracy of 0.8235 // ~0.73
        - Validation accuracy seems to be the highest at 7th epoch with 0.7440
        - Could still vastly improve past 10 epochs?
- Train EfficientNetV2-S and EfficientNetV2-M. They perform well, but will need more ram.
- Train EfficientNetB6 and B7.
    - Larger input image size
        - But most training images are at B5 (~500x500 px) size, so likely little improvements?
- [x] Create and train own convolutional neural network.
    - Likely would not do better than our best models
