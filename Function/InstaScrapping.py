from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings

warnings.simplefilter("ignore")

# Set up the Chrome driver with webdriver-manager
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument('--headless')  # Uncomment for headless mode

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.get("https://www.instagram.com/")
sleep(3)

class Log_in:
    def __init__(self, driver):
        self.driver = driver

    def username(self, username):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))
            ).send_keys(username)
        except Exception as e:
            print(f"Error entering username: {e}")

    def password(self, password):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'))
            ).send_keys(password)
        except Exception as e:
            print(f"Error entering password: {e}")

    def click_Log_In(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button'))
            ).click()
        except Exception as e:
            print(f"Error clicking login button: {e}")

class Save_your_log_in_info:
    def __init__(self, driver):
        self.driver = driver

    def click_on_log_in_info(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'))
            ).click()
        except Exception as e:
            print(f"Error clicking save login info: {e}")

class Check_Message:
    def __init__(self, driver):
        self.driver = driver

    def is_Message_Send(self):
        try:
            d = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/div/span/div/a/div/div[1]/div/div[2]/div/div/span'))
            ).text
            print(f"Sir, you got {d} messages on Instagram")
        except Exception as e:
            print(f"Error checking messages: {e}")



# Credentials (use environment variables or a secure method to store credentials)
USERNAME = "username"
PASSWORD = "password"

person_log = Log_in(driver)
person_log.username(USERNAME)
person_log.password(PASSWORD)
person_log.click_Log_In()

# Uncomment to check for messages
message = Check_Message(driver)
message.is_Message_Send()


# Close the driver after operations
driver.quit()
