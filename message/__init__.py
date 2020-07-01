import random
import linecache
import os

def getMsg():
	realPath = os.path.split(os.path.realpath(__file__))[0]
	count = len(open(realPath+'/message.txt','r').readlines())#获取行数
	hellonum=random.randrange(1,count, 1)#生成随机行数
	return linecache.getline(realPath+'/message.txt',hellonum)#随机读取某行