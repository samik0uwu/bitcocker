import os

class Laptop:
    def __init__(self, name, id, key):
        self.name = name
        self.id = id
        self.key = key


directory = 'files'
filesList=[]
laptops=[]

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    if os.path.isfile(f):
        short=filename.replace(".TXT","")
        filesList.append(short)

        line_numbers=[17,33]
        lines=[]
        with open(f) as file:
            for i, line in enumerate(file):
                if i in line_numbers:
                    lines.append(line.strip().replace(" ",""))

        laptops.append(Laptop(short, lines[0], lines[1]))
        

result=open("laptops.txt","x")

for computer in laptops:
    result.write(computer.name+";"+computer.id.strip()+"\n")
    print(computer.name)
    print(computer.id)
    print(computer.key)



#read name, id and key
# with open(path_to_file) as f:
#     contents = f.readlines()
#save that line into another list

#save out that list into a csv file