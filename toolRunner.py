# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 13:58:59 2017

@author: Daiwin
"""
import subprocess
import os

import xml.etree.ElementTree as ET
import re


#def run_opennlp():


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
     run_tomita()