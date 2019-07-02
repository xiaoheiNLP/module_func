#-*-coding:utf-8-*-
'''
排序去重



'''
fall = open('/Users/zhuxinquan/Desktop/汇总词库/2/vulgar2.txt','r')
fw = open('/Users/zhuxinquan/Desktop/汇总词库/2/vulgar3.txt','w')
lines = fall.readlines()

wordlist = []

for line in lines:
    line = line.strip()
    if len(line) != 0:
        wordlist.append(line)
print len(wordlist)
wordlist = set(wordlist)
print len(wordlist)
wordlist = sorted(wordlist)
for i in wordlist:
    fw.write(i+'\n')


fw.close()

