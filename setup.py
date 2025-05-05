from setuptools import find_packages, setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

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
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="visual compare image diff testing",
    packages=find_packages(exclude=("tests",)),
    install_requires=[
        "numpy",
        "opencv-python",
        "scikit-image"
    ],
    zip_safe=False,
)