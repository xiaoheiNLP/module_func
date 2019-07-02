#-*-coding:utf-8-*-
import re

punctuation = '!*,;:?"\''


def removePunctuation(text):
    text = re.sub(r'[{}]+'.format(punctuation), '', text)
    return text.strip().replace(' ','')


text = "三|陪    庞3*452659238博   "
print removePunctuation(text)