#encoding "utf-8"


Discs -> Word<kwtype="орг_дискрипторы">;

org_name -> Word<h-reg1,quoted>;


org_name_lat -> Word<h-reg1,lat>;

ORG ->   org_name+  interp (+Org.Name::not_norm)  
			  Discs interp (+Org.Name) 
			  org_name* interp (+Org.Name::not_norm);
			  
ORG ->   org_name*  interp (+Org.Name::not_norm)
              Discs interp (+Org.Name) 
			  org_name+ interp (+Org.Name::not_norm);
		  
ORG ->   org_name_lat+  interp (+Org.Name::not_norm)  
			  Discs interp (+Org.Name) 
			  org_name_lat* interp (+Org.Name::not_norm);
			  
ORG ->   org_name_lat*  interp (+Org.Name::not_norm)
              Discs interp (+Org.Name) 
			  org_name_lat+ interp (+Org.Name::not_norm);			  
			  		  
ORG ->   Discs interp (+Org.Name) 
              Word<l-quoted>+ interp (+Org.Name::not_norm) 
              Word<kwtype=~"и_разделитель">+ interp (+Org.Name::not_norm) 
              Word<h-reg1, r-quoted>+ interp (+Org.Name::not_norm); //ООО   "Санкт-Петербургский   молочный   завод   "Пискаревский"

ORG ->   Discs interp (+Org.Name)   //компании «Кремонини групп»
			  Word<h-reg1,l-quoted>+ interp (+Org.Name::not_norm) 
			  Word<kwtype=~"и_разделитель">* interp (+Org.Name::not_norm) 
			  Word<r-quoted>+ interp (+Org.Name::not_norm) ;
	
Desk_name_of -> 'имя';
Person -> Word<kwtype="фио">;	
ORG ->   Discs  interp (+Org.Name) 
              Desk_name_of interp (+Org.Name::not_norm) 
			  Person interp (+Org.Name::not_norm);  //Парк   имени   А.С. Пушкина
