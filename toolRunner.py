# -*- coding: utf-8 -*-

import subprocess
import os
import xml.etree.ElementTree as ET
import re
import threading
import combinator




def parse_tomita_results():
     dictionary = {}
     tree = ET.parse('tomita/output/facts.xml')
     root = tree.getroot()
     for some in root:
         f = open("workdir/tools_results/tomita/"+some.attrib.get('url'), 'w')
         dictionary[some.attrib.get('url')] = []
         for child in some[0]:
             b =[]
             position = child.attrib.get('pos')
             length = child.attrib.get('len')
             for child1 in child:
                 b.append(   re.sub(r'\s+', ' ',child1.attrib.get('val')  ) )
             dictionary[some.attrib.get('url')].append([child.tag, position, length, " ".join(b)])
             f.write(  child.tag +':'+  position  +':'+  length   +':'+   " ".join(b)     + '\r')
         f.close()

def parse_rco_results():
     tree = ET.parse('rco/output/result.xml')
     root = tree.getroot()
     for some in root:
         f = open("workdir/tools_results/rco/"+some.attrib.get('id'), 'w')
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
                    entity_data=entity[2].text
                    f.write(  etype +':'+  epos  +':'+  elength   +':'+   entity_data+'\r')
         f.close()

def run_rco():
     print("   -RCO started")
     parse_rco_results()

def run_tomita():
     print("   -Tomita started")
     startupinfo = None
     if os.name == 'nt':
          startupinfo = subprocess.STARTUPINFO()
          startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
     executable = r'tomita\tomitaparser.exe'
     config = r'config.proto'
     p = subprocess.Popen([executable, config], cwd=r"tomita", shell=False, startupinfo=startupinfo)
     p.wait()
     parse_tomita_results()

def run_tools():
     print("ok run tools")

     t_tomita = threading.Thread(target=run_rco)
     t_rco = threading.Thread(target=run_tomita)
     t_tomita.start()
     t_rco.start()
     t_tomita.join()
     t_rco.join()
     
     combinator.run_comb()
