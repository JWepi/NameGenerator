
import json

class JU:

    def __init__(self):
        print('JU init')
    
    def setPropValInFile(self, filePath, prop, val):
        if self.getValFromPropInFile(filePath, prop) != None:
            with open(filePath, 'r') as of:
                obj = json.load(of)
            obj[prop] = val
            with open(filePath, 'w') as nf:
                json.dump(obj, nf)
            #print('Attribute "' + prop + '" set as "' + str(val) + '" in file "' + filePath + '"')
            
    def getValFromPropInFile(self, filePath, prop):
        with open(filePath, 'r') as f:
            obj = json.load(f)
        try:
            return(obj[prop])
        except:
            print('Attribute not found in file "' + filePath + '"')
            return None
            
    def getFromJsonFile(self, filePath):
        with open(filePath, 'r') as f:
            return json.load(f)