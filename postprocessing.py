# -*- coding: utf-8 -*-
from os import listdir
from collections import Counter

def run_post():
     print("ok run postprocessing")
      #открываем файлы и группируем
      
     files = listdir("workdir/combined_results")
     
     for file in files:
          if file[-4:] == ".txt":
               f = open("workdir/combined_results/"+file, "r")
               mass=[]
               for line in f.readlines():
                    splited= line.split(':')
                    mass.append(splited[0]+":"+splited[3])
               mass = [line.rstrip() for line in mass]
               
               
               f = open("output/"+file, "w")
               try:
                    for NE in mass:
                         f.write("%s\n" % NE)
               except Exception:
                    print ("error")
               finally:
                    f.close()
                         