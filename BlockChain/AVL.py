
import Open_Files
from Open_Files import open_file,start_file
import random
import unittest


class Node:
    def __init__(self, key,name):
        self.key = key
        self.name = name
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0

    def get_height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def insert(self, key , name):
        """
        Insert nodes to the tree.
        """
        tree = self.node
        new_node = Node(key,name)

        if tree is None:
            self.node = new_node
            self.node.left = AVLTree()
            self.node.right = AVLTree()

        elif key < tree.key:
            self.node.left.insert(key,name)

        elif key > tree.key:
            self.node.right.insert(key,name)

        self.re_balance_tree()

    def re_balance_tree(self):
        """
        Rebalanced the tree if it is unbalanced.
        """

        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.rotate_left()
                    self.update_heights()
                    self.update_balances()
                self.rotate_right()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rotate_right()
                    self.update_heights()
                    self.update_balances()
                self.rotate_left()
                self.update_heights()
                self.update_balances()

    def rotate_right(self):
        root = self.node
        left_child = self.node.left.node
        right_child = left_child.right.node

        self.node = left_child
        left_child.right.node = root
        root.left.node = right_child

    def rotate_left(self):
        root = self.node
        right_child = self.node.right.node
        left_child = right_child.left.node

        self.node = right_child
        right_child.left.node = root
        root.right.node = left_child

    def update_heights(self, recurse=True):
        if not self.node is None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_heights()
                if self.node.right is not None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.node is None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_balances()
                if self.node.right is not None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def check_balanced(self):
        if self is None or self.node is None:
            return True

        self.update_heights()
        self.update_balances()
        return ((abs(
            self.balance) < 2) and self.node.left.check_balanced() and
                self.node.right.check_balanced())

    def print_tree_in_order_traversal(self):
        if self.node is None:
            return []

        nodes_list = []

        l = self.node.left.print_tree_in_order_traversal()
        for i in l:
            nodes_list.append(i)
        stringnode= str(self.node.key) + " \\n " + self.node.name
        nodes_list.append(stringnode)
    
        l = self.node.right.print_tree_in_order_traversal()
        for i in l:
            nodes_list.append(i)
        return nodes_list

    def print_tree_pre_order_traversal(self):
        if self.node is None:
            return []
        nodes_list = []
        stringnode= str(self.node.key) + " \\n " + self.node.name
        nodes_list.append(stringnode)
        l = self.node.left.print_tree_pre_order_traversal()
        for i in l:
            nodes_list.append(i)
        l = self.node.right.print_tree_pre_order_traversal()
        for i in l:
            nodes_list.append(i)
        return nodes_list

    def print_tree_post_order_traversal(self):
        if self.node is None:
            return []
        nodes_list = []
        l = self.node.left.print_tree_pre_order_traversal()
        for i in l:
            nodes_list.append(i)
        l = self.node.right.print_tree_pre_order_traversal()
        for i in l:
            nodes_list.append(i)
        stringnode= str(self.node.key) + " \\n " + self.node.name
        nodes_list.append(stringnode)
        return nodes_list

    def print_tree_as_tree_shape(self, node=None, level=0):
        if not node:
            node = self.node

        if node.right.node:
            self.print_tree_as_tree_shape(node.right.node, level + 1)
            print(('\t' * level), (' / '))
        print (('\t' * level) , node.key)
        if node.left.node:
            print (('\t' * level), (' \\ '))
            self.print_tree_as_tree_shape(node.left.node, level + 1)

    def getCodigoInternoAVL(self, node=None,level=0):
        etiqueta = ""
        if not node:
           node = self.node
           level = self.height

        if(node.left.node == None and node.right.node):
            etiqueta = "nodo"
            etiqueta = etiqueta + str(node.key)
            etiqueta = etiqueta + "[label =\"|"
            etiqueta = etiqueta + "Canet: " + str(node.key)
            etiqueta = etiqueta + "\\nNombre: " + node.name
            etiqueta = etiqueta + "\\nAltura: " + str(level)
            etiqueta = etiqueta + "\\nFE: " + str(self.balance)
            etiqueta = etiqueta +  "|\"];\n"
        else:
            etiqueta ="nodo"
            etiqueta = etiqueta + str(node.key)
            etiqueta = etiqueta + " [ label =\"<C0>|"
            etiqueta = etiqueta + "Carnet: " + str(node.key)
            etiqueta = etiqueta + "\\nNombre: " + node.name
            etiqueta = etiqueta + "\\nAltura: " + str(level)
            etiqueta = etiqueta + "\\nFE: " + str(self.balance)
            etiqueta = etiqueta + "|<C1>\"];\n"
        if(node.left.node != None):
            etiqueta = etiqueta + self.getCodigoInternoAVL(node.left.node, level - 1)
            etiqueta = etiqueta + "nodo"
            etiqueta = etiqueta + str(node.key)
            etiqueta = etiqueta +":C0->nodo"
            etiqueta = etiqueta + str(node.left.node.key)
            etiqueta = etiqueta +"\n"
        if(node.right.node != None):
            etiqueta = etiqueta + self.getCodigoInternoAVL(node.right.node, level - 1)
            etiqueta = etiqueta + "nodo"
            etiqueta = etiqueta + str(node.key)
            etiqueta = etiqueta + ":C1->nodo"
            etiqueta = etiqueta + str(node.right.node.key)
            etiqueta = etiqueta + "\n"
        return etiqueta

    def graphTree(self): #Genera el Archivo .dot para la lista doble enlazada y Genera la Imagen
            f_output = open('AVL.txt','w')
            f_output.write("digraph{\n node[shape = record , color = black];")
            f_output.write("rankdir=TB;\n")
            f_output.write("label = \"\n\n\nDATA IN BLOCK OF THE BLOCKCHAIN\";\n")
            f_output.write("\n")

            nodos = self.getCodigoInternoAVL()

            f_output.write(nodos)
            f_output.write("\n\t\t}\n")
            f_output.close()

            commandfile = 'dot -Tpng AVL.txt -o AVL.png'
            start_file(commandfile)
            path = 'AVL.png'
            open_file(path)
    
    def Report_TrasversalPre(self): #Genera el Archivo .dot para la lista  enlazada y Genera la Imagen
        nodonum =0
        f_output = open('Trasversalpre.txt','w')
        f_output.write("digraph{\n node[shape = record,style=filled];")
        f_output.write("rankdir=LR;\n")
        f_output.write("label = \"Trasversal Preorden Report\"; \n")
        f_output.write("\n")
        aux = self.print_tree_pre_order_traversal()
            #Imprimir Nodos
        a=""
        for stringnodo in aux:
            f_output.write("\t\t a%d[label=\"{ %s }\"];\n"%(nodonum,stringnodo))
            a = a + stringnodo + "->"
            nodonum+=1
        print(a)
            #Enlazar Nodos
        for i in range(0,nodonum):
            if i != nodonum-1:
                f_output.write("\t\t a%s->a%s[color=\"chocolate1\"];\n"%(i,i+1))
        f_output.write("\t }")
        f_output.close()
        commandfile = 'dot -Tpng Trasversalpre.txt -o Trasversalpre.png'
        start_file(commandfile)
        path = 'Trasversalpre.png'
        open_file(path)

    def Report_TrasversalIn(self): #Genera el Archivo .dot para la lista  enlazada y Genera la Imagen
        nodonum =0
        f_output = open('Trasversalin.txt','w')
        f_output.write("digraph{\n node[shape = record,style=filled];")
        f_output.write("rankdir=LR;\n")
        f_output.write("label = \"Trasversal Inorden Report\"; \n")
        f_output.write("\n")
        aux = self.print_tree_in_order_traversal()
            #Imprimir Nodos
        a=""
        for stringnodo in aux:
            f_output.write("\t\t a%d[label=\"{ %s }\"];\n"%(nodonum,stringnodo))
            a = a + stringnodo + "->"
            nodonum+=1
        print(a)
            #Enlazar Nodos
        for i in range(0,nodonum):
            if i != nodonum-1:
                f_output.write("\t\t a%s->a%s[color=\"chocolate1\"];\n"%(i,i+1))
        f_output.write("\t }")
        f_output.close()
        commandfile = 'dot -Tpng Trasversalin.txt -o Trasversalin.png'
        start_file(commandfile)
        path = 'Trasversalin.png'
        open_file(path)

    def Report_TrasversalPost(self): #Genera el Archivo .dot para la lista  enlazada y Genera la Imagen
        nodonum =0
        f_output = open('Trasversalpo.txt','w')
        f_output.write("digraph{\n node[shape = record,style=filled];")
        f_output.write("rankdir=LR;\n")
        f_output.write("label = \"Trasversal Postorden Report\"; \n")
        f_output.write("\n")
        aux = self.print_tree_post_order_traversal()
            #Imprimir Nodos
        a = ""
        for stringnodo in aux:
            f_output.write("\t\t a%d[label=\"{ %s }\"];\n"%(nodonum,stringnodo))
            a = a + stringnodo + "->"
            nodonum+=1
        print(a)
            #Enlazar Nodos
        for i in range(0,nodonum):
            if i != nodonum-1:
                f_output.write("\t\t a%s->a%s[color=\"chocolate1\"];\n"%(i,i+1))
        f_output.write("\t }")
        f_output.close()
        commandfile = 'dot -Tpng Trasversalpo.txt -o Trasversalpo.png'
        start_file(commandfile)
        path = 'Trasversalpo.png'
        open_file(path)

def create_random_node_list():
    # Create random list for node values.
    random_node_list = random.sample(range(1, 100), 10)
    print ("Input :", random_node_list, "\n")
    return random_node_list


def create_avl_tree(node_list):
    # Create tree and insert node values.
    tree = AVLTree()
    for node in node_list:
        tree.insert(node,"a")
    return tree



'''
avl_tree = create_avl_tree(create_random_node_list())
#avl_tree.print_tree_as_tree_shape()
avl_tree.graphTree()
avl_tree.Report_TrasversalPost()
'''

