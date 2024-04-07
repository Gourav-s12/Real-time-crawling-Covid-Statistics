import ply.lex as lex
import ply.yacc as yacc
import re
from urllib.request import Request, urlopen

arr = []
s = ''

###DEFINING TOKENS###
tokens = ('OPENH2', 'CLOSEH2', 'EDIT', 'OPENH3', 'CLOSEH3', 'SKIP', 'END', 'STYLE',
'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
'CONTENT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN',
'CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GA')
t_ignore = '\t'

###############Tokenizer Rules################
def t_SKIP(t):
    r'<h2.class="vector-pinnable-header-label">Contents</h2>'
    return t

def t_END(t):
    r'See.also</span>|References</span>|External.links</span>'
    return t

def t_OPENH2(t):
    r'<h2>'
    return t

def t_CLOSEH2(t):
    r'</h2>'
    return t

def t_OPENH3(t):
    r'<h3>'
    # return t

def t_CLOSEH3(t):
    r'</h3>'
    # return t
    
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
    print("Illegal character:", t.value[0])
    t.lexer.skip(1)
    
def p_st(p):
    '''
    st : T1
    '''

def p_T1(p):
    '''
    t1 : OH2 T1_CNTT_tail
    '''

def p_t1_CNTT_tail(p):
    '''
    t1_CNTT_tail : t1_CNTT tail_CH2
    '''
    print('\n' + p[1])

def p_tail_CH2(p):
    '''
    tail_CH2 : CLOSEH2
    '''
    pass


def p_t1_CNTT(p):
    '''
    t1_CNTT : single_CNTT
               | multiple_CNTT
               | h3_CNTT
    '''
    pass

def p_single_CNTT(p):
    '''
    single_CNTT : CNTT
                   | single_CNTT CNTT
    '''
    pass

def p_multiple_CNTT(p):
    '''
    multiple_CNTT : single_CNTT single_CNTT
                     | multiple_CNTT single_CNTT
    '''
    pass

def p_h3_CNTT(p):
    '''
    h3_CNTT : single_CNTT OPENH3 CNTT EDIT CLOSEH3
               | multiple_CNTT OPENH3 CNTT EDIT CLOSEH3
    '''
    pass

def p_error(p):
    pass



import urllib.request
import ply.lex as lex

def get_webpage_data(name):
    print('Getting page')
    req = urllib.request.Request('https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_' + name, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urllib.request.urlopen(req).read()
    return webpage.decode("utf8")

def process_data(data):
    ans = ''
    lexer = lex.lex()
    lexer.input(data)
    prev = ''
    is_inside_h2 = False
    for tok in lexer:
        if tok.type == 'END' and tok.value == 'See also</span>':
            break
        if prev == 'OPENH2':
            if tok.type == 'CONTENT':
                ans += tok.value + '\n'
        elif tok.type == 'CLOSEH2':
            is_inside_h2 = True
        elif is_inside_h2:
            if tok.type == 'CONTENT':
                ans += prev + tok.value
            elif tok.type != 'EDIT':
                ans += '\n\n'
                is_inside_h2 = False
        prev = tok.type
    return ans
s


def write_to_file(name, ans):
    print(ans)
    with open(f'./Files/{name}.txt', 'w', encoding="utf-8") as f:
        f.write(ans)

def main(name= '2023'):
    webpage_data = get_webpage_data(name)
    processed_data = process_data(webpage_data)
    write_to_file(name, processed_data)

# def main():
#     main('2023')  # 2019

