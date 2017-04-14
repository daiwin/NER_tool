# -*- coding: utf-8 -*-
import preprocessing
import postprocessing
import toolRunner
import combinator

class system:
     def run(self):
          prep = preprocessing.preprocessing()
          prep.run_pre()
          
          tr= toolRunner.toolrunner()
          tr.run_tools()
          
          comb = combinator.combinator()
          comb.run_combinator()
          
          postp = postprocessing.postprocessing()
          postp.run_post()
     

def main():
     prep = preprocessing.preprocessing()
     prep.run_pre()
     
     tr= toolRunner.toolrunner()
     tr.run_tools()
     
     comb = combinator.combinator()
     comb.run_combinator()
     
     postp = postprocessing.postprocessing()
     postp.run_post()
     
     

if __name__ == '__main__':
      main()