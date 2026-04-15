from visual_comparison import ImageComparisonUtil


expected_image = ImageComparisonUtil.read_image("sample_images\\basic comparison\\expected.png")
actual_image = ImageComparisonUtil.read_image("sample_images\\basic comparison\\actual.png")

result_destination = "result.png"
similarity_index = ImageComparisonUtil.compare_images(expected_image, actual_image, result_destination)
print("Similarity Index:", similarity_index)
