import os
import subprocess
import platform

#rutadeubicacion = os.path.dirname(os.path.abspath(__file__))
#print(rutadeubicacion)

#Abre los archivos desde Cualquier OS
def open_file(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])

#Ejecuta un comando en consola en cualquiero OS
def start_file(commandfile):
    if platform.system() == "Windows":
        os.system(commandfile)
    elif platform.system() == "Darwin":
        subprocess.call(commandfile, shell=True)
    else:
        os.system(commandfile)
