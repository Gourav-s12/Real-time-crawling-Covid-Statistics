import ply.lex as lex
import ply.yacc as yacc
import re
from urllib.request import Request, urlopen

arr = []
s = ''

###DEFINING TOKENS###
tokens_list = []

### DEFINING TOKENS ###
tokens = ('OH2', 'CH2', 'EDIT', 'OH3', 'CH3', 'SKIP', 'END', 'STYLE', 'OLI',
          'OT', 'CT', 'OR', 'CR', 'OHR', 'CHR', 'OPEF', 'CPEF', 'CNTNT', 
          'OTA', 'CTA' ,'OPSN', 'CPSN', 'ODV', 'CLDIV', 'OTLE', 'CTLE', 'GBAG')

t_ignore = '\t'

###############Tokenizer Rules################
def t_SKIP(t):
    r'<h2.class="vector-pinnable-header-label">CNTNTs</h2>'
    t.value = '<h2 class="vector-pinnable-header-label">CNTNTs</h2>'
    return t

def t_END(t):
    r'References</span>|External.links</span>|Notes</span>|See.also</span>'
    t.value = 'References</span>|External.links</span>|Notes</span>|See.also</span>'
    return t

def t_OLI(t):
    r'<p>'
    t.value = '<p>'
    return t

def t_OHR(t):
    r'<th[^>]*>'
    t.value = '<th>'
    return t

def t_CPSN(t):
    r'</span[^>]*>'
    t.value = '</span>'
    return t

def t_OH3(t):
    r'<h3>'
    t.value = '<h3>'
    return t

def t_CH2(t):
    r'</h2>'
    t.value = '</h2>'
    return t

def t_OT(t):
    r'<tbody[^>]*>'
    t.value = '<tbody>'
    return t

def t_CTA(t):
    r'</td[^>]*>'
    t.value = '</td>'
    return t

def t_OTLE(t):
    r'<style[^>]*>'
    t.value = '<style>'
    return t

def t_CHR(t):
    r'</th[^>]*>'
    t.value = '</th>'
    return t

def t_ODV(t):
    r'<div[^>]*>'
    t.value = '<div>'
    return t

def t_CPEF(t):
    r'</a>'
    t.value = '</a>'
    return t

def t_CH3(t):
    r'</h3>'
    t.value = '</h3>'
    return t
    
def t_CT(t):
    r'</tbody[^>]*>'
    t.value = '</tbody>'
    return t

def t_OPSN(t):
    r'<span[^>]*>'
    t.value = '<span>'
    return t

def t_OH2(t):
    r'<h2>'
    t.value = '<h2>'
    return t

def t_OR(t):
    r'<tr[^>]*>'
    t.value = '<tr>'
    return t

def t_EDIT(t):
    r'<span>edit</span>'
    t.value = '<span>edit</span>'
    return t

def t_CLDIV(t):
    r'</div[^>]*>'
    t.value = '</div>'
    return t

def t_OTA(t):
    r'<td[^>]*>'
    t.value = '<td>'
    return t

def t_STYLE(t):
    r'<style[^>]*>[^<]*</style>'
    t.value = '<style>...</style>'
    return t

def t_CNTNT(t):
    r'[A-Za-z0-9, /()–.\':-]+'
    return t


def t_GBAG(t):
    r'<[^>]*>'
    
def t_CGBAG(t):
    r'[A-Za-z0-9, /#&;]+'


def t_error(t):
    t.lexer.skip(1)
####################################################################################################################################################################################################
                                            #GRAMMAR RULES

def p_Begin(p):
    '''
    Begin : CNTNT_section
    '''
    
def p_CNTNT_section(p):
    '''
    CNTNT_section : OH2 CNTNT
    ''' 
    print('\n' + p[2])
    
def p_CNTNT_selection2(p):
    '''
    CNTNT_selection2 : CH2 save_CNTNT
    ''' 
    
def p_save_CNTNT(p):
    '''
    save_CNTNT : CNTNT 
                  | save_CNTNT CNTNT
    '''

def p_sub_CNTNT(p):
    '''
    CNTNT : OH3 sub_CNTNT EDIT CH3
    '''
    print(p[2], end='')

def p_sub_CNTNT_recursive(p):
    '''
    sub_CNTNT : CNTNT 
                  | sub_CNTNT CNTNT
    '''
    if len(p) == 2:
        print(p[1], end='')
    else:
        print(p[2], end='')


def p_empty_production(p):
    '''empty_production :'''
    pass

def p_syntax_error(p):
    '''syntax_error :'''
    pass


import ply.lex as lex
from urllib.request import Request, urlopen


def get_webpage_CNTNT(name):
    print('Getting page')
    req = Request('https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_'+name, headers={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    webpage_CNTNT = webpage.decode("utf8")
    with open('../Files/try.html', 'w', encoding="utf-8") as file:
        file.write(webpage_CNTNT)
    return webpage_CNTNT

def process_tokens(tokens):
    result = ''
    prev = ''
    for token in tokens:
        if token.type == 'OH2' and result:
            result += '\n\n'
        elif token.type == 'END':
            break
        elif token.type == 'OLI':
            result += '\n'
        elif token.type == 'CNTNT' and prev == 'OH3':
            result += token.value + '\n'
        elif token.type == 'CNTNT':
            result += token.value
        prev = token.type
    return result

def write_result_to_file(result, name):
    print(result)
    with open(f'../Files/Responses_{name}.txt', 'w', encoding="utf-8") as file:
        file.write(result)

def process_wikipedia_timeline(name):
    webpage_CNTNT = get_webpage_CNTNT(name)
    lexer = lex.lex()
    lexer.input(webpage_CNTNT)
    tokens = list(lexer)
    result = process_tokens(tokens)
    write_result_to_file(result, name)

if __name__ == '__main__':
    process_wikipedia_timeline('Australia_(July-December_2021)')

