# -*- coding: utf-8 -*-

from os import listdir
import codecs





class preprocessing:
     def convert_to_utf8(self,filename):
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
          
          
     def run_pre(self):
          print("ok run preprocessing")

          files = listdir("input")
          i=0
          for file in files:
               if file[-4:] == ".txt":
                    self.convert_to_utf8(file)
                    i=i+1
          print("preprocessing done, complete ", i, " files")
