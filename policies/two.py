
from utils import U
from policies.one import Policy

class Policy(Policy):

    def load(self):
        super().load()
        self.minLen = 5
        self.minAppearances = 7
        self.strLen = 1100000 #1.100.000
        self.name = 'Policy two - Another angle'