import ply.lex as lex
import re
from urllib.request import Request, urlopen

arr = []
s = ''

### DEFINING TOKENS ###
tokens_dict = {
    'END': r'See\.also</span>|References</span>|External\.links</span>|June\.2020–present</span>|<b>This\.section\.is\.empty',
    'OH2': r'<h2>',
    'OPENHEADER': r'<th[^>]*>',
    'CLOSEHEADER': r'</th[^>]*>',
    'OHF': r'<a[^>]*>',
    'OH3': r'<h3>',
    'CH2': r'</h2>',
    'CH3': r'</h3>',
    'EDIT': r'<span>edit</span>',
    'OLII': r'<li>',
    'OT': r'<tbody[^>]*>',
    'CT': r'</tbody[^>]*>',
    'OR': r'<tr[^>]*>',
    'CR': r'</tr[^>]*>',
    'OPENDATA': r'<td[^>]*>',
    'CLOSEDATA': r'</td[^>]*>',
    'OAN': r'<span[^>]*>',
    'CLN': r'</span[^>]*>',
    'OPV': r'<div[^>]*>',
    'CDV': r'</div[^>]*>',
    'OSE': r'<style[^>]*>',
    'CLST': r'</style[^>]*>',
    'STYLE': r'<style[^>]*>[^<]*</style>',
    'CNTT': r'[A-Za-z0-9, /()–.\':-]+',
    'SKIP': r'<h2\.class="vector-pinnable-header-label">CNTTs</h2>',
    'GRB': r'<[^>]*>',
    'CGRB': r'[A-Za-z0-9, /#&;]+',
}

tokens = tuple(tokens_dict.keys())

def t_error(t):
    t.lexer.skip(1)

for token_name, regex in tokens_dict.items():
    regex = regex.replace('\\', '\\\\')  # Escaping backslashes in the regex
    exec(f"def t_{token_name}(t):\n    r'{regex}'\n    return t", globals(), locals())

t_ignore = '\t'

### PARSING RULES ###
# Your parsing rules here


### PARSING RULES ###

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



import ply.yacc as yacc

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
    fetch_data('Singapore_(2022)')  # You can change the country name here

