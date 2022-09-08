
import sys
from enum import Enum

class Pair(Enum):
    value = 'value'
    union = 'union'
    all_args = 'all_args'

class Predefined(Enum):
    true = '[true]'
    false = '[false]'
    null = '[null]'


class PyParse:
    def __init__(self, args, pair=Pair.value):
        self.declared_arguments = {}
        self.undeclared_arguments = {}
        self.all_args = self.undeclared_arguments | self.declared_arguments
        self.pair = pair
        self.args = args

    def parse(self):
        
        if self.pair == Pair.value:
            return self.__value_pairs()
        elif self.pair == Pair.union:
            return self.__union_pairs()
        elif self.pair == Pair.all_args:
            pass

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
        return self.declared_arguments[argument]['contents']

    def __value_pairs(self):

        ignored = []
        arg:str
        i:int
    
        
        for key in self.declared_arguments.keys():
            for i, arg in enumerate(self.args):
                if arg == key:
                    if self.args[i+1] == Predefined.true:
                        self.undeclared_arguments[key]['contents'] = True
                    elif self.args[i+1] == Predefined.false:
                        self.undeclared_arguments[key]['contents'] = False
                    elif self.args[i+1] == Predefined.null:
                        self.undeclared_arguments[key]['contents'] = None
                    else:
                        self.undeclared_arguments[key]['contents'] = self.declared_arguments[key]['type'](self.args[i+1])
                else:
                    ignored.append(arg)



    def __union_pairs(self):

        pairs = {}
        all_ = []
        arg:str
        i:int
    
        for i, arg in enumerate(self.args):
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
                            if self.args[i+1] == Predefined.true:
                                self.declared_arguments[key]['contents'] = True
                            elif self.args[i+1] == Predefined.false:
                                self.declared_arguments[key]['contents'] = False
                            elif self.args[i+1] == Predefined.null:
                                self.declared_arguments[key]['contents'] = None
                            else:
                                self.declared_arguments[key]['contents'] = self.declared_arguments[key]['type'](self.args[i+1])
                    
        return pairs



a = PyParse(sys.argv, pair=Pair.union)
a.add_argument('--test', type=int, discriminator=':', usage="test 123")
a.add_argument('--test2', type=int, discriminator="=", usage="test 1234")
a.parse()

print(a.contents('--test') + a.contents('--test2'))