import os

class Laptop:
    def __init__(self, name, id, key, date):
        self.name = name
        self.id = id
        self.key = key
        self.date = date

#checking if key/id is real and not empty or random text (happens when there was an error generating text file)
class CheckIdKey: #returns true if data is broken
    def check(item):
        return (item.id==""or item.key=="" or " " in item.id or " " in item.key)

directory = 'blbecek' #path to folder
#filesList=[]
laptops=[] #correct list
broken=[] #list of laptops with missing/old id/key
last=Laptop("Název v síti","BitLocker Id", "BitLocker Key", "")
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    if os.path.isfile(f):
        short=filename.upper().replace(".TXT","")

        line_numbers=[17,33] #lines with id and key
        with open(f) as file:
            content=file.readlines()

        timeOfMod = os.path.getmtime(f)

        try: #some files are empty or just wrong
            new = Laptop(short.strip(), content[17].strip().replace("\x00",""), content[33].strip().replace("\x00",""), timeOfMod) 
            if(new.name in last.name or last.name in new.name):
                if len(new.name) > len (last.name):
                    new.name=last.name
                else:
                    laptops[-1].name=new.name
                if last.date > new.date: #if the last one was created later, putting the new in my error list (new is older)
                    #checking if last is key/id ok so i can trash new
                    if(CheckIdKey.check(last)):
                        if(CheckIdKey.check(new)): 
                            broken.append(new)
                        else:
                            if laptops[-1] == last:
                                laptops.pop() #nevivm jestli je last vubec v laptops
                            broken.append(last)

                            laptops.append(new)
                            last = new
                    else:
                        broken.append(new)
                        # #might have to change last names to new name tho
                        # if len(last.name) > len (new.name):
                        #     print("changed name from "+last.name+" to "+new.name)
                        #     laptops[-1].name=new.name #not sure jestli funguje jestli to nejak nevytvori nejakou kopii

                else:
                    # if len(new.name) > len(last.name): #checking names so they dont end with _NEW-1 etc
                    #     new.name = last.name

                    if(CheckIdKey.check(new)): 
                        broken.append(new)
                    else:
                        if laptops[-1] == last:
                            laptops.pop()
                        broken.append(last)
                        laptops.append(new)
                        last = new
            else:
                if(CheckIdKey.check(new)):
                    broken.append(new)
                else:
                    laptops.append(new) 
                last=new 

        except:
            err=Laptop(short.strip(),"", "","")
            if(err.name in last.name or last.name in err.name):
                if len(err.name) > len (last.name):
                    err.name=last.name
            print("error: "+err.name)  
            broken.append(err) 
            last.name=err.name
            last.id=err.id
            last.key=err.key

result=open("laptops.csv","x")
for computer in laptops:
        result.write(computer.name+";"+computer.id.strip()+";"+computer.key.strip()+"\n")

errors=open("broken.csv","x")
for puter in broken:
    errors.write(puter.name+";"+puter.id.strip()+";"+puter.key.strip()+"\n")

#TODO
# DTPC0NE2NH_1 doesnt change, its older but the new one is broken :c