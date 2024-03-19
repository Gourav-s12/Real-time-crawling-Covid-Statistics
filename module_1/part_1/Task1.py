import ply.lex as lex
import ply.yacc as yacc
import os
from urllib.request import Request, urlopen

###DEFINING TOKENS###
tokens = ('BEGINTABLE', 
'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
'CONTENT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN','TABLEHEADER','TABLECLOSER', 'WASTE','NOBR','NOBR2',
'CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE','PSTART','PEND','SUPSTART','SUPEND','FISH')
t_ignore = '\t'
lst = []
ans=[[]]
###############Tokenizer Rules################
def t_BEGINTABLE(t):
    #  r'<caption>2020.Summer.Olympics.host.city.election<sup.id="cite_ref-Statesman-AP_25-0".class="reference"><a.href=".cite_note-Statesman-AP-25">&.91;21&.93;</a></sup>'
    r'<table.id="main_table_countries_yesterday".class="table.table-bordered.table-hover.main_table_countries".style="width:100%;margin-top:.0px.!important;display:none;">'
    return t
def t_TABLEHEADER(t):
    r'<thead>'
    return t
def t_CONTENT(t):
    r'[A-Za-z0-9 -, /]+'
    return t
def t_TABLECLOSER(t):
    r'</thead>'
    return t
def t_OPENTABLE(t):
    r'<tbody[^>]*>'
    return t
def t_CLOSETABLE(t):
    r'</tbody[^>]*>'
    return t
def t_OPENROW(t):
    r'<tr[^>]*>'
    return t
def t_WASTE(t):
    r'<br[^>]*'
    return t
def t_NOBR(t):
    r'<nobr>'
    return t
def t_NOBR2(t):
    r'</nobr>'
    return t
def t_FISH(t):
    r'<table[^>]*>'
    return t
def t_CLOSEROW(t):
    r'</tr[^>]*>'
    return t

def t_OPENHEADER(t):
    r'<th[^>]*>'
    return t

def t_CLOSEHEADER(t):
    r'</th[^>]*>'
    return t
def t_OPENHREF(t):
    r'<a[^>]*>'
    return t
def t_CLOSEHREF(t):
    r'</a[^>]*>'
    return t
def t_OPENDATA(t):
    r'<td[^>]*>'
    return t
def t_CLOSEDATA(t):
    r'</td>'
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

def t_CLOSESPAN(t):
    r'</span[^>]*>'
def t_GARBAGE(t):
    r'<[^>]*>'

def t_error(t):
    t.lexer.skip(1)
####################################################################################################################################################################################################
											#GRAMMAR RULES
def p_start(p):
    '''start : table'''
def p_skip(p):
    '''skip : OPENHEADER content skip
            | CLOSEHEADER content skip
            | OPENDATA content skip
            | temp content skip
            | closerow content skip
            | OPENROW content skip
            | OPENHREF content skip
            | CLOSEHREF content skip
            | NOBR content skip
            | NOBR2 content skip
            | WASTE content skip
            | content skip 
            | empty
    ''' 
def p_skipper(p):
    '''skipper : OPENHEADER content skipper
            | CLOSEHEADER content skipper
            | OPENHREF content skipper
            | CLOSEHREF content skipper
            | NOBR content skipper
            | NOBR2 content skipper
            | WASTE content skipper
            | content skipper 
            | empty
    ''' 
def p_temp(p):
    '''temp : CLOSEDATA       
    '''
    # lst.append('!')
def p_closerow(p):
    '''closerow : CLOSEROW
    '''
    lst.append('@')
def p_skiptag(p):
    '''skiptag : CONTENT skiptag
               | OPENHEADER skiptag
               | CLOSEHEADER skiptag
               | WASTE skiptag
               | NOBR skiptag
               | NOBR2 skiptag
               | OPENHREF skiptag
               | CLOSEHREF skiptag
               | empty'''
def p_row(p):
    '''row : OPENROW content data closerow content row
            | empty
    '''
def p_data(p):
    '''data : OPENDATA CLOSEDATA data
            | OPENDATA skipper CLOSEDATA data
            | content data
            | empty
    '''
    if len(p)==4:
        lst.append("---")
def p_table(p):
    '''table : BEGINTABLE CONTENT TABLEHEADER skip TABLECLOSER CONTENT OPENTABLE content row CLOSETABLE'''
    # lst.append(p[3])

def p_empty(p):
    '''empty :'''
    pass

def p_content(p):
    '''content : content CONTENT
               | empty'''
    if len(p) == 3:
        p[0] = p[1] + p[2]
        if p[2] != '160' and p[2] !=' ':
            lst.append(p[2])
    if len(p) ==2:
        p[0] = ""
def p_error(p):
    pass

#########DRIVER FUNCTION#######
def main():
    # url = "https://www.worldometers.info/coronavirus/" 
    # req = Request(url,headers ={'User-Agent':'Mozilla/5.0'})
    # webpage = urlopen(req).read()
    # mydata = webpage.decode("utf8")
    # f=open('webpage.html','w',encoding="utf-8")
    # f.write(mydata)
    # f.close
    file_obj= open('webpage.html','r',encoding="utf-8")
    data=file_obj.read()
    lexer = lex.lex()
    lexer.input(data) 
    # with open('write.txt','w') as file:
    #     for tok in lexer:
    #         # print(tok)
    #         file.write("\n")
    #         file.write(str(tok))
    # parser = yacc.yacc()
    # parser.parse(data)
    # print(lst)
    rst = []
    for i in lst:
        s = i
        count = 0
        for j in range(len(s)):
            if s[j] != ' ':
                break
            else:
                count+=1
        if count < len(s):
            x =''
            for j in range(len(s)):
                if s[j]!=' ':
                    x+=s[j]
            rst.append(x)
    i=1
    while i in range(10):
         rst[i] = rst[i]+rst[i+1]
         rst.pop(i+1)
         i+=1
    rst[i] = rst[i]+rst[i+1]+rst[i+2]
    rst.pop(i+1)
    rst.pop(i+1)
    i+=1
    while i in range(17):
        rst[i] = rst[i]+rst[i+1]
        rst.pop(i+1)
        i+=1
    i=0
    for i in range(7):
        rst.insert(23+23*i,f"C{i+1}")
    rst.insert(23*8-1,'C8')
    # print(rst)
    with open('text.txt','w') as file:
        for i in range(len(rst)):
            if rst[i] == '@':
                file.write('\n')
            else:
                file.write(rst[i])
                file.write("  ")
    print("The required data of all Countries/World/Continent is written in the textfile text.txt.\n")
    
if __name__ == '__main__':
    main()