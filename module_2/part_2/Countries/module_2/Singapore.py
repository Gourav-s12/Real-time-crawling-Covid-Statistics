import ply.lex as lex
import ply.yacc as yacc
import re
from urllib.request import Request, urlopen

arr = []
s = ''

token_names = {
    'END', 'OH2', 'OPENHEADER', 'CLOSEHEADER', 'OHF', 'OH3', 'CH2', 'CH3', 'EDIT', 'OLII',
    'OT', 'CT', 'OR', 'CR', 'OPENDATA', 'CLOSEDATA', 'OAN', 'CLN', 'OPV', 'CDV', 'OSE', 'CLST', 'STYLE',
    'SKIP', 'GRB', 'CGRB', 'CNTT'
}

tokens = tuple(token_names)

t_ignore = '\t'


def t_SKIP(t):
    r'<h2.class="vector-pinnable-header-label">CNTTs</h2>'
    return t

def t_END(t):
    r'See.also</span>|References</span>|External.links</span>|June.2020–present</span>|<b>This.section.is.empty'
    return t


def t_OLII(t):
    r'<li>'
    return t

def t_OH2(t):
    r'<h2>'
    return t


def t_CH2(t):
    r'</h2>'
    # return t

def t_OH3(t):
    r'<h3>'
    return t

def t_CH3(t):
    r'</h3>'
    # return t

def t_CT(t):
    r'</tbody[^>]*>'
    # return t
   
def t_EDIT(t):
    r'<span>edit</span>'
    return t

def t_OT(t):
    r'<tbody[^>]*>'
    # return t


def t_OR(t):
    r'<tr[^>]*>'
    # return t

def t_CR(t):
    r'</tr[^>]*>'
    # return t

def t_OPHHRR(t):
    r'<th[^>]*>'
    # return t

def t_CLHHRR(t):
    r'</th[^>]*>'
    # return t

def t_OHF(t):
    r'<a[^>]*>'
    # return t

def t_CEF(t):
    r'</a>'
    # return t

def t_ODATA(t):
    r'<td[^>]*>'
    # return t

def t_STYLE(t):
    r'<style[^>]*>[^<]*</style>'
    # return t

def t_OPV(t):
    r'<div[^>]*>'

   
def t_CNTT(t):
    r'[A-Za-z0-9, /()–.\':-]+'
    return t

def t_CDATA(t):
    r'</td[^>]*>'
    # return t
    

def t_OSE(t):
    r'<style[^>]*>'

def t_CLST(t):
    r'</style[^>]*>'

def t_OAN(t):
    r'<span[^>]*>'
    # return t

def t_CLN(t):
    r'</span[^>]*>'
    # return t

def t_CDV(t):
    r'</div[^>]*>'

def t_CGRB(t):
    r'[A-Za-z0-9, /#&;]+'

def t_GRB(t):
    r'<[^>]*>'

def t_error(t):
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
    tail_CH2 : CH2
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
    h3_CNTT : single_CNTT OH3 CNTT EDIT CH3
               | multiple_CNTT OH3 CNTT EDIT CH3
    '''
    pass

def p_error(p):
    pass



import urllib.request as req
import ply.lex as lex

def fetch_page_data(country_name):
    request = req.Request('https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_' + country_name, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = req.urlopen(request).read()
    page_content = webpage.decode("utf8")
    with open('../Files/try.html', 'w', encoding="utf-8") as file:
        file.write(page_content)
    return '../Files/try.html'

def process_page_data(file_path):
    result = ''
    print('Processing page')
    with open(file_path, 'r', encoding="utf-8") as file_obj:
        page_content = file_obj.read()
        lexer = lex.lex()
        lexer.input(page_content)
        previous_token = ''
        inside_section = False
        for token in lexer:
            if inside_section and token.type == 'OH2':
                result += '\n\n'
            if token.type == 'OH2':
                inside_section = True
            elif token.type in ['END', 'CNTT']:
                if token.type == 'END':
                    break
                result += (token.value + '\n') if previous_token == 'OH3' else token.value
            elif token.type == 'OLII':
                result += '\n' if inside_section else ''
            previous_token = token.type
    print(result)
    return result

def fetch_data(country_name):
    file_path = fetch_page_data(country_name)
    result = process_page_data(file_path)
    with open(f'../Files/Responses_{country_name}.txt', 'w', encoding="utf-8") as file:
        file.write(result)

if __name__ == '__main__':
    fetch_data('Singapore_(2022)')  # ENGLAND SINGAPUR

