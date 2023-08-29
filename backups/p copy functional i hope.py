import os
import copy


class Laptop:
    def __init__(self, name, id, key, date):
        self.name = name
        self.id = id
        self.key = key
        self.date = date


directory = 'blbecek'
laptops = []
broken = []
last = Laptop("", "", "", 0)

for filename in os.listdir(directory):  # cycling through the whole folder

    # variable that holds true path to file
    filepath = os.path.join(directory, filename)

    if os.path.isfile(filepath):
        new = Laptop("", "", "", "")
        new.name = (filename.upper().replace(".TXT", "").strip()[:10])  # laptop name without extension

        lines = [17, 33]  # lines of ID and KEY

        with open(filepath) as f:
            content = f.readlines()  # open file, save to content, close file

        new.date = os.path.getmtime(filepath)
        print(last.name)
        if (len(content) == 48):  # content is okay
            print(new.name+": OK"+str(len(new.name)))
            new.id = content[17].strip().replace("\x00", "")
            new.key = content[33].strip().replace("\x00", "")
            temp = copy.deepcopy(laptops)
            temp.append(last)
            if (len(laptops) > 0):
                print(temp[-1].name+" this is last item")
                print(temp[0].name+" first item in laptops")
                print(str(len(temp))+" is the current laptops count")
            if (temp[-1].name == new.name):
                if (temp[-1].date > new.date):  # true if last is newer
                    broken.append(new)
                else:
                    if (len(laptops) > 0):
                        laptops.pop()
                        print("pop")
                    laptops.append(new)
                    broken.append(temp[-1])
            else:
                laptops.append(new)

        else:
            print(new.name+": err" + str(len(new.name)))  # content is wrong
            # save name to last and rest is empty
            # names are all good so i dont need to save it at all if its broken
            broken.append(new)


for e in laptops:
    print(e.name)
    print("hi")


result = open("laptops.csv", "x")
for computer in laptops:
    result.write(computer.name+";"+computer.id.strip() +
                 ";"+computer.key.strip()+"\n")

errors = open("broken.csv", "x")
for puter in broken:
    errors.write(puter.name+";"+puter.id.strip()+";"+puter.key.strip()+"\n")
