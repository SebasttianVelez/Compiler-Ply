'''

Analizador Lexico MINI-PHP

'''

import ply.lex as lex
import sys


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
	'EQUAL'
	'NOT_EQUAL'
	'L_PAREN',
	'R_PAREN',
	'DIFERENT',
	'DOLAR',
	'DIVIDE',
	'GREATER',
	'GREATER_EQUAL',
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
	'XOR'
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