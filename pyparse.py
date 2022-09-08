
import warnings,sys
from enum import Enum

warnings.simplefilter('always', DeprecationWarning)

class Pair(Enum):
    value = 'value'
    union = 'union'
    all_args = 'all_args'

class Predefined(Enum):
    true = '[true]'
    false = '[false]'
    null = '[null]'

def disable_warnings():
    warnings.filterwarnings("ignore")

class PyParse:
    def __init__(self, args, pair=Pair.value):
        self.declared_arguments = {}
        self.undeclared_arguments = {}
        self.all_args = self.undeclared_arguments | self.declared_arguments
        self.pair = pair
        self.arguments = args

    def parse(self):
        for key in self.declared_arguments.keys():
            

            if self.pair == Pair.value:
                self.__value_pairs()
                return setattr(self, key.replace('-','_')\
            .replace('--','__')\
            .replace('~','_')\
            .replace('!','_')\
            .replace('@','_')\
            .replace('#','_')\
            .replace('$','_')\
            .replace('%','_')\
            .replace('^','_')\
            .replace('&','_')\
            .replace('*','_')\
            .replace('(','_')\
            .replace(')','_')\
            .replace('+','_')\
            .replace('=','_')\
            .replace('{','_')\
            .replace('}','_')\
            .replace('[','_')\
            .replace(']','_')\
            .replace('|','_')\
            .replace('\\','_')\
            .replace(':','_')\
            .replace(';','_')\
            .replace('"','_')\
            .replace("'",'_')\
            .replace('<','_')\
            .replace('>','_')\
            .replace('?','_')\
            .replace('/','_')\
            .replace('.','_'), self.undeclared_arguments[key]['contents'])
            elif self.pair == Pair.union:
                self.__union_pairs()
                print(key)
                return setattr(self, key.replace('-','_')\
            .replace('--','__')\
            .replace('~','_')\
            .replace('!','_')\
            .replace('@','_')\
            .replace('#','_')\
            .replace('$','_')\
            .replace('%','_')\
            .replace('^','_')\
            .replace('&','_')\
            .replace('*','_')\
            .replace('(','_')\
            .replace(')','_')\
            .replace('+','_')\
            .replace('=','_')\
            .replace('{','_')\
            .replace('}','_')\
            .replace('[','_')\
            .replace(']','_')\
            .replace('|','_')\
            .replace('\\','_')\
            .replace(':','_')\
            .replace(';','_')\
            .replace('"','_')\
            .replace("'",'_')\
            .replace('<','_')\
            .replace('>','_')\
            .replace('?','_')\
            .replace('/','_')\
            .replace('.','_'), self.declared_arguments[key]['contents'])

            elif self.pair == Pair.all_args:
                
                setattr(self, key.replace('-','_')\
            .replace('--','__')\
            .replace('~','_')\
            .replace('!','_')\
            .replace('@','_')\
            .replace('#','_')\
            .replace('$','_')\
            .replace('%','_')\
            .replace('^','_')\
            .replace('&','_')\
            .replace('*','_')\
            .replace('(','_')\
            .replace(')','_')\
            .replace('+','_')\
            .replace('=','_')\
            .replace('{','_')\
            .replace('}','_')\
            .replace('[','_')\
            .replace(']','_')\
            .replace('|','_')\
            .replace('\\','_')\
            .replace(':','_')\
            .replace(';','_')\
            .replace('"','_')\
            .replace("'",'_')\
            .replace('<','_')\
            .replace('>','_')\
            .replace('?','_')\
            .replace('/','_')\
            .replace('.','_'), self.all_arguments[key]['contents'])

    def add_argument(self, argument, type=str, usage="Usage: ", discriminator=None):
        if self.pair == Pair.value and discriminator != None:
            raise Exception("Discriminator not allowed for value pairs")
        if self.pair == Pair.union and discriminator == None:
            raise Exception("Discriminator required for union pairs")
        else:
            self.declared_arguments[argument]={
                'contents':None,
                'type':type,
                'discriminator':discriminator,
                'usage':usage
            }


    def arg_data(self, argument):
        try:
            return self.declared_arguments[argument]
        except:
            return None
        
    def contents(self, argument):
        # warnings.warn(f"contents() is deprecated, use PyParse().{argument.replace('--','__').replace('-','_')}", DeprecationWarning)
        return self.declared_arguments[argument]['contents']

    def __value_pairs(self):

        ignored = []
        arg:str
        i:int
    
        
        for key in self.declared_arguments.keys():
            for i, arg in enumerate(self.arguments):
                if arg == key:
                    if self.arguments[i+1] == Predefined.true:
                        self.undeclared_arguments[key]['contents'] = True
                    elif self.arguments[i+1] == Predefined.false:
                        self.undeclared_arguments[key]['contents'] = False
                    elif self.arguments[i+1] == Predefined.null:
                        self.undeclared_arguments[key]['contents'] = None
                    else:
                        self.undeclared_arguments[key]['contents'] = self.declared_arguments[key]['type'](self.arguments[i+1])
                else:
                    ignored.append(arg)



    def __union_pairs(self):

        pairs = {}
        all_ = []
        arg:str
        i:int
    
        for i, arg in enumerate(self.arguments):
            all_.append(arg)
            for key in self.declared_arguments.keys():
                if arg == key:
                    continue
                else:
                    if arg.startswith('--') or arg.startswith('-'):
                        if key in arg:
                            temp = arg.split(self.declared_arguments[key]['discriminator'])
                            if len(temp) > 1:
                                self.declared_arguments[key]['contents'] = self.declared_arguments[key]['type'](temp[1])
                    else:
                        if arg == self.declared_arguments[key]['discriminator']:
                            if self.arguments[i+1] == Predefined.true:
                                self.declared_arguments[key]['contents'] = True
                            elif self.arguments[i+1] == Predefined.false:
                                self.declared_arguments[key]['contents'] = False
                            elif self.arguments[i+1] == Predefined.null:
                                self.declared_arguments[key]['contents'] = None
                            else:
                                self.declared_arguments[key]['contents'] = self.declared_arguments[key]['type'](self.arguments[i+1])
                    
        return pairs
