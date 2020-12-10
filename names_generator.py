
from utils import U
from json_util import JU
from sql_logger import SL
from alphabets.alphabets_util import AU
from policies.policies_util import PU
import importlib

class NG:

    def __init__(self):
        print('NG init')
        self.util = U()
        self.jsonU = JU()
        self.policies = PU()
        self.alphabets = AU()
        self.sqlL = SL(self.util.getConst('server'), self.util.getConst('database'))
        self.terminate = False
        self.generation = 0
        
        while not self.terminate:
            print('----------')
            alphabet = self.alphabets.askAlphabet()
            if (self.alphabets.checkAlphabetValidity(alphabet)):
                to_import = self.policies.askRules()
                policy_module = importlib.import_module('policies.'+to_import, '.')
                self.policy = policy_module.Policy(self.alphabets.getAlphabetJson(alphabet))
                self.sqlL.new_policy(self.policy.name)
                #Environment setted-------------------------------------------
                
                self.generate(alphabet)
            print('\n\n----------\nPress enter to start a new generation, type anything to terminate:\n----------')
            self.terminate = input() != ''
    
    def generate(self, alphabetFile):
        self.getNewGeneration()
        validNames = self.policy.getValidNames()
        self.saveNames(validNames)
        self.sqlL.validate_changes()
        #for name in validNames:
        
    def getNewGeneration(self):
        newGeneration = self.util.getConst('generation') + 1
        self.generation = newGeneration
        self.util.setConst('generation',  self.generation)
        self.sqlL.new_session('Session' + str(newGeneration), self.policy.getMinMaxStr(), self.alphabets.name)
        
    def saveNames(self, validNames):
        for vName, appear in dict(validNames).items():
            self.sqlL.new_name(vName, appear, self.policy.getPointsForName(vName), self.policy.name, 'generation' + str(self.generation))

generator = NG()