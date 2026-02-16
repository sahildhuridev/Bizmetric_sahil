d = [1,2,3,4,5]

def sub2(*d):
    tot = 0
    for i in d:
        tot += i
        print(i,tot)
        return tot
    

def sub3(*d):
    tot = 0
    for i in d:
        tot += i
        print(i,tot)
        yield f'{tot} first time'
        yield f'{tot} second time'
        yield f'{tot} third time'
        yield f'this is the fourth time'

