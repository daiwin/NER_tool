
import codecs
from os import listdir

files = listdir("testdata")

fmeasure_vals=[]
p_vals=[]
r_vals=[]

def calculate_file_fmeasure(file):
     NE_test = list(filter(None,codecs.open("testdata/"+file, "r", "utf-8").read().split("\n")))
     NE = list(filter(None,open("../"+file, "r").read().split("\n")))

     K_susnostei_v_krpuse = len(NE_test)
     K_vsex_vid_susnostey = len(NE)

     K_vero_videlen = 0;
     for b in NE:
          for a in NE_test:
               if(str.upper(a)==str.upper(b)):
                    K_vero_videlen= K_vero_videlen + 1
                    break

     #print(file)

     #print('Колличество сущностей в файле ' + str(K_susnostei_v_krpuse))
     #print('Всего выделенно сущностей ' + str(K_vsex_vid_susnostey))
     #print('Колличество верно выделенных ' + str(K_vero_videlen)) 

     Precision = K_vero_videlen / K_vsex_vid_susnostey # точность
     p_vals.append(Precision)
     
     Recall = K_vero_videlen/ K_susnostei_v_krpuse # полнота
     r_vals.append(Recall)
     
     F_measure = (2*Precision*Recall)/(Precision+Recall) # ф-мера
     fmeasure_vals.append(F_measure)


     #print(Precision*100)
     #print(Recall*100)
     #print(F_measure*100)







for file in files:
     if file[-4:] == ".txt":
          calculate_file_fmeasure(file)


print(sum(p_vals) / len(p_vals)*100)
print(sum(r_vals) / len(r_vals)*100)
print(sum(fmeasure_vals) / len(fmeasure_vals)*100)



