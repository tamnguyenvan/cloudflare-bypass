import unittest
from cloudflare_bypass.auto import bypass

from selenium import webdriver


class TestAuto(unittest.TestCase):
    def test_bypass(self):
        url = 'https://nopecha.com/demo'
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome()
        driver.get(url)
        result = bypass(mode='dark', warmup_time=5, timeout=5)

        # Assertions
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()