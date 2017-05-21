# -*- coding: utf-8 -*-

from os import listdir

class combinator:
     def splitted_data(self,List):
          splitedNamedEntities=[]
          for element in List:
               splitedNamedEntities.append(element.split(':'))
          return splitedNamedEntities
     
     
     def run_combinator(self):
          print("ok run combinator")
          
          tomita_status = False
          texterra_status = False
          

          files1 = listdir("workdir/tools_results/tomita")
          if(len(files1)>0):
               tomita_status = True
          
          files3= listdir("workdir/tools_results/texterra")
          if(len(files3)>0):
               texterra_status = True
          
          if(texterra_status & tomita_status):
               fileNamesOverlap = list(set(files1) & set(files3))
          elif(tomita_status):
               fileNamesOverlap = list(set(files1))
          elif(texterra_status):
               fileNamesOverlap = list(set(files3))
               
          
          
          for fileName in fileNamesOverlap:
               if fileName[-4:] == ".txt":
                    try:
                         print(fileName)
                         
                         
                         if(texterra_status & tomita_status):
                              tomita = filter(None,open("workdir/tools_results/tomita/"+fileName, "r").read().split("\n"))
                              texterra = filter(None,open("workdir/tools_results/texterra/"+fileName, "r").read().split("\n"))
                              t=set(tomita)
                              tt=set(texterra)
                              overlap = (t&tt)
                              
                         elif(tomita_status):
                              tomita = filter(None,open("workdir/tools_results/tomita/"+fileName, "r").read().split("\n"))
                              t=set(tomita)
                              overlap = t
                         elif(texterra_status):
                              texterra = filter(None,open("workdir/tools_results/texterra/"+fileName, "r").read().split("\n"))
                              tt=set(texterra)
                              overlap = tt

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
                         
