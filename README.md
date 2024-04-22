

![logo-trans](https://user-images.githubusercontent.com/16310793/42029324-df117c42-7ad7-11e8-8d3e-9c6cd8822d6c.png)

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
##### The default way to compare two images looks like:
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


## Demo
Demo shows how `image-comparison` works.

### Expected Image
![expected](https://user-images.githubusercontent.com/16310793/28955567-52edeabe-78f0-11e7-8bb2-d435c8df23ff.png)

### Actual Image
![actual](https://user-images.githubusercontent.com/16310793/28955566-52ead892-78f0-11e7-993c-847350da0bf8.png)

### Result
![result](https://user-images.githubusercontent.com/16310793/28955568-52f23e02-78f0-11e7-92c5-07602b6a0887.png)

#### Thanks Team
