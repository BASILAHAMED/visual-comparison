from visual_comparison.utils import ImageComparisonUtil

# Using ImageComparisonUtil - Get similarity index
# Load images to be compared
expected_image = ImageComparisonUtil.read_image("sample_images\\basic comparison\\expected.png")
actual_image = ImageComparisonUtil.read_image("sample_images\\basic comparison\\actual.png")

# Choose the path to save the result 
result_destination = "result.png"

# Compare the images and save it as result.png
similarity_index = ImageComparisonUtil.compare_images(expected_image, actual_image, result_destination)
print("Similarity Index:", similarity_index)