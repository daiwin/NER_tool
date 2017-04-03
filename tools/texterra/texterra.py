# -*- coding: utf-8 -*-

import codecs
from os import listdir
from ispras import texterra

def extractNE(filename):
     try:
          f = codecs.open("workdir\input_utf8\\"+filename, "r", "utf-8").read()
          t = texterra.API('0e980bc9834613239ded640555f33b5458b7e543')
          doc = t.namedEntitiesAnnotate(f) 
          fw = open("workdir/tools_results/texterra/"+filename, 'w')
          
          GEO=['GPE_COUNTRY','GPE_CITY','GPE_STATE_PROVINCE','GPE_OTHER','LOCATION_RIVER','LOCATION_LAKE_SEA_OCEAN','LOCATION_REGION','LOCATION_CONTINENT','LOCATION_OTHER']
          ORG=['ORGANIZATION_CORPORATION','ORGANIZATION_EDUCATIONAL','ORGANIZATION_POLITICAL','ORGANIZATION_OTHER']

          for an in doc['annotations']['named-entity']:
               length=an['end']-an['start']
               if(an['value']['tag'] =='PERSON'):
                    try:
                         fw.write("Person"+":"+str(an['start'])+":"+str(length)+":"+an['text'].upper()+"\n")
                    except:
                         print("не удалось записать", an['text'].upper())
               for tag in GEO:
                    if(an['value']['tag'] == tag):
                         try:
                              fw.write("Geo"+":"+str(an['start'])+":"+str(length)+":"+an['text'].upper()+"\n")
                         except:
                              print("не удалось записать", an['text'].upper())
               for tag in ORG:
                    if(an['value']['tag'] == tag):
                         try:
                              fw.write("Org"+":"+str(an['start'])+":"+str(length)+":"+an['text'].upper()+"\n")
                         except:
                              print("не удалось записать", an['text'].upper())
               if(an['value']['tag'] == 'DATE'):
                    try:
                         fw.write("Date"+":"+str(an['start'])+":"+str(length)+":"+an['text'].upper()+"\n")
                    except:
                         print("не удалось записать", an['text'].upper())
     except Exception:
          print("Ошибка открытия файла", filename)
          for an in doc['annotations']['named-entity']:
               print(an['value']['tag']+":"+str(an['start'])+":"+str(length)+":"+an['text'].upper())
               
               
def run():
     files = listdir("workdir/input_utf8")
     for file in files:
          if file[-4:] == ".txt":
               extractNE(file)



