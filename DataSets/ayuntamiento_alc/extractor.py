from tika import parser

raw = parser.from_file('contratos_antiguos-2014.pdf')

f = open("data.txt", "a")
f.write(raw['content'])
f.close()

# print(raw['content'])