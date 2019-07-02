fw = open('/Users/zhuxinquan/Desktop/weibo清洗.txt','w')
zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')
with open(u'/Users/zhuxinquan/Desktop/weibo.txt') as f:
    for line in f.readlines():
        line = line.strip()
        if line != '':
            for left in line.split('<'):
                # print('------------------------这是一条神奇的分割线------------------------')
                # print(left)
                # print('------------------------这是一条神奇的分割线------------------------')
                for right in left.split('>'):
                    if zh_pattern.search(right.decode('utf-8', 'ignore')) and right.find('=') == -1:
                        print(right)
                        fw.write(right+'\n')
                # print('='*100)
fw.close()
