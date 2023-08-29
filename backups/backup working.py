#get all files from a folder

# import required module
import os


class Puter:
    def __init__(self, name, id, key):
        self.name = name
        self.id = id
        self.key = key

# assign directory
directory = 'files'
filesList=[]
puterList=[]
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        short=filename.replace(".TXT","")
        filesList.append(short)
        #print(f)
        line_numbers=[17,33]
        lines=[]
        with open(f) as file:
            for i, line in enumerate(file):
                if i in line_numbers:
                    lines.append(line.strip().replace(" ",""))
        # print(lines[0])
        # print(lines[1])

            # contents = file.read()
            # #print(contents)
            # print(type(contents))
        puterList.append(Puter(short, lines[0], lines[1]))
        


for computer in puterList:
    print(computer.name)
    print(computer.id)
    print(computer.key)



#read name, id and key
# with open(path_to_file) as f:
#     contents = f.readlines()
#save that line into another list

#save out that list into a csv file