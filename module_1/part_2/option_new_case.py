import ply.lex as lex
import ply.yacc as yacc
import re

###DEFINING TOKENS###
tokens = ('BEGINTABLEA',
'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN','CATEGORIE',
'CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENH4', 'OPENH2', 'CLOSEH4', 'OPENH3', 'CLOSEH3', 'OPENSTYLE', 'CLOSESTYLE', 'CONTENT','GARBAGE','CHART',
    'TITLE',
    'SUBTITLE',
    'XAXIS',
    'YAXIS',
    'LEGEND',
    'CREDITS',
    'PLOTOPTIONS',
    'RESPONSIVE','NAMETAG','DATATAG','SERIES','DATATAGCLOSE')
t_ignore = '\t'

###############Tokenizer Rules################
def t_BEGINTABLEA(t):
     r'''<div.id="graph-cases-daily">'''
     return t

def t_CATEGORIE(t):
     r'''\s*(c|C)ategories?\s*:\s*\[\s*'''
     return t

def t_SERIES(t):
     r'''\s*(s|S)eries\s*:\s*\[\s*'''
     return t

def t_CHART(t):
    r'''\s*chart\:\s*{[^}]*}\s*,\s*'''
    return t

def t_TITLE(t):
    r'''\s*title\:\s*{[^}]*}\s*,\s*'''
    return t

def t_SUBTITLE(t):
    r'''\s*subtitle\:\s*{[^}]*}\s*,\s*'''
    return t

def t_XAXIS(t):
    r'''\s*xAxis\:\s*{\s*'''
    return t

def t_YAXIS(t):
    r'''\s*yAxis\:\s*{[^,]*}\s*,\s*'''
    return t

def t_LEGEND(t):
    r'''\s*legend\:\s*{[^}]*}\s*,\s*'''
    return t

def t_CREDITS(t):
    r'''\s*credits\:\s*{[^}]*}\s*,\s*'''
    return t

def t_PLOTOPTIONS(t):
    r'''\s*plotOptions\:\s*{[^}]*}\s*,\s*'''
    return t

def t_RESPONSIVE(t):
    r'''\s*responsive\:\s*{[^}]*}\s*,\s*'''
    return t

def t_NAMETAG(t):
    r'''\s*[A-Za-z0-9 #'"–//./-]+\:\s*[A-Za-z0-9 #'"–//./-]+\s*,'''
    return t

def t_DATATAG(t):
    r'''\s*(d|D)ata\s*:\s*\[\s*'''
    return t

def t_DATATAGCLOSE(t):
    r'''\s*\]\s*'''
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

def t_CLOSEROW(t):
    r'</tr[^>]*>'
    return t

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
    r'</a[^>]*>'
    # return t

def t_OPENDATA(t):
    r'<td[^>]*>'
    # return t

def t_CLOSEDATA(t):
    r'</td[^>]*>'
    # return t

# def t_OPENIMG(t):
#     r'<img[^>]*/>'
#     return t



def t_OPENDIV(t):
    r'<div[^>]*>'
    return t

def t_CLOSEDIV(t):
    r'</div[^>]*>'
    return t

# def t_OPENH4(t):
#     r'<h4[^>]*>'
#     # return t

# def t_CLOSEH4(t):
#     r'</h4[^>]*>'
#     # return t

def t_OPENH3(t):
    r'<h3[^>]*>'
    return t

# def t_OPENH2(t):
#     r'<h2[^>]*>'
#     return t

def t_CLOSEH3(t):
    r'</h3[^>]*>'
    return t


def t_OPENSTYLE(t):
    r'<style[^>]*>'
    return t

def t_CLOSESTYLE(t):
    r'</style[^>]*>'
    return t

# def t_OPENSPAN(t):
#     r'<span[^>]*>'
#     # return t

# def t_CLOSESPAN(t):
#     r'</span[^>]*>'
#     # return t

def t_CONTENT(t):
    r'[A-Za-z0-9, #"–/s//./-]+'   # [A-Za-z0-9, –//./-]+'
    return t

def t_GARBAGE(t):
    r'<[^>]*>'
    # return t

def t_error(t):
    t.lexer.skip(1)
####################################################################################################################################################################################################
											#GRAMMAR RULES
def p_start(p):
    '''start : table'''
    # print("okkkkkkkkkkkkk")
    p[0] = p[1]
def p_skiptag(p):
    '''skiptag : CONTENT skiptag
               | OPENHREF skiptag
               | CLOSEHREF skiptag
               | CHART skiptag
               | TITLE skiptag
               | SUBTITLE skiptag
               | YAXIS skiptag 
               | LEGEND skiptag 
               | CREDITS skiptag
               | PLOTOPTIONS skiptag
               | empty'''

# def p_skipnametag(p):
#     '''skipnametag : NAMETAG skipnametag
#                 | CONTENT skipnametag
#                 | empty'''
#     print("skip")

def p_handledata(p):
    '''handledata : XAXIS CATEGORIE CONTENT DATATAGCLOSE handledata
                | skiptag SERIES handleseriesdata DATATAGCLOSE skiptag RESPONSIVE 
                | empty '''

    global country_name
    # print("odjskc")
    # print(len(p))
    if len(p) == 6:
        with open('./output/new_recovered_case_date.txt', 'w') as file:
            # Write the line to the file
            file.write(p[3])

    if len(p) == 7:
        with open('./output/'+country_name+'_new_case.txt', 'w') as file:
            # Write the line to the file
            file.write(p[3])

def p_handleseriesdata(p):
    '''handleseriesdata : NAMETAG handleseriesdata
                | CONTENT handleseriesdata
                | DATATAG CONTENT DATATAGCLOSE handleseriesdata
                | empty  '''

    p[0] = ""
    
    if len(p) == 3:
        p[0] = p[2]
    if len(p) == 5:
        if p[4] == "":
            p[0] = p[2]
        else:
            p[0] = p[2] + "\n" + p[4]
    

def p_table_B(p):
    '''table : BEGINTABLEA CLOSEDIV skiptag handledata '''

def p_empty(p):
    '''empty :'''
    p[0] = ""

def p_content(p):
    '''content : CONTENT
               | empty'''
    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    pass
    # if p is None:
    #     print(f"Syntax error incomplete sentence")
    # else:
    #     print(f"Syntax error at '{p.value}' at position {p.lexpos} it should not be a {p.type}")

#########DRIVER FUNCTION#######
country_name = "India"
def main(name):
    global country_name
    country_name = name
    file_obj= open('webpage_country.html','r',encoding="utf-8")
    # print("\nICC Rankings: \n")
    data=file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    
    with open('token.txt', 'w') as file:
        # Write the line to the file
        for tok in lexer:
            file.write("\n")
            file.write(str(tok))
    parser = yacc.yacc()
    print()
    parser.parse(data)
    file_obj.close()

if __name__ == '__main__':
    main(country_name)