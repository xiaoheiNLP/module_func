#-*-coding:utf-8 -*-
'''
    结巴分词模块
    '''
import time
import jieba_fast

jieba_fast.load_userdict('/Users/zhuxinquan/Desktop/招聘信息/mykeyword_招聘.dict')
#存储停用词
fid2 = '/Users/zhuxinquan/Desktop/招聘信息/停用词调整_招聘.txt'
stopword = {}
fid2 = open(fid2,'r')
for j in fid2.readlines():
    #stopword.append(j.strip().decode("utf-8"))  # 储存停用词表
    stopword[j.strip().decode("utf-8")]= 1

def stop_word(line):
    data_line = line.strip()
    wordList = jieba_fast.cut(data_line)  # wordlist是一个生成器
    outStr = ''
    for word in wordList:
        if word not in stopword:
            outStr += word
            outStr += ' '
    lineOut = outStr.strip().encode('utf-8')
    return lineOut





if __name__ == '__main__':
    t1 = time.time()
    fread = open('/Users/zhuxinquan/Desktop/房屋租售/房屋租售1.txt','r')
    #fwrite  = open('/Users/zhuxinquan/Desktop/房屋租售/房屋租售_分词.txt','w')
    for line in fread.readlines():
        line = line.strip().decode('utf-8')
        result = stop_word(line)
        print result
#fwrite.close()





