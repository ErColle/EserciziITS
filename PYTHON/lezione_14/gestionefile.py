PATH: str = "PYTHON/lezione_14/example.txt"
mode: str = "w" # a -> append r -> read w -> read  
encoding: str = "utf-8"

file = open(PATH, mode=mode, encoding=encoding)

print(file)


# output: str = file.read()
output: str = file.write("ciaociao")  # con mode a-> aggiunge alla fine testo con mode -> w sovrascrive tutto con testo nelle parentesi  
print(output)
file.close