import PyParse
root = PyParse.PyParse(sys.argv)

root.add_argument("--fnum",discriminator="=",type=int,requirement=True)

root.add_argument("--snum",discriminator="=",type=int,requirement=True)

root.parse()

print("The product of --fnum and --snum multiplied by 2 is: ", (root.contents("--fnum") + root.contents('--snum')) * 2)