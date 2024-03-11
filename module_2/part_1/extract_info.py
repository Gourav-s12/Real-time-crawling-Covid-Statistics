import os
import ply.lex as lex
import ply.yacc as yacc
import re
from datetime import datetime
###DEFINING TOKENS###
tokens = ('BEGINTABLE', 
'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
'OPENH3', 'CLOSEH3', 'OPENHREF', 'CLOSEHREF',
'CONTENT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN', 'OPENPARA', 'CLOSEPARA', 'OPENH2','CLOSEH2',
'CLOSESPAN', 'OPENDIV', 'CLOSEDIV','OPENUL','CLOSEUL','OPENLI','CLOSELI','GARBAGE')
t_ignore = '\t'

###############Tokenizer Rules################
def t_CONTENT(t):
    r'[A-Za-z0-9, :#"–/s//./-]+'
    return t

def t_OPENHREF(t):
    r'<a[^>]*>'
    return t

def t_CLOSEHREF(t):
    r'</a[^>]*>'
    return t

def t_OPENDIV(t):
    r'<div[^>]*>'
    return t

def t_CLOSEDIV(t):
    r'</div[^>]*>'
    return t

def t_OPENLI(t):
    r'<li[^>]*>'
    return t

def t_OPENPARA(t):
    r'<p[^>]*>'
    return t

def t_CLOSEPARA(t):
    r'</p[^>]*>'
    return t

def t_OPENH2(t):
    r'<h2[^>]*>'
    return t

def t_CLOSEH2(t):
    r'</h2[^>]*>'
    return t

def t_OPENH3(t):
    r'<h3[^>]*>'
    return t

def t_CLOSEH3(t):
    r'</h3[^>]*>'
    return t

def t_OPENSPAN(t):
    r'<span[^>]*>'
    return t

def t_CLOSESPAN(t):
    r'</span[^>]*>'
    return t

def t_CLOSELI(t):
    r'</li[^>]*>'
    return t

def t_GARBAGE(t):
    r'<[^>]*>'

def t_error(t):
    t.lexer.skip(1)

para = ''
list1 =[]
####################################################################################################################################################################################################
											#GRAMMAR RULES
def p_start(p):
    '''start : handleheader dataCell
             | handleheader dataLI
             | empty'''
    p[0] = p[1]


def p_dataContent(p):
    '''dataContent : CONTENT
                   | CONTENT CONTENT
                   | CONTENT CONTENT CONTENT
                   | CONTENT CONTENT CONTENT CONTENT
                   | CONTENT CONTENT CONTENT CONTENT CONTENT
                   | CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT
                   | CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT'''
    global para
#   if(len(p)==2):
#        if(not re.search(r'edit|tibet|see also|references|reactions', p[1],re.IGNORECASE)):
#            if(re.search(r'january|febuary|march|april|may|june|july|august|september|october|november|december',p[1],re.IGNORECASE)):
#                para+=(p[1]+':')
    curr = ''
    if(len(p)==3):
        curr =(p[1]+p[2])
    elif(len(p)==4):
        curr =(p[1]+p[2]+p[3])
    elif(len(p)==5):
        curr =(p[1]+p[2]+p[3]+p[4])
    elif(len(p)==6):
        curr =(p[1]+p[2]+p[3]+p[4]+p[5])
    elif(len(p)==7):
        curr =(p[1]+p[2]+p[3]+p[4]+p[5]+p[6])
    elif(len(p)==8):
        curr =(p[1]+p[2]+p[3]+p[4]+p[5]+p[6]+p[7])

    para = para + curr
        #        if re.search(r'January|February|March|April|May|June|July|August|September|October|November|December', p[0], re.IGNORECASE):


def p_reLI(p):
    '''reLI : dataContent dataHREF reLI
            | dataHREF dataContent reLI
            | '''

def p_dataLI(p):
    '''dataLI : OPENLI reLI CLOSELI dataLI
              | '''

def p_skiptag(p):
    '''skiptag : OPENHREF skiptag
               | CLOSEHREF skiptag
               | CONTENT skiptag
               | empty'''
def p_dataSpan(p):
    '''dataSpan : OPENSPAN CLOSESPAN
                | OPENSPAN dataContent CLOSESPAN
                | OPENSPAN
                | CLOSESPAN'''

def p_dataHREF(p):
    '''dataHREF : OPENHREF dataContent CLOSEHREF
                | OPENHREF CONTENT CONTENT CONTENT CLOSEHREF
                | OPENHREF dataSpan CLOSEHREF'''

def p_dataCell(p):
    '''dataCell : OPENPARA dataContent dataHREF dataContent dataHREF CLOSEPARA 
                | OPENPARA dataContent dataHREF CLOSEPARA
                |'''

def p_handleheader(p):
    '''handleheader : OPENH2 dataSpan dataSpan dataSpan dataSpan dataHREF dataSpan dataSpan CLOSEH2
                    | OPENH3 OPENSPAN CONTENT CLOSESPAN dataSpan dataSpan dataHREF dataSpan dataSpan CLOSEH3
                    '''
    global para
    if(len(p)==11):
        try:
            date = datetime.strptime(p[3].strip() + " 2024", "%d %B %Y").strftime("%m-%d")
        except:
            date = datetime.strptime(p[3].strip() + " 2024", "%B %d %Y").strftime("%m-%d")
        para+=("\n" +date+ ':')
    

        
def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    pass

def main(file_name, folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    match = re.match(r'(\w+)_(\d{4})', file_name)
    if match:
        month = match.group(1)
        year = match.group(2)
        # print(month+" " + year)

        month_number = {
        "january": "01",
        "february": "02",
        "march": "03",
        "april": "04",
        "may": "05",
        "june": "06",
        "july": "07",
        "august": "08",
        "september": "09",
        "october": "10",
        "november": "11",
        "december": "12"
        }[month.lower().replace("_","")]    

        year_folder = os.path.join(folder_name,year)
        if not os.path.exists(year_folder):
            os.makedirs(year_folder)
        
        output_file_path = os.path.join(year_folder, f"{year}_{month_number}.txt")


        file_obj= open('webpage.html','r',encoding="utf-8")
        data=file_obj.read()
        lexer = lex.lex()
        lexer.input(data)
        with open('token.txt', 'w') as file:
            # Write the line to the file
            for tok in lexer:
                try:
                    file.write("\n")
                    file.write(str(tok))
                except:
                    pass
        parser = yacc.yacc()
        parser.parse(data)
        file_obj.close()

        global para
        with open(output_file_path ,'w') as output_file:
            output_file.write(para+'\n')
            para=''

if __name__ == '__main__':
    main("August__2021",'timeline')