# -*- coding: utf-8 -*-

import postprocessing
from os import listdir


def splitted_data(List):
     splitedNamedEntities=[]
     for element in List:
          splitedNamedEntities.append(element.split(':'))
     return splitedNamedEntities


def run_combinator():
     print("ok run combinator")
     
     files1 = listdir("workdir/tools_results/tomita")
     #files2 = listdir("workdir/tools_results/rco")
     files3= listdir("workdir/tools_results/texterra")
     
     fileNamesOverlap = list(set(files1) & set(files3))
     
     for fileName in fileNamesOverlap:
          if fileName[-4:] == ".txt":
               try:
                    #print(fileName)
                    tomita = filter(None,open("workdir/tools_results/tomita/"+fileName, "r").read().split("\n"))
                    #rco = filter(None,open("workdir/tools_results/rco/"+fileName, "r").read().split("\n"))
                    texterra = filter(None,open("workdir/tools_results/texterra/"+fileName, "r").read().split("\n"))
                    
                    t=set(tomita)
                    #r=set(rco)
                    tt=set(texterra)
                    
#                    ne_overlap = list(t & r & tt)
                    overlap = list(tt&t)
                    print(overlap)
#                    tomita_only = list((t - r) | (t - tt))
#                    rco_only = list((r - t) | (r - tt))
#                    texterra_only= list((tt - t)|(tt-r))
                    data = overlap
                    
               except Exception:
                    print("Ошибка открытия файла для кобинирования")
               f = open("workdir/combined_results/"+fileName, "w")
               try:
                    for NE in data:
                         f.write("%s\n" % NE)
               except Exception:
                    print ("error")
               finally:
                    f.close()
                    
     postprocessing.run_post()