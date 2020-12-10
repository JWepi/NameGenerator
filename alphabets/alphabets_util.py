
from utils import U
from json_util import JU
from os import listdir
from os.path import isfile, join

class AU:

    def __init__(self):
        print('AU init')
        self.utils = U()
        self.jsonU = JU()
    
    def askAlphabet(self):
        onlyfiles = [f for f in listdir('alphabets') if isfile(join('alphabets', f)) and f != 'alphabets_util.py']
        it = 1
        print('\n----------\nChoose an alphabet to use to generate string:')
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
                toret = file
            flag += 1
        print('----------\n')
        return toret
        
    def checkAlphabetValidity(self, alphabetFile):
        alphabet = self.getAlphabetJson(alphabetFile)
        try:
            self.name = alphabet['name']
            tot = 0
            for cat in alphabet['letters']:
                subtot = 0
                tot += cat['chances']
                if (tot > 100):
                    print('Chances are above 100 for categories total')
                    return False
                for subcat in cat['subchances']:
                    subtot += subcat['chances']
                    if (subtot > 100):
                        print('Chances are above 100 for sub-category with chars ' + str(cat['chars']))
                        return False
                if (subtot < 100):
                    print('Chances are below 100 for sub-category with chars ' + str(cat['chars']))
                    return False
            if tot < 100:
                print('Chances are below 100 for categories total')
                return False
            return True
        except:
            print('Something is wrong ...')
            return False
            
    def getAlphabetJson(self, alphabetFile):
        return (self.jsonU.getFromJsonFile('alphabets/'+alphabetFile))
            
            
            
            