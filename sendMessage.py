from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from configparser import ConfigParser
from time import sleep
import message



# 读取配置
cp = ConfigParser()
cp.read('config/user.config')
phoneNumber = cp.get('user','phoneNumber')
password = cp.get('user','password')
user_id = cp.get('following','user_id')
nickname = cp.get('following','nickname')
msg = nickname + ',' + message.getMsg('love.txt')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# # 启动浏览器，获取网页源代码
browser = webdriver.Chrome(chrome_options=chrome_options)
browser = webdriver.Chrome()
mainUrl = 'https://m.weibo.cn/u/'+user_id
browser.get(mainUrl)
browser.implicitly_wait(10)
chatBtn = browser.find_element_by_xpath('/html/body/div/div[1]/div[3]/div[2]/div/div[2]/div/div/h4');
chatBtn.click()

# 登录用户
loginBtn = browser.find_element_by_xpath('/html/body/div/div/a[2]')

loginBtn.click()
browser.find_element_by_id('loginName').send_keys(phoneNumber)
browser.find_element_by_id('loginPassword').send_keys(password)
browser.find_element_by_id('loginAction').click()

chatBtn = browser.find_element_by_xpath('/html/body/div/div[1]/div[3]/div[2]/div/div[2]/div/div/h4')
chatBtn.click()

browser.find_element_by_xpath('/html/body/div/article/div[2]/div[1]/textarea').send_keys(msg)
sleep(3)
browser.find_element_by_xpath('/html/body/div/article/div[2]/section/div[2]/button').click()
sleep(3)
browser.close()




