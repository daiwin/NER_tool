# -*- coding: utf-8 -*-

from os import listdir
import toolRunner
import codecs
import os

def delete_files_from_tree(path):
   files = os.listdir(path)
   for f in files:
        p = os.path.join(path, f)
        print(p)
        os.remove(p)



def convert_to_utf8(filename):
    try:
        f = open("input\\"+filename, "rb").read()
        data = f.decode("UTF-8")
    except Exception:
        try:
            f = codecs.open("input\\"+filename).read()
            data = f
        except Exception:
            print("Ошибка открытия файла для конвертации в utf-8")

    f = codecs.open("workdir\input_utf8\\"+filename, "w", "utf-8")
    try:
        f.write(data)
    except Exception:
        print ("error")
    finally:
        f.close()
     
     
def run_pre():
     print("ok run preprocessing")
     
     delete_files_from_tree("workdir\input_utf8")
     
     
     files = listdir("input")
     i=0
     for file in files:
          if file[-4:] == ".txt":
               convert_to_utf8(file)
               i=i+1
     print("preprocessing done, complete ", i, " files")
     
     toolRunner.run_tools()