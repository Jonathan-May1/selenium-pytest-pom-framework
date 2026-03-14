from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

def get_driver(browser_name="chrome"):
    if browser_name.lower() == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        return webdriver.Chrome(service=service, options=options)
    elif browser_name.lower() == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        return webdriver.Firefox(service=service, options=options)
    raise ValueError(f"Unsupported browser: {browser_name}")
