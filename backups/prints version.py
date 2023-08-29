import os


class Laptop:
    def __init__(self, name, id, key, date):
        self.name = name
        self.id = id
        self.key = key
        self.date = date

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

        timeOfCreation = os.path.getctime(f)

        try:
            new = Laptop(short.strip(), content[17].strip().replace("\x00",""), content[33].strip().replace("\x00",""), timeOfCreation)
            if(new.name in last.name or last.name in new.name):
                print("old "+last.name+": "+str(last.date)+" , new "+ new.name+": "+str(timeOfCreation))
                if last.date > new.date:
                    broken.append(new)
                    print("keeping old")
                else:
                    print("debug")
                    if len(new.name) > len(last.name):
                        print("changing name from "+ new.name +" to "+last.name)
                        new.name = last.name
                    else:
                        print(new.name + " is shorter than " + last.name)

                    print("meow")
                    laptops.pop()
                    broken.append(last)
                    laptops.append(new)
                    print("keeping new")
                    last = new
            else:
                laptops.append(new) 
                last=new 


        except:
            print("error: "+short)  
            broken.append(Laptop(short.strip(),"", "","")) 

result=open("laptops.csv","x")
for computer in laptops:
    if(computer.id==""or computer.key=="" or " " in computer.id or " " in computer.key):
        broken.append(computer)
        laptops.remove(computer)
    else:
        result.write(computer.name+";"+computer.id.strip()+";"+computer.key.strip()+"\n")

errors=open("broken.csv","x")
for puter in broken:
    errors.write(puter.name+";"+puter.id.strip()+";"+puter.key.strip()+"\n")