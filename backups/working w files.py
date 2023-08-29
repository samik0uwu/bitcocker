import os

class Laptop:
    def __init__(self, name, id, key):
        self.name = name
        self.id = id
        self.key = key

directory = 'files' #path to folder
filesList=[]
laptops=[]

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    if os.path.isfile(f):
        short=filename.replace(".TXT","")
        filesList.append(short.strip())

        line_numbers=[17,33] #lines with id and key
        lines=[]
        with open(f) as file:
            content=file.readlines()

        laptops.append(Laptop(short, content[17].strip().replace("\x00",""), content[33].strip().replace("\x00","")))       

result=open("laptops.csv","x")
for computer in laptops:
    result.write(computer.name+";"+computer.id.strip()+";"+computer.key.strip()+"\n")