#encoding "utf-8"


Sobst_fw -> Word<gram="geo", h-reg1,~l-quoted>;


Discs -> Word<kwtype="гео_дискрипторы">;
			
			
GEO ->  Sobst_fw interp (Geo.Name::not_norm);			
			
GEO ->  Word<h-reg1,~h-reg2, gnc-agr[1], gram='A'>  interp (+Geo.Name::not_norm)  Sobst_fw< gnc-agr[1]> interp (+Geo.Name::not_norm);

GEO -> Discs<l-reg, gnc-agr[1]> interp (+Geo.Name::not_norm) 
			Word<h-reg1, gnc-agr[1]>+ interp (+Geo.Name::not_norm);
		
GEO -> Discs interp (+Geo.Name::not_norm) 
			Word<h-reg1> interp (+Geo.Name::not_norm);


		
GEO -> Word<h-reg1,~h-reg2, gnc-agr[1]>+ interp (Geo.Name::not_norm) 
			Discs<gnc-agr[1]> interp (+Geo.Name::not_norm) 
			Sobst_fw<gnc-agr[1]>* interp (+Geo.Name::not_norm);