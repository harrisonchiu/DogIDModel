images and files (not folders) that have a `n` as a prefix in the file name `n*_*` is from the stanford dog dataset.

`u` prefix is from the udacity dog dataset `https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/dogImages.zip`

note that some images may be repeated

will now base image dataset on the tsinghua dataset\
stanford_120_breeds \subset tsinghua_130_breeds\
some images in stanford are not present in tsinghua, but many are

use tsinghua as base for dog breed identifier and dog object recognition\
add missing stanford images if needed (for breed identifier, unlikely; for dog object recognition, more likely)\

will add udacity, oxford, microsoft dog images but does not have bounding boxes

`n` prefix - tsinghua
`s` prefix - stanford
`u` prefix - udacity
`x` prefix - oxford
`m` prefix - microsoft
