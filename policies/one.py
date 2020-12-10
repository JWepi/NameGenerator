
from utils import U
from policies.default_policy import DP

class Policy(DP):

    def load(self):
        super().load()
        self.minLen = 4
        self.minAppearances = 5
        self.strLen = 1000000 #1.000.000
        self.name = 'Policy one - Min Appearances'
        
    # Override validInStr setting a minimum of appearances in the generated string
    def validInStr(self, bigstr):
        toret = super().validInStr(bigstr)
        
        for key, value in dict(toret).items():
            if value < self.minAppearances:
                del toret[key]
                
        return toret