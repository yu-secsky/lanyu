

def test1():
    print('1-7')
    st = input('请输入:')
    for i in st:
        i = i.replace('1', '8')
        i = i.replace('2', '9')
        i = i.replace('3', '0')
        i = i.replace('4', 'q')
        i = i.replace('5', 'w')
        i = i.replace('6', 'e')
        i = i.replace('7', 'r')
        print(i, end='')
def test2():
    print('8-r')
    st = input('请输入:')
    for i in st:
        i = i.replace('8', 't')
        i = i.replace('9', 'y')
        i = i.replace('0', 'u')
        i = i.replace('q', 'i')
        i = i.replace('w', 'o')
        i = i.replace('e', 'p')
        i = i.replace('r', 'a')
        print(i, end='')

def test3():
    print('t-a')
    st = input('请输入:')
    for i in st:
        i = i.replace('t', 's')
        i = i.replace('y', 'd')
        i = i.replace('u', 'f')
        i = i.replace('i', 'g')
        i = i.replace('o', 'h')
        i = i.replace('p', 'j')
        i = i.replace('a', 'k')
        print(i, end='')

def test4():
    print('s-k')
    st = input('请输入:')
    for i in st:
        i = i.replace('s', 'l')
        i = i.replace('d', 'z')
        i = i.replace('f', 'x')
        i = i.replace('g', 'c')
        i = i.replace('h', 'v')
        i = i.replace('j', 'b')
        i = i.replace('k', 'n')
        print(i, end='')


def zhuanhuan():
    st = input('请输入:')
    for i in st:
        i = i.replace('s', 'l')
        i = i.replace('d', 'z')
        i = i.replace('f', 'x')
        i = i.replace('g', 'c')
        i = i.replace('h', 'v')
        i = i.replace('j', 'b')
        i = i.replace('k', 'n')
        print(i, end='')

if __name__ == '__main__':
    print('1\t8\tt\ts\tl')
    print('2\t9\ty\td\tz')
    print('3\t0\tu\tf\tx')
    print('4\tq\ti\tg\tc')
    print('5\tw\to\th\tv')
    print('6\te\tp\tj\tb')
    print('7\tr\ta\tk\tn')
    # 1-7
    # test1()

    # 8-r
    # test2()

    # t-a
    # test3()

    # s-k
    # test4()
    # num = [];
    # i = 2
    # for i in range(100, 201):
    #     j = 2
    #     for j in range(2, i):
    #         if (i % j == 0):
    #             break
    #     else:
    #         num.append(i)
    # print(num)