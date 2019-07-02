# -*-coding:utf-8-*-
# @Time    : 2019/7/1 0001 15:16
# @Author   :zhuxinquan
# @File    : make_random_number_1.py


# 一些简答的函数调用
def test_random_numpy_1():
    import numpy as np
    from numpy import random as nr

    # 只显示小数点后两位
    np.set_printoptions(precision=2)
    r1 = nr.rand(3, 4)
    r2 = nr.randn(5, 4)
    r3 = nr.randint(0, 10, size=(4, 3))

    print(r1)
    print()
    print(r2)
    print()
    print(r3)


# 一些分布的调用
def test_random_numpy_2():
    """
    1）normal(）　　正太分布
　　2）uniform()　　均匀分布
　　3）poisson()　　泊松分布
    """
    import numpy as np
    from numpy import random as nr

    # 只显示小数点后两位
    np.set_printoptions(precision=2)

    # 第一个参数是均值，第二个参数是标准差
    r1 = nr.normal(100, 10, size=(3, 4))
    # print(r1)

    # 前两个参数分别是区间的初始值和终值
    r2 = nr.uniform(0, 10, size=(3, 4))
    print(r2)

    # 第一个参数为指定的lanbda系数
    r3 = nr.poisson(2.0, size=(3, 4))
    # print(r3)



def test_random_numpy_3():
    """
    permutation()随机生成一个乱序数组，当参数是n时，返回[0,n)的乱序，他返回一个新数组。
    而shuffle()则直接将原数组打乱。
    choice（）是从指定的样本中随机抽取。
    """
    import numpy as np
    from numpy import random as nr

    # 只显示小数点后两位
    np.set_printoptions(precision=2)

    # 返回打乱数组，原数组不变
    r1 = nr.randint(10, 100, size=(3, 4))
    print(r1)
    print()
    nr.permutation(r1)
    print(r1)
    print()
    nr.permutation(5)

    # 使用shuffle打乱数组顺序
    x = np.arange(10)
    nr.shuffle(x)
    print(x)

    # choice()函数从指定数组中随机抽取样本
    # size参数用于指定输出数组的大小
    # replace参数为True时，进行可重复抽取，而False表示进行不可重复的抽取。默认为True
    x = np.array(10)
    c1 = nr.choice(x, size=(2, 3))
    print(c1)

    c2 = nr.choice(x, 5, replace=False)
    print(c2)


if __name__ == '__main__':
    # test_random_numpy_1()
    # test_random_numpy_2()
    test_random_numpy_3()

