
from utils import U
from os import listdir
from os.path import isfile, join

class PU:

    def __init__(self):
        print('PU init')
        self.utils = U()
    
    def askRules(self):
        onlyfiles = [f for f in listdir('policies') if isfile(join('policies', f)) and f != 'policies_util.py' and f != 'default_policy.py']
        it = 1
        print('----------\nChoose a policy file number to apply when evaluating string:')
        for file in onlyfiles:
            print(str(it) + ':' + file.split('.')[0])
            it += 1
        toret = None
        while toret == None or not self.utils.isNb(toret) or int(toret) >= it or int(toret) < 1:
            if toret:
                if self.utils.isNb(toret):
                    print('Wrong number')
                else:
                    print('Not a number')
            toret = input()
        flag = 1
        for file in onlyfiles:
            if str(toret) == str(flag):
                toret = file.split('.')[0]
            flag += 1
            
        print('----------\n')
        return toret
        