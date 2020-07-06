
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from configparser import ConfigParser
import time
import message
import os
import logging

realPath = os.path.split(os.path.realpath(__file__))[0]
logging.basicConfig(level=logging.INFO,#控制台打印的日志级别
                    filename=realPath+'/new-image-post.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )
 
msgData = message.getMsg('image-post.txt')
index = int(message.getMsg('index.txt')[0])
if len(msgData) < index:
	exit()
currentData = msgData[index].split('|')
msg = currentData[0]
filePath = currentData[1].strip()
# 读取配置
cp = ConfigParser()
cp.read(realPath+'/config/user.config')
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
browser.find_element_by_xpath('/html/body/div/div[1]/div/main/div[2]/input').send_keys(filePath);


loginBtn = browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/a')
if loginBtn:
	# 需要登录
	loginBtn.click()
	browser.find_element_by_id('loginName').send_keys(phoneNumber)
	browser.find_element_by_id('loginPassword').send_keys(password)
	browser.find_element_by_id('loginAction').click()
	browser.find_element_by_xpath('/html/body/div/div[1]/div/main/div[2]/input').send_keys(filePath);
	time.sleep(10)
	browser.find_element_by_class_name('m-send-btn').click()
	realPath = os.path.split(os.path.realpath(__file__))[0]
	with open(realPath+'/message/index.txt',"w") as file:   #”w"代表着每次运行都覆盖内容
		index = index + 1
		file.write(str(index))
	logging.info('image-post:'+msg)
browser.close()
