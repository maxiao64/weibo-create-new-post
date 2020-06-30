import random
import linecache

def getMsg():
	count = len(open('config/message.txt','r').readlines())#获取行数
	hellonum=random.randrange(1,count, 1)#生成随机行数
	return linecache.getline('config/message.txt',hellonum)#随机读取某行