import os


class Laptop:
    def __init__(self, name, id, key, date, ok):
        self.name = name
        self.id = id
        self.key = key
        self.date = date
        self.ok = ok


# class Main:
#     def checkIdKey(id, key): #i might not need it anymore since i check content length
#         # check if ID and KEY are not empty and have the same length
#         return True

#     # renaming old to new, returning new laptop and broken list
#     def rename(last, new, laptops):
#         if (new.name in last.name or last.name in new.name):
#             if len(new.name) > len(last.name):
#                 new.name = last.name
#             else:
#                 laptops[-1].name = new.name

#         return laptops, new

#     # def setLast(new, last):

#     #     return last


directory = '_zaloha_complete'
laptops = []
broken = []
last = Laptop("Název v síti", "", "", "", False)
new = Laptop("", "", "", "", False)

for filename in os.listdir(directory):  # cycling through the whole folder

    # variable that holds true path to file
    filepath = os.path.join(directory, filename)

    if os.path.isfile(filepath):
        new.name = (filename.upper().replace(
            ".TXT", "").strip()[:10])  # laptop name without extension

        lines = [17, 33]  # lines of ID and KEY

        with open(filepath) as f:
            content = f.readlines()  # open file, save to content, close file

        new.date = os.path.getmtime(filepath)

        if (len(content) == 48):  # content is okay
            print(new.name+": OK"+str(len(new.name)))
            #  new = Laptop(short.strip(), content[17].strip().replace(
            #     "\x00", ""), content[33].strip().replace("\x00", ""), timeOfMod)

            #check time of last and new also? wait

        else:
            print(new.name+": err" +str(len(new.name)))  # content is wrong
            # save name to last and rest is empty




