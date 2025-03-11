from pathlib import Path
from cloudflare_bypass.base_detector import BaseDetector

image_dir = Path(__file__).parent


class CloudFlarePopupDetector(BaseDetector):
    def __init__(self, mode: str = 'light', threshold: float = 0.8):
        """
        Initializes the CloudFlarePopupDetector with the path to the template image.

        The template image is used for detecting the presence of a CloudFlare popup.

        """
        if mode == 'light':
            self.template_path = str(image_dir / 'images/cf_popup.png')
        else:
            self.template_path = str(image_dir / 'images/cf_popup_dark.png')

        super().__init__(template_path=self.template_path, threshold=threshold)


class CloudFlareLogoDetector(BaseDetector):
    def __init__(self, mode: str = 'light', threshold: float = 0.8):
        """
        Initializes the CloudFlareLogoDetector with the path to the template image.

        The template image is used for detecting the presence of the CloudFlare logo.

        """
        if mode == 'light':
            self.template_path = str(image_dir / 'images/cf_logo.png')
        else:
            self.template_path = str(image_dir / 'images/cf_logo_dark.png')
        super().__init__(template_path=self.template_path, threshold=threshold)