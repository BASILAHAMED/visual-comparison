![visual-comparison logo](https://github.com/BASILAHAMED/visual-comparison/raw/main/logo.png)

[![PyPI version](https://badge.fury.io/py/visual-comparison.svg)](https://badge.fury.io/py/visual-comparison)
[![License](https://img.shields.io/github/license/BASILAHAMED/visual-comparison.svg)](https://github.com/BASILAHAMED/visual-comparison/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)

# visual-comparison

`visual-comparison` is a lightweight Python library for visual regression testing. It compares two images of the same size, computes a structural similarity score, and can generate output images that highlight visual differences.

It is designed for automation and QA workflows where you want a simple API, reliable packaging, and compatibility with current NumPy releases.

## Features

- Supports modern Python versions from 3.9 through 3.13.
- Compatible with current NumPy releases, including NumPy 2.x.
- Compares images from file paths or in-memory NumPy arrays.
- Produces SSIM-based similarity scores.
- Can save either a combined diff box or separate diff boxes.
- Useful for UI testing, screenshot comparison, and visual regression checks.

## Installation

```bash
pip install visual-comparison
```

For local development:

```bash
pip install -e .
```

## Quick Start

```python
from visual_comparison import ImageComparisonUtil

expected = ImageComparisonUtil.read_image("expected.png")
actual = ImageComparisonUtil.read_image("actual.png")

similarity = ImageComparisonUtil.compare_images(
    expected,
    actual,
    "result.png",
)

print(f"Similarity Index: {similarity}")
```

## API

| Method | Description |
| --- | --- |
| `read_image(path)` | Load an image from disk. |
| `save_image(path, image)` | Save an image to disk. |
| `compare_images(expected, actual, result_destination=None)` | Return the SSIM score and optionally save one combined red bounding box around changed regions. |
| `compare_images_sep(expected, actual, result_destination=None)` | Return the SSIM score and optionally save separate bounding boxes for each changed region. |
| `compare_images_bw(expected, actual, result_destination=None)` | Return the SSIM score and optionally save a black-and-white diff image. |
| `check_match(expected, actual)` | Return `True` when images are effectively identical. |
| `check_mismatch(expected, actual)` | Return `True` when images differ. |

## Repository Structure

```text
.
|-- src/visual_comparison/   # Library source
|-- tests/                   # Unit tests
|-- examples/                # Example scripts
|-- sample_images/           # Demo images
|-- .github/workflows/       # CI configuration
|-- README.md
|-- LICENSE
|-- pyproject.toml
|-- requirements.txt
`-- setup.py
```

## Examples

- Similarity example: `examples/get_similarity_index.py`
- Match and mismatch assertions: `examples/asserting_match.py`

## Demo Images

Basic comparison:

- Expected: ![expected](https://github.com/BASILAHAMED/visual-comparison/raw/main/sample_images/basic%20comparison/expected.png)
- Actual: ![actual](https://github.com/BASILAHAMED/visual-comparison/raw/main/sample_images/basic%20comparison/actual.png)
- Result: ![result](https://github.com/BASILAHAMED/visual-comparison/raw/main/sample_images/basic%20comparison/result.png)

Colour comparison:

- Expected: ![expected-colour](https://github.com/BASILAHAMED/visual-comparison/raw/main/sample_images/colour%20comparison/expected.jpg)
- Actual: ![actual-colour](https://github.com/BASILAHAMED/visual-comparison/raw/main/sample_images/colour%20comparison/actual.png)
- Result: ![result-colour](https://github.com/BASILAHAMED/visual-comparison/raw/main/sample_images/colour%20comparison/result.png)

## Development

Install dependencies and run the tests:

```bash
pip install -r requirements.txt
python -m unittest discover -v
```

## Contributing

Contributions are welcome through issues and pull requests. If you are proposing an API or packaging change, please include a test update alongside it.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
