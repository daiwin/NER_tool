# -*- coding: utf-8 -*-
from os import listdir

def run_post():
     print("ok run postprocessing")
      #открываем файлы и группируем
      
     fileNames = listdir("workdir/combined_results")
     
     for fileName in fileNames:
          if fileName[-4:] == ".txt":
               file = open("workdir/combined_results/"+fileName, "r")
               namedEntities=[]
               for line in file.readlines():
                    splited= line.split(':')
                    namedEntities.append(splited[0]+":"+splited[3])
               namedEntities = [line.rstrip() for line in namedEntities]
               file.close()
               
               file = open("output/"+fileName, "w")
               try:
                    for namedEnitity in namedEntities:
                         file.write("%s\n" % namedEnitity)
               except Exception:
                    print ("error")
               finally:
                    file.close()