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
          'OPENHREF',
          'CLOSEHREF',
          'H3')
t_ignore = ' \t\n'
edit_encounter = 0 
has_seen_reference = False
s = ""
x = ""
###############Tokenizer Rules################
def t_FIRST(t):
     r'<h2>'
     return t

def t_H3(t): 
    r'<h3[^>]*>'
    return t

def t_OPENHREF(t):
    r'<a[^>]*>'
    return t

def t_CLOSEHREF(t):
    r'</a[^>]*>'
    return t

def t_CONTENT(t):
    r'[A-Za-z0-9, .\-:\'()]+'
    return t

def t_SKIPTAG(t):
    r'<[^>]*>'
    pass

def t_error(t):
    t.lexer.skip(1)

####################################################################################################################################################################################################
											#GRAMMAR RULES
def p_start(p):
    '''start : content_section'''

def p_content_section(p):
    '''content_section : FIRST content_items'''

count = 1
def p_content_items(p):
    '''content_items : content_item content_items
                     | content_item'''


def p_content_item(p):
    '''content_item : contents
                    | FIRST
                    | link
                    | heading'''

def p_heading(p):
    '''
    heading : H3 CONTENT
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
    x = str(p[2])
    s = ""


def p_contents(p):
    '''contents : CONTENT'''
    global has_seen_reference 
    global s 
    if p[1] == "See also":
        has_seen_reference = True

    if not has_seen_reference and p[1] != '160':
        s+=(str(p[1]))

def p_link(p):
    '''link : OPENHREF CONTENT CLOSEHREF
            | OPENHREF CONTENT CONTENT CONTENT CLOSEHREF
            | OPENHREF CONTENT CONTENT CLOSEHREF
            | OPENHREF CLOSEHREF'''
    global has_seen_reference 
    global s 
    global x
    global edit_encounter
    if len(p) == 4:
        try:
            float(p[2])
            int(p[2])
        except ValueError:
            if p[2] != 'edit' and not has_seen_reference:
                s+=(str(p[2]))
    if len(p) == 5 :
        try:
            float(p[2])
            int(p[2])
            float(p[3])
            int(p[3])
        except ValueError:
            if p[2] != 'edit' and p[3] != 'edit' and not has_seen_reference:
                s+=(str(p[2]))
                s+=(str(p[3]))



def p_error(p):
    pass


para = ""
def main(file_name, folder_name):
    global edit_encounter
    global has_seen_reference
    has_seen_reference = False
    edit_encounter = 0 

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
    main("August__2021",'response')