import ply.lex as lex
import ply.yacc as yacc
import re
from urllib.request import Request, urlopen

arr = []
s = ''

###DEFINING TOKENS###
tokens = ['OH2', 'CH2', 'EDIT', 'OH3', 'CH3', 'SKIP', 'END', 'STLE', 'OLI',
'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
'CTTNT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN',
'CLOSESPAN', 'ODIV', 'CLOSEDIV', 'OPENSTLE', 'CLOSESTLE','GA']
t_ignore = '\t'

###############Tokenizer Rules################
def t_SKIP(t):
    r'<h2.class="vector-pinnable-header-label">CTTNTs</h2>'
    return t

def t_END(t):
    r'References</span>|External.links</span>|Notes</span>|See.also</span>'
    return t

def t_EDIT(t):
    r'<span>edit</span>'
    return t

def t_OH3(t):
    r'<h3>'
    return t

def t_CH2(t):
    r'</h2>'
    # return t

def t_OH2(t):
    r'<h2>'
    return t

def t_CH3(t):
    r'</h3>'
    # return t

def t_OPENTABLE(t):
    r'<tbody[^>]*>'
    # return t

def t_OLI(t):
    r'<p>'
    return t


def t_CLOSETABLE(t):
    r'</tbody[^>]*>'
    # return t

def t_OPENROW(t):
    r'<tr[^>]*>'
    # return t

def t_CLOSEROW(t):
    r'</tr[^>]*>'
    # return t

def t_OPENHEADER(t):
    r'<th[^>]*>'
    # return t

def t_CLOSEHEADER(t):
    r'</th[^>]*>'
    # return t

def t_OPENHREF(t):
    r'<a[^>]*>'
    # return t

def t_CLOSEHREF(t):
    r'</a>'
    # return t

def t_OPENDATA(t):
    r'<td[^>]*>'
    # return t

def t_CLOSEDATA(t):
    r'</td[^>]*>'
    # return t
    
def t_STLE(t):
    r'<STLE[^>]*>[^<]*</STLE>'
    # return t

def t_CTTNT(t):
    r'[A-Za-z0-9, /()–.\':-]+'
    return t

def t_ODIV(t):
    r'<div[^>]*>'

def t_CLOSEDIV(t):
    r'</div[^>]*>'

def t_OPENSTLE(t):
    r'<STLE[^>]*>'

def t_CLOSESTLE(t):
    r'</STLE[^>]*>'

def t_OPENSPAN(t):
    r'<span[^>]*>'
    # return t

def t_CLOSESPAN(t):
    r'</span[^>]*>'
    # return t

def t_GA(t):
    r'<[^>]+>'
    t.type = 'GA'
    # return t
    
def t_CGA(t):
    r'[^<>]+'
    t.type = 'CGA'
    # return t

def t_error(t):
    print("Illegal character:", t.value[0])
    t.lexer.skip(1)

 

def p_start(p):
    '''
    start : t1 a
    '''

def p_a(p):
    '''
    a : 
    '''
    pass

def p_t1(p):
    '''
    t1 : t2
    '''

def p_t2(p):
    '''
    t2 : OH2 CTTNT CH2 save1
    '''
    print(p[2], end='')

def p_save1(p):
    '''
    save1 : 
          | save1 CTTNT
          | save1 OH3 CTTNT EDIT CH3
    '''
    if len(p) > 1:
        print(p[len(p)-2], end='')


def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    pass

import urllib.request as urllib2
import ply.lex as lex

def get_webpage(name):
    print('Getting page')
    req = urllib2.Request('https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_'+name, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urllib2.urlopen(req).read()
    mydata = webpage.decode("utf8")
    with open('./Files/try.html', 'w', encoding="utf-8") as f:
        f.write(mydata)

def process_page(name):
    print('Processing page')
    with open('./Files/try.html', 'r', encoding="utf-8") as file_obj:
        data = file_obj.read()
        lexer = lex.lex()
        lexer.input(data)
        ans = ''
        prev = ''
        for tok in lexer:
            if tok.type == 'OH2':
                if 'prev_OH2' in locals() or 'prev_OH2' in globals():
                    ans = ans + '\n\n'
                prev_OH2 = True

            elif 'prev_OH2' in locals() or 'prev_OH2' in globals():
                if tok.type == 'END': 
                    break
                elif tok.type == 'OLI': 
                    ans += '\n'
                elif tok.type == 'CTTNT':
                    if prev == 'OH3': 
                        ans += tok.value + '\n'
                    else: 
                        ans += tok.value
            prev = tok.type
    print(ans)
    with open(f'./Files/Responses_{name}.txt', 'w', encoding="utf-8") as f:
        f.write(ans)

def main():
    name = 'Australia_(July-December_2021)' # or 'Malaysia' 
    get_webpage(name)
    process_page(name)

if __name__ == '__main__':
    main()

