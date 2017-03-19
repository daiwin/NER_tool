#encoding "utf-8"


//Sobst_fw -> Word<gram="persn", h-reg1,~h-reg2, ~l-quoted> | Word<gram="famn", h-reg1,~h-reg2, ~l-quoted> | Word<gram="patrn", h-reg1, ~h-reg2,~l-quoted>;
//Name -> Word<gram="persn">;
//Fam -> Word<gram="famn">;

//добавить правила на основе дескриптора


Initial -> Word<wff=/[А-Я]\./>;
Initials -> Initial+;

P1 -> Word<h-reg1,~h-reg2,~l-quoted, gram=~"abbr"> Initials;
P2 -> Initials Word<h-reg1,~h-reg2,~l-quoted, gram=~"abbr">;


P3 -> Word<h-reg1,~h-reg2,~l-quoted, gram=~"abbr,geo,V,persn">*
			Word<gram="persn", h-reg1,~h-reg2, ~l-quoted> 
			Word<h-reg1,~h-reg2,~l-quoted, gram=~"abbr,geo,V,persn">;  //Андрей Рубайло   или Рубайло Андрей Валерьевич

P4 -> Word<gram="famn", h-reg1,~h-reg2, ~l-quoted> 
		Word<h-reg1,~h-reg2,~l-quoted, gram=~"abbr,geo,V,famn"> 
		Word<h-reg1,~h-reg2,~l-quoted, gram=~"abbr,geo,V,famn">*;//Рубайло Андрей (Валерьевич)


			
			
Person ->P1 interp (Person.FIO) | P2 interp (Person.FIO) | P3 interp (Person.FIO) | P4 interp (Person.FIO);



			
