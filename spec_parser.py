from ply.lex import lex
from ply.yacc import yacc

tokens=['KV','TITLE','TBH','TBS','TBR','STH','SPL']

def t_TITLE(t):
    pass

def t_TBH(t):
    pass

def t_TBS(t):
    pass

def t_TBR(t):
    pass

def t_STH(t):
    pass

def t_SPL(t):
    pass

def p_table(p):
    '''
    table=TBH TBS table_body
    '''
    pass

def p_table_body(p):
    '''
    table_body=table_body TBR 
    '''
    pass

def p_interface(p):
    '''
    interface=TITLE table params
    '''

def p_params(p):
    '''
    params=params param
    '''

def p_param(p):
    '''
    '''

lex()
yacc()
