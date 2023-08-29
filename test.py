import os

time1 = os.path.getmtime('_zaloha/NBPF0VURXE-1.TXT')
time2 = os.path.getmtime('_zaloha/NBPF0VURXE.TXT')
time3 = os.path.getmtime('_zaloha/NBPF0VURXE1.TXT')

print(time1)
print(time2)
print(time3)

#first one is newest so why does it delete it?
# NBPF0VURXE-1.TXT
# NBPF0VURXE.TXT
# NBPF0VURXE1.TXT

