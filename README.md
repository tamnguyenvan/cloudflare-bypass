# Cloudflare CAPTCHA Bypass

<div style="text-align: center; margin-bottom: 50px">
  <img src="https://tamnv.imgix.net/cf_bypass_logo.png" alt="Cloudflare CAPTCHA Bypass Logo" width="250">
</div>

Detect and bypass Cloudflare CAPTCHA challenges effortlessly with the Cloudflare Captcha Bypass package.

<img src="https://tamnv.imgix.net/cf_turnstile.gif" alt="Bypassed image" width="200">


## Installation

```bash
pip install cloudflare_bypass
```

## Usage
```Python
from cloudflare_bypass import bypass

bypassed = bypass(mode='dark', warmup_time=5, timeout=30, interval=0.5)

if bypassed:
    print("Cloudflare CAPTCHA bypassed successfully!")
else:
    print("Timeout reached, CAPTCHA not bypassed.")
```

Explanation of parameters:

- `mode` (str): Choose 'light' for a light-colored webpage or 'dark' for a dark-colored webpage.
- `warmup_time` (int): Optional warm-up time before starting detection (in seconds).
- `timeout` (int): Maximum time to wait for the CAPTCHA logo to disappear after clicking (in seconds).
- `interval` (int): Time interval between successive detections (in seconds).

## Limitations
- This package only works on Cloudflare turnstile.
- It can only run in GUI mode (not headless/background).
- The speed is relatively slow.

## Disclaimer
Note: This package is provided for educational and testing purposes only. Unauthorized use of this package to circumvent security measures is strictly prohibited. The author and contributors are not responsible for any misuse or consequences arising from the use of this package.

## Support
If you find this project helpful, consider buying me a coffee to support ongoing development

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/tamnvworkr)


## Contact
For inquiries or support, please contact me:
```
Name: Tam Nguyen
Email: tamnv.work@gmail.com
```

Feel free to open issues or contribute to the project on GitHub.