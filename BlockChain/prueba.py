import json

'''
with open("ENVIO_BLOQUE.json", "r") as readit: 
    x = json.load(readit) 
    print(x)
    print(x['INDEX'])
    print(x['TIMESTAMP'])
    print(x['CLASS'])
    print(x['DATA'])
    print(x['PREVIOUSHASH'])
    print(x['HASH'])
'''
'''
pythonData = {"value":"201403525-Nery","left":{"value":"201212963-Andes","left":{"value":"201005874-Estudiante1","left":None,"right":None},"right":{"value":"201313526-Alan","left":None,   "righ":None } },"right":{  "value":"201403819-Anne","left":{ "value":"201403624-Fernando", "left":None, "right":None }  ,"right":{ "value": "201602255-Estudiante2", "left":None,"right":None } } } 
y = json.dumps(pythonData)
print(y)
#jsonToPython = json.loads(jsonData)   
#print(jsonToPython['value'])
'''

p = "{""value"":""201403525-Nery"",""left"":{""value"":""201212963-Andes"",""left"":{""value"":""201005874-Estudiante1"",""left"":null,""right"":null},""right"":{value:""201313526-Alan"",""left"":null,   ""righ"":null } },right:{  ""value"":""201403819-Anne"",""left"":{ ""value"":""201403624-Fernando"", ""left"":null, ""right"":null }  ,right:{ ""value"": ""201602255-Estudiante2"", ""left"":null,right:null } } }"
y = eval(p)
#y =json.dumps(p)
print(y)
#-2.102478,-79.902976