
from utils import U
from policies.six import Policy
from collections import Counter 

class Policy(Policy):

    def load(self):
        super().load()
        #Minimum length of retained words (CRITICAL : Below 4)
        self.minLen = 5
        #Maximum length of retained words (CRITICAL : Above 9)
        self.maxLen = 8
        
        #Minimum appearances for a word do be retained (CRITICAL : Below 3)
        self.minAppearances = 3
        
        #Minimum appearances of a word for the big string to be retained (CRITICAL : situational, but generally above 8~9,
        # if stopApprearanceForLen is above 7, and minlen below 5, should be minAppearances or minAppearances + 1 AT MOST)
        self.stopAppearances = 3
        #Length checked for the stopAppearances configuration (CRITICAL : situational, but generally above 9~10)
        self.stopApprearanceForLen = 8
        
        #Loops operated with this configuration
        self.massResearchLoops = 10
        
        #Size of the big string of "random" chars (CRITICAL : Above 250.000)
        self.strLen = 200000 #200.000
        
        #Name of the policy
        self.name = 'Policy seven - establishing a heavy configuration for fulfilling DB with various patterns'