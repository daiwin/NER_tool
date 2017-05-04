# -*- coding: utf-8 -*-

import subprocess
import os
import xml.etree.ElementTree as ET
import re
import threading
import sys
sys.path.insert(0, 'tools/texterra')
import texterra


class toolrunner:
     def parse_tomita_results(self):
          dictionary = {}
          tree = ET.parse('tools/tomita/output/facts.xml')
          root = tree.getroot()
          for some in root:
              file = open("workdir/tools_results/tomita/"+some.attrib.get('url'), 'w')
              dictionary[some.attrib.get('url')] = []
              for child in some[0]:
                  b =[]
                  position = child.attrib.get('pos')
                  length = child.attrib.get('len')
                  for child1 in child:
                      b.append(   re.sub(r'\s+', ' ',child1.attrib.get('val')  ) )
                  dictionary[some.attrib.get('url')].append([child.tag, position, length, " ".join(b)])
                  file.write(  child.tag +':'+  position  +':'+  length   +':'+   " ".join(b)     + '\r')
              file.close()
     
     def parse_rco_results(self):
          tree = ET.parse('tools/rco/output/result.xml')
          root = tree.getroot()
          for some in root:
              file = open("workdir/tools_results/rco/"+some.attrib.get('id'), 'w')
              for entity in some.iter('entity'):
                   if(entity.attrib.get('type')=='Geoplace:Name' or entity.attrib.get('type')=='Organization:Name' or entity.attrib.get('type')=='Person:Name' or entity.attrib.get('type')=='Time:Date'):
                         if entity.attrib.get('type')=='Geoplace:Name':
                             etype='Geo'
                         elif entity.attrib.get('type')=='Organization:Name':
                             etype='Org'
                         elif entity.attrib.get('type')=='Person:Name':
                             etype='Person'
                         elif  entity.attrib.get('type')=='Time:Date':
                             etype='Date'
                         epos=entity.attrib.get('offset')
                         elength=entity.attrib.get('length')
                         entity_data=   entity[0].text.replace("\"", "").replace("«", "").replace("»", "")
                         file.write(  etype +':'+  epos  +':'+  elength   +':'+   entity_data+'\r')
              file.close()
     
     def run_rco(self):
          print("   -RCO started")
          self.parse_rco_results()
          
     def run_texterra(self):
          texterra.run()
     
     
     def run_tomita(self):
          print("   -Tomita started")
          startupinfo = None
          if os.name == 'nt':
               startupinfo = subprocess.STARTUPINFO()
               startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
          executable = r'tools\tomita\tomitaparser.exe'
          config = r'config.proto'
          process = subprocess.Popen([executable, config], cwd=r"tools\tomita", shell=False, startupinfo=startupinfo)
          process.wait()
          self.parse_tomita_results()
     
     def run_tools(self):
          print("ok run tools")
     
          tomitaThread = threading.Thread(target=self.run_tomita)
          rcoThread = threading.Thread(target=self.run_rco)
          texterraThread = threading.Thread(target=self.run_texterra)
          tomitaThread.start()
          rcoThread.start()
          texterraThread.start()
          tomitaThread.join()
          rcoThread.join()
          texterraThread.join()
