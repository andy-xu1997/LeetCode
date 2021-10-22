#分析 ：想用数学的方式来解决这个问题 获取到输入的数字后 分析数字的长度length 之后


n = 112233445566
def countAndSay(n):
    array = [] #数组 用来记录算出的结果 最后输出
    length = len(str(n)) #输入数字的长度
    count = 0 #用来计数
    while (n != 0 ):    #当数字没有递减到0 的时候程序一直运行
        t = n // (10 ** (length-1)) # t 是用来记录现在最高位的数字 并且跟之前的最高位进行判断
        count +=1

        if
        array.append(t)
        n = n - t *(10 ** (length-1))
        length -=1

    print(array)




countAndSay(n)
