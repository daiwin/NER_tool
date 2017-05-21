# -*- coding: utf-8 -*-
from os import listdir


class postprocessing:
     combined_results_path = "workdir/combined_results/"
     output_path = "output/"

     def run_post(self):
          print("ok run postprocessing")
           #открываем файлы и группируем
           
          fileNames = listdir(self.combined_results_path)
          
          for fileName in fileNames:
               if fileName[-4:] == ".txt":
                    file = open(self.combined_results_path+fileName, "r")
                    namedEntities=[]
                    for line in file.readlines():
                         splited= line.split(':')
                         namedEntities.append(splited[0]+":"+splited[3])
                    namedEntities = [line.rstrip() for line in namedEntities]
                    file.close()
                    
                    file = open(self.output_path+fileName, "w")
                    try:
                         for namedEnitity in namedEntities:
                              file.write("%s\n" % namedEnitity)
                    except Exception:
                         print ("error")
                    finally:
                         file.close()