# -*- coding: utf-8 -*-
# PROJECT INITITATED BY : VASANTHA KUMAR
# E-MAIL                : VASANTHFRIEND.RAJU@GMAIL.COM

TAMIL_FLAG = 0
MALAYALAM_FLAG = 1


unicode_help = {
    
    TAMIL_FLAG : 'a : அ, aa/A : ஆ,  i : இ, ii/I : ஈ,  u : உ,  uu/U : ஊ \ne : எ,  ee/E : ஏ,  ai : ஐ,  o : ஒ,  oo/O : ஓ,  ou : ஒள, q : ஃ,\n\
k : க்,   ng : ங், ch/s : ச்,  nj : ஞ், t/d : ட்,   N : ண்,\n\
th : த், nth/w : ந், p/b : ப், m : ம், y : ய், r : ர், \n\
l : ல், v : வ், z : ழ், L : ள், R : ற், n : ன், \n\
j : ஜ், S : ஸ், sh : ஷ், ksh : க்ஷ், h : ஹ், \n\n\
ammaa : அம்மா',
    
    MALAYALAM_FLAG : 'a : അ, aa : ആ, A : ആ, i : ഇ, ii : ഈ, I : ഈ, \n\
u : ഉ,  uu : ഊ, U : ഊ, \n\
e : എ, ee : ഏ, E : ഏ, ai : ഐ, o : ഒ, oo : ഓ, O : ഓ, o : ഔ, \n\
k : ക്,\n\
K : ഖ്,\n\
g : ഗ്,\n\
G : ഘ്,\n\
n : ങ്,\n\
ch : ച്,\n\
Ch : ഛ്,\n\
j : ജ്,\n\
J : ഝ്,\n\
N : ഞ്,\n\
t : ട്,\n\
th : ഠ്,\n\
d : ഡ്,\n\
dh : ഢ്,\n\
w : ണ്,\n\
T : ത്,\n\
Th : ഥ്,\n\
D : ദ്,\n\
Dh : ധ്,\n\
W : ന്,\n\
p : പ്,\n\
P : ഫ്,\n\
b : ബ്,\n\
B : ഭ്,\n\
m : മ്,\n\
y : യ്,\n\
r : ര്,\n\
R : റ്,\n\
l : ല്,\n\
L : ള്,\n\
z : ഴ്,\n\
v : വ്,\n\
s : ശ്,\n\
sh : ഷ്,\n\
S : സ്,\n\
h : ഹ്,\n\n\
ammee : അമ്മേ'
    }


unicode_map = {
    TAMIL_FLAG : {
        'a' : u'அ', 'aa' : u'ஆ', 'A' : u'ஆ', 'i' : u'இ', 'ii' : u'ஈ', 'I' : u'ஈ', 'u' : u'உ', 'uu' : u'ஊ', 'U' : u'ஊ', 
        'e' : u'எ', 'ee' : u'ஏ', 'E' : u'ஏ', 'ai' : u'ஐ', 'o' : u'ஒ', 'oo' : u'ஓ', 'O' : u'ஓ', 'ou' : u'ஒள', 'q' : u'ஃ',

        'k' : u'க்', 'g' : u'க்', 'ng' : u'ங்', 'ch' : u'ச்', 's' : u'ச்', 'nj' : u'ஞ்', 't' : u'ட்', 'd' : u'ட்', 'N' : u'ண்', 'th' : u'த்', 'nth' : u'ந்', 'p' : u'ப்',  'b' : u'ப்',
        'm' : u'ம்', 'y' : u'ய்', 'r' : u'ர்', 'l' : u'ல்', 'v' : u'வ்', 'z' : u'ழ்', 'L' : u'ள்', 'R' : u'ற்', 'n' : u'ன்', 'w': u'ந்',
        'j' : u'ஜ்', 'S' : u'ஸ்', 'sh' : u'ஷ்', 'ksh' : u'க்ஷ்', 'h' : u'ஹ்',
        
        'ka' : u'க', 'kaa' : u'கா', 'kA' : u'கா', 'ki' : u'கி', 'kii' : u'கீ', 'kI' : u'கீ',
        'ku' : u'கு', 'kuu' : u'கூ', 'kU' : u'கூ',  'ke' : u'கெ', 'kee' : u'கே', 'kE' : u'கே',
        'kai' : u'கை', 'ko' : u'கொ', 'koo' : u'கோ', 'kO' : u'கோ', 'keLa' : u'கெள',
        
        'ga' : u'க', 'gaa' : u'கா', 'gA' : u'கா', 'gi' : u'கி', 'gii' : u'கீ', 'gI' : u'கீ',
        'gu' : u'கு', 'guu' : u'கூ', 'gU' : u'கூ',  'ge' : u'கெ', 'gee' : u'கே', 'gE' : u'கே',
        'gai' : u'கை', 'go' : u'கொ', 'goo' : u'கோ', 'gO' : u'கோ', 'geLa' : u'கெள',


        'nga' : u'ங', 'ngaa' : u'ஙா', 'ngA' : u'ஙா', 'ngi' : u'ஙி', 'ngii' : u'ஙீ', 'ngI' : u'ஙீ',
        'ngu' : u'ஙு', 'nguu' : u'ஙூ', 'ngU' : u'ஙூ', 'nge' : u'ஙெ', 'ngee' : u'ஙே', 'ngE' : u'ஙே',
        'ngai' : u'ஙை', 'ngo' : u'ஙொ', 'ngoo' : u'ஙோ', 'ngO' : u'ஙோ', 'ngeLa' : u'ஙெள', 

        'cha' : u'ச', 'chaa' : u'சா', 'chA' : u'சா', 'chi' : u'சி', 'chii' : u'சீ', 'chI' : u'சீ',
        'chu' : u'சு', 'chuu' : u'சூ', 'chU' : u'சூ', 'che' : u'செ', 'chee' : u'சே', 'chE' : u'சே',
        'chai' : u'சை', 'cho' : u'சொ', 'choo' : u'சோ', 'chO' : u'சோ', 'cheLa' : u'செள',

        'sa' : u'ச', 'saa' : u'சா', 'sA' : u'சா', 'si' : u'சி', 'sii' : u'சீ', 'sI' : u'சீ',
        'su' : u'சு', 'suu' : u'சூ', 'sU' : u'சூ', 'se' : u'செ', 'see' : u'சே', 'sE' : u'சே',
        'sai' : u'சை', 'so' : u'சொ', 'soo' : u'சோ', 'sO' : u'சோ', 'seLa' : u'செள', 

        'nja' : u'ஞ', 'njaa' : u'ஞா', 'njA' : u'ஞா', 'nji' : u'ஞி', 'njii' : u'ஞீ', 'njI' : u'ஞீ',
        'nju' : u'ஞு', 'njuu' : u'ஞூ', 'njU' : u'ஞூ', 'nje' : u'ஞெ', 'njee' : u'ஞே', 'njE' : u'ஞே',
        'njai' : u'ஞை', 'njo' : u'ஞொ', 'njoo' : u'ஞோ', 'njO' : u'ஞோ', 'njeLa' : u'ஞெள', 

        'ta' : u'ட', 'taa' : u'டா', 'tA' : u'டா', 'ti' : u'டி', 'tii' : u'டீ', 'tI' : u'டீ',
        'tu' : u'டு', 'tuu' : u'டூ', 'tU' : u'டூ', 'te' : u'டெ', 'tee' : u'டே', 'tE' : u'டே',
        'tai' : u'டை', 'to' : u'டொ', 'too' : u'டோ', 'tO' : u'டோ', 'teLa' : u'டெள',

        'da' : u'ட', 'daa' : u'டா', 'dA' : u'டா', 'di' : u'டி', 'dii' : u'டீ', 'dI' : u'டீ',
        'du' : u'டு', 'duu' : u'டூ', 'dU' : u'டூ', 'de' : u'டெ', 'dee' : u'டே', 'dE' : u'டே',
        'dai' : u'டை', 'do' : u'டொ', 'doo' : u'டோ', 'dO' : u'டோ', 'deLa' : u'டெள', 

        'Na' : u'ண', 'Naa' : u'ணா', 'NA' : u'ணா', 'Ni' : u'ணி', 'Nii' : u'ணீ', 'NI' : u'ணீ', 'Nu' : u'ணு', 'Nuu' : u'ணூ', 'NU' : u'ணூ', 
        'Ne' : u'ணெ', 'Nee' : u'ணே', 'NE' : u'ணே', 'Nai' : u'ணை', 'No' : u'ணொ', 'Noo' : u'ணோ', 'NO' : u'ணோ', 'NeLa' : u'ணெள', 

        'tha' : u'த', 'thaa' : u'தா', 'thA' : u'தா', 'thi' : u'தி', 'thii' : u'தீ', 'thI' : u'தீ', 'thu' : u'து', 'thuu' : u'தூ', 'thU' : u'தூ', 
        'the' : u'தெ', 'thee' : u'தே', 'thE' : u'தே', 'thai' : u'தை', 'tho' : u'தொ', 'thoo' : u'தோ', 'thO' : u'தோ', 'theLa' : u'தெள', 

        'ntha' : u'ந்த', 'nthaa' : u'ந்தா', 'nthA' : u'ந்தா', 'nthi' : u'ந்தி', 'nthii' : u'ந்தீ', 'nthI' : u'ந்தீ', 'nthu' : u'ந்து', 'nthuu' : u'ந்தூ', 'nthU' : u'ந்தூ', 
        'nthe' : u'ந்தெ', 'nthee' : u'ந்தே', 'nthE' : u'ந்தே', 'nthai' : u'ந்தை', 'ntho' : u'ந்தொ', 'nthoo' : u'ந்தோ', 'nthO' : u'ந்தோ', 'ntheLa' : u'ந்தெள', 

        'wa' : u'ந', 'waa' : u'நா', 'wA' : u'நா', 'wi' : u'நி', 'wii' : u'நீ', 'wI' : u'நீ', 'wu' : u'நு', 'wuu' : u'நூ', 'wU' : u'நூ', 
        'we' : u'நெ', 'wee' : u'நே', 'wE' : u'நே', 'wai' : u'நை', 'wo' : u'நொ', 'woo' : u'நோ', 'wO' : u'நோ', 'weLa' : u'நெள', 

        'pa' : u'ப', 'paa' : u'பா', 'pA' : u'பா', 'pi' : u'பி', 'pii' : u'பீ', 'pI' : u'பீ', 'pu' : u'பு', 'puu' : u'பூ', 'pU' : u'பூ', 
        'pe' : u'பெ', 'pee' : u'பே', 'pE' : u'பே', 'pai' : u'பை', 'po' : u'பொ', 'poo' : u'போ', 'pO' : u'போ', 'peLa' : u'பெள', 

        'ba' : u'ப', 'baa' : u'பா', 'bA' : u'பா', 'bi' : u'பி', 'bii' : u'பீ', 'bI' : u'பீ', 'bu' : u'பு', 'buu' : u'பூ', 'bU' : u'பூ', 
        'be' : u'பெ', 'bee' : u'பே', 'bE' : u'பே', 'bai' : u'பை', 'bo' : u'பொ', 'boo' : u'போ', 'bO' : u'போ', 'beLa' : u'பெள', 

        'ma' : u'ம', 'maa' : u'மா', 'mA' : u'மா', 'mi' : u'மி', 'mii' : u'மீ', 'mI' : u'மீ', 'mu' : u'மு', 'muu' : u'மூ', 'mU' : u'மூ', 
        'me' : u'மெ', 'mee' : u'மே', 'mE' : u'மே', 'mai' : u'மை', 'mo' : u'மொ', 'moo' : u'மோ', 'mO' : u'மோ', 'meLa' : u'மெள', 

        'ya' : u'ய', 'yaa' : u'யா', 'yA' : u'யா', 'yi' : u'யி', 'yii' : u'யீ', 'yI' : u'யீ', 'yu' : u'யு', 'yuu' : u'யூ', 'yU' : u'யூ', 
        'ye' : u'யெ', 'yee' : u'யே', 'yE' : u'யே', 'yai' : u'யை', 'yo' : u'யொ', 'yoo' : u'யோ', 'yO' : u'யோ', 'yeLa' : u'யெள', 

        'ra' : u'ர', 'raa' : u'ரா', 'rA' : u'ரா', 'ri' : u'ரி', 'rii' : u'ரீ', 'rI' : u'ரீ', 'ru' : u'ரு', 'ruu' : u'ரூ', 'rU' : u'ரூ', 
        're' : u'ரெ', 'ree' : u'ரே', 'rE' : u'ரே', 'rai' : u'ரை', 'ro' : u'ரொ', 'roo' : u'ரோ', 'rO' : u'ரோ', 'reLa' : u'ரெள', 

        'la' : u'ல', 'laa' : u'லா', 'lA' : u'லா', 'li' : u'லி', 'lii' : u'லீ', 'lI' : u'லீ', 'lu' : u'லு', 'luu' : u'லூ', 'lU' : u'லூ', 
        'le' : u'லெ', 'lee' : u'லே', 'lE' : u'லே', 'lai' : u'லை', 'lo' : u'லொ', 'loo' : u'லோ', 'lO' : u'லோ', 'leLa' : u'லெள', 

        'va' : u'வ', 'vaa' : u'வா', 'vA' : u'வா', 'vi' : u'வி', 'vii' : u'வீ', 'vI' : u'வீ', 'vu' : u'வு', 'vuu' : u'வூ', 'vU' : u'வூ', 
        've' : u'வெ', 'vee' : u'வே', 'vE' : u'வே', 'vai' : u'வை', 'vo' : u'வொ', 'voo' : u'வோ', 'vO' : u'வோ', 'veLa' : u'வெள', 

        'za' : u'ழ', 'zaa' : u'ழா', 'zA' : u'ழா', 'zi' : u'ழி', 'zii' : u'ழீ', 'zI' : u'ழீ', 'zu' : u'ழு', 'zuu' : u'ழூ', 'zU' : u'ழூ', 
        'ze' : u'ழெ', 'zee' : u'ழே', 'zE' : u'ழே', 'zai' : u'ழை', 'zo' : u'ழொ', 'zoo' : u'ழோ', 'zO' : u'ழோ', 'zeLa' : u'ழெள', 

        'La' : u'ள', 'Laa' : u'ளா', 'LA' : u'ளா', 'Li' : u'ளி', 'Lii' : u'ளீ', 'LI' : u'ளீ', 'Lu' : u'ளு', 'Luu' : u'ளூ', 'LU' : u'ளூ', 
        'Le' : u'ளெ', 'Lee' : u'ளே', 'LE' : u'ளே', 'Lai' : u'ளை', 'Lo' : u'ளொ', 'Loo' : u'ளோ', 'LO' : u'ளோ', 'LeLa' : u'ளெள', 

        'Ra' : u'ற', 'Raa' : u'றா', 'RA' : u'றா', 'Ri' : u'றி', 'Rii' : u'றீ', 'RI' : u'றீ', 'Ru' : u'று', 'Ruu' : u'றூ', 'RU' : u'றூ', 
        'Re' : u'றெ', 'Ree' : u'றே', 'RE' : u'றே', 'Rai' : u'றை', 'Ro' : u'றொ', 'Roo' : u'றோ', 'RO' : u'றோ', 'ReLa' : u'றெள', 

        'na' : u'ன', 'naa' : u'னா', 'nA' : u'னா', 'ni' : u'னி', 'nii' : u'னீ', 'nI' : u'னீ', 'nu' : u'னு', 'nuu' : u'னூ', 'nU' : u'னூ', 
        'ne' : u'னெ', 'nee' : u'னே', 'nE' : u'னே', 'nai' : u'னை', 'no' : u'னொ', 'noo' : u'னோ', 'nO' : u'னோ', 'neLa' : u'னெள',

        'ja' : u'ஜ', 'jaa' : u'ஜா', 'jA' : u'ஜா', 'ji' : u'ஜி', 'jii' : u'ஜீ', 'jI' : u'ஜீ', 'ju' : u'ஜு', 'juu' : u'ஜூ', 'jU' : u'ஜூ',
        'je' : u'ஜெ', 'jee' : u'ஜே', 'jE' : u'ஜே', 'jai' : u'ஜை', 'jo' : u'ஜொ', 'joo' : u'ஜோ', 'jO' : u'ஜோ', 'jeLa' : u'ஜெள', 

        'Sa' : u'ஸ', 'Saa' : u'ஸா', 'SA' : u'ஸா', 'Si' : u'ஸி', 'Sii' : u'ஸீ', 'SI' : u'ஸீ', 'Su' : u'ஸு', 'Suu' : u'ஸூ', 'SU' : u'ஸூ',
        'Se' : u'ஸெ', 'See' : u'ஸே', 'SE' : u'ஸே', 'Sai' : u'ஸை', 'So' : u'ஸொ', 'Soo' : u'ஸோ', 'SO' : u'ஸோ', 'SeLa' : u'ஸெள', 

        'sha' : u'ஷ', 'shaa' : u'ஷா', 'shA' : u'ஷா', 'shi' : u'ஷி', 'shii' : u'ஷீ', 'shI' : u'ஷீ', 'shu' : u'ஷு', 'shuu' : u'ஷூ', 'shU' : u'ஷூ',
        'she' : u'ஷெ', 'shee' : u'ஷே', 'shE' : u'ஷே', 'shai' : u'ஷை', 'sho' : u'ஷொ', 'shoo' : u'ஷோ', 'shO' : u'ஷோ', 'sheLa' : u'ஷெள', 

        'ksha' : u'க்ஷ', 'kshaa' : u'க்ஷா', 'kshA' : u'க்ஷா', 'kshi' : u'க்ஷி', 'kshii' : u'க்ஷீ', 'kshI' : u'க்ஷீ', 'kshu' : u'க்ஷு', 'kshuu' : u'க்ஷூ', 'kshU' : u'க்ஷூ',
        'kshe' : u'க்ஷெ', 'kshee' : u'க்ஷே', 'kshE' : u'க்ஷே', 'kshai' : u'க்ஷை', 'ksho' : u'க்ஷொ', 'kshoo' : u'க்ஷோ', 'kshO' : u'க்ஷோ', 'ksheLa' : u'க்ஷெள', 

        'ha' : u'ஹ', 'haa' : u'ஹா', 'hA' : u'ஹா', 'hi' : u'ஹி', 'hii' : u'ஹீ', 'hI' : u'ஹீ', 'hu' : u'ஹு', 
        'huu' : u'ஹூ', 'hU' : u'ஹூ', 'he' : u'ஹெ', 'hee' : u'ஹே', 'hE' : u'ஹே', 'hai' : u'ஹை', 'ho' : u'ஹொ', 
        'hoo' : u'ஹோ', 'hO' : u'ஹோ', 'heLa' : u'ஹெள', 
        },
    
    MALAYALAM_FLAG :
        {

        'a' : u'അ', 'aa' : u'ആ', 'A' : u'ആ', 'i' : u'ഇ', 'ii' : u'ഈ', 'I' : u'ഈ', 'u' : u'ഉ', 'uu' : u'ഊ', 'U' : u'ഊ', 
        'e' : u'എ', 'ee' : u'ഏ', 'E' : u'ഏ', 'ai' : u'ഐ', 'o' : u'ഒ', 'oo' : u'ഓ', 'O' : u'ഓ', 'ou' : u'ഔ', 
        
	"kam" : u'കം',  "kaha" : u'കഃ',  "kaa" : u'കാ',  "kA" : u'കാ',  "ki" : u'കി',  "kii" : u'കീ',  "kI" : u'കീ',  "ku" : u'കു',  "kuu" : u'കൂ',  "kU" : u'കൂ',  
	"kru" : u'കൃ',  "ke" : u'കെ',  "kee" : u'കേ',  "kE" : u'കേ',  "kai" : u'കൈ',  "ko" : u'കൊ',  "koo" : u'കോ',  "kO" : u'കോ',  "kau" : u'കൗ',  "k" : u'ക്',  "ka" : u'ക',  

	"Kam" : u'ഖം',  "Kaha" : u'ഖഃ',  "Kaa" : u'ഖാ',  "KA" : u'ഖാ',  "Ki" : u'ഖി',  "Kii" : u'ഖീ',  "KI" : u'ഖീ',  "Ku" : u'ഖു',  "Kuu" : u'ഖൂ',  "KU" : u'ഖൂ',  
	"Kru" : u'ഖൃ',  "Ke" : u'ഖെ',  "Kee" : u'ഖേ',  "KE" : u'ഖേ',  "Kai" : u'ഖൈ',  "Ko" : u'ഖൊ',  "Koo" : u'ഖോ',  "KO" : u'ഖോ',  "Kau" : u'ഖൗ',  "K" : u'ഖ്',  "Ka" : u'ഖ',  

	"gam" : u'ഗം',  "gaha" : u'ഗഃ',  "gaa" : u'ഗാ',  "gA" : u'ഗാ',  "gi" : u'ഗി',  "gii" : u'ഗീ',  "gI" : u'ഗീ',  "gu" : u'ഗു',  "guu" : u'ഗൂ',  "gU" : u'ഗൂ',  
	"gru" : u'ഗൃ',  "ge" : u'ഗെ',  "gee" : u'ഗേ',  "gE" : u'ഗേ',  "gai" : u'ഗൈ',  "go" : u'ഗൊ',  "goo" : u'ഗോ',  "gO" : u'ഗോ',  "gau" : u'ഗൗ',  "g" : u'ഗ്',  "ga" : u'ഗ',  

	"Gam" : u'ഘം',  "Gaha" : u'ഘഃ',  "Gaa" : u'ഘാ',  "GA" : u'ഘാ',  "Gi" : u'ഘി',  "Gii" : u'ഘീ',  "GI" : u'ഘീ',  "Gu" : u'ഘു',  "Guu" : u'ഘൂ',  "GU" : u'ഘൂ',  
	"Gru" : u'ഘൃ',  "Ge" : u'ഘെ',  "Gee" : u'ഘേ',  "GE" : u'ഘേ',  "Gai" : u'ഘൈ',  "Go" : u'ഘൊ',  "Goo" : u'ഘോ',  "GO" : u'ഘോ',  "Gau" : u'ഘൗ',  "G" : u'ഘ്',  "Ga" : u'ഘ',  

	"nam" : u'ങം',  "naha" : u'ങഃ',  "naa" : u'ങാ',  "nA" : u'ങാ',  "ni" : u'ങി',  "nii" : u'ങീ',  "nI" : u'ങീ',  "nu" : u'ങു',  "nuu" : u'ങൂ',  "nU" : u'ങൂ',  
	"nru" : u'ങൃ',  "ne" : u'ങെ',  "nee" : u'ങേ',  "nE" : u'ങേ',  "nai" : u'ങൈ',  "no" : u'ങൊ',  "noo" : u'ങോ',  "nO" : u'ങോ',  "nau" : u'ങൗ',  "n" : u'ങ്',  "na" : u'ങ',  

	"cham" : u'ചം',  "chaha" : u'ചഃ',  "chaa" : u'ചാ',  "chA" : u'ചാ',  "chi" : u'ചി',  "chii" : u'ചീ',  "chI" : u'ചീ',  "chu" : u'ചു',  "chuu" : u'ചൂ',  "chU" : u'ചൂ',  
	"chru" : u'ചൃ',  "che" : u'ചെ',  "chee" : u'ചേ',  "chE" : u'ചേ',  "chai" : u'ചൈ',  "cho" : u'ചൊ',  "choo" : u'ചോ',  "chO" : u'ചോ',  "chau" : u'ചൗ',  "ch" : u'ച്',  "cha" : u'ച',  

	"Cham" : u'ഛം',  "Chaha" : u'ഛഃ',  "Chaa" : u'ഛാ',  "ChA" : u'ഛാ',  "Chi" : u'ഛി',  "Chii" : u'ഛീ',  "ChI" : u'ഛീ',  "Chu" : u'ഛു',  "Chuu" : u'ഛൂ',  "ChU" : u'ഛൂ',  
	"Chru" : u'ഛൃ',  "Che" : u'ഛെ',  "Chee" : u'ഛേ',  "ChE" : u'ഛേ',  "Chai" : u'ഛൈ',  "Cho" : u'ഛൊ',  "Choo" : u'ഛോ',  "ChO" : u'ഛോ',  "Chau" : u'ഛൗ',  "Ch" : u'ഛ്',  "Cha" : u'ഛ',  

	"jam" : u'ജം',  "jaha" : u'ജഃ',  "jaa" : u'ജാ',  "jA" : u'ജാ',  "ji" : u'ജി',  "jii" : u'ജീ',  "jI" : u'ജീ',  "ju" : u'ജു',  "juu" : u'ജൂ',  "jU" : u'ജൂ',  
	"jru" : u'ജൃ',  "je" : u'ജെ',  "jee" : u'ജേ',  "jE" : u'ജേ',  "jai" : u'ജൈ',  "jo" : u'ജൊ',  "joo" : u'ജോ',  "jO" : u'ജോ',  "jau" : u'ജൗ',  "j" : u'ജ്',  "ja" : u'ജ',  

	"Jam" : u'ഝം',  "Jaha" : u'ഝഃ',  "Jaa" : u'ഝാ',  "JA" : u'ഝാ',  "Ji" : u'ഝി',  "Jii" : u'ഝീ',  "JI" : u'ഝീ',  "Ju" : u'ഝു',  "Juu" : u'ഝൂ',  "JU" : u'ഝൂ',  
	"Jru" : u'ഝൃ',  "Je" : u'ഝെ',  "Jee" : u'ഝേ',  "JE" : u'ഝേ',  "Jai" : u'ഝൈ',  "Jo" : u'ഝൊ',  "Joo" : u'ഝോ',  "JO" : u'ഝോ',  "Jau" : u'ഝൗ',  "J" : u'ഝ്',  "Ja" : u'ഝ',  

	"Nam" : u'ഞം',  "Naha" : u'ഞഃ',  "Naa" : u'ഞാ',  "NA" : u'ഞാ',  "Ni" : u'ഞി',  "Nii" : u'ഞീ',  "NI" : u'ഞീ',  "Nu" : u'ഞു',  "Nuu" : u'ഞൂ',  "NU" : u'ഞൂ',  
	"Nru" : u'ഞൃ',  "Ne" : u'ഞെ',  "Nee" : u'ഞേ',  "NE" : u'ഞേ',  "Nai" : u'ഞൈ',  "No" : u'ഞൊ',  "Noo" : u'ഞോ',  "NO" : u'ഞോ',  "Nau" : u'ഞൗ',  "N" : u'ഞ്',  "Na" : u'ഞ',  

	"tam" : u'ടം',  "taha" : u'ടഃ',  "taa" : u'ടാ',  "tA" : u'ടാ',  "ti" : u'ടി',  "tii" : u'ടീ',  "tI" : u'ടീ',  "tu" : u'ടു',  "tuu" : u'ടൂ',  "tU" : u'ടൂ',  
	"tru" : u'ടൃ',  "te" : u'ടെ',  "tee" : u'ടേ',  "tE" : u'ടേ',  "tai" : u'ടൈ',  "to" : u'ടൊ',  "too" : u'ടോ',  "tO" : u'ടോ',  "tau" : u'ടൗ',  "t" : u'ട്',  "ta" : u'ട',  

	"tham" : u'ഠം',  "thaha" : u'ഠഃ',  "thaa" : u'ഠാ',  "thA" : u'ഠാ',  "thi" : u'ഠി',  "thii" : u'ഠീ',  "thI" : u'ഠീ',  "thu" : u'ഠു',  "thuu" : u'ഠൂ',  "thU" : u'ഠൂ',  
	"thru" : u'ഠൃ',  "the" : u'ഠെ',  "thee" : u'ഠേ',  "thE" : u'ഠേ',  "thai" : u'ഠൈ',  "tho" : u'ഠൊ',  "thoo" : u'ഠോ',  "thO" : u'ഠോ',  "thau" : u'ഠൗ',  "th" : u'ഠ്',  "tha" : u'ഠ',  

	"dam" : u'ഡം',  "daha" : u'ഡഃ',  "daa" : u'ഡാ',  "dA" : u'ഡാ',  "di" : u'ഡി',  "dii" : u'ഡീ',  "dI" : u'ഡീ',  "du" : u'ഡു',  "duu" : u'ഡൂ',  "dU" : u'ഡൂ',  
	"dru" : u'ഡൃ',  "de" : u'ഡെ',  "dee" : u'ഡേ',  "dE" : u'ഡേ',  "dai" : u'ഡൈ',  "do" : u'ഡൊ',  "doo" : u'ഡോ',  "dO" : u'ഡോ',  "dau" : u'ഡൗ',  "d" : u'ഡ്',  "da" : u'ഡ',  

	"dham" : u'ഢം',  "dhaha" : u'ഢഃ',  "dhaa" : u'ഢാ',  "dhA" : u'ഢാ',  "dhi" : u'ഢി',  "dhii" : u'ഢീ',  "dhI" : u'ഢീ',  "dhu" : u'ഢു',  "dhuu" : u'ഢൂ',  "dhU" : u'ഢൂ',  
	"dhru" : u'ഢൃ',  "dhe" : u'ഢെ',  "dhee" : u'ഢേ',  "dhE" : u'ഢേ',  "dhai" : u'ഢൈ',  "dho" : u'ഢൊ',  "dhoo" : u'ഢോ',  "dhO" : u'ഢോ',  "dhau" : u'ഢൗ',  "dh" : u'ഢ്',  "dha" : u'ഢ',  

	"wam" : u'ണം',  "waha" : u'ണഃ',  "waa" : u'ണാ',  "wA" : u'ണാ',  "wi" : u'ണി',  "wii" : u'ണീ',  "wI" : u'ണീ',  "wu" : u'ണു',  "wuu" : u'ണൂ',  "wU" : u'ണൂ',  
	"wru" : u'ണൃ',  "we" : u'ണെ',  "wee" : u'ണേ',  "wE" : u'ണേ',  "wai" : u'ണൈ',  "wo" : u'ണൊ',  "woo" : u'ണോ',  "wO" : u'ണോ',  "wau" : u'ണൗ',  "w" : u'ണ്',  "wa" : u'ണ',  

	"Tam" : u'തം',  "Taha" : u'തഃ',  "Taa" : u'താ',  "TA" : u'താ',  "Ti" : u'തി',  "Tii" : u'തീ',  "TI" : u'തീ',  "Tu" : u'തു',  "Tuu" : u'തൂ',  "TU" : u'തൂ',  
	"Tru" : u'തൃ',  "Te" : u'തെ',  "Tee" : u'തേ',  "TE" : u'തേ',  "Tai" : u'തൈ',  "To" : u'തൊ',  "Too" : u'തോ',  "TO" : u'തോ',  "Tau" : u'തൗ',  "T" : u'ത്',  "Ta" : u'ത',  

	"Tham" : u'ഥം',  "Thaha" : u'ഥഃ',  "Thaa" : u'ഥാ',  "ThA" : u'ഥാ',  "Thi" : u'ഥി',  "Thii" : u'ഥീ',  "ThI" : u'ഥീ',  "Thu" : u'ഥു',  "Thuu" : u'ഥൂ',  "ThU" : u'ഥൂ',  
	"Thru" : u'ഥൃ',  "The" : u'ഥെ',  "Thee" : u'ഥേ',  "ThE" : u'ഥേ',  "Thai" : u'ഥൈ',  "Tho" : u'ഥൊ',  "Thoo" : u'ഥോ',  "ThO" : u'ഥോ',  "Thau" : u'ഥൗ',  "Th" : u'ഥ്',  "Tha" : u'ഥ',  

	"Dam" : u'ദം',  "Daha" : u'ദഃ',  "Daa" : u'ദാ',  "DA" : u'ദാ',  "Di" : u'ദി',  "Dii" : u'ദീ',  "DI" : u'ദീ',  "Du" : u'ദു',  "Duu" : u'ദൂ',  "DU" : u'ദൂ',  
	"Dru" : u'ദൃ',  "De" : u'ദെ',  "Dee" : u'ദേ',  "DE" : u'ദേ',  "Dai" : u'ദൈ',  "Do" : u'ദൊ',  "Doo" : u'ദോ',  "DO" : u'ദോ',  "Dau" : u'ദൗ',  "D" : u'ദ്',  "Da" : u'ദ',  

	"Dham" : u'ധം',  "Dhaha" : u'ധഃ',  "Dhaa" : u'ധാ',  "DhA" : u'ധാ',  "Dhi" : u'ധി',  "Dhii" : u'ധീ',  "DhI" : u'ധീ',  "Dhu" : u'ധു',  "Dhuu" : u'ധൂ',  "DhU" : u'ധൂ',  
	"Dhru" : u'ധൃ',  "Dhe" : u'ധെ',  "Dhee" : u'ധേ',  "DhE" : u'ധേ',  "Dhai" : u'ധൈ',  "Dho" : u'ധൊ',  "Dhoo" : u'ധോ',  "DhO" : u'ധോ',  "Dhau" : u'ധൗ',  "Dh" : u'ധ്',  "Dha" : u'ധ',  

	"Wam" : u'നം',  "Waha" : u'നഃ',  "Waa" : u'നാ',  "WA" : u'നാ',  "Wi" : u'നി',  "Wii" : u'നീ',  "WI" : u'നീ',  "Wu" : u'നു',  "Wuu" : u'നൂ',  "WU" : u'നൂ',  
	"Wru" : u'നൃ',  "We" : u'നെ',  "Wee" : u'നേ',  "WE" : u'നേ',  "Wai" : u'നൈ',  "Wo" : u'നൊ',  "Woo" : u'നോ',  "WO" : u'നോ',  "Wau" : u'നൗ',  "W" : u'ന്',  "Wa" : u'ന',  

	"pam" : u'പം',  "paha" : u'പഃ',  "paa" : u'പാ',  "pA" : u'പാ',  "pi" : u'പി',  "pii" : u'പീ',  "pI" : u'പീ',  "pu" : u'പു',  "puu" : u'പൂ',  "pU" : u'പൂ',  
	"pru" : u'പൃ',  "pe" : u'പെ',  "pee" : u'പേ',  "pE" : u'പേ',  "pai" : u'പൈ',  "po" : u'പൊ',  "poo" : u'പോ',  "pO" : u'പോ',  "pau" : u'പൗ',  "p" : u'പ്',  "pa" : u'പ',  

	"Pam" : u'ഫം',  "Paha" : u'ഫഃ',  "Paa" : u'ഫാ',  "PA" : u'ഫാ',  "Pi" : u'ഫി',  "Pii" : u'ഫീ',  "PI" : u'ഫീ',  "Pu" : u'ഫു',  "Puu" : u'ഫൂ',  "PU" : u'ഫൂ',  
	"Pru" : u'ഫൃ',  "Pe" : u'ഫെ',  "Pee" : u'ഫേ',  "PE" : u'ഫേ',  "Pai" : u'ഫൈ',  "Po" : u'ഫൊ',  "Poo" : u'ഫോ',  "PO" : u'ഫോ',  "Pau" : u'ഫൗ',  "P" : u'ഫ്',  "Pa" : u'ഫ',  

	"bam" : u'ബം',  "baha" : u'ബഃ',  "baa" : u'ബാ',  "bA" : u'ബാ',  "bi" : u'ബി',  "bii" : u'ബീ',  "bI" : u'ബീ',  "bu" : u'ബു',  "buu" : u'ബൂ',  "bU" : u'ബൂ',  
	"bru" : u'ബൃ',  "be" : u'ബെ',  "bee" : u'ബേ',  "bE" : u'ബേ',  "bai" : u'ബൈ',  "bo" : u'ബൊ',  "boo" : u'ബോ',  "bO" : u'ബോ',  "bau" : u'ബൗ',  "b" : u'ബ്',  "ba" : u'ബ',  

	"Bam" : u'ഭം',  "Baha" : u'ഭഃ',  "Baa" : u'ഭാ',  "BA" : u'ഭാ',  "Bi" : u'ഭി',  "Bii" : u'ഭീ',  "BI" : u'ഭീ',  "Bu" : u'ഭു',  "Buu" : u'ഭൂ',  "BU" : u'ഭൂ',  
	"Bru" : u'ഭൃ',  "Be" : u'ഭെ',  "Bee" : u'ഭേ',  "BE" : u'ഭേ',  "Bai" : u'ഭൈ',  "Bo" : u'ഭൊ',  "Boo" : u'ഭോ',  "BO" : u'ഭോ',  "Bau" : u'ഭൗ',  "B" : u'ഭ്',  "Ba" : u'ഭ',  

	"mam" : u'മം',  "maha" : u'മഃ',  "maa" : u'മാ',  "mA" : u'മാ',  "mi" : u'മി',  "mii" : u'മീ',  "mI" : u'മീ',  "mu" : u'മു',  "muu" : u'മൂ',  "mU" : u'മൂ',  
	"mru" : u'മൃ',  "me" : u'മെ',  "mee" : u'മേ',  "mE" : u'മേ',  "mai" : u'മൈ',  "mo" : u'മൊ',  "moo" : u'മോ',  "mO" : u'മോ',  "mau" : u'മൗ',  "m" : u'മ്',  "ma" : u'മ',  

	"yam" : u'യം',  "yaha" : u'യഃ',  "yaa" : u'യാ',  "yA" : u'യാ',  "yi" : u'യി',  "yii" : u'യീ',  "yI" : u'യീ',  "yu" : u'യു',  "yuu" : u'യൂ',  "yU" : u'യൂ',  
	"yru" : u'യൃ',  "ye" : u'യെ',  "yee" : u'യേ',  "yE" : u'യേ',  "yai" : u'യൈ',  "yo" : u'യൊ',  "yoo" : u'യോ',  "yO" : u'യോ',  "yau" : u'യൗ',  "y" : u'യ്',  "ya" : u'യ',  

	"ram" : u'രം',  "raha" : u'രഃ',  "raa" : u'രാ',  "rA" : u'രാ',  "ri" : u'രി',  "rii" : u'രീ',  "rI" : u'രീ',  "ru" : u'രു',  "ruu" : u'രൂ',  "rU" : u'രൂ',  
	"rru" : u'രൃ',  "re" : u'രെ',  "ree" : u'രേ',  "rE" : u'രേ',  "rai" : u'രൈ',  "ro" : u'രൊ',  "roo" : u'രോ',  "rO" : u'രോ',  "rau" : u'രൗ',  "r" : u'ര്',  "ra" : u'ര',  

	"Ram" : u'റം',  "Raha" : u'റഃ',  "Raa" : u'റാ',  "RA" : u'റാ',  "Ri" : u'റി',  "Rii" : u'റീ',  "RI" : u'റീ',  "Ru" : u'റു',  "Ruu" : u'റൂ',  "RU" : u'റൂ',  
	"Rru" : u'റൃ',  "Re" : u'റെ',  "Ree" : u'റേ',  "RE" : u'റേ',  "Rai" : u'റൈ',  "Ro" : u'റൊ',  "Roo" : u'റോ',  "RO" : u'റോ',  "Rau" : u'റൗ',  "R" : u'റ്',  "Ra" : u'റ',  

	"lam" : u'ലം',  "laha" : u'ലഃ',  "laa" : u'ലാ',  "lA" : u'ലാ',  "li" : u'ലി',  "lii" : u'ലീ',  "lI" : u'ലീ',  "lu" : u'ലു',  "luu" : u'ലൂ',  "lU" : u'ലൂ',  
	"lru" : u'ലൃ',  "le" : u'ലെ',  "lee" : u'ലേ',  "lE" : u'ലേ',  "lai" : u'ലൈ',  "lo" : u'ലൊ',  "loo" : u'ലോ',  "lO" : u'ലോ',  "lau" : u'ലൗ',  "l" : u'ല്',  "la" : u'ല',  

	"Lam" : u'ളം',  "Laha" : u'ളഃ',  "Laa" : u'ളാ',  "LA" : u'ളാ',  "Li" : u'ളി',  "Lii" : u'ളീ',  "LI" : u'ളീ',  "Lu" : u'ളു',  "Luu" : u'ളൂ',  "LU" : u'ളൂ',  
	"Lru" : u'ളൃ',  "Le" : u'ളെ',  "Lee" : u'ളേ',  "LE" : u'ളേ',  "Lai" : u'ളൈ',  "Lo" : u'ളൊ',  "Loo" : u'ളോ',  "LO" : u'ളോ',  "Lau" : u'ളൗ',  "L" : u'ള്',  "La" : u'ള',  

	"zam" : u'ഴം',  "zaha" : u'ഴഃ',  "zaa" : u'ഴാ',  "zA" : u'ഴാ',  "zi" : u'ഴി',  "zii" : u'ഴീ',  "zI" : u'ഴീ',  "zu" : u'ഴു',  "zuu" : u'ഴൂ',  "zU" : u'ഴൂ',  
	"zru" : u'ഴൃ',  "ze" : u'ഴെ',  "zee" : u'ഴേ',  "zE" : u'ഴേ',  "zai" : u'ഴൈ',  "zo" : u'ഴൊ',  "zoo" : u'ഴോ',  "zO" : u'ഴോ',  "zau" : u'ഴൗ',  "z" : u'ഴ്',  "za" : u'ഴ',  

	"vam" : u'വം',  "vaha" : u'വഃ',  "vaa" : u'വാ',  "vA" : u'വാ',  "vi" : u'വി',  "vii" : u'വീ',  "vI" : u'വീ',  "vu" : u'വു',  "vuu" : u'വൂ',  "vU" : u'വൂ',  
	"vru" : u'വൃ',  "ve" : u'വെ',  "vee" : u'വേ',  "vE" : u'വേ',  "vai" : u'വൈ',  "vo" : u'വൊ',  "voo" : u'വോ',  "vO" : u'വോ',  "vau" : u'വൗ',  "v" : u'വ്',  "va" : u'വ',  

	"sam" : u'ശം',  "saha" : u'ശഃ',  "saa" : u'ശാ',  "sA" : u'ശാ',  "si" : u'ശി',  "sii" : u'ശീ',  "sI" : u'ശീ',  "su" : u'ശു',  "suu" : u'ശൂ',  "sU" : u'ശൂ',  
	"sru" : u'ശൃ',  "se" : u'ശെ',  "see" : u'ശേ',  "sE" : u'ശേ',  "sai" : u'ശൈ',  "so" : u'ശൊ',  "soo" : u'ശോ',  "sO" : u'ശോ',  "sau" : u'ശൗ',  "s" : u'ശ്',  "sa" : u'ശ',  

	"sham" : u'ഷം',  "shaha" : u'ഷഃ',  "shaa" : u'ഷാ',  "shA" : u'ഷാ',  "shi" : u'ഷി',  "shii" : u'ഷീ',  "shI" : u'ഷീ',  "shu" : u'ഷു',  "shuu" : u'ഷൂ',  "shU" : u'ഷൂ',  
	"shru" : u'ഷൃ',  "she" : u'ഷെ',  "shee" : u'ഷേ',  "shE" : u'ഷേ',  "shai" : u'ഷൈ',  "sho" : u'ഷൊ',  "shoo" : u'ഷോ',  "shO" : u'ഷോ',  "shau" : u'ഷൗ',  "sh" : u'ഷ്',  "sha" : u'ഷ',  

	"Sam" : u'സം',  "Saha" : u'സഃ',  "Saa" : u'സാ',  "SA" : u'സാ',  "Si" : u'സി',  "Sii" : u'സീ',  "SI" : u'സീ',  "Su" : u'സു',  "Suu" : u'സൂ',  "SU" : u'സൂ',  
	"Sru" : u'സൃ',  "Se" : u'സെ',  "See" : u'സേ',  "SE" : u'സേ',  "Sai" : u'സൈ',  "So" : u'സൊ',  "Soo" : u'സോ',  "SO" : u'സോ',  "Sau" : u'സൗ',  "S" : u'സ്',  "Sa" : u'സ',  

	"ham" : u'ഹം',  "haha" : u'ഹഃ',  "haa" : u'ഹാ',  "hA" : u'ഹാ',  "hi" : u'ഹി',  "hii" : u'ഹീ',  "hI" : u'ഹീ',  "hu" : u'ഹു',  "huu" : u'ഹൂ',  "hU" : u'ഹൂ',  
	"hru" : u'ഹൃ',  "he" : u'ഹെ',  "hee" : u'ഹേ',  "hE" : u'ഹേ',  "hai" : u'ഹൈ',  "ho" : u'ഹൊ',  "hoo" : u'ഹോ',  "hO" : u'ഹോ',  "hau" : u'ഹൗ',  "h" : u'ഹ്',  "ha" : u'ഹ',  

        'kva' : u"ക്വ",         'gva' : u'ഗ്വ',        'Kva' : u'ഖ്വ',        'Gva' : u'ഘ്വ',            
    },
    
    }


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                   'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                   'q', 'r', 's', 't', 'u', 'v', 'w',
                   'x', 'y', 'z',
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                   'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                   'X', 'Y', 'Z'
                   ]
