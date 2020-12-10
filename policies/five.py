
from utils import U
from policies.four import Policy
from collections import Counter 

class Policy(Policy):

    def load(self):
        super().load()
        self.minLen = 4
        self.maxLen = 10
        self.minAppearances = 3
        self.stopAppearances = 8
        self.strLen = 200000 #200.000
        self.stopApprearanceForLen = 6
        self.name = 'Policy five - Stop with appearance for length'
        
    def validInStrUntil(self, names):
        reflect = True
        toadd = super().validInStr(self.util.generateString(self.alphabetJson, self.strLen))
        final = Counter(names) + Counter(toadd)
        for name, value in dict(final).items():
            if reflect and len(name) == self.stopApprearanceForLen and value >= self.stopAppearances:
                reflect = False
                break
        if reflect:
            return self.validInStrUntil(final)
        for name, value in dict(final).items():
            if value < self.minAppearances:
                del final[name]
        return final