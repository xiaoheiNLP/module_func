import pprint


def lizi():
    # 方法一：
    list1 = ['k1', 'k2', 'k3']
    list2 = ['v1', 'v2', 'v3']
    dic = dict(map(lambda x,y:[x,y],list1,list2))

    print(dic)
    # {'k3': 'v3', 'k2': 'v2', 'k1': 'v1'}

    # 方法二：
    dict(zip(list1, list2))
    #{'k3': 'v3', 'k2': 'v2', 'k1': 'v1'}

    l1 = [1, 2, 3, 4, 5, 6]
    l2 = [4, 5, 6, 7, 8, 9]

    {k:v for k,v in zip(l1,l2)}
    {1: 4, 2: 5, 3: 6, 4: 7, 5: 8, 6: 9}

    x = {1: 4, 2: 5, 3: 6, 4: 7, 5: 8, 6: 9}
    {v:k for k,v in x.items()}            # 反过来 将字典中的v和k调换
    {4: 1, 5: 2, 6: 3, 7: 4, 8: 5, 9: 6}


if __name__ == '__main__':
    list1 = ['k1', 'k2', 'k3', 'k3']
    list2 = ['v1', 'v2', 'v3', 'v4']
    pprint.pprint(dict(zip(list1, list2)))
    print(dict(map(lambda x, y: [x, y], list1, list2)))