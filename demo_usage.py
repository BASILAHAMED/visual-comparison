from ImageComparison import ImageComparison
from ImageComparisonUtil import ImageComparisonUtil


# Using ImageComparisonUtil - Method I
# Load images to be compared
expected_image = ImageComparisonUtil.read_image_from_resources("expected.png")
actual_image = ImageComparisonUtil.read_image_from_resources("actual.png")

# Where to save the result (leave None if you want to see the result in the UI)
result_destination = "result.png"

# Compare the images and save result.png
similarity_index = ImageComparisonUtil.compare_images(expected_image, actual_image, result_destination)
print("Similarity Index:", similarity_index)

# =================================================>


# Using ImageComparison - Method II

# expected_image = ImageComparisonUtil.read_image_from_resources("expected.png")
# actual_image = ImageComparisonUtil.read_image_from_resources("actual.png")

# Where to save the result
# result_destination = "result.png"

# # Create an instance of ImageComparison
# image_comparison = ImageComparison(expected_image, actual_image, result_destination)

# # Compare the images
# comparison_result = image_comparison.compare_images()

# # Print the difference percentage
# print("Difference percentage:", comparison_result['difference_percent'])


# =================================================>
