
from utils import U
from policies.three import Policy
from collections import Counter 

class Policy(Policy):

    def load(self):
        super().load()
        self.minLen = 6
        self.maxLen = 7
        self.minAppearances = 4
        self.stopAppearances = 7
        self.strLen = 200000 #200.000
        self.name = 'Policy four - Another angle'