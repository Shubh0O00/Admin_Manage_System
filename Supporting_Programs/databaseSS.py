import pandas as pd
import os
from itertools import chain

def write_to_file(dictionary,file):
    file=file+'.csv'
    df=pd.DataFrame(dictionary)
    #print(df)
    df.to_csv(file, mode='a', index=False, header=False)

'''
file : name of file
attribute: column in which value need to be searched
value: value to be searched

@ return a list with all entries except ""value""
'''
def search(file,attribute,value):
    file=file+".csv"
    data=pd.read_csv(file,index_col =attribute)  
    #print(file,attribute,value)    
    try:
        rows=data.loc[value]
        a=rows.tolist()
        #a.insert(0,name)
        return(a)
    except:
        return(["Not Available","Not Available","Not Available","Not Available","Not Available","Not Available","Not Available","Not Available","Not Available","Not Available","Not Available","Not Available"])
    
def deleteRecord(file,value):
    if (search(file,"roll number",value)==["Not Available","Not Available","Not Available","Not Available","Not Available","Not Available","Not Available","Not Available","Not Available","Not Available","Not Available","Not Available"]):
        print("RECORD NOT PRESENT")
        return
    file=file+'.csv'
    f_out=open("temp.csv",'w')
    with open(file,'r') as fp:
        for line in fp:
            stripped_line = line.strip()
            line_list = stripped_line.split(',')
            if line_list[2]==value:
                pass
            else:
                line_list_mod=(',').join(line_list)
                f_out.write(line_list_mod+'\n')
        fp.close()
        f_out.close()
        try:
            os.remove(file)
            os.rename(r"temp.csv",file)
        except Exception as e:
            print(e)
        finally:
            return("RECORD DELETED SUCCESSFULLY")
           
def modify_details(file,value,dic):
    if(search(file,"roll number", value)==["Not Available","Not Available","Not Available","Not Available","Not Available","Not Available","Not Available","Not Available","Not Available","Not Available","Not Available","Not Available"]):
        print("Record Not Present")
        return
    file=file+'.csv'
    f_out=open("new.csv",'w')
    with open(file,'r') as fp:
        for line in fp:
         stripped_line = line.strip()
         line_list = stripped_line.split(',')
         if line_list[2]==value:
             f_out.write((",").join(list(chain.from_iterable(dic.values())))+'\n')
         else:
             line_list_mod=(',').join(line_list)
             f_out.write(line_list_mod+'\n')
    fp.close()
    f_out.close()
    os.remove(file)
    os.rename(r"new.csv",file)
    
def get_details(file):
    file=file+'.csv'
    with open(file,'r') as fp:
       line=[(r.strip('\n')).split(',') for r in fp]
       length=len(line)
       dictionary={i:line[i] for i in range(1,length)}
       return(length-1,dictionary)