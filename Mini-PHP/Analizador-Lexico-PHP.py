
#list of tokens names

import ply.lex as lex
import sys


#List tokens names

tokens = (

	#Reserved Words
	'class',
	'break',
	'abstract',
	'and',
	'array',
	'as',
	'switch',
	'catch',
	'case',
	'clone',
	'const',
	'__construct',
	'continue',
	'die',
	'do',
	'echo',
	'else',
	'elseif',
	'empty',
	'eddeclare',
	'endif',
	'endwhile',
	'endfor',
	'endforeach',
	'endswitch',
	'eval',
	'exit',
	'extends',
	'final',
	'finally',
	'for',
	'foreach',
	'function',
	'global',
	'goto',
	'if',
	'implements',
	'include',
	'include_once',
	'instanceof',
	'interface',
	'isset',
	'list',
	'namespace',
	'null',
	'or',
	'print',
	'private',
	'public',
	'protected',
	'require',
	'require_once',
	'return',
	'static',
	'throw',
	'try',
	'unset',
	'use',
	'void',
	'var',
	'while',
	'xor',
	'TRUE',
	'FALSE',

	#Simbols
	'EQUAL',
	'NOT_EQUAL',
	'L_PAREN',
	'R_PAREN',
	'DIFERENT',
	'DOLAR',
	'DIVIDE',
	'GREATER',
	'GREATER_EQUAL',
	'SMALLER',
	'SMALLER_EQUAL',
	'EQUAL_EQUAL',
	'MORE_EQUAL',
	'MINUS_EQUAL',
	'OR_EQUAL',
	'POW',
	'POW_EQUAL',
	'WHITE_SPACE',
	'COMMENT',
	'INIT_COMMENT',
	'FINAL_COMMENT',
	'PLUS_PLUS',
	'INIT_TAG',
	'FINAL_TAG',
	'POINT',
	'POINT_AND_COME',
	'MORE',
	'MINUS',
	'SINGLE_QUOTES',#'COMILLASIMPLE',
	'DOUBLE_COMILLAS',#'COMILLASDOBLE',
	'UNDERSCORE',#'GUIONBAJO'
	'L_SQUARE_BRACKET',#'LCORCHETE',
	'R_SQUARE_BRACKET',#'RCORCHETE',
	'BARRA',#'BARRA',
	'AND_EQUAL',
	'AND',
	'OR',
	'XOR',
	'HASHTAG',
	'ASTERISK',


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



t_L_PAREN = r'('
t_R_PAREN = r')'
t_EQUAL = r'='
t_DIFERENT = r'!='
t_DOLAR = r'$'
t_DIVIDE = r'/'
t_GREATER = r'>'
t_SMALLER = r'<'
t_GREATER_EQUAL = r'>='
t_SMALLER_EQUAL = r'<='
t_EQUAL_EQUAL = r'=='
t_MORE_EQUAL = r'+='
t_MINUS_EQUAL = r'-='
t_OR_EQUAL = r'='
t_POW = r'**'
t_POW_EQUAL = r'**='
t_WHITE_SPACE = r'\n'
t_COMMENT = r'//'
t_INIT_COMMENT = r'/*'
t_FINAL_COMMENT = r'*/'
t_PLUS_PLUS = r'++'
t_INIT_TAG = r'<?php '
t_FINAL_TAG = r'?> '
t_POINT = r'.'
t_POINT_AND_COME = r';'
t_MORE = r'+'
t_MINUS = r'-'
t_SINGLE_QUOTES = r' '' '   #COMILLASIMPLE = r''
t_DOUBLE_COMILLAS = r'"'#COMILLASDOBLE = r''
t_UNDERSCORE = r'_'#GUIONBAJO
t_L_SQUARE_BRACKET = r'{'#LCORCHETE = r''
t_R_SQUARE_BRACKET = r'}'#RCORCHETE = r''
t_BARRA = r''#BARRA = r''
t_AND_EQUAL = r'&='
t_AND = r'&'
t_OR = r'or'
t_XOR = r'xor'
t_HASHTAG = r'#'
t_ASTERISK = r'*'
#Reconoce numeros.

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

	print (data)
	lexer.input(data)
	test(data, lexer)
	input()
