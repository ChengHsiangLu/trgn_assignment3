import sys
import fileinput
import re


if sys.argv[1][0:2] == "-f":
    column_number = int(re.findall(r'\d+',sys.argv[1])[0])
    f_opt=1
else:
    column_number = 2
    f_opt=0


    
creat_dict= sys.argv[1+f_opt]
idname_Hugo={}
for line in fileinput.input(creat_dict):

    g_id = re.findall('gene_id \"(.*?)"',line, re.I)
    g_name = re.findall('gene_name \"(.*?)"',line, re.I)
    if g_id:
        if g_name:
            idname_Hugo[g_id[0]] = g_name[0]

sample = open('final_Hugo.csv', 'w')

unit_change=sys.argv[2+f_opt]
for line in fileinput.input(unit_change):
    org_data = re.sub(r"(ENSG\d+)\.\d*", r"\1", line)
    org_data = re.split(',',org_data.replace( '"' ,'').replace('\n',''))

    if org_data[0] == '': 
        turn_into_str = str(org_data)[1:-1]
        final_text = turn_into_str.replace("\'", "")
        print(final_text, file = sample)
        continue
    if org_data[1] in idname_Hugo:

        org_data[column_number-1] = idname_Hugo[org_data[1]]



        turn_into_str = str(org_data)[1:-1]
        final_text = turn_into_str.replace("\'", "")
        print(final_text, file = sample)
sample.close()   
