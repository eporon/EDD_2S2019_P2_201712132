
import hashlib
import sys
import datetime
import json 
import os
import csv
import time
import Blockchain
from Blockchain import LinkedList
import Block
from Block import Block 
import AVL
from AVL import create_avl_tree,create_random_node_list

noindex=-1
bc = LinkedList()
def ReadFile(filename,index,pvh):
   try:   
      f_input = open(nombrearchivo +'.csv','r')
      nameclass = f_input.readline().strip()
      data = ""
      for line in f_input:
         line = line.strip()
         line = line.strip(" ")
         line = line.lstrip()
         line = line.rstrip('\n')
         data = data + line
      f_input.close()
      datenow = datetime.datetime.now()
      date = "{}-{}-{}-::{}:{}:{}".format(datenow.day, datenow.month, datenow.year,datenow.hour,datenow.minute,datenow.second)
      hash = hashlib.sha256(b"mehhfge").hexdigest()
      bloque = Block(index,date,nameclass.strip('class,'),data.strip('data,'),"",hash)
      print(data)
      return bloque
   except IOError:
      print('Su archivo de carga No existe')

if __name__ == "__main__":

    bandera = True
    
    while(bandera):
       print("\t\t"+"*"*5 +" MAIN MENU " + "*"*5)
       print("\t\t"+"*    "+"           "+ "    *")
       print("\t\t"+"*    "+" 1-Insert  "+ "    *")
       print("\t\t"+"*    "+" 2-Select  "+ "    *")
       print("\t\t"+"*    "+" 3-Report  "+ "    *")
       print("\t\t"+"*    "+" 4-Exit    "+ "    *")
       print("\t\t"+"*    "+"           "+ "    *") 
       print("\t\t"+"*"*5 +"***********" + "*"*5)
       opcion = int(input("Enter your selected option: "))
       if(opcion is 1):
          os.system ("cls") 
          print("\t\t"+"*    "+" 1-Insert  "+ "    *")
          nombrearchivo = input("Input name file: ") 
          noindex = noindex +1
          if(bc.is_Empty):
             bloque = ReadFile(nombrearchivo,noindex,"0000")
             bloque.CreateBlock()
          else:
             pvh = bc.get_last()
             bloque = ReadFile(nombrearchivo,noindex,pvh)
             bloque.CreateBlock()
          time.sleep(2)
       if(opcion is 2):
          os.system ("cls") 
          bandera = False
       if(opcion is 3):
          os.system ("cls") 
          bandera = False
       if(opcion is 4):
          os.system ("cls") 
          bandera = False


    '''
    jsonData = '{"value": "201403525-Nery", "left": {"value": "201212963-Andres", "left": {"value": "201005874-Estudiante1", "left": "None", "right": "None"}, "right": {"value": "201313526-Alan", "left": "None", "right": "None" } }, "right": {"value": "201403819-Anne", "left": {"value": "201403624-Fernando", "left": "None", "right": "None"}, "right": {"value": "201602255-Estudiante2", "left": "None", "right": "None" } } }'
    jsonToPython = json.loads(jsonData)   
    print(jsonToPython['value'])
    '''
    
    '''
      aList=[]
      with open(filename +'.csv', 'r') as f:
         reader = csv.reader(f, skipinitialspace=False,delimiter=';', quoting=csv.QUOTE_NONE)
         for row in reader:
            aList.append(row)
         return(aList)
          '''