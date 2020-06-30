
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from configparser import ConfigParser
import time
import message

msg = message.getMsg()

# 读取配置
cp = ConfigParser()
cp.read('config/user.config')
phoneNumber = cp.get('user','phoneNumber')
password = cp.get('user','password')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# # 启动浏览器，获取网页源代码
browser = webdriver.Chrome(chrome_options=chrome_options)
# browser = webdriver.Chrome()
mainUrl = 'https://m.weibo.cn'
browser.get(mainUrl)
browser.implicitly_wait(10)
browser.find_element_by_class_name('lite-iconf-releas').click()
# browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/header/div[1]/i').click()
browser.find_element_by_xpath('/html/body/div/div[1]/div/main/div[1]/div/span/textarea[1]').send_keys(msg);
browser.find_element_by_class_name('m-send-btn').click();
# browser.implicitly_wait(10)

loginBtn = browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/a')
if loginBtn:
	# 需要登录
	loginBtn.click()
	browser.find_element_by_id('loginName').send_keys(phoneNumber)
	browser.find_element_by_id('loginPassword').send_keys(password)
	browser.find_element_by_id('loginAction').click()
	browser.find_element_by_class_name('m-send-btn').click();
browser.close()
