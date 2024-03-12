import os
import ply.lex as lex
import ply.yacc as yacc
import re
from datetime import datetime, timedelta

###DEFINING TOKENS###
tokens = ('FIRST',
          'SECOND',
          'CONTENT',
          'SKIPTAG',
          'HEADSTART',
          'HEADEND',
          'OPENHREF',
          'CLOSEHREF',
          'OPENFIG',
          'CLOSEFIG')
t_ignore = ' \t\n'
date = ""
s = ""
x = ""
###############Tokenizer Rules################
def t_FIRST(t):
     r'<h2><span.class="mw-headline".id="Pandemic_chronology">'
     return t

def t_SECOND(t):
    r'<h2><span.class="mw-headline".id="Summary">'
    return t

def t_HEADSTART(t):
    r'<h3>'
    return t

def t_HEADEND(t):
    r'</span></h3>'
    return t

def t_OPENHREF(t):
    r'<a[^>]*>'
    return t

def t_CLOSEHREF(t):
    r'</a[^>]*>'
    return t

def t_OPENFIG(t):
    r'<figure[^>]*>'
    return t

def t_CLOSEFIG(t):
    r'</figure[^>]*>'
    return t

def t_CONTENT(t):
    r'[A-Za-z0-9, .–]+'
    return t

def t_SKIPTAG(t):
    r'<[^>]*>'
    pass

def t_error(t):
    t.lexer.skip(1)
####################################################################################################################################################################################################
											#GRAMMAR RULES
def p_start(p):
    '''start : section'''

def p_section(p):
    '''section : FIRST skipTags contentSequence SECOND '''

def p_skipTags(p):
    '''
    skipTags : CONTENT skipTags
            |  OPENHREF skipTags
            | CLOSEHREF skipTags
            |
    '''
# count = 0
def p_contentSequence(p):
    '''contentSequence : date contentElement contentSequence 
                       | contentElement
    '''
    global x 
    global s
    global para
    if len(x) > 0 and len(s)>0 and any(char.isdigit() for char in x):
        x = x.replace("–", "-")
        if '-' in x:
            day_start, day_end, month_name = x.replace(" ", "").partition("-")[0], x.split("-")[1].split(" ")[0], x.split(" ")[-1]
            for i in range(int(day_start),int(day_end)+1):
                date = datetime.strptime(str(i) + " "+ month_name + " 2024", "%d %B %Y").strftime("%m-%d")
                para+=("\n" + date + ':' + s)
        else:
            try:
                date = datetime.strptime(x.strip() + " 2024", "%d %B %Y").strftime("%m-%d")
            except:
                date = datetime.strptime(x.strip() + " 2024", "%B %d %Y").strftime("%m-%d")
            para+=("\n" + date + ':' + s)
    x = ""
    s = ""

def p_date(p): 
    '''
    date : HEADSTART CONTENT OPENHREF CONTENT CLOSEHREF HEADEND
         | HEADSTART CONTENT HEADEND
    '''
    # global count
    # print(count)
    # count+=1
    global x 
    global s
    global para
    if len(x) > 0 and len(s)>0 and any(char.isdigit() for char in x):
        x = x.replace("–", "-")
        if '-' in x:
            day_start, day_end, month_name = x.replace(" ", "").partition("-")[0], x.split("-")[1].split(" ")[0], x.split(" ")[-1]
            for i in range(int(day_start),int(day_end)+1):
                date = datetime.strptime(str(i) + " "+ month_name + " 2024", "%d %B %Y").strftime("%m-%d")
                para+=("\n" + date + ':' + s)
        else:
            try:
                date = datetime.strptime(x.strip() + " 2024", "%d %B %Y").strftime("%m-%d")
            except:
                date = datetime.strptime(x.strip() + " 2024", "%B %d %Y").strftime("%m-%d")
            para+=("\n" + date + ':' + s)

    x = str(p[2])
    s = ""
    



def p_contentElement(p):
    '''contentElement : OPENHREF skip CLOSEHREF contentElement
                      | OPENFIG skipcontent CLOSEFIG contentElement
                      | CONTENT contentElement
                      | empty
                      '''
    
    global s 
    if len(p) == 3:
        s = str(p[1]) + " " + s 

def p_skip(p):
    '''skip : CONTENT skip
            | empty'''
    
    global s
    if len(p) == 3:
        try:
            float(p[1])
            int(p[1])
        except ValueError:
            if p[1] != 'edit':
                s = str(p[1]) +" "+ s

def p_skipcontent(p):
    '''skipcontent : CONTENT skipcontent
                   | OPENHREF skipcontent
                   | CLOSEHREF skipcontent
                   | empty'''

def p_content(p):
    ''' content : CONTENT'''
    global s
    if len(p) == 2:
        s = str(p[1]) + " " + s

def p_error(p):
    pass

def p_empty(p):
    '''empty :'''
    pass

para = ""
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

        # if(len(p)==11):
        # try:
        #     date = datetime.strptime(p[3].strip() + " 2024", "%d %B %Y").strftime("%m-%d")
        # except:
        #     date = datetime.strptime(p[3].strip() + " 2024", "%B %d %Y").strftime("%m-%d")
        # para+=("\n" +date+ ':')

        global para
        with open(output_file_path ,'w') as output_file:
            output_file.write(para+'\n')
            para=''

if __name__ == '__main__':
    main("August__2021",'timeline')