import os
import Open_Files
from Open_Files import open_file,start_file
import Block
from Block import Block 

class Node:
    def __init__(self,indice = None,block = Block()):
        self.next = None
        self.prior = None
        self.indice = indice 
        self.block = block

    def See_Node(self):
        return self.indice


class LinkedList:

    def __init__(self):
        self.head = None
        self.last = None
        self.sizesBlockchain= 0


    def is_Empty(self): #Pregunga si la lista esta vacia
        if self.head == None:
            return True
        else:
            return False


    def insert_first(self,indice,block): #Inserta el nodo en la cabeza de la lista
        self.sizesBlockchain+=1
        temp = Node(indice,block)
        if self.is_Empty() == True:
            self.head = temp

        else:
            temp.next = self.head
            self.head.prior =temp
            self.head =temp
        aux = self.head
        while aux!=None:
            if(aux.next is None):
                self.last = aux
            aux = aux.next

    def delete_first(self):  #Elimina elementos desde la cabeza
        self.sizesBlockchain-=1
        if self.is_Empty()==False:
            self.head = self.head.next
            self.head.prior = None

    def delete_last(self): #Elimina Elmenetos desde la cola
        self.sizesBlockchain-=1
        if self.head is None:
            print("The list has no element to delete")
            return
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.prior.next = None

    def get_last(self):
        n = self.head
        while n.next is not None:
            n = n.next
        return n.block.HASH

    def delete(self,pos): #Elimina Elementos desde determinada posicion
        self.sizesBlockchain-=1
        prior = self.head
        current = self.head
        k=0
        if pos>0:
            while k !=pos and current.next !=None:
                prior = current
                current = current.next
                k+=1
            if k==pos:
                temp = current.next
                prior.next = current.next
                temp.prior = prior



    def list_node(self): #Lista los elementos desde la cabeza
        print('*'*10)
        temp = self.head
        print('[',end=' ')
        while temp!=None:
            print("[%s,%s],"%(temp.indice,temp.indice),end='')
            temp = temp.next
        print(']')


    def insert_at_end(self,indice,block): #Inserta elementos al final de la lista
        self.sizesBlockchain+=1
        if self.head is None:
            new_node = Node(indice,block)
            self.head = new_node
            self.last = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        new_node = Node(indice,block)
        n.next = new_node
        new_node.prior = n
        self.last = new_node


    def Report_BlockChain(self): #Genera el Archivo .dot para la lista doble enlazada y Genera la Imagen
            nodonum =0
            f_output = open('BlockChain.txt','w')
            f_output.write("digraph{\n node[shape = record,style=filled];")
            f_output.write("label = \"BLOCKCHAIN\"; \n")
            f_output.write("\n")
            aux = self.head
            #Imprimir Nodos
            while aux:
                contenido = "CLASS= %s\\nTIMESTAMP= %s\\nPSHASH= %s\\nHASH= %s"%(aux.block.CLASS,aux.block.TIMESTAMP,aux.block.PREVIOUSHASH[0:40],aux.block.HASH[0:40])
                f_output.write("\t\t a%d[label=\"{|%s|}\"];\n"%(nodonum,contenido))
                aux = aux.next
                nodonum+=1
            #Enlazar Nodos
            for i in range(0,nodonum):
                if i==0 and i != nodonum-1:
                     f_output.write("\t\t a%s->a%s[color=\"crimson\"];\n"%(i,i+1))
                elif(i!=nodonum-1):
                     f_output.write("\t\t a%s->a%s[color=\"crimson\"];\n"%(i,i+1))
                     f_output.write("\t\t a%s->a%s[color=\"crimson\"];\n"%(i,i-1))
                else:
                    if(i==nodonum-1 and i!=0):
                        f_output.write("\t\t a%s->a%s[color=\"crimson\"];\n"%(i, i-1))
            f_output.write("\t }")
            f_output.close()

            commandfile = 'dot -Tpng BlockChain.txt -o BlockChain.png'
            start_file(commandfile)
            path = 'BlockChain.png'
            open_file(path)
'''
bc = LinkedList()
bloque = Block(0,"date","nameclass","data","0000","hash")
bc.insert_at_end(0,bloque)
bc.insert_at_end(1,bloque)
bc.insert_at_end(2,bloque)
bc.insert_at_end(3,bloque)
bc.insert_at_end(4,bloque)
bc.Report_BlockChain()
'''