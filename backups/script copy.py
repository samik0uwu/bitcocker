import os

class Laptop:
    def __init__(self, name, id, key, date):
        self.name = name
        self.id = id
        self.key = key
        self.date = date

class CheckIdKey: #returns true if data is broken
    def check(item):
        return (item.id==""or item.key=="" or " " in item.id or " " in item.key)



directory = '_zaloha' #path to folder
filesList=[]
laptops=[]
broken=[]
last=Laptop("Název v síti","BitLocker Id", "BitLocker Key", "")
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    if os.path.isfile(f):
        short=filename.upper().replace(".TXT","")
        filesList.append(short.strip())

        line_numbers=[17,33] #lines with id and key
        lines=[]
        with open(f) as file:
            content=file.readlines()

        timeOfMod = os.path.getmtime(f)

        try: #some files are empty or just wrong
            new = Laptop(short.strip(), content[17].strip().replace("\x00",""), content[33].strip().replace("\x00",""), timeOfMod) 
            if(new.name in last.name or last.name in new.name):
                if last.date > new.date: #if the last one was created later, putting the new in my error list
                    #checking if last is key/id ok so i can trash new
                    if(CheckIdKey.check(last)):
                        print("function returned false")
                    #if(last.id==""or last.key=="" or " " in last.id or " " in last.key):
                        if(new.id==""or new.key=="" or " " in new.id or " " in new.key): #checking if key/id is real and not empty or random text (happens when there was an error generating text file)
                            broken.append(new)
                        else:
                            laptops.pop()
                            broken.append(last)
                            laptops.append(new)
                            last = new
                    else:
                        broken.append(new)
                        #might have to change last names to new name tho
                        if len(last.name) > len (new.name):
                            laptops[-1].name=new.name

                else:
                    if len(new.name) > len(last.name): #checking names so they dont end with _NEW-1 etc
                        new.name = last.name

                    if(new.id==""or new.key=="" or " " in new.id or " " in new.key): #checking if key/id is real and not empty or random text (happens when there was an error generating text file)
                        broken.append(new)
                    else:

                        laptops.pop()
                        broken.append(last)
                        laptops.append(new)
                        last = new
            else:
                if(new.id==""or new.key=="" or " " in new.id or " " in new.key): #make into a function dork
                    broken.append(new)
                else:
                    laptops.append(new) 
                last=new 

        except:
            print("error: "+short)  
            broken.append(Laptop(short.strip(),"", "","")) 

result=open("laptops.csv","x")
for computer in laptops:
        result.write(computer.name+";"+computer.id.strip()+";"+computer.key.strip()+"\n")

errors=open("broken.csv","x")
for puter in broken:
    errors.write(puter.name+";"+puter.id.strip()+";"+puter.key.strip()+"\n")