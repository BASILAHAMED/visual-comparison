from ImageComparison import ImageComparison
from ImageComparisonUtil import ImageComparisonUtil


# Using ImageComparisonUtil - Method I
# Load images to be compared
expected_image = ImageComparisonUtil.read_image_from_resources("expected.png")
actual_image = ImageComparisonUtil.read_image_from_resources("actual.png")

# Where to save the result 
result_destination = "result.png"

# Assert image match
match_result = ImageComparisonUtil.check_match(expected_image, actual_image)
assert match_result

# Compare the images and save result.png
similarity_index = ImageComparisonUtil.compare_images(expected_image, actual_image, result_destination)
print("Similarity Index:", similarity_index)
