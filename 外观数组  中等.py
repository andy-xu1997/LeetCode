#分析 ：想用数学的方式来解决这个问题 获取到输入的数字后 分析数字的长度length 之后


n = 112233445566
def countAndSay(n):
    array = []
    length = len(str(n))
    count = 0
    while (n != 0 ):
        t = n // (10 ** (length-1))
        count +=1



countAndSay(n)