
from utils import U

class DP:

    def __init__(self, alphabetJson):
        self.alphabetJson = alphabetJson
        self.util = U()
        self.load()
        
    def load(self):
        self.strLen = 100000
        self.minLen = 3
        self.maxLen = 10
        self.doubles = self.getAllowedDoubles()
        self.majors = self.getMajors()
        
    #Get allowed double letters from dictionnary configuration
    def getAllowedDoubles(self):
        toret = []
        for item in self.alphabetJson['letters']:
            toret.extend(item['doubles'])
        return toret
        
    #Get major letters from dictionnary configuration
    def getMajors(self):
        for item in self.alphabetJson['letters']:
            if item['major']:
                return item['chars']
        return []
        
    #Returns the list of names which format got validated with their amount of occurence 
    def validInStr(self, bigstr):
        toret = {}
        loopnb = 0
        for pos, letter in enumerate(bigstr):
            last = self.minLen + pos
            while last <= self.maxLen + pos and pos + last < self.strLen:
                name = bigstr[pos:last]
                loopnb += 1
                #print(str(loopnb) + ': considering ' + name + ' pos=' + str(pos) + ' last=' + str(last))
                if self.validateName(name):
                    try:
                        toret[name] += 1
                    except:
                        toret[name] = 1
                last += 1
        
        return toret
        
    #Validates a name as a string by its build
    def validateName(self, name):
        prev = None
        prevprev = None
        for letter in name:
            if prev:
                if prev == letter and letter not in self.doubles:
                    return False
            if prevprev:
                if (letter in self.majors and prev in self.majors and prevprev in self.majors) or (letter not in self.majors and prev not in self.majors and prevprev not in self.majors):
                    return False
            prevprev = prev
            prev = letter
        return True
        
    #Evaluates the score of a name
    def getPointsForName(self, name):
        return 0
        
    #Returns an array of valid name with their occurences
    def getValidNames(self):
        print('getValidNames IN DP')
        return(self.validInStr(self.util.generateString(self.alphabetJson, self.strLen)))
        
    #Returns the min-max length opperated for a chosen configuration
    def getMinMaxStr(self):
        return str(self.minLen) + '-' + str(self.maxLen)