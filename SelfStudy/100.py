__author__ = 'tanmch791115'
# _*_ coding: utf-8 _*_
from datetime import datetime

startTime = datetime.now()
def triAdd(operators):
    #三进制加一算法，以8个元素为例
    #列表中的数字从【0,0,0,0,0,0,0,0】变到【3,3,3,3,3,3,3,3】
    lastPosition=len(operators)-1
    c=1
    for i in range(lastPosition,-1,-1):
        c,operators[i]=divmod(operators[i]+c,3)
        if c is 0:
            return None
        #如果循环结束时c的值为1
        #表示列表已经变到【3,3,3,3,3,3,3,3】，不允许再变
    return 1
def main(digits='123456789',total=10):
    #分别在1到9之间的数字之间插入空格、-或+
    d=' +-'
    operators=[0]*((len(digits)-1))
    while not triAdd(operators):
        #对于三进制的数字列表operators
        #其中数字0对应空格，1对应+，2对应-
        operator=map(lambda o:d[o],operators)
        experession=''.join((o+c for o,c in zip(digits,operator)))+digits[-1]
        #删除表达式中的空格
        experession=''.join(experession.split())
        if eval(experession)==total:
            print (experession+'='+str(total))




if __name__=='__main__':
    main()
    endTime = datetime.now()
    executeTime = endTime - startTime
    print executeTime

