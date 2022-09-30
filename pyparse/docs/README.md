# Documents
- Welcome to PyParse! PyParse is a system argument vector parsing library made in Python, heavily inspired by the argparse module.
- PyParse was made in August of 2022, and is still heavily in development, but usable!
# How to Use
To use the PyParse module, we need to start by downloading it using
``pip install PyParse`` or ``python3 -m pip install PyParse`` inside of our shell environment.

To start using PyParse, we need to import it in our code.
```py
import PyParse

```
Next, we need to inistantiate the PyParse object using
``` py
root = PyParse.PyParse(sys.argv) # our variable name does not need to be root, but is conventional.
```
**Adding an argument**

To add an argument, we need to use this following syntax
```py
root.add_argument("--hello-world", discriminator="=",type=int) # the type defualts to string, but in this case im explicitly stating that it is an integer.
"""
add_argument parameters:
  argument:str
  type:Any=str
  usage:str="Unknown"
  requirement:bool=False
  discriminator:str="="
  no_usage:bool=False
     
"""

```

**Parsing the arguments**

To parse the argument, all you need to run is
```py
root.parse()
```
And now, running ``python3 main.py --hello-world=123`` in our shell stores the value '123' inside of the '--hello-world'.

You are able to access the command line argument data using either of the following:
```py
root.contents("--hello-world")
>> 123
# or
root.__hello_world
>> 123
```

**Retrieving ignored arguments**

By default, PyParse ignores implicitly stated arguments, and appends them to a list. To access this list is simple.
Running ``python3 main.py --hello-world=123 testing 123``
```py
root.ignored
>> ["testing","123"] # list of ignored arguments
```


**Examples**

Adding two numbers together and then multiplying them by 2.
```py
import PyParse
root = PyParse.PyParse(sys.argv)

root.add_argument("--fnum",discriminator="=",type=int,requirement=True)

root.add_argument("--snum",discriminator="=",type=int,requirement=True)

root.parse()

print("The product of --fnum and --snum multiplied by 2 is: ", (root.contents("--fnum") + root.contents('--snum')) * 2)
```
``python3 add.py --fnum=2 --snum=4``
```
The product of --fnum and --snum multipled by 2 is: 12
```

Retrieve the data from a specified website and write it into a file. 
```py
import PyParse,requests
root = PyParse.PyParse(sys.argv)

root.add_argument("--website",discriminator=":",requirement=True)

root.add_argument("--file",discrminator=":",requirement=True)

root.parse()

file = root.contents('--file')
website = root.contents('--website')
with open(file, "w") as f:
  f.write(requests.get(website).text)
```
*shell*:

``python3 curl.py --website:https://jackstrating.com --file:test.html``

*test.html*:
```html
<html>
  ...
</html>
```
