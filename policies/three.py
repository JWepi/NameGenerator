
from utils import U
from policies.default_policy import DP
from collections import Counter 

class Policy(DP):

    def load(self):
        super().load()
        self.minLen = 5
        self.maxLen = 10
        self.minAppearances = 10
        self.stopAppearances = 12
        self.strLen = 100000 #100.000
        self.name = 'Policy three - Reloading random string & stopApprearances'
        
    # Reload random strings until theres a name with stopAppearances counter,
    # then retains all words with minAppearances
    def validInStrUntil(self, names):
        reflect = True
        toadd = super().validInStr(self.util.generateString(self.alphabetJson, self.strLen))
        final = Counter(names) + Counter(toadd)
        for name, value in dict(final).items():
            if value >= self.stopAppearances:
                reflect = False
                break
        if reflect:
            return self.validInStrUntil(final)
        for name, value in dict(final).items():
            if value < self.minAppearances:
                del final[name]
        return final
        
    def getValidNames(self):
        return(self.validInStrUntil({}))