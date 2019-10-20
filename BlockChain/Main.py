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
from AVL import create_avl_tree,create_random_node_list,AVLTree


global nodes_list
nodes_list = []
noindex=-1
blockchain = LinkedList()
bloqueSelect = Block()

def Yeison(jsonp):
    if(jsonp is not None):
        #print(jsonp['value'])
        nodes_list.append(jsonp['value'])
        if jsonp['right'] is not None:
            Yeison(jsonp['right'])
        if jsonp['left'] is not None:
            Yeison(jsonp['left'])


def ArrayTo():
    return nodes_list
    
def ReadFile(nombrearchivo,index,pvh):
   try:   
      rutadeubicacion = os.path.dirname(os.path.abspath(__file__))
      archivof = rutadeubicacion + '\\Bloques\\' + nombrearchivo + '.csv'
      f_input = open(archivof,'r')
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
      bloque = Block(index,str(date),str(nameclass.strip('class,')),str(data.strip('data,')),pvh,str(hash))
      return bloque
   except IOError:
      print('Su archivo de carga No existe')


if __name__ == "__main__":
    bandera = True
    while(bandera):
       os.system ("cls") 
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
          if(blockchain.is_Empty()):
             bloque = ReadFile(nombrearchivo,noindex,"0000")
             #bloque.CreateBlock()
          else:
             pvh = blockchain.get_last()
             bloque = ReadFile(nombrearchivo,noindex,pvh)
             #bloque.CreateBlock()
          time.sleep(1)
        
          blockchain.insert_at_end(noindex,bloque)
       if(opcion is 2):
          os.system ("cls") 
          opcionr = True
          bloqueSelect = blockchain.head
          while(opcionr):
             os.system ("cls") 
             print("\t\tINDEX: " + bloqueSelect.block.getIndex())
             print("\t\tTIMESTAMP: "+ bloqueSelect.block.getTime())
             print("\t\tCLASS: "+ bloqueSelect.block.getClass())
             print("\t\tDATA: "+ bloqueSelect.block.getData())
             print("\t\tPREHASH: " + bloqueSelect.block.getPH())
             print("\t\tHASH: " + bloqueSelect.block.getHash())
             print("\n\n")
             optionrulet = input("Presione 1 para siguiente y 0 para seleccionar (cualquier key para salir): ") 
             
             if((bloqueSelect is None) or optionrulet is "0" ):
                os.system ("cls")
                opcionr =False
             elif(optionrulet == "1"):
                bloqueSelect = bloqueSelect.next
                blockchain.current = bloqueSelect
                os.system ("cls")
             else:
                opcionr =False
       if(opcion is 3):
          os.system ("cls") 
          global tree 
          tree = AVLTree()
          print("\t\t"+"*"*7 +" MAIN MENU " + "*"*7)
          print("\t\t"+"*    "+"               "+ "    *")
          print("\t\t"+"*    "+" 1-BlockChain  "+ "    *")
          print("\t\t"+"*    "+" 2-Tree        "+ "    *")
          print("\t\t"+"*    "+" 3-Exit        "+ "    *")
          print("\t\t"+"*    "+"               "+ "    *") 
          print("\t\t"+"*"*5 +"***************" + "*"*5)
          opcionReport = int(input("Enter your selected option: "))
          if(opcionReport is 1):
             blockchain.Report_BlockChain()
          elif(opcionReport is 2):
             if(bloqueSelect is not None):
                jsonData = str(bloqueSelect.block.getDataComplete())
                jsonToPytho = json.loads(jsonData)  
                os.system ("cls")
                Yeison(jsonToPytho)
                nodosTree = ArrayTo()
                for palabra in nodosTree:
                   tree.insert(int(palabra[0:9]),str(palabra[10:50]))
                tree.graphTree()
                tree.Report_TrasversalIn()
                tree.Report_TrasversalPre()
                tree.Report_TrasversalPost()
                time.sleep(4)
                #JsonToTree(jsonToPytho)
             else: 
               print("NO HA SELECCIONADO UN BLOQUE")
          elif(opcionReport is 3):
              pass
          else:
              pass
       if(opcion is 4):
          os.system ("cls") 
          bandera = False
       if(opcion is 5):
          os.system ("cls")
          
         
          


   

