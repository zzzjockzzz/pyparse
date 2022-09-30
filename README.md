# Welcome to PyParse!

PyParse is a argv/list parser, made purely in Python.

# USAGE

```py
# main.py
from pyparse import *

parser = PyParse(sys.argv, pair=Pair.union)
parser.add_argument(argument="--test", type=int, discriminator="=")
parser.add_argument(argument="--test2", type=int, discriminator=":")
parser.parse()

print("Value of --test and --test2 combined:", a.contents("--test") + a.contents("--test2"))
```

Running our program with:

``python main.py --test=123 --test2:123``



Outputs:

``Value of --test and --test2 combined: 246``


