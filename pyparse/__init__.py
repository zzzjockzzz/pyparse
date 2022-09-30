
import warnings,sys
from enum import Enum

__all__ = ['PyParse', 'Pair']

warnings.simplefilter('always', DeprecationWarning)

class ArgException(Exception):
  """base exception class"""
  pass

class Pair(Enum):
    value = "<type 'value_args'>"
    union = "<type 'union_args'>"
    all_args = "<type 'all_args'>"




def disable_warnings():
    warnings.filterwarnings("ignore")

class PyParse:
    def __init__(self, args, pair=Pair.union):
        self.declared_arguments = {}
        self.undeclared_arguments = {}
        self.default_discriminator = None
        self.usage = f"USAGE:\n\t{sys.executable} {__file__}"
        for i in self.declared_arguments.keys():
          self.usage += f"{i} : type:{self.declared_arguments[i]['contents']}\n"
        #self.all_args = self.undeclared_arguments | self.declared_arguments
        self.pair = pair
        self.arguments = args
        self.ignored = self.get_ignored_values()
        self.default_discriminator = '='

    def parse(self):
        for key in self.declared_arguments.keys():
            if self.pair == Pair.value:
                self.__value_pairs()
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
            .replace('.','_'), self.undeclared_arguments[key]['contents'])
            elif self.pair == Pair.union:
                self.__union_pairs()
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
            .replace('.','_'), self.declared_arguments[key]['contents'])
                self.__requirement_check()

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
        self.__requirement_check()

      
    def add_argument(self, argument, type=str, usage="use", requirement=False, discriminator="=", no_usage=False):
        if self.pair == Pair.value and discriminator != None:
            raise Exception("Discriminator not allowed for value pairs")
        if self.pair == Pair.union and discriminator == None:
            raise Exception("Discriminator required for union pairs")
        else:
            self.declared_arguments[argument]={
                'contents':None,
                'type':type,
                'discriminator':discriminator,
                'usage':usage,
                'requirement':requirement
            }
        if no_usage:
            pass
        else:
            self.usage += f"\n\t{argument}: {usage} :type:{type}"

    def __requirement_check(self):
      for key in self.declared_arguments.keys():
        if self.declared_arguments[key]['requirement'] == True and self.declared_arguments[key]['contents']==None:
          raise ValueError(f"Argument {key} is required")
        else:
          pass

  
    def get_ignored_values(self):

      ignored = []

      # for arg,i in enumerate(self.arguments):

      return ignored
  
    def arg_data(self, argument):
        try:
            return self.declared_arguments[argument]
        except:
            return None
        
    def contents(self, argument):
        # warnings.warn(f"contents() is deprecated, use PyParse().{argument.replace('--','__').replace('-','_')}", DeprecationWarning)
        return self.declared_arguments[argument]['contents']

    def __value_pairs(self):


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
                      try:
                        self.declared_arguments[key]['contents'] = self.declared_arguments[key]['type'](self.arguments[i+1])
                      except:
                          continue
                  
        return pairs
