import os
import copy


class Laptop:
    def __init__(self, name, id, key, date):
        self.name = name
        self.id = id
        self.key = key
        self.date = date


directory = 'files'
laptops = []
broken = []


for filename in os.listdir(directory):  # cycling through the whole folder

    # variable that holds true path to file aaaaa
    filepath = os.path.join(directory, filename)

    if os.path.isfile(filepath):
        new = Laptop("", "", "", "")
        last = Laptop("", "", "", 0)
        new.name = (filename.upper().replace(".TXT", "").strip()
                    [:10])  # laptop name without extension

        lines = [17, 33]  # lines of ID and KEY

        with open(filepath) as f:
            content = f.readlines()  # open file, save to content, close file

        new.date = os.path.getmtime(filepath)

        if (len(content) == 48):  # content is okay
            print(new.name+": OK"+str(len(new.name)))
            new.id = content[17].strip().replace("\x00", "")
            new.key = content[33].strip().replace(
                "\x00", "")  # fill new with data

            if (len(laptops) > 0):
                last = copy.deepcopy(laptops[-1])
            if (last.name == new.name):
                if (last.date > new.date):  # true if last is newer
                    broken.append(new)
                else:
                    if (len(laptops) > 0):
                        laptops.pop()
                        print("pop")
                    laptops.append(new)
                    broken.append(last)
            else:
                laptops.append(new)

        else:
            print(new.name+": err" + str(len(new.name)))  # content is wrong
            # save name to last and rest is empty
            broken.append(new)


result = open("laptops.csv", "x")
for computer in laptops:
    result.write(computer.name+";"+computer.id.strip() +
                 ";"+computer.key.strip()+"\n")

errors = open("broken.csv", "x")
for puter in broken:
    errors.write(puter.name+";"+puter.id.strip()+";"+puter.key.strip()+"\n")