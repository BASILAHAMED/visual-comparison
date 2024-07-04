![logo-trans](https://github.com/BASILAHAMED/visual-comparison/raw/main/logo.png)

## About
Developed with Python utilizing the OpenCV library, this program compares two images of identical sizes, visually highlighting their differences by drawing red rectangles. Offering flexibility for various automation Quality Assurance (QA) tests, especially visual regression testing.

**Key Features:**

* Utilizes standard Python language and specific modules for implementation.
* Generates an output comprising copies of the 'actual' images, with discrepancies delineated by red rectangles.
* This tool serves as a valuable asset for automated visual regression testing, facilitating precise visual comparisons to ensure the integrity and accuracy of image-based applications. 

## Usage

#### Installation
```python
pip install visual-comparison
```

## To compare two images through visual-comparison module

#### 1. Sample Code to get Similarity Index:

[Get Similarity Index](https://github.com/BASILAHAMED/visual-comparison/blob/main/get_similarity_index.py)

```python
    # Using ImageComparisonUtil to get similarity index and save output image as result.png
    # Load images to be compared
    expected_image = ImageComparisonUtil.read_image("expected.png")
    actual_image = ImageComparisonUtil.read_image("actual.png")
    
    # Provide the path to save output image
    result_destination = "result.png"
    
    # Compare the images and save it as result.png
    similarity_index = ImageComparisonUtil.compare_images(expected_image, actual_image, result_destination)
    print("Similarity Index:", similarity_index)
```

#### 2. Sample Code to assert match/mismatch:

[Assert Match/Mismatch](https://github.com/BASILAHAMED/visual-comparison/blob/main/asserting_match.py)

```python
    # Using ImageComparisonUtil
    # Load images to be compared
    expected_image = ImageComparisonUtil.read_image("expected.png")
    actual_image = ImageComparisonUtil.read_image("actual.png")
    
    # Asserting both images
    match_result = ImageComparisonUtil.check_match(expected_image, actual_image)
    assert match_result
```

## Demo
1. Demo shows how **`basic image comparison`** works.

### Expected Image
![expected](https://github.com/BASILAHAMED/visual-comparison/raw/main/sample_images/basic%20comparison/expected.png)

### Actual Image
![actual](https://github.com/BASILAHAMED/visual-comparison/raw/main/sample_images/basic%20comparison/actual.png) 

### Result
![result](https://github.com/BASILAHAMED/visual-comparison/raw/main/sample_images/basic%20comparison/result.png)


2. Demo shows how **`colour comparison`** works.
### Expected Image
![expected](https://github.com/BASILAHAMED/visual-comparison/raw/main/sample_images/colour%20comparison/expected.jpg)

### Actual Image
![actual](https://github.com/BASILAHAMED/visual-comparison/raw/main/sample_images/colour%20comparison/actual.png)

### Result
![result](https://github.com/BASILAHAMED/visual-comparison/raw/main/sample_images/colour%20comparison/result.png)

### Support and Contributions
If you find this project useful, please consider giving it a star! ⭐ Your support is greatly appreciated. If you have any ideas for improvements or would like to contribute, we welcome your input and collaboration. Feel free to open an issue or submit a pull request. Thanks for your support!

