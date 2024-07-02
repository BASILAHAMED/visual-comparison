from image_comparison.image_comparison_util import ImageComparisonUtil


# Using ImageComparisonUtil - Verify image match/mismatch
# Load images to be compared
expected_image = ImageComparisonUtil.read_image_from_resources("sample_images\\basic comparison\\expected.png")
actual_image = ImageComparisonUtil.read_image_from_resources("sample_images\\basic comparison\\actual.png")


# Assert image match, if image mismatches throws assertion error
match_result = ImageComparisonUtil.check_match(expected_image, actual_image)
assert match_result


# Assert image mismatch, if image matches throws assertion error
mismatch_result = ImageComparisonUtil.check_mismatch(expected_image, actual_image)
assert mismatch_result

