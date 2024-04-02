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
'CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE')
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
    t.lexer.skip(1)
####################################################################################################################################################################################################
											#GRAMMAR RULES

def p_start(p):
    '''
        start : t1
    '''
    
def p_t1(p):
    '''
        t1 : OPENH2 CONTENT
    ''' 
    print('\n'+p[2])
    
def p_t2(p):
    '''
        t2 : CLOSEH2 save1
    ''' 
    
def p_save1(p):
    '''
        save1 : CONTENT 
              | save1 CONTENT
              | save1 OPENH3 CONTENT EDIT CLOSEH3
    '''
    if len(p) ==2: print(p[1], end='')
    elif len(p) == 6: print(p[3], end='')
    else: print(p[2], end='')


def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    pass

#########DRIVER FUNCTION#######
def a(name):
    ans = ''
    print('Getting page')
    req = Request('https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_'+name,headers ={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    mydata = webpage.decode("utf8")
    f=open('./Files/try.html','w',encoding="utf-8")
    f.write(mydata)
    f.close
    print('Processing page')
    file_obj= open('./Files/try.html','r',encoding="utf-8")
    data=file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    prev = ''
    flag = 0
    for tok in lexer:
        if tok.type == 'END':
            if tok.value == 'See also</span>': break
        if prev == 'OPENH2':
            if tok.type == 'CONTENT': ans = ans + tok.value + '\n'
        elif tok.type == 'CLOSEH2':
            flag = 1
        elif flag == 1:
            if tok.type == 'CONTENT':
                ans = ans + prev
                ans = ans + tok.value
            elif tok.type == 'EDIT':
                prev = tok.type
            else: 
                ans = ans + '\n\n'
                flag = 0
        prev = tok.type
        # print(tok)
    print(ans)
    f=open(f'./Files/{name}.txt','w',encoding="utf-8")
    f.write(ans)
    f.close
    file_obj.close()
    
def b(name):
    ans = ''
    print('Getting page')
    req = Request('https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_'+name,headers ={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    mydata = webpage.decode("utf8")
    f=open('./Files/try.html','w',encoding="utf-8")
    f.write(mydata)
    f.close
    print('Processing page')
    file_obj= open('./Files/try.html','r',encoding="utf-8")
    data=file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    prev = ''
    flag = 0
    for tok in lexer:
        if tok.type == 'END':
            if tok.value == 'See also</span>': break
        if prev == 'OPENH2':
            if tok.type == 'CONTENT': ans = ans + tok.value + '\n'
        elif tok.type == 'CLOSEH2':
            flag = 1
        elif flag == 1:
            if tok.type == 'CONTENT':
                # ans = ans + prev
                ans = ans + tok.value
            elif tok.type == 'EDIT':
                prev = tok.type
            else: 
                ans = ans + '\n\n'
                flag = 0
        prev = tok.type
        # print(tok)
    print(ans)
    f=open(f'./Files/{name}.txt','w',encoding="utf-8")
    f.write(ans)
    f.close
    file_obj.close()
    
if __name__ == '__main__':
    a('2023') #2019

    pass