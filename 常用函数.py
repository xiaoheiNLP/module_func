# -*-coding:utf-8-*-
import pymysql


# 辅助函数:正则化处理句子
def zhengzehua(a):
    b = re.compile(u"[\u4e00-\u9fa5]*")
    c = b.findall(a)
    tmpline = ''.join(c)
    tmpline = tmpline.strip()
    return tmpline


# 辅助函数：创建文件夹
def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---")
        print("---  OK  ---")

    else:
        print("---  There is this folder!  ---")





'''
数据库
'''
# 辅助函数,数据库插入
def insert_toMysql(tid, tid_base, subject, subject_base, score):
    print('*插入到数据库*')
    t1 = time.time()
    insertTime = time.strftime('%Y-%m-%d %H:%M', time.localtime(t1))
    # print subject_base
    try:
        subject_base = subject_base.encode('utf-8')
    except:
        pass

    conn = pymysql.connect(host='39.105.51.17', port=4306, user='root', passwd='wuchen123', db='NLP', charset='utf8')
    cursor1 = conn.cursor()
    sql_command = 'insert into similarity_log (insertTime, tid, tid_base, subject, subject_base , score) VALUES ( \'%s\' ,%d, %d, \'%s\', \'%s\',%f)'% (insertTime, tid, tid_base, subject, subject_base, score)

    print(sql_command)

    try:
        cursor1.execute(sql_command)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()

    cursor1.close()  # 关闭
    conn.close()

# 辅助函数,数据库更新库
def updata_toMysql():
    conn = pymysql.connect(host='39.106.0.62', port=5728, user='root', passwd='2417@gmail.com', db='ultrax',
                           charset='utf8')
    # 创建游标
    cursor1 = conn.cursor()

    fopen = open('/Users/zhuxinquan/Desktop/1.txt', 'r')
    for i in fopen.readlines():
        i = i.strip()
        i = int(i)
        tid = i

        try:
            sql_command = 'UPDATE pre_forum_post set invisible = 0 WHERE invisible != 0 and tid = {0} '.format(tid)
            print(sql_command)
            cursor1.execute(sql_command)
            conn.commit()

        except Exception as e:
            print(e)
            conn.rollback()

        print('操作pre_forum_post表 成功')

        try:
            sql_command = 'UPDATE pre_forum_thread set displayorder = 0 WHERE displayorder != 0 and tid = {0} '.format(
                tid)
            print(sql_command)
            cursor1.execute(sql_command)
            conn.commit()

        except Exception as e:
            print(e)
            conn.rollback()

        print('操作pre_forum_thread表 成功')
    cursor1.close()  # 关闭
    conn.close()


'''
日志
'''

def log_make():
    import logging
    import time
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler("zhu.txt")
    formatter1 = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
    formatter2 = logging.Formatter()

    handler.setFormatter(formatter1)
    logger.addHandler(handler)

    t1 = time.time()
    logger.info("starting")
    for i in range(0, 53):
        print(i)
        logger.info(i)

    print(time.time() - t1)
    logger.info(time.time() - t1)
    logger.info("Finish")


'''
忽略警告
'''
import warnings     # 忽略警告
warnings.filterwarnings("ignore")   # 忽略警告

'''
编码格式设定
'''
import sys
reload(sys)
sys.setdefaultencoding('utf8')




"""数据处理"""

'''
结巴分词模块
'''
import time
import jieba_fast
import jieba_fast.posseg as pseg
import sys
reload(sys)
sys.setdefaultencoding('utf8')

jieba_fast.load_userdict('/Users/zhuxinquan/Desktop/mykeyword.dict')
jieba_fast.add_word('烤鸭炉')
#存储停用词
fid2 = '/Users/zhuxinquan/Desktop/停用词调整_二手.txt'
stopword = {}
fid2 = open(fid2, 'r')
for j in fid2.readlines():
    stopword[j.strip().decode("utf-8")]= 1

def stop_word(line):
    data_line = line.strip()
    wordList = jieba_fast.cut(data_line)  # wordlist是一个生成器
    outStr = ''
    t1 = time.time()
    for word in wordList:
        if word not in stopword:
            outStr += word
            outStr += ' '
    t2 = time.time()
    lineOut = outStr.strip().encode('utf-8')
    return lineOut


# 字典排序
sorted(d.items(), key=lambda x: x[1], reverse=True)

