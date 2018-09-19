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
def t_class(t):
	r'class'
	return t
def t_break(t):
	r'break'
	return t
def t_abstract(t):
	r'abstract'
	return t
def t_AND(t):
	r'AND'
	return t
def t_array(t):
	r'array'
	return t
def t_as(t):
	r'as'
	return t
def t_switch(t):
	r'switch'
	return t
def t_case(t):
	r'case'
	return t
def t_clone(t):
	r'clone'
	return t
def t_const(t):
	r'const'
	return t
def t___construct(t):
	r'__construct'
	return t
def t_continue(t):
	r'continue'
	return t
def t_die(t):
	r'die'
	return t
def t_do(t):
	r'do'
	return t
def t_echo(t):
	r'echo'
	return t
def t_else(t):
	r'else'
	return t
def t_elseif(t):
	r'elseif'
	return t
def t_empty(t):
	r'empty'
	return t
def t_eddeclare(t):
	r'eddeclare'
	return t
def t_endif(t):
	r'endif'
	return t
def t_endwhile(t):
	r'endwhile'
	return t
def t_endfor(t):
	r'endfor'
	return t
def t_endforeach(t):
	r'endforeach'
	return t
def t_endswitch(t):
	r'endswitch'
	return t
def t_eval(t):
	r'eval'
	return t
def t_exit(t):
	r'exit'
	return t
def t_extends(t):
	r'extends'
	return t
def t_final(t):
	r'final'
	return t
def t_finally(t):
	r'finally'
	return t
def t_for(t):
	r'for'
	return t
def t_foreach(t):
	r'foreach'
	return t
def t_function(t):
	r'function'
	return t
def t_global(t):
	r'global'
	return t
def t_goto(t):
	r'goto'
	return t
def t_if(t):
	r'if'
	return t
def t_implements(t):
	r'implements'
	return t
def t_include(t):
	r'include'
	return t
def t_include_once(t):
	r'include_once'
	return t
def t_instanceof(t):
	r'instanceof'
	return t
def t_interface(t):
	r'interface'
	return t
def t_isset(t):
	r'isset'
	return t
def t_list(t):
	r'list'
	return t
def t_namespace(t):
	r'namespace'
	return t
def t_null(t):
	r'null'
	return t
def t_or(t):
	r'or'
	return t
def t_print(t):
	r'print'
	return t
def t_private(t):
	r'private'
	return t
def t_public(t):
	r'public'
	return t
def t_protected(t):
	r'protected'
	return t
def t_require(t):
	r'require'
	return t
def t_require_once(t):
	r'require_once'
	return t
def t_return(t):
	r'return'
	return t
def t_static(t):
	r'static'
	return t
def t_throw(t):
	r'throw'
	return t
def t_try(t):
	r'try'
	return t
def t_unset(t):
	r'unset'
	return t
def t_use(t):
	r'use'
	return t
def t_void(t):
	r'void'
	return t
def t_var(t):
	r'var'
	return t
def t_while(t):
	r'while'
	return t
def t_xor(t):
	r'xor'
	return t
def t_TRUE(t):
	r'TRUE'
	return t
def t_FALSE(t):
	r'FALSE'
	return t

def t_VARIABLE(t):
    r'\$w+(_\d\w)*'
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
