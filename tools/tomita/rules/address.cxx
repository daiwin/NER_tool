#encoding "utf-8"


//StreetW -> 'проспект' | 'проезд' | 'улица' | 'шоссе';
//StreetSokr -> 'пр' | 'просп' | 'пр-д' | 'ул' | 'ш';

//StreetDescr -> StreetW | StreetSokr;

//StreetNameNoun -> (Adj<gnc-agr[1]>) Word<gnc-agr[1],rt> (Word<gram="род">);

//NumberW_1 -> AnyWord<wff=/[1-9]?[0-9]-?((ый)|(ий)|(ой)|й)/> {outgram="муж,ед,им"};
//NumberW_2 -> AnyWord<wff=/[1-9]?[0-9]-?((ая)|(яя)|(ья)|я)/> {outgram="жен,ед,им"};
//NumberW_3 -> AnyWord<wff=/[1-9]?[0-9]-?((ее)|(ье)|(ое)|е)/> {outgram="сред,ед,им"};

//NumberW -> NumberW_1 | NumberW_2 | NumberW_3;

//StreetNameAdj -> Adj<h-reg1> Adj*;
//StreetNameAdj -> NumberW<gnc-agr[1]> Adj<gnc-agr[1]>;

//Dot -> ',' | ' ';
//Number -> Dot AnyWord<wff=/[1-2]?[0-9]{1,3}/>;

//Street -> StreetDescr interp (Street.Descr) StreetNameNoun<gram="род", h-reg1> interp (Street.StreetName::not_norm)  ;
//Street -> StreetDescr interp (Street.Descr) StreetNameNoun<gram="им", h-reg1> interp (Street.StreetName::not_norm)  ;

//Street -> StreetNameAdj<gnc-agr[1]> interp (Street.StreetName) StreetW<gnc-agr[1]> interp (Street.Descr)  ;
//Street -> StreetNameAdj interp (Street.StreetName) StreetSokr interp (Street.Descr)  ;
//Street -> StreetW<gnc-agr[1]> interp (Street.Descr) StreetNameAdj<gnc-agr[1]> interp (Street.StreetName)  ;
//Street -> StreetSokr interp (Street.Descr) StreetNameAdj interp (Street.StreetName)  ;
