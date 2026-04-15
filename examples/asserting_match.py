from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from visual_comparison import ImageComparisonUtil


expected_path = "sample_images\\basic comparison\\expected.png"
actual_path = "sample_images\\basic comparison\\actual.png"

match_result = ImageComparisonUtil.check_match(expected_path, expected_path)
assert match_result

mismatch_result = ImageComparisonUtil.check_mismatch(expected_path, actual_path)
assert mismatch_result
