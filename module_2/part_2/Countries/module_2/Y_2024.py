import ply.lex as lex
import ply.yacc as yacc
import re
from urllib.request import Request, urlopen

arr = []
s = ''

###DEFINING TOKENS###
tokens = ('OPENH4', 'CLOSEH4', 'EDIT', 'STYLE', 'OPENH2',
'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
'CONTENT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN',
'CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE')
t_ignore = '\t'

###############Tokenizer Rules################
def t_OPENH4(t):
    r'<h4>'
    return t

def t_CLOSEH4(t):
    r'</h4>'
    return t

def t_OPENH2(t):
    r'<h2>'
    return t

# def t_CLOSEH3(t):
#     r'</h3>'
#     # return t
    
def t_EDIT(t):
    r'<span>edit</span>'
    return t

def t_OPENTABLE(t):
    r'<tbody[^>]*>'
    # return t

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
    
def t_STYLE(t):
    r'<style[^>]*>[^<]*</style>'
    # return t

def t_CONTENT(t):
    r'[A-Za-z0-9, /()–.\':-]+'
    return t

def t_OPENDIV(t):
    r'<div[^>]*>'

def t_CLOSEDIV(t):
    r'</div[^>]*>'

def t_OPENSTYLE(t):
    r'<style[^>]*>'

def t_CLOSESTYLE(t):
    r'</style[^>]*>'

def t_OPENSPAN(t):
    r'<span[^>]*>'
    # return t

def t_CLOSESPAN(t):
    r'</span[^>]*>'
    # return t

def t_GARBAGE(t):
    r'<[^>]*>'
    
def t_CGARBAGE(t):
    r'[A-Za-z0-9, /#&;]+'

def t_error(t):
    t.lexer.skip(1)
####################################################################################################################################################################################################
											#GRAMMAR RULES

def p_start(p):
    '''
    start : handle1
    '''
    pass

def p_t1(p):
    '''
    t1 : OPENH4 T2
    ''' 
    print(p[2])

def p_t2(p):
    '''
    T2 : CONTENT EDIT CLOSEH4 handle1
    '''
    pass

def p_t2_content(p):
    '''
    T2 : CONTENT
    '''
    print(p[1])

def p_handle1_single_content(p):
    '''
    handle1 : CONTENT
    '''
    if len(p) == 2: 
        print(p[1], end='')
    print()

def p_handle1_concat(p):
    '''
    handle1 : handle1 CONTENT
    '''
    print(p[2], end='')

def p_handle1_newline(p):
    '''
    handle1 : CONTENT handle1
    '''
    if len(p) == 3:
        print(p[1])

def p_error(p):
    pass


def p_error(p):
    pass

import urllib.request
import ply.lex as lex

def get_webpage_content(name):
    print('Getting page')
    url = 'https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_' + name
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urllib.request.urlopen(req).read()
    return webpage.decode("utf8")

def process_html_data(html_data):
    print('Processing page')
    lexer = lex.lex()
    lexer.input(html_data)
    ans = ''
    prev = ''
    is_open_h4_encountered = False
    
    for tok in lexer:
        if tok.type == 'OPENH4':
            ans += '\n\n' if is_open_h4_encountered else ''
            is_open_h4_encountered = True
            
        elif is_open_h4_encountered and tok.type == 'CONTENT':
            ans += (tok.value + '\n') if prev == 'OPENH4' else tok.value
        
        elif tok.type == 'OPENH2' and is_open_h4_encountered:
            break
        
        prev = tok.type
        
    return ans

def write_to_file(content, name):
    with open(f'../Files/{name}.txt', 'w', encoding="utf-8") as file:
        file.write(content)
    print(f'Output written to {name}.txt')

def call(name):
    webpage_content = get_webpage_content(name)
    processed_content = process_html_data(webpage_content)
    write_to_file(processed_content, name)

if __name__ == '__main__':
    call('2024')  # 2023, 2024

