
from utils import U
from policies.five import Policy
from collections import Counter 

class Policy(Policy):

    def load(self):
        super().load()
        #Minimum length of retained words
        self.minLen = 5
        #Maximum length of retained words
        self.maxLen = 7
        
        #Minimum appearances for a word do be retained
        self.minAppearances = 4
        
        #Minimum appearances of a word for the big string to be retained
        self.stopAppearances = 7
        #Length checked for the stopAppearances configuration
        self.stopApprearanceForLen = 6
        
        #Loops operated with this configuration
        self.massResearchLoops = 10
        
        #Size of the big string of "random" chars
        self.strLen = 200000 #200.000
        
        #Name of the policy
        self.name = 'Policy six - Mass research loop'
        
    def validInStrUntil(self, names):
        final = names
        while self.massResearchLoops > 0:
            print('******* massResearchLoops ' + str(self.massResearchLoops))
            self.massResearchLoops -= 1
            toadd = self.validInStrUntilInMass(names)
            final = Counter(final) + Counter(toadd)
        return final
        
    def validInStrUntilInMass(self, names):
        reflect = True
        toadd = super().validInStr(self.util.generateString(self.alphabetJson, self.strLen))
        final = Counter(names) + Counter(toadd)
        for name, value in dict(final).items():
            if reflect and len(name) == self.stopApprearanceForLen and value >= self.stopAppearances:
                reflect = False
                break
        if reflect:
            return self.validInStrUntilInMass(final)
        for name, value in dict(final).items():
            if value < self.minAppearances:
                del final[name]
        return final