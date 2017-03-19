# -*- coding: utf-8 -*-

import postprocessing
from os import listdir


def run_comb():
     print("ok run combinator")
     
     files = listdir("workdir/tools_results/tomita")
     for file in files:
          if file[-4:] == ".txt":
               try:
                    f = open("workdir/tools_results/tomita/"+file, "r").read()
                    data = f
               except Exception:
                    print("Ошибка открытия файла для кобинирования")
               f = open("workdir/combined_results/"+file, "w")
               try:
                    f.write(data)
               except Exception:
                    print ("error")
               finally:
                    f.close()
     
     postprocessing.run_post()