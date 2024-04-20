import numpy as np
from collections import namedtuple
import cv2

Rectangle = namedtuple('Rectangle', ['min_point', 'max_point'])

class ImageComparison:
    def __init__(self, expected, actual, destination=None):
        self.threshold = 5
        self.expected = expected
        self.actual = actual
        self.destination = destination
        self.rectangle_line_width = 1
        self.counter = 2
        self.region_count = self.counter
        self.minimal_rectangle_size = 1
        self.maximal_rectangle_count = -1
        self.pixel_tolerance_level = 0.1
        self.difference_constant = self.calculate_difference_constant()
        self.matrix = None
        self.excluded_areas = []
        self.draw_excluded_rectangles = False
        self.difference_percent = None
        self.fill_difference_rectangles = False
        self.percent_opacity_difference_rectangles = 20.0
        self.fill_excluded_rectangles = False
        self.percent_opacity_excluded_rectangles = 20.0
        self.allowing_percent_of_different_pixels = 0.0
        self.difference_rectangle_color = (0, 0, 255)  # Red
        self.excluded_rectangle_color = (0, 255, 0)    # Green

    def compare_images(self):
        if self.is_image_sizes_not_equal(self.expected, self.actual):
            actual_resized = cv2.resize(self.actual, (self.expected.shape[1], self.expected.shape[0]))
            difference_percent = self.get_difference_percent(actual_resized, self.expected)
            return {'mismatch': True, 'difference_percent': difference_percent}
        
        self.populate_rectangles()
        
        if not self.rectangles:
            match_result = {'match': True, 'difference_percent': self.get_difference_percent(self.actual, self.expected)}
            if self.draw_excluded_rectangles:
                result = self.draw_rectangles(self.rectangles)
                self.save_image_for_destination(result)
                match_result['result'] = result
            return match_result
        
        result_image = self.draw_rectangles(self.rectangles)
        self.save_image_for_destination(result_image)
        return {'mismatch': True, 'difference_percent': self.get_difference_percent(self.actual, self.expected), 'result': result_image, 'rectangles': self.rectangles}

    def is_image_sizes_not_equal(self, expected, actual):
        return expected.shape[0] != actual.shape[0] or expected.shape[1] != actual.shape[1]

    def populate_the_matrix_of_the_differences(self):
        count_of_different_pixels = 0
        self.matrix = np.zeros_like(self.expected, dtype=np.uint8)
        for y in range(self.expected.shape[0]):
            for x in range(self.expected.shape[1]):
                if (x, y) not in self.excluded_areas:
                    if self.is_different_pixels(self.expected[y, x], self.actual[y, x]):
                        self.matrix[y, x] = 1
                        count_of_different_pixels += 1
        return count_of_different_pixels

    def is_different_pixels(self, expected_rgb, actual_rgb):
        diff_channels = np.abs(expected_rgb - actual_rgb)
        diff_sum = np.sum(diff_channels)
        return diff_sum > self.difference_constant

    def populate_rectangles(self):
        count_of_different_pixels = self.populate_the_matrix_of_the_differences()
        
        if count_of_different_pixels == 0:
            self.rectangles = []
            return
        
        if self.is_allowed_percent_of_different_pixels(count_of_different_pixels):
            self.rectangles = []
            return
        
        self.group_regions()
        self.rectangles = []
        while self.counter <= self.region_count:
            rectangle = self.create_rectangle()
            if rectangle != (0, 0, 0, 0) and rectangle[2] * rectangle[3] >= self.minimal_rectangle_size:
                self.rectangles.append(rectangle)
            self.counter += 1

    def create_rectangle(self):
        min_x, min_y, max_x, max_y = self.expected.shape[1], self.expected.shape[0], 0, 0
        for y in range(self.matrix.shape[0]):
            for x in range(self.matrix.shape[1]):
                if self.matrix[y, x] == self.counter:
                    min_x = min(min_x, x)
                    max_x = max(max_x, x)
                    min_y = min(min_y, y)
                    max_y = max(max_y, y)
        return min_x, min_y, max_x - min_x + 1, max_y - min_y + 1

    def group_regions(self):
        for y in range(self.matrix.shape[0]):
            for x in range(self.matrix.shape[1]):
                if self.matrix[y, x] == 1:
                    self.join_to_region(x, y)
                    self.region_count += 1

    def join_to_region(self, x, y):
        if self.is_jump_rejected(x, y):
            return
        
        self.matrix[y, x] = self.region_count
        
        for i in range(self.threshold):
            self.join_to_region(x + 1 + i, y)
            self.join_to_region(x, y + 1 + i)
            self.join_to_region(x + 1 + i, y - 1 - i)
            self.join_to_region(x - 1 - i, y + 1 + i)
            self.join_to_region(x + 1 + i, y + 1 + i)

    def is_jump_rejected(self, x, y):
        return y < 0 or y >= self.matrix.shape[0] or x < 0 or x >= self.matrix.shape[1] or self.matrix[y, x] != 1

    def calculate_difference_constant(self):
        return np.square(self.pixel_tolerance_level * np.sqrt(np.square(255) * 3))

    def get_difference_percent(self, actual, expected):
        return np.count_nonzero(actual != expected) / (actual.shape[0] * actual.shape[1]) * 100

    def draw_rectangles(self, rectangles):
        result_image = self.actual.copy()
        for rectangle in rectangles:
            cv2.rectangle(result_image, (rectangle[0], rectangle[1]), (rectangle[0] + rectangle[2], rectangle[1] + rectangle[3]), self.difference_rectangle_color, self.rectangle_line_width)
        return result_image

    def save_image_for_destination(self, image):
        if self.destination is not None:
            cv2.imwrite(self.destination, image)
