import PyParse,requests
root = PyParse.PyParse(sys.argv)

root.add_argument("--website",discriminator=":",requirement=True)

root.add_argument("--file",discrminator=":",requirement=True)

root.parse()

file = root.contents('--file')
website = root.contents('--website')
with open(file, "w") as f:
  f.write(requests.get(website).text)