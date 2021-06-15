# DogID

### Breed classification only model comparison branch
Testing branch for different pretrained image classification models.
Detailed results are saved on Drive. Summary results displayed below.

### Models Tested So Far
Final Accuracy and loss format is `training // validation` to 4 decimals.

| Base Pretrained Model       | Final Accuracy   | Final Loss          | Epochs            | Batchsize | Learning Rate | Training |
| --------------------------- | ---------------- | ------------------- | ----------------- | --------- | ------------- | -------- |
| Inception V3                | 0.7719 // 0.8117 | 0.7154 // 0.6062    | 5                 | 16        | 0.0001        | Top only |
| VGG16                       | 0.6715 // 0.5127 | 1.1107 // 1.8994    | 30                | 32        | 0.001         | Top only |
| EfficientNetB5-GAP          | 0.8688 // 0.8690 | 0.3810 // 0.4286    | 5                 | 24        | 0.001         | Top only |
| EfficientNetB5-FC           | 0.6210 // 0.5702 | 1.6619 // 2.0661    | 15                | 24        | 0.001         | Top only |
| EfficientNetV2-M            | 0.8675 // 0.8870 | 0.3830 // 0.3937    | 20                | 24        | 0.001         | Top only |
| EfficientNetV2-B3           | 0.8235 //        | 0.5267 //           | 1603/2038 in 10th | 32        | 0.001         | All      |
| EfficientNetB5-NoisyStudent | 0.8662 //        | 0.3871 //           | 450/2038 in 4th   | 32        | 0.001         | Top only |

#### Notes
- VGG16 performed the worst.
- InceptionV3 and ResNet (not recorded) performed similarly.
- The EfficientNet model family performed the best.
    - B5 variant was chosen because the input size `456x456` is the closest resolution to the majority of our training images. Larger resolutions offered in B6 and B7 is hypothesized to have little improvements while having a longer training time.
    - B5 with global average pooling performed better than fully connected layers.
        - See https://arxiv.org/pdf/1312.4400.pdf Section 3.2 for Global average pooling as a classifier replacing fully connected layers.
    - B5 with NoisyStudent weights (with the same classifying layers as its counterpart: EfficientNetB5-GAP) performed very slightly better than it. May consider using this. If batch normalization is added in the GAP layers, it loses ~3% accuracy in first 2 epochs.
- EfficientNetV2-M (pretrained on ImageNet1K) trained much faster (approximately 35 minutes to V1's 50 minutes). But, it offered little improvement and a much larger model size: 230 MB to V1's 110 MB.
    - Performed the worst in terms of model memory size.
    - If the entire model is to be trained, only EfficientNetV2-B3 or lower can be done; EfficientNetV2-S requires more than 12 VRAM.


#### TODO
- Train EfficientNetB5 with 10-15? epochs, might as well use noisy student weights. Train locally.
- Train EfficientNetV2-B3 with 30? epochs. Train on colab because local GPU does not have enough ram.
    - Done only for 10 epochs so far with peak accuracy of 0.8235 // ~0.73
        - Validation accuracy seems to be the highest at 7th epoch with 0.7440
        - Could still vastly improve past 10 epochs?