#-*-coding:utf-8 -*-
'''
    
    利用结巴来判断词性
    
    问题1：词性的增强对结巴"posseg"模块没有影响，已经解决
    问题2：
    
    想法1：利用结巴分词的词性标注功能，给句子标记然后再进行处理，起到一个降维的作用
    
    '''


import time
from collections import Counter
import jieba
import jieba.posseg as pseg
from gensim.models import word2vec
from find_num import *
from numpy import *
from test_TextGrocery import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



#存储停用词
fid2 = '/Users/zhuxinquan/Desktop/二手市场/停用词调整_二手.txt'
stopword = {}
fid2 = open(fid2,'r')
for j in fid2.readlines():
    stopword[j.strip().decode("utf-8")] = 1

#词性的增强
jieba.load_userdict('/Users/zhuxinquan/Desktop/二手市场/mykeyword_二手.dict')
fread1 = open('/Users/zhuxinquan/Desktop/二手市场/mykeyword_二手.dict','r')
key_word = []
for line in fread1.readlines():
    line = line.strip().decode('utf-8').split()[0]
    jieba.add_word(line)



NUM = ['0','1','2','3','4','5','6','7','8','9']
pay_list = [u'价格',u'售价',u'现价',u'卖',u'以内',u'左右',u'面值',u'出售',u'转让',u'包邮',u'不包邮',u'转',u'处理',u'低于',u'卖掉']

keyword = [u'一',u'二',u'三',u'仨',u'四',u'五',u'六',u'七',u'八',u'九',u'十',u'万',u'千',u'k',u'K',u'w',u'W',]
NumInChinese = [u'一',u'二',u'三',u'仨',u'四',u'五',u'六',u'七',u'八',u'九',u'十',u'两']
tebie = [u'特价',u'低价',u'底价',u'便宜',u'白菜价',u'面议']
pay_list.extend(tebie)
model = word2vec.Word2Vec.load(u"新闻数据.model")
In_word = [u'收购',u'入手',u'求购',u'买',u'回收',u'购入']
Out_word = [u'出售',u'售',u'转让',u'出手',u'卖',u'转出',u'处理',u'销售']

all_word = Out_word+In_word+pay_list




#并列的介词
p_list = [u'或者',u'和',u'以及',u'与',u'或']

#导入量词
del_m = {}
fread = open('/Users/zhuxinquan/Desktop/二手市场/中文量词.txt','r')
for one in fread.readlines():
    one = one.strip().decode('utf-8')
    del_m[one] = 1


class process_sentence(object):
    # 遍历打印dic
    def readDic2(self, Dic):
        print('\n*打印字典*')
        keys = Dic.keys()
        for one in keys:
            print(one, Dic[one][0], Dic[one][1])
        print('*打印结束*\n')
    
    '''
        处理句子：
        1.对结巴分词不准确的地方进行弥补，例如数字、名词，以及分词上的不准确
        2.去掉一些干扰项（disturbance term）
        '''
    
    def process_sentence(self,sentence):
        #print '我'*78
        sentence = sentence.strip().decode('utf-8')
        sentence = sentence.replace(' ', '')
        words = pseg.cut(sentence)
        # 提前除去电话号码这个干扰项
        try:
            phonenum = main_phone(sentence)
        
        except:
            phonenum = 0
        #print sentence
        words_property = []
        words_value = []
        for w in words:
            if str(w.word).decode('utf-8') not in stopword:
                tmpflag = str(w.flag)
                tmpvalue = str(w.word).decode('utf-8')
                if tmpvalue == phonenum:
                    continue
                else:
                    words_property.append(tmpflag)
                    words_value.append(str(w.word).decode('utf-8'))
    
        num = 0
        while num < len(words_value):
            if words_value[num].isdigit():
                words_property[num] = 'm'
            num += 1

        # 结巴容易把量词和数字拆开，加一个函数，强行合并
        num = 0
        while num < len(words_value) - 1:
            tmp = ''.join(words_property[num:num + 2])
            if tmp == 'mm':
                if words_value[num] in del_m or words_value[num + 1] in del_m:
                    words_property.pop(num)
                    tmp1 = words_value[num] + words_value[num + 1]
                    words_value.pop(num)
                    words_value[num] = tmp1
                num += 1

            # 结巴会把小数拆开，此函强行把小数合并起来
            num = 0
            while num < len(words_value) - 1:
                if words_property[num] == 'm' and '.' in words_value[num]:
                    if words_property[num + 1] == 'm':
                        tmp = words_value[num] + words_value[num + 1]
                        # print tmp
                        words_property.pop(num)
                        words_value.pop(num)
                        words_value[num] = tmp

            num += 1

            # 对"成"的处理      今日 推荐 跑步机 9.9 成新 诚心 卖 议价-----t v n    m v     a v n
            num = 0
            while num < len(words_value):
                if num == 0:
                    num += 1
                    continue
                if words_value[num] == '成新' and words_property[num - 1] == 'm':
                    words_property.pop(num - 1)
                    words_property[num - 1] = 'oldOrNew'
                    tmp = words_value[num - 1] + words_value[num]
                    words_value.pop(num - 1)
                    words_value[num - 1] = tmp
                num += 1

            # 对中文的几成新进行优化
            num = 0
            while num < len(words_value):
                # 先改词性
                # bool(lambda x: True if x == '新' else False)
                if '成新' in words_value[num]:
                    tmp = words_value[num]
                    tmp1 = tmp.replace('成新', '').strip()
                    if tmp1 in NumInChinese:
                        # print 'I am here'
                        words_property[num] = 'oldOrNew'
                # 判断需要合并否--》合并
                # 前 九五成
                if words_property[num] == 'oldOrNew' and num != 0:
                    if len(words_value[num - 1]) == 1 and words_value[num - 1] in NumInChinese:
                        words_property.pop(num - 1)
                        tmp = words_value[num - 1] + words_value[num]
                        words_value.pop(num - 1)
                        words_value[num - 1] = tmp

                # 后 九成九
                # print len(words_value)
                #print len(words_property)
                if num + 1 < len(words_value) - 1 and words_property[num] == 'm' and '成' in words_value[num]:
                    if len(words_value[num + 1]) == 1 and words_value[num + 1] in NumInChinese:
                        words_property.pop(num + 1)
                        tmp = words_value[num] + words_value[num + 1]
                        words_value.pop(num + 1)
                        words_value[num] = tmp

            # 对'新'字的处理

            if num < len(words_value) - 1:
                x = words_value[num + 1]
                # print "I am here"
                if words_property[num] == 'm' and '成' in words_value[num] and x == '新':
                    # print bool(lambda x: True if x == '新' else False)
                    words_property.pop(num + 1)
                    tmp3 = words_value[num] + words_value[num + 1]
                    words_value.pop(num + 1)
                    words_value[num] = tmp3
                    words_property[num] = 'oldOrNew'
                num += 1

                # 去掉本身的干扰项
                #print '价格' in all_word
                count = 0
                while count < len(words_property):
                    #print words_value[count],  words_property[count]
                    if words_value[count] in all_word:
                        # print 'I am here2'
                        words_property[count] = 'dt'
                    count += 1

                # 转化成字典
                Dic = {}
                count = 0
                while count < len(words_property):
                    tmp = (words_value[count], words_property[count])
                    Dic[count] = tmp
                    count += 1
        return Dic, words_property, words_value
