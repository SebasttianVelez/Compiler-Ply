'''
Creacion de un analizador lexico para reconocer operaciones en una calculadora


Sebastian Velez Montoya

git clone https://github.com/SebasttianVelez/Compiler-Ply
'''

import ply.lex as lex
import sys


#List tokens names

tokens = (

	#Reserved Words
	'SEN',
	'COS',
	'TAN',
	'COT',
	'SEC',
	'CSC',
	#Simbols
	'PLUS',
	'MINUS',
	'TIMES',
	'DIVIDE',
	'COMMA',
	'LPAREN',
	'RPAREN',


	#Other
	'NUMBER',
	'ID',
)

# Regular expressions rules for a simple tokens 

t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'

#Reconoce numeros

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

#Palabras Reservadas
def t_SEN(t):
	r'sen'
	return t
def t_COS(t):
	r'cos'
	return t
def t_TAN(t):
	r'tan'
	return t
def t_COT(t):
	r'cot'
	return t
def t_SEC(t):
	r'sec'
	return t
def t_CSC(t):
	r'csc'
	return t

def t_ID(t):
    r'\w+(_\d\w)*'
    return t

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)

def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()

if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'data.op'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	input()