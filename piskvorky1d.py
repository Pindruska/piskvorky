"""
Dnešním úkolem je naprogramovat hru 1D Piškvorky. Nakonec bude fungovat následovně:

1-D piškvorky se hrají na řádku s dvaceti políčky. Hráči střídavě přidávají kolečka (`o`) a křížky (`x`), třeba:
1. kolo: -------x------------
2. kolo: -------x--o---------
3. kolo: -------xx-o---------
4. kolo: -------xxoo---------
5. kolo: ------xxxoo---------
Hráč, která dá tři své symboly vedle sebe, vyhrál."""

import random

def vyhodnot(pole):
	"""Vrati jednoznakovy retezec podle stavu hry"""
	if 'xxx' in pole:
		return "x"
	elif 'ooo' in pole:
		return "o"
	elif '-' not in pole:
		return "!"
	else:
		return "-"

#print(vyhodnot('xoxoxoxoxoxoxoxoxoxo'))

def tah(pole, pozice, symbol):
    """Vrátí herní pole s daným symbolem umístěným na danou pozici

    `pole` je herní pole, na které se hraje.
    `pozice` je číslo políčka. Čísluje se od nuly.
    `symbol` může být 'x' nebo 'o', podle toho jestli je tah za křížky
    nebo za kolečka.
    """

    if pozice < 0 or pozice > 19:
    	raise ValueError(f'Zadaná pozice není v rozsahu 0-19.')
    elif symbol !="x" and symbol != "o":
    	raise ValueError(f'Symbol musí být x nebo o.')
    elif "-" != pole[pozice]:
    	raise ValueError('Pozice už je obsazená.')
    else:
    	pole_list = list(pole)   #vytvářím z retezce seznam, ktery se snaze meni
    	pole_list[pozice] = symbol
    	pole = ''.join(pole_list)
    	return pole

#print(tah('--------------------', 0, 'o'))

def tah_hrace(pole, symbol):
	"""Zeptá se hráče na tah a vrátí nové herní pole
	`pole` je herní pole, na kterém se hraje.
	`symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
	 nebo za kolečka.
	"""
	while True:
		kam_hrajes = input("Kam chceš hrát? (Zadej číslo 0-19) ")
		try:
			kam_hrajes = int(kam_hrajes)
		except ValueError:
			print("Musíš zadat číslo.")
		else:
			try:
				return tah(pole, kam_hrajes, symbol)
			except ValueError:
				print("Tam nejde hrát.")

#print(tah_hrace('o-------------------', 'x'))

SABLONY = [
	"MM!", "!MM", "M!M",
	"PP!", "!PP", P!P,
	"-!M", "M!-", "-!M",
	"-M!", "P!-", "-!P"
]

def tah_pocitace(pole, symbol):
	if symbol == "x":
		p = "o"
	else:
		p = "x"

	for sablona in SABLONY:
		co_hledam = sablona.replace("M",symbol).replace("P",p).replace("!", "-")
		cim_to_nahradim = sablona.replace("M",symbol).replace("P",p).replace("!", symbol)
		if co_hledam in pole:
			pozice = pole.index(co_hledam) + sablona.index("!")
			return tah(pozice, pole, symbol)
		pozice = pole.index("-")
		return tah(pozice, pole, symbol)
	
#print(tah_pocitace('o-------------------', 'x'))

def piskvorky1d():
	"""Vytvoří řetězec s herním polem
	Stále dokola:
	zavolá volá funkci tah_hrace, a výsledek uloží jako nové pole
	vypíše stav hry
	zavolá volá funkci tah_pocitace, a výsledek uloží jako nové pole
	vypíše stav hry
	"""

	pole = "--------------------"
	symbol_hrace = "x"
	symbol_pc = "o"

	nove_pole = tah_hrace(pole, symbol_hrace)
	while True:
		print(nove_pole)
		if vyhodnot(nove_pole) == "x":
			print("Vyhrál jsi!")
			break
		elif vyhodnot(nove_pole) == "!":
			print("Remíza!")
			break
		else:
			nove_pole = tah_pocitace(nove_pole, symbol_pc)
			print("Tah počítače")
			print(nove_pole)
			if vyhodnot(nove_pole) == "o":
				print("Prohrál jsi!")
				break
			elif vyhodnot(nove_pole) == "!":
				print("Remíza!")
				break
			else:
				nove_pole = tah_hrace(nove_pole, symbol_hrace)

piskvorky1d()
