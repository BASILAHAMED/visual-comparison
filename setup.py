from pathlib import Path

from setuptools import find_packages, setup

here = Path(__file__).resolve().parent
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="visual-comparison",
    version="1.0.4",
    description="Image Comparison Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BASILAHAMED/visual-comparison",
    author="Basil Ahamed",
    author_email="sbasil.ahamed@gmail.com",
    license="MIT",
    project_urls={
        "Source": "https://github.com/BASILAHAMED/visual-comparison",
        "Issues": "https://github.com/BASILAHAMED/visual-comparison/issues",
    },
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Testing",
    ],
    keywords="visual compare image diff testing",
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=("tests",)),
    python_requires=">=3.9",
    install_requires=[
        "numpy>=1.26.4,<3",
        "opencv-python>=4.10.0.84",
        "scikit-image>=0.24.0",
    ],
    zip_safe=False,
)
