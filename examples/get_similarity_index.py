from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from visual_comparison import ImageComparisonUtil


expected_image = ImageComparisonUtil.read_image(
    "sample_images\\basic comparison\\expected.png"
)
actual_image = ImageComparisonUtil.read_image(
    "sample_images\\basic comparison\\actual.png"
)

result_destination = "result.png"
similarity_index = ImageComparisonUtil.compare_images(
    expected_image,
    actual_image,
    result_destination,
)

print("Similarity Index:", similarity_index)
