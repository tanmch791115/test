__author__ = 'tanmch791115'
from itertools import combinations,permutations
def main(digits='123456789',total=100):
    result=set()
    length=len(digits)
    for k in range(1,length):
        for item in combinations(range(1,length),k):
            tempDigits=digits
            operands=[]
            for i in item[::-1]:
                operands.append(tempDigits[i:])
                tempDigits=tempDigits[:i]
            operands.append(tempDigits)
            operands.reverse()
            for operator in permutations('+-'*k,k):
                exp=''.join((d+o for d,o in zip(operands,operator))) +operands[-1]
                if exp not in result and eval(exp)==total:
                    print (exp,'=',total)
                    result.add(exp)

if __name__=="__main__":
    main()