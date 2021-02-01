Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> valorHora=4
>>> dias=30
>>> horasTrabalho=8
>>> vencimentoMensal=horasTrabalho*dias
>>> nome=tiago
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    nome=tiago
NameError: name 'tiago' is not defined
>>> nome="tiago"
>>> print(valorHora)
4
>>> print(horasTrabalho)
8
>>> print(vencimentoMensal)
240
>>> vencimentoMensal=horasTrabalho*dias*valorHora
>>> print(vencimentoMensal)
960
>>> float(valorHora)
4.0
>>> int(10.5)
10
>>> atr(valorHora)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    atr(valorHora)
NameError: name 'atr' is not defined
>>> str(valorHora)
'4'
>>> print(valorHora)
4
>>> nome('Angelo Ricardo')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    nome('Angelo Ricardo')
TypeError: 'str' object is not callable
>>> nome="Angelo Ricardo"
>>> print(nome)
Angelo Ricardo
>>> print("Angelo Ricardo"+valorHora)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print("Angelo Ricardo"+valorHora)
TypeError: can only concatenate str (not "int") to str
>>> print("Angelo"+"Ricardo")
AngeloRicardo
>>> int(valorHora)
4
>>> print(nome+valorHora+'teste')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(nome+valorHora+'teste')
TypeError: can only concatenate str (not "int") to str
>>> valor=[1,2,3,4,5,6,7]
>>> valor[0:5]
[1, 2, 3, 4, 5]
>>> nome="12345678"
>>> nome[0,4]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    nome[0,4]
TypeError: string indices must be integers
>>> nome[0:4]
'1234'
>>> "0" in nome
False
>>> "2" in nome
True
>>> lista=[1,4,7,12,"angelo",35]
>>> print(lista)
[1, 4, 7, 12, 'angelo', 35]
>>> lista.append("python")
>>> print(lista)
[1, 4, 7, 12, 'angelo', 35, 'python']
>>>  "angelo" in lista
 
SyntaxError: unexpected indent
>>> "angelo" in lista
True
>>> "Angelo" in lista
False
>>> lista.index("angelo")
4
>>> lista.count("angelo")
1
>>> lista.append(4)
>>> lista.index(4)
1
>>> print(lista)
[1, 4, 7, 12, 'angelo', 35, 'python', 4]
>>> lista.count(4)
2
>>> lista.remove(1)
>>> print(lista)
[4, 7, 12, 'angelo', 35, 'python', 4]
>>> lista.reverse()
>>> print(lista)
[4, 'python', 35, 'angelo', 12, 7, 4]
>>> lista.reverse(2:4)
SyntaxError: invalid syntax
>>> lsita.reverse(2,4)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    lsita.reverse(2,4)
NameError: name 'lsita' is not defined
>>> lista2=1,2,3,4,5,6,7
>>> lista2.sort
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    lista2.sort
AttributeError: 'tuple' object has no attribute 'sort'
>>> lista2.sort()
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    lista2.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> print(lista2)
(1, 2, 3, 4, 5, 6, 7)
>>> lista2=2,3,7,3,6,0
>>> lista2.sort
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    lista2.sort
AttributeError: 'tuple' object has no attribute 'sort'
>>> lista2.sort()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    lista2.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> lista2=(2,9,4,8,5,7)
>>> print(lista2)
(2, 9, 4, 8, 5, 7)
>>> lista2.sort()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    lista2.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> lista2=[9,2,8,3,7,4,6,5]
>>> lista2.sort()
>>> print(lista2)
[2, 3, 4, 5, 6, 7, 8, 9]
>>> [2, 3, 4, 5, 6, 7, 8, 9]
[2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> telefones={"angelo":939393,"ricardo":9494949}
>>> print(telefones)
{'angelo': 939393, 'ricardo': 9494949}
>>> telefones{"rita"}=919191
SyntaxError: invalid syntax
>>> telefone["rita"]=919191
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    telefone["rita"]=919191
NameError: name 'telefone' is not defined
>>> telefones["rita"]=919191
>>> print(telefones)
{'angelo': 939393, 'ricardo': 9494949, 'rita': 919191}
>>> del telefones["ricardo"]
>>> print(telefones)
{'angelo': 939393, 'rita': 919191}
>>> tuplas=("tiago","python","Udemy")
>>> tuplas
('tiago', 'python', 'Udemy')
>>> tuplas(0)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    tuplas(0)
TypeError: 'tuple' object is not callable
>>> tuplax.index(0)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    tuplax.index(0)
NameError: name 'tuplax' is not defined
>>> tuplas.index(0)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    tuplas.index(0)
ValueError: tuple.index(x): x not in tuple
>>> tuplas(0)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    tuplas(0)
TypeError: 'tuple' object is not callable
>>> tuplas[0]
'tiago'
>>> tuplas[0:1]
('tiago',)
>>> tuplas[0:3]
('tiago', 'python', 'Udemy')
>>> tuplas+tuplas
('tiago', 'python', 'Udemy', 'tiago', 'python', 'Udemy')
>>> tuplas*5
('tiago', 'python', 'Udemy', 'tiago', 'python', 'Udemy', 'tiago', 'python', 'Udemy', 'tiago', 'python', 'Udemy', 'tiago', 'python', 'Udemy')
>>> 4 in tuplas
False
>>> "Udemy" in tuplas
True
>>> numero=1
>>> if(numero==1):
	print("numero é igual a 1")

numero é igual a 1
>>> if(numero==1):
	print("Numero é igual a 1")
else
SyntaxError: invalid syntax
>>> print("Numero errado")
Numero errado
>>> if(numero==1):
	print("Numero é igual a 1")
else
SyntaxError: invalid syntax
>>> if(numero==1):
	print("Numero é igual a 1")
else 	print("Errado")
SyntaxError: invalid syntax
>>> nome="angelo"
>>> if ( "j" in nome)
SyntaxError: invalid syntax
>>> if ("j" in nome):
	print("Sim")
	elif ("h" in nome):
		
SyntaxError: invalid syntax
>>> if ("j" in nome):
	print("Sim")
	elif ("h" in nome):
		
SyntaxError: invalid syntax
>>> if ("j" in nome):
	print("Sim")
	elif ("h" in nome):
		
SyntaxError: invalid syntax
>>> if ("j" in nome):
	print("Sim")
	elif ("h" in nome)
	
SyntaxError: invalid syntax
>>> for x in range(0,5):
	print("Valor de x é: ",x)

	
Valor de x é:  0
Valor de x é:  1
Valor de x é:  2
Valor de x é:  3
Valor de x é:  4
>>> nome="Angelo"
>>> for letra in nome:
	print(letra)

	
A
n
g
e
l
o
>>> lista=["angelo", 19,"brasil"]
>>> for valor in lista:
	print(valor)

	
angelo
19
brasil
>>> numero=15
>>> while (numero>0):
	print(numero)
	numero=numero-1

	
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
>>> numero=20
>>> while True:
	numero=numero-1
	print(numero)
	if(numero==2):
		break

	
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
>>> nome="jon"
>>> print(nome)
jon
>>>  numero=10
 
SyntaxError: unexpected indent
>>> numero=10
>>> while True:
	numero=numero-1
	if (numero==4):
		continue
	print(numero):
		
SyntaxError: invalid syntax
>>> numero=10
>>> while True:
	numero=numero-1
	if (numero==4):
		continue
	print(numero)
	
SyntaxError: multiple statements found while compiling a single statement
>>> numero=10
>>> while True
SyntaxError: invalid syntax
>>> numero = 10
>>> while True:
	numero=numero-1
	if(numero==4):
		continue
	print(numero)
	if(numero==2):
		break

	
9
8
7
6
5
3
2
>>> for x in range(0,5):
	pass

>>> 