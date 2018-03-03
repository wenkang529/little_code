#2018-3-3 white this code for renumbering Document
# use re and file reading and writing
import re
import os

filename='a.txt'
new_file='c.txt'
txt=[]
patt='\(\d+\)'
i=1
with open(filename,'r') as f:
    while True:
        line=f.readline()
        if not line:
            break
        print(line)
        new_line=re.sub(patt,'('+str(i)+')',line,1)
        print(new_line)
        i+=1
        txt.append(new_line)

with open(new_file,'w') as f:
    for i in txt:
        f.writelines(i)
# i=9
# patt='\(\d+\)'
# str1='(15)aabbewwc(3)'
# result=re.sub(patt,'('+str(i)+')',str1,1)
# print(result)