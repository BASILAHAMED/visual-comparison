![logo-trans](https://github.com/BASILAHAMED/visual-comparison/blob/main/logo.png)
*   [About](#about)

*   [Release Notes](#release-notes)

*   [Usage](#usage)

*   [Demo](#demo)

## About
Developed in Python utilizing the OpenCV library, this program compares two images of identical sizes, visually highlighting their differences by drawing red rectangles. Offering flexibility for various automation Quality Assurance (QA) tests, especially visual regression testing.

**Key Features:**

* Utilizes standard Python language and specific modules for implementation.
* Generates an output comprising copies of the 'actual' images, with discrepancies delineated by red rectangles.
* This tool serves as a valuable asset for automated visual regression testing, facilitating precise visual comparisons to ensure the integrity and accuracy of image-based applications.

## Release Notes

Read through [RELEASE_NOTES](RELEASE_NOTES.md).

## Usage

#### Modules Required
```python
numpy
opencv-python
scikit-image
```

## To compare two images programmatically
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
1. Demo shows how **`image-comparison`** works.

### Expected Image
![expected](https://github.com/BASILAHAMED/visual-comparison/blob/main/images/expected.png)

### Actual Image
![actual](https://github.com/BASILAHAMED/visual-comparison/blob/main/images/actual.png) 

### Result
![result](https://github.com/BASILAHAMED/visual-comparison/blob/main/images/result.png)


2. Demo shows how **`colour-comparison`** works.
### Expected Image
![expected](https://github.com/BASILAHAMED/visual-comparison/blob/main/images/colour%20comparison/expected.png)

### Actual Image
![actual](https://github.com/BASILAHAMED/visual-comparison/blob/main/images/colour%20comparison/actual.png)

### Result
![result](https://github.com/BASILAHAMED/visual-comparison/blob/main/images/colour%20comparison/result.png)

