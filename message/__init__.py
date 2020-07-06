import random
import linecache
import os

def getRandomMsg(fileName):
	realPath = os.path.split(os.path.realpath(__file__))[0]
	count = len(open(realPath+'/'+fileName,'r').readlines())#获取行数
	hellonum=random.randrange(1,count, 1)#生成随机行数
	return linecache.getline(realPath+'/'+fileName,hellonum)#随机读取某行

def getMsg(fileName):
	realPath = os.path.split(os.path.realpath(__file__))[0]
	count = len(open(realPath+'/'+fileName,'r').readlines())#获取行数
	data = [];
	ranges = range(1,count)
	if count == 1:
		ranges = [1]
	for x in ranges:
		data.append(linecache.getline(realPath+'/'+fileName,x))	
	return data