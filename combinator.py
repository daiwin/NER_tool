# -*- coding: utf-8 -*-

import postprocessing
from os import listdir


def run_comb():
     print("ok run combinator")
     
     files1 = listdir("workdir/tools_results/tomita")
     files2 = listdir("workdir/tools_results/rco")
     
     files_overlap = list(set(files1) & set(files2))
     
     for file in files_overlap:
          if file[-4:] == ".txt":
               try:
                    #print(file)
                    
                    tomita = filter(None,open("workdir/tools_results/tomita/"+file, "r").read().split("\n"))
                    rco = filter(None,open("workdir/tools_results/rco/"+file, "r").read().split("\n"))
                    t=set(tomita)
                    r=set(rco)
                    
                    ne_overlap = list(t & r)
                    tomita_only = list(t - r)
                    rco_only = list(r - t)
                    
                    #print(tomita_only)
                    #print(ne_overlap)
                    data = ne_overlap  + tomita_only
                    
               except Exception:
                    print("Ошибка открытия файла для кобинирования")
               f = open("workdir/combined_results/"+file, "w")
               try:
                    for NE in data:
                         f.write("%s\n" % NE)
               except Exception:
                    print ("error")
               finally:
                    f.close()
     
     postprocessing.run_post()