from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings
import pathlib

warnings.simplefilter("ignore")

# Set up the Chrome driver with webdriver-manager
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
# chrome_options.add_argument('--headless')  # Uncomment for headless mode

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.get("https://www.instagram.com/")
sleep(3)

class Log_in:
    def __init__(self, driver):
        self.driver = driver

    def username(self, username):
        try:
            sleep(2)
            self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
        except:
            sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(1) > div > label > input").send_keys(username)
            sleep(2)

    def password(self, password):
        try:
            sleep(2)
            self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
        except:
            sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(2) > div > label > input").send_keys(password)
            sleep(2)

    def click_Log_In(self):
        try:
            sleep(2)
            self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
        except:
            sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3) > button").click()
            sleep(7)

class Save_your_log_in_info:
    def __init__(self, driver):
        self.driver = driver

    def click_on_log_in_info(self):
        try:
            sleep(2)
            self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div').click()
        except:
            sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, "#mount_0_0_dd > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div > div > section > div > button").click()
            sleep(7)

class Check_Message:
    def __init__(self, driver):
        self.driver = driver

    def is_Message_Send(self):
        
        try:
            
            d = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_5z"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/div/span/div/a/div/div[1]/div/div[2]/div/div/span').text
            print(f"Sir you got {d} message on instagram")
        except:
            d = self.driver.find_element(By.CSS_SELECTOR, "#mount_0_0_5z > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1.x1dr59a3.xixxii4.x13vifvy.xeq5yr9.x1n327nk > div > div > div > div > div.x1iyjqo2.xh8yej3 > div:nth-child(5) > div > div > span > div > a > div > div:nth-child(1) > div > div.xjp7ctv > div > div > span").click()
            print(f"Sir you got {d} message on instagram")
        sleep(2)

class find_person:
    def __init__(self, driver):
        self.driver = driver

    def checkpersonname(self):
        try:
            d = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0_Fi"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div[1]/span/span'))
            ).text
            print(d)
        except Exception as e:
            print(f"Error: {e}")
            sleep(2)
            try:
                d = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#mount_0_0_Fi > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x1v4esvl > section > div > div > div > div.xjp7ctv > div > div.x9f619.x1n2onr6.x1ja2u2z.x78zum5.xdt5ytf.x2lah0s.x193iq5w.xeuugli.xvbhtw8 > div > div.x78zum5.xdt5ytf.x1iyjqo2.x6ikm8r.x10wlt62.x1n2onr6 > div > div > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z.x78zum5.x1iyjqo2.xs83m0k.xeuugli.x1qughib.x6s0dn4.x1a02dak.x1q0g3np.xdl72j9 > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.x1nhvcw1 > span > span"))
                ).text
                print(d)
            except Exception as e:
                print(f"Error: {e}")


# Credentials (use environment variables or a secure method to store credentials)
USERNAME = "nakulsharma123"
PASSWORD = "Nsharma@123"

person_log = Log_in(driver)
person_log.username(USERNAME)
person_log.password(PASSWORD)
person_log.click_Log_In()

# Uncomment to check for messages
message = Check_Message(driver)
message.is_Message_Send()

# find = find_person(driver)
# find.checkpersonname()
