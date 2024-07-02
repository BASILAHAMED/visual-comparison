from visual_comparison.utils import ImageComparisonUtil

# Using ImageComparisonUtil - Verify image match/mismatch
# Load images to be compared
expected_image = ImageComparisonUtil.read_image("sample_images\\basic comparison\\expected.png")
actual_image = ImageComparisonUtil.read_image("sample_images\\basic comparison\\actual.png")

# Assert image match using check_match method
match_result = ImageComparisonUtil.check_match(expected_image, actual_image)
assert match_result

# Assert image mismatch using check_mismatch method
mismatch_result = ImageComparisonUtil.check_mismatch(expected_image, actual_image)
assert mismatch_result
