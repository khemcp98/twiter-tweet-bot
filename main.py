import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

DOWNLOAD = 40.00
UPLOAD = 40.00
YOUR_USERNAME = ''
YOUR_PASSWORD = ''


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrom_driver = '/home/khem/environments/chromedriver_linux64/'
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.options, service=Service(executable_path=self.chrom_driver))
        self.up = None
        self.down = None

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        cookie = self.driver.find_element(By.XPATH, '//*[@id="onetrust-close-btn-container"]/button')
        cookie.click()
        time.sleep(3)
        go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go.click()
        time.sleep(60)
        download = self.driver.find_element(By.CLASS_NAME, 'download-speed')
        self.down = float(download.text)
        upload = self.driver.find_element(By.CLASS_NAME, 'upload-speed')
        self.up = float(upload.text)

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/i/flow/signup')

        time.sleep(3)
        log_in = self.driver.find_element(By.XPATH,
                                          '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[7]/span[2]')
        log_in.click()

        time.sleep(3)
        user = self.driver.find_element(By.NAME, 'text')
        user.send_keys(YOUR_USERNAME, Keys.ENTER)

        time.sleep(3)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(YOUR_PASSWORD, Keys.ENTER)

        time.sleep(3)
        tweet = self.driver.find_element(By.XPATH,
                                         '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet.click()
        time.sleep(2)
        msg = self.driver.find_element(By.XPATH,
                                       '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div/span')
        msg.send_keys(
            f'Promised internet speed {DOWNLOAD}MB/{UPLOAD}MB but getting lower speed at {self.down}MB/{self.up}MB')
        tweet_key = self.driver.find_element(By.XPATH,
                                             '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[3]/div/div/div[2]/div[4]')
        tweet_key.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
download_spd = bot.down
print(download_spd)
if DOWNLOAD > download_spd:
    print(download_spd)
    bot.tweet_at_provider()
