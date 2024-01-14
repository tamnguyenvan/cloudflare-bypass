from typing import Union, Tuple
import cv2
from PIL import ImageGrab
import numpy as np


class BaseDetector:
    def __init__(self, template_path: str, threshold: float = 0.8) -> None:
        """
        Initializes the BaseDetector with a template image and a matching threshold.

        Parameters:
            - template_path (str): Path to the template image file.
            - threshold (float): Matching threshold (default is 0.8).
        """
        self.template = cv2.imread(template_path, 0)
        self.threshold = threshold
        self.matched_bbox = None

    def _match(self, img: np.ndarray, template: np.ndarray) -> Union[None, Tuple[int]]:
        """
        Performs template matching on the input image.

        Parameters:
            - img (np.ndarray): Input image.
            - template (np.ndarray): Template image.

        Returns:
            - Union[None, Tuple[int]]: Bounding box coordinates if match is found, else None.
        """
        result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        _, confidence, _, max_loc = cv2.minMaxLoc(result)

        if confidence >= self.threshold:
            h, w = template.shape
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            return top_left[0], top_left[1], bottom_right[0], bottom_right[1]
        else:
            return None

    def is_detected(self) -> bool:
        """
        Checks if the template is detected in the current screen.

        Returns:
            - bool: True if template is detected, else False.
        """
        img = np.array(ImageGrab.grab())
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        self.matched_bbox = self._match(img_gray, self.template)
        return self.matched_bbox is not None