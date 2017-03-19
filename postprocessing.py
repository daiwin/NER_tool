# -*- coding: utf-8 -*-
from os import listdir
from collections import Counter

def run_post():
     print("ok run postprocessing")
      #открываем файлы и группируем
      
     files = listdir("workdir/combined_results")
     
     for file in files:
          if file[-4:] == ".txt":
               try:
                    f = open("workdir/combined_results/"+file, "r")
                    mass=[]
                    for line in f.readlines():
                         splited= line.split(':')
                         mass.append(splited[0]+":"+splited[3])
                    mass = [line.rstrip() for line in mass]
                    
                    countedMass = Counter(mass)
                    
                    f = open("output/"+file, "w")
                    for word,cnt in countedMass.most_common():
                         try:
                              f.write(word+":"+str(cnt)+"\r")
                         except Exception:
                              print ("error")
                    f.close()
               except Exception:
                    print("Ошибка открытия файла постпроцессинг")

#               f = open("workdir/combined_results/"+file, "w")
#               try:
#                    f.write(data)
#               except Exception:
#                    print ("error")
#               finally:
#                    f.close()