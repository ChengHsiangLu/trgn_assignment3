import sys
import re
import fileinput
from matplotlib import pyplot as plt

if sys.argv[1][0:2] == "-f":
    column_number = int(re.findall(r'\d+',sys.argv[1])[0])
    f_opt=1
else:
    column_number = 2
    f_opt=0
    
column=[]  
expres= sys.argv[1+f_opt]
for line in fileinput.input(expres):
    org_data = re.sub(r"(ENSG\d+)\.\d*", r"\1", line)
    org_data = re.split(',',org_data.replace( '"' ,'').replace('\n',''))

    if org_data[0] == '': 
        continue
    else:
        column.append(float(org_data[column_number-1]))
        
# print(column)


fig, ax=plt.subplots(figsize=[10,10])
ax.hist(column,color="grey")
fig.savefig('final_HIS.png')
