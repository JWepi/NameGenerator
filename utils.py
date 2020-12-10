
from json_util import JU
from random import randrange
import math

class U:

    def __init__(self):
        print('U init')
        self.jsonU = JU()
        
    def isNb(self, nb):
        try:
            int(nb)
            return True
        except ValueError:
            return False
            
    def setConst(self, prop, val):
        self.jsonU.setPropValInFile('consts.json', prop,  val)
        
    def getConst(self, prop):
        return self.jsonU.getValFromPropInFile('consts.json', prop)
        
    def getRand(self):
        return randrange(100) + 1
        
    def getItemFromListAtPosition(self, list, pos):
        flag = 0
        for item in list:
            flag += item['chances']
            if pos <= flag:
                return item
        return None

    def generateString(self, alphabetJson, strLen):
        it = 0
        randString = ''
        while it < strLen:
            randString += self.getItemFromListAtPosition(self.getItemFromListAtPosition(alphabetJson['letters'], self.getRand())['subchances'], self.getRand())['char']
            it += 1
            if it % 100 == 0:
                completed = math.ceil(it/strLen*100)
                print('Generating string %d%% \r'%completed, end="")
        return randString