import AVL
from AVL import AVLTree

class Block:
     def __init__(self,INDEX=None,TIMESTAMP=None,CLASS=None,DATA=None,PREVIOUSHASH=None,HASH=None,next=None,prior=None,jsondate = None):
        self.next = next
        self.prior = prior
        self.INDEX =INDEX 
        self.TIMESTAMP = TIMESTAMP
        self.CLASS = CLASS
        self.DATA = DATA
        self.PREVIOUSHASH = PREVIOUSHASH
        self.HASH = HASH
        self.jsondate = jsondate

     def getIndex(self):
        return str(self.INDEX)
      
     def getTime(self):
        return str(self.TIMESTAMP)

     def getClass(self):
        return str(self.CLASS)

     def getData(self):
        return str(self.DATA[0:40])
      
     def getDataComplete(self):
        return str(self.DATA)
      
     def getPH(self):
        return str(self.PREVIOUSHASH)

     def getHash(self):
        return str(self.HASH)

     def CreateBlock(self):
        f_output = open('ENVIO_BLOQUE.json','w')
        f_output.write("{\n")
        f_output.write("\"INDEX\": %s ,\n"%(self.INDEX))
        f_output.write("\"TIMESTAMP\": \"%s\",\n"%(self.TIMESTAMP))
        f_output.write("\"CLASS\": \"%s\",\n"%(self.CLASS))
        f_output.write("\"DATA\": %s,\n"%(self.DATA))
        f_output.write("\"PREVIOUSHASH\": \"%s\",\n"%(self.PREVIOUSHAS))
        f_output.write("\"HASH\": \"%s\"\n"%(self.HASH))
        f_output.write("}")
        f_output.close()
        #path = 'ENVIO_BLOQUE.json'
        #open_file(path) #Esta en el archivo Open_Files

     def CreateJsonBlock(self):
         jsonstring =""
         jsonstring  = jsonstring + "{"
         jsonstring  = jsonstring + "\nINDEX:" + self.INDEX
         jsonstring  = jsonstring + "\nTIMESTAMP:" + self.TIMESTAMP
         jsonstring  = jsonstring + "\nCLASS:" + self.CLASS
         jsonstring  = jsonstring + "\nDATA:" + self.DATA 
         jsonstring  = jsonstring + "\nPREVIOUSHASH:" + self.PREVIOUSHASH
         jsonstring  = jsonstring + "\nHASH:" + self.HASH
         jsonstring  = jsonstring + "}"
         return jsonstring 