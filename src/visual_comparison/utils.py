from os import fspath

import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

from visual_comparison.exceptions import ImageComparisonException, ImageNotFoundException


class ImageComparisonUtil:
    """Utility helpers for visual image comparison workflows."""

    @staticmethod
    def read_image(path):
        image_path = fspath(path)
        try:
            image = cv2.imread(image_path)
            if image is None:
                raise ImageNotFoundException(f"Image with path '{image_path}' not found")
            return image
        except ImageNotFoundException:
            raise
        except Exception as e:
            raise ImageComparisonException(
                f"Cannot read image from the file, path={image_path}",
                e,
            ) from e

    @staticmethod
    def save_image(path, image):
        image_path = fspath(path)
        try:
            if not cv2.imwrite(image_path, image):
                raise ImageComparisonException(f"Cannot save image to path={image_path}")
        except Exception as e:
            if isinstance(e, ImageComparisonException):
                raise
            raise ImageComparisonException(f"Cannot save image to path={image_path}", e) from e

    @staticmethod
    def _ensure_image(image_or_path):
        """Accept either a NumPy image array or a filesystem path."""
        if isinstance(image_or_path, np.ndarray):
            return image_or_path
        return ImageComparisonUtil.read_image(image_or_path)

    @staticmethod
    def _prepare_images(expected_image, actual_image):
        expected = ImageComparisonUtil._ensure_image(expected_image)
        actual = ImageComparisonUtil._ensure_image(actual_image)
        if expected.shape != actual.shape:
            raise ImageComparisonException(
                f"Images must have the same shape, got {expected.shape} and {actual.shape}"
            )
        return expected, actual

    @staticmethod
    def _to_grayscale(expected_image, actual_image):
        expected, actual = ImageComparisonUtil._prepare_images(expected_image, actual_image)
        expected_gray = cv2.cvtColor(expected, cv2.COLOR_BGR2GRAY)
        actual_gray = cv2.cvtColor(actual, cv2.COLOR_BGR2GRAY)
        return expected, actual, expected_gray, actual_gray

    @staticmethod
    def compare_images_bw(expected_image, actual_image, result_destination=None):
        """Return the SSIM score and optionally save a black/white diff image."""
        _, _, expected_gray, actual_gray = ImageComparisonUtil._to_grayscale(
            expected_image, actual_image
        )
        similarity_index = ssim(expected_gray, actual_gray)

        if result_destination:
            diff_image = cv2.absdiff(expected_gray, actual_gray)
            ImageComparisonUtil.save_image(result_destination, diff_image)

        return similarity_index

    @staticmethod
    def compare_images_sep(expected_image, actual_image, result_destination=None):
        """Return the SSIM score and optionally save separate diff rectangles."""
        _, actual, expected_gray, actual_gray = ImageComparisonUtil._to_grayscale(
            expected_image, actual_image
        )
        similarity_index = ssim(expected_gray, actual_gray)

        if result_destination:
            diff_image = cv2.absdiff(expected_gray, actual_gray)
            _, thresholded_diff = cv2.threshold(diff_image, 30, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(
                thresholded_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
            )

            result_image = actual.copy()
            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(result_image, (x, y), (x + w, y + h), (0, 0, 255), 2)

            ImageComparisonUtil.save_image(result_destination, result_image)

        return similarity_index

    @staticmethod
    def compare_images(expected_image, actual_image, result_destination=None):
        """Return the SSIM score and optionally save a single combined diff rectangle."""
        _, actual, expected_gray, actual_gray = ImageComparisonUtil._to_grayscale(
            expected_image, actual_image
        )
        similarity_index = ssim(expected_gray, actual_gray)

        if result_destination:
            diff_image = cv2.absdiff(expected_gray, actual_gray)
            _, thresholded_diff = cv2.threshold(diff_image, 30, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(
                thresholded_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
            )

            result_image = actual.copy()
            if contours:
                x, y, w, h = cv2.boundingRect(np.concatenate(contours))
                cv2.rectangle(result_image, (x, y), (x + w, y + h), (0, 0, 255), 2)

            ImageComparisonUtil.save_image(result_destination, result_image)

        return similarity_index

    @staticmethod
    def check_mismatch(expected_image, actual_image):
        similarity_index = ImageComparisonUtil.compare_images(expected_image, actual_image)
        return not np.isclose(similarity_index, 1.0)

    @staticmethod
    def check_match(expected_image, actual_image):
        similarity_index = ImageComparisonUtil.compare_images(expected_image, actual_image)
        return np.isclose(similarity_index, 1.0)
