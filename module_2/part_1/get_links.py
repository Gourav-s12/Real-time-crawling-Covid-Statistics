import ply.lex as lex
import ply.yacc as yacc
import re
import marge_output

###DEFINING TOKENS###
tokens = ('OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
          'CONTENT', 'OPENDIV', 'CLOSEDIV', 'OPENUL', 'CLOSEUL', 'OPENLI', 'CLOSELI', 'GARBAGE')
t_ignore = '\t'

###############Tokenizer Rules################


def t_CONTENT(t):
    r'[A-Za-z0-9, #"–/s//./-]+'   # [A-Za-z0-9, –//./-]+'
    return t


def t_OPENHREF(t):
    r'<a[^>]*>'
    return t


def t_CLOSEHREF(t):
    r'</a[^>]*>'
    return t


def t_OPENHEADER(t):
    r'<h2[^>]*>'
    return t


def t_CLOSEHEADER(t):
    r'</h2[^>]*>'
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


def t_CLOSELI(t):
    r'</li[^>]*>'
    return t


def t_GARBAGE(t):
    r'<[^>]*>'


def t_error(t):
    t.lexer.skip(1)


####################################################################################################################################################################################################
											#GRAMMAR RULES
def p_start(p):
    '''start : orderedlist'''
    p[0] = p[1]


def p_orderedlist(p):
    '''orderedlist : OPENLI OPENHREF CONTENT CLOSEHREF'''

    global main_list
    if len(p) == 5:
        if (re.search(r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\b', p[3]) \
                and ('timeline' in p[2].lower() or 'response' in p[2].lower())) \
                and re.search(r'\b\d{4}\b', p[2]):
            link_list.append(p[2])
        elif re.search(r'_of_the_COVID-19_pandemic_in_(\d{4})', p[2]):
            link_list.append(p[2])

def p_empty(p):
    '''empty :'''
    pass

# Error rule for syntax errors
def p_error(p):
    pass
    # if p is None:
    #     print(f"Syntax error incomplete sentence")
    # else:
    #     print(f"Syntax error at '{p.value}' at position {p.lexpos} it should not be a {p.type}")

#########DRIVER FUNCTION#######
link_list = []
def main():
    global link_list
    file_obj = open('main.html', 'r', encoding="utf-8")
    data = file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    # with open('token.txt', 'w') as file:
    #     # Write the line to the file
    #     for tok in lexer:
    #         file.write("\n")
    #         file.write(str(tok))
    parser = yacc.yacc()
    parser.parse(data)
    file_obj.close()

    extracted_links = []
    for link in link_list:
        # Extract the URL from the anchor tag
        match = re.search(r'href="([^"]+)"', link)
        if match:
            extracted_links.append(match.group(1))

    # Save links to a text file
    return extracted_links

if __name__ == '__main__':
    main()