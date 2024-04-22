

![logo-trans](https://github.com/BASILAHAMED/visual-comparison/blob/main/logo.png)

*   [About](#about)

*   [Release Notes](#release-notes)

*   [Usage](#usage)

*   [Demo](#demo)

## About
Developed with Python - Opencv Library that compares two images with the same sizes and shows the differences visually by drawing rectangles. Some parts of the image can be excluded from the comparison. Can be used for automation QA tests. 

*   Implementation is using only standard core python language and modules required.

*   The output of the comparison is a copy of `actual` images. The differences are outlined with red rectangles as shown below.

## Release Notes

Read through [RELEASE_NOTES](RELEASE_NOTES.md).

## Usage

#### Modules Required
```python
numpy
opencv-python
scikit-image
```

#### To compare two images programmatically
#### 1. To get similarity index:
```python
    # Using ImageComparisonUtil
    # Load images to be compared
    expected_image = ImageComparisonUtil.read_image_from_resources("expected.png")
    actual_image = ImageComparisonUtil.read_image_from_resources("actual.png")
    
    # Where to save the result 
    result_destination = "result.png"
    
    # Compare the images and save result.png
    similarity_index = ImageComparisonUtil.compare_images(expected_image, actual_image, result_destination)
    print("Similarity Index:", similarity_index)
```

#### 2. To assert match/mismatch:
```python
    # Using ImageComparisonUtil
    # Load images to be compared
    expected_image = ImageComparisonUtil.read_image_from_resources("expected.png")
    actual_image = ImageComparisonUtil.read_image_from_resources("actual.png")
    
    # Where to save the result 
    result_destination = "result.png"
    
    # Asserting both images
    match_result = ImageComparisonUtil.check_match(expected_image, actual_image)
    assert match_result
```

## Demo
Demo shows how `image-comparison` works.

### Expected Image
![expected](https://github.com/BASILAHAMED/visual-comparison/blob/main/images/expected.png)

### Actual Image
![actual](https://github.com/BASILAHAMED/visual-comparison/blob/main/images/actual.png)

### Result
![result](https://github.com/BASILAHAMED/visual-comparison/blob/main/images/result.png)

#### Thanks Team
