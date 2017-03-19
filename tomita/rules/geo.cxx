#encoding "utf-8"


Sobst_fw -> Word<gram="geo", h-reg1,~l-quoted>;


Discs -> Word<kwtype="гео_дискрипторы">;
			
			
GEO ->  Sobst_fw interp (Geo.Name);			
			
GEO ->  Word<h-reg1,~h-reg2, gnc-agr[1], gram='A'>  interp (+Geo.Name)  Sobst_fw< gnc-agr[1]> interp (+Geo.Name);

GEO -> Discs<l-reg, gnc-agr[1]> interp (Geo.Descr) 
			Word<h-reg1,~h-reg2, gnc-agr[1]>+ interp (Geo.Name);
			
GEO -> Word<h-reg1,~h-reg2, gnc-agr[1]>+ interp (Geo.Name) 
			Discs<gnc-agr[1]> interp (+Geo.Name) 
			Sobst_fw<gnc-agr[1]>* interp (+Geo.Name);