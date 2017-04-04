# -*- coding: utf-8 -*-

import postprocessing
from os import listdir


def splitted_data(List):
     mass=[]
     for element in List:
          mass.append(element.split(':'))
     return mass

#def stage2(tomita, rco, texterra):
#     tomita=splitted_data(tomita)
#     rco=splitted_data(rco)
#     texterra=splitted_data(texterra)
#     
#     for ne_tomita in tomita :
#          for ne_rco in rco:
#               if(ne_tomita[1]==ne_rco[1]):
#                    print("RCO",ne_rco)
#          for ne_texterra in texterra:
#               if(ne_tomita[1]==ne_rco[1]):
#                    print("TEXTERRA",ne_texterra)
#                    





def run_comb():
     print("ok run combinator")
     
     files1 = listdir("workdir/tools_results/tomita")
     files2 = listdir("workdir/tools_results/rco")
     files3= listdir("workdir/tools_results/texterra")
     
     files_overlap = list(set(files1) & set(files2)& set(files3))
     
     for file in files_overlap:
          if file[-4:] == ".txt":
               try:
                    print(file)
                    
                    tomita = filter(None,open("workdir/tools_results/tomita/"+file, "r").read().split("\n"))
                    rco = filter(None,open("workdir/tools_results/rco/"+file, "r").read().split("\n"))
                    texterra = filter(None,open("workdir/tools_results/texterra/"+file, "r").read().split("\n"))
                    
                    
                    t=set(tomita)
                    r=set(rco)
                    tt=set(texterra)
                    
#                    ne_overlap = list(t & r & tt)
                    
                    overlap_stage2 = list((t&r)|(r&tt)|(tt&t))
                    print(overlap_stage2)
                    
#                    tomita_only = list((t - r) | (t - tt))
#                    rco_only = list((r - t) | (r - tt))
#                    texterra_only= list((tt - t)|(tt-r))
                    
                    
#                    stage2(tomita_only,rco_only,texterra_only)
                    
                    
                    #print(tomita_only)
                    #print(ne_overlap)
                    data = overlap_stage2
                    
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