import cv2
import numpy as np
from exception import ImageComparisonException,ImageNotFoundException
from skimage.metrics import structural_similarity as ssim

class ImageComparisonUtil:
    @staticmethod
    def read_image_from_resources(path):
        try:
            image = cv2.imread(path)
            if image is None:
                raise ImageNotFoundException(f"Image with path '{path}' not found")
            return image
        except Exception as e:
            raise ImageComparisonException(f"Cannot read image from the file, path={path}", e)

    @staticmethod
    def save_image(path, image):
        try:
            cv2.imwrite(path, image)
        except Exception as e:
            raise ImageComparisonException(f"Cannot save image to path={path}", e)

    # show difference as B/W Image
    @staticmethod
    def compare_images_bw(expected_image, actual_image, result_destination=None):
        # Convert images to grayscale
        expected_gray = cv2.cvtColor(expected_image, cv2.COLOR_BGR2GRAY)
        actual_gray = cv2.cvtColor(actual_image, cv2.COLOR_BGR2GRAY)

        # Calculate Structural Similarity Index (SSI)
        similarity_index = ssim(expected_gray, actual_gray)

        # If result destination is provided, save the difference image
        if result_destination:
            diff_image = cv2.absdiff(expected_gray, actual_gray)
            ImageComparisonUtil.save_image(result_destination, diff_image)

        return similarity_index

    # show difference as individual red boxes
    @staticmethod
    def compare_images_sep(expected_image, actual_image, result_destination=None):
        # Convert images to grayscale
        expected_gray = cv2.cvtColor(expected_image, cv2.COLOR_BGR2GRAY)
        actual_gray = cv2.cvtColor(actual_image, cv2.COLOR_BGR2GRAY)

        # Calculate Structural Similarity Index (SSI)
        similarity_index = ssim(expected_gray, actual_gray)

        # If result destination is provided, save the difference image
        if result_destination:
            # Calculate absolute difference image
            diff_image = cv2.absdiff(expected_gray, actual_gray)
            
            # Threshold the difference image
            _, thresholded_diff = cv2.threshold(diff_image, 30, 255, cv2.THRESH_BINARY)
            
            # Find contours of differences
            contours, _ = cv2.findContours(thresholded_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            # Draw rectangles around differences
            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(actual_image, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Red rectangles
                
            # Save the resulting image
            cv2.imwrite(result_destination, actual_image)

        return similarity_index

    # show difference as a complete rectangular box
    @staticmethod
    def compare_images(expected_image, actual_image, result_destination=None):
        # Convert images to grayscale
        expected_gray = cv2.cvtColor(expected_image, cv2.COLOR_BGR2GRAY)
        actual_gray = cv2.cvtColor(actual_image, cv2.COLOR_BGR2GRAY)

        # Calculate Structural Similarity Index (SSI)
        similarity_index = ssim(expected_gray, actual_gray)

        # If result destination is provided, save the difference image
        if result_destination:
            # Calculate absolute difference image
            diff_image = cv2.absdiff(expected_gray, actual_gray)
            
            # Threshold the difference image
            _, thresholded_diff = cv2.threshold(diff_image, 30, 255, cv2.THRESH_BINARY)
            
            # Find contours of differences
            contours, _ = cv2.findContours(thresholded_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            # Combine all bounding rectangles into one
            combined_rect = cv2.boundingRect(np.concatenate(contours))
            x, y, w, h = combined_rect
            
            # Draw a rectangle around the combined differences
            cv2.rectangle(actual_image, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Red rectangle
                
            # Save the resulting image
            cv2.imwrite(result_destination, actual_image)

        return similarity_index

    @staticmethod
    def check_mismatch(expected_image, actual_image):
        similarity_index = ImageComparisonUtil.compare_images(expected_image, actual_image)
        # If similarity index is less than 1.0, there is a mismatch
        if similarity_index < 1.0:
            return True
        return False


    @staticmethod
    def check_match(expected_image, actual_image):
        similarity_index = ImageComparisonUtil.compare_images(expected_image, actual_image)
        # If similarity index is 1.0, images are identical
        if similarity_index == 1.0:
            return True
        return False
