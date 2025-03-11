from typing import Union
import time
import random
import pyautogui
from cloudflare_bypass.cloudflare_detector import CloudFlareLogoDetector, CloudFlarePopupDetector


def wait_until(detector, warmup_time: Union[None, int] = None, timeout: int = 20):
    """
    Wait until a detector is detected or timeout is reached.

    Parameters:
        - detector: An instance of a detector.
        - warmup_time (int or None): Optional warm-up time before starting to detect.
        - timeout (int): Maximum time to wait for detection.

    Returns:
        - Union[None, Tuple[int]]: Bounding box coordinates if detection occurs, else None.
    """
    if warmup_time:
        time.sleep(warmup_time)

    t0 = time.time()
    while True:
        time.sleep(1)
        if detector.is_detected():
            return detector.matched_bbox

        if time.time() - t0 > timeout:
            break


def click_like_human(x: int, y: int, max_value: int = 5):
    """
    Simulate a human-like click with a small random deviation.

    Parameters:
        - x (int): X-coordinate of the click.
        - y (int): Y-coordinate of the click.
        - max_value (int): Maximum deviation from the specified coordinates.
    """
    delta_x = random.randint(-max_value, max_value)
    delta_y = random.randint(-max_value, max_value)
    pyautogui.click(x=x + delta_x, y=y + delta_y)


def bypass(
    mode: str = 'light',
    warmup_time: int = None,
    timeout: int = 20,
    interval: int = 1,
    threshold: float = 0.8,
):
    """
    Bypass CloudFlare challenges by clicking on the detected popup.

    Parameters:
        - mode (str): Choose the appropriate mode based on the webpage background color ('light' or 'dark').
        - warmup_time (int or None): Optional warm-up time before starting to detect.
        - timeout (int): Maximum time to wait for the CloudFlare logo to disappear after clicking the popup.
        - interval (int): Time interval between successive detections (default: 1 second).
        - threshold (float): Detection threshold for the CloudFlare logo and popup. Default is 0.8.

    Returns:
        - bool: True if the logo disappears within the timeout, else False.
    """
    # Optionally wait for warmup_time before starting the detection process
    if warmup_time is not None and isinstance(warmup_time, (int, float)):
        time.sleep(warmup_time)

    # Initialize CloudFlare detectors with the specified mode
    cf_popup_detector = CloudFlarePopupDetector(mode=mode, threshold=threshold)
    cf_logo_detector = CloudFlareLogoDetector(mode=mode, threshold=threshold)

    t0 = time.time()
    clicked = False
    while cf_logo_detector.is_detected():
        # Click on the popup if detected and not clicked before
        if not clicked and cf_popup_detector.is_detected():
            x1, y1, x2, y2 = cf_popup_detector.matched_bbox
            cx = x1 + int((x2 - x1) * 0.1)
            cy = (y1 + y2) // 2
            click_like_human(x=cx, y=cy)
            clicked = True

        # Wait for `interval` second before the next iteration
        time.sleep(interval)

        # Check if the timeout has been reached
        if time.time() - t0 > timeout:
            return clicked

    return clicked
