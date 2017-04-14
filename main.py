# -*- coding: utf-8 -*-
import preprocessing
import postprocessing
import toolRunner
import combinator
import os

class system:
     
     def delete_files_from_tree(self,path):
        files = os.listdir(path)
        for f in files:
             p = os.path.join(path, f)
             os.remove(p)

     
     def run(self):
          prep = preprocessing.preprocessing()
          prep.run_pre()
          
          tr= toolRunner.toolrunner()
          tr.run_tools()
          
          comb = combinator.combinator()
          comb.run_combinator()
          
          postp = postprocessing.postprocessing()
          postp.run_post()
          
          self.delete_files_from_tree("workdir/input_utf8")
          self.delete_files_from_tree("workdir/combined_results")
          self.delete_files_from_tree("workdir/tools_results/texterra")
          self.delete_files_from_tree("workdir/tools_results/tomita")
          self.delete_files_from_tree("workdir/tools_results/rco")


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