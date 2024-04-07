import ply.lex as lex
import ply.yacc as yacc
import re
from urllib.request import Request, urlopen
import urllib.request
import ply.lex as lex

arr = []
s = ''

###DEFINING TOKENS###
def get_tokens():
    return (
        'OH2', 'CH2', 'EDIT', 'OH3', 'CH3', 'SKIP', 'END', 'STYLE',
        'OTAB', 'CTAB', 'OROW', 'CROW',
        'OHDR', 'CHDR', 'OPHR', 'CHRF',
        'CONTENT', 'ODATA', 'CDATA', 'OSPAN',
        'CSPAN', 'ODIV', 'CDIV', 'OSTYLE', 'CSTY', 'GBG'
    )

tokens = get_tokens()

t_ignore = '\t'

###############Tokenizer Rules################
def t_SKIP(t):
    r'<h2.class="vector-pinnable-header-label">Contents</h2>'
    t.value = '<h2.class="vector-pinnable-header-label">Contents</h2>'
    return t

def t_END(t):
    r'See.also</span>|References</span>|External.links</span>|June.2020–present</span>|<b>This.section.is.empty'
    t.value = t.value
    return t

def t_CHDR(t):
    r'</th[^>]*>'
    t.value = '</th>'
    return t

def t_OTAB(t):
    r'<tbody[^>]*>'
    t.value = '<tbody>'
    return t

def t_CH2(t):
    r'</h2>'
    t.value = '</h2>'
    return t

def t_OSTYLE(t):
    r'<style[^>]*>'
    t.value = '<style>'
    return t

def t_CHRF(t):
    r'</a>'
    t.value = '</a>'
    return t

def t_CSTY(t):
    r'</style[^>]*>'
    t.value = '</style>'
    return t

def t_OHDR(t):
    r'<th[^>]*>'
    t.value = '<th>'
    return t

def t_CSPAN(t):
    r'</span[^>]*>'
    t.value = '</span>'
    return t

def t_OPHR(t):
    r'<a[^>]*>'
    t.value = '<a>'
    return t

def t_ODIV(t):
    r'<div[^>]*>'
    t.value = '<div>'
    return t

def t_OH2(t):
    r'<h2>'
    t.value = '<h2>'
    return t

def t_CDIV(t):
    r'</div[^>]*>'
    t.value = '</div>'
    return t

def t_ODATA(t):
    r'<td[^>]*>'
    t.value = '<td>'
    return t

def t_STYLE(t):
    r'<style[^>]*>[^<]*</style>'
    t.value = '<style>[^<]*</style>'
    return t

def t_CH3(t):
    r'</h3>'
    t.value = '</h3>'
    return t

def t_OH3(t):
    r'<h3>'
    t.value = '<h3>'
    return t

def t_CDATA(t):
    r'</td[^>]*>'
    t.value = '</td>'
    return t

def t_OSPAN(t):
    r'<span[^>]*>'
    t.value = '<span>'
    return t

def t_OROW(t):
    r'<tr[^>]*>'
    t.value = '<tr>'
    return t

def t_CONTENT(t):
    r'[A-Za-z0-9, /()–.\':-]+'
    t.value = t.value
    return t

def t_GBG(t):
    r'<[^>]*>'
    t.value = t.value

def t_CGBG(t):
    r'[A-Za-z0-9, /#&;]+'
    t.value = t.value

def t_error(t):
    t.lexer.skip(1)

####################################################################################################################################################################################################
                                            #GRAMMAR RULES

def p_start(p):
    '''
    start : heading_section
    '''
    
def p_heading_section(p):
    '''
    heading_section : heading
    ''' 

def p_heading(p):
    '''
    heading : OH2 heading_content CH2
    ''' 
    print('\n' + p[2])

def p_heading_content(p):
    '''
    heading_content : CONTENT 
                    | heading_content CONTENT
    '''
    if len(p) == 2:
        print(p[1], end='')
    else:
        print(p[2], end='')

def p_error(p):
    pass


#########DRIVER FUNCTION#######
def get_webpage_content(name):
    print('Getting page')
    req = Request('https://en.wikipedia.org/wiki/Responses_to_the_COVID-19_pandemic_in_'+name, headers={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    mydata = webpage.decode("utf8")
    with open(f'../Files/try_{name}.html', 'w', encoding="utf-8") as f:
        f.write(mydata)
    return mydata

def process_webpage_content(data, name):
    print('Processing page')
    ans = ''
    lexer = lex.lex()
    lexer.input(data)
    prev = ''
    for tok in lexer:
        if tok.type == 'OH3':
            ans += '\n\n' if prev == 'OH3' else ''
        elif tok.type == 'END':
            break
        elif tok.type == 'CONTENT':
            ans += tok.value + '\n' if prev == 'OH3' else tok.value
        prev = tok.type

    print(ans)
    with open(f'../Files/Responses_{name}.txt', 'w', encoding="utf-8") as f:
        f.write(ans)
        

def b(name):
    print('Getting page')
    req = urllib.request.Request('https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_' + name, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urllib.request.urlopen(req).read()
    mydata = webpage.decode("utf8")
    with open('../Files/try.html', 'w', encoding="utf-8") as f:
        f.write(mydata)
    print('Processing page')
    data = read_data_from_file()
    ans = process_data(data)
    print(ans)
    write_to_file(name, ans)

def read_data_from_file():
    with open('./Files/try.html', 'r', encoding="utf-8") as file_obj:
        return file_obj.read()

def process_data(data):
    ans = ''
    lexer = lex.lex()
    lexer.input(data)
    prev = ''
    for tok in lexer:
        if tok.type == 'OH3':
            if prev == 'OH3':
                ans += '\n\n'
        elif tok.type == 'OH2':
            break
        elif tok.type == 'CONTENT':
            if prev == 'OH3':
                ans += tok.value + '\n'
            else:
                ans += tok.value
        prev = tok.type
    return ans

def write_to_file(name, content):
    with open(f'../Files/{name}.txt', 'w', encoding="utf-8") as f:
        f.write(content)


def c(name):
    print('Getting page')
    req = urllib.request.Request('https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_'+name, headers={'User-Agent':'Mozilla/5.0'})
    webpage = urllib.request.urlopen(req).read()
    mydata = webpage.decode("utf8")
    with open('../Files/try.html', 'w', encoding="utf-8") as f:
        f.write(mydata)
    print('Processing page')
    data = read_from_file()
    processed_data = process_data(data)
    print(processed_data)
    write_to_file(name, processed_data)

def read_from_file():
    with open('../Files/try.html', 'r', encoding="utf-8") as file_obj:
        return file_obj.read()

def process_data(data):
    ans = ''
    lexer = lex.lex()
    lexer.input(data)
    prev = ''
    for tok in lexer:
        if tok.type == 'OH3':
            if prev == 'OH3':
                ans += '\n\n'
        elif tok.type == 'END':
            break
        elif tok.type == 'CONTENT':
            if prev == 'OH3':
                ans += tok.value + '\n'
            else:
                ans += tok.value
        prev = tok.type
    return ans

def write_to_file(name, content):
    with open(f'../Files/{name}.txt', 'w', encoding="utf-8") as f:
        f.write(content)
    
if __name__ == '__main__':
    c('England_(January-June_2020)')
    months = [
        'January', 'February', 'March', 'April',
        'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December'
    ]

    pass
