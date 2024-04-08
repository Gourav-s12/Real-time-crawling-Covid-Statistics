import ply.lex as lex
import ply.yacc as yacc
import re
import marge_output as mo

### DEFINING TOKENS ###
tokens = ('OPEN_LINK', 'CLOSE_LINK',
          'CONTENT', 'OPEN_LIST_ITEM', 'CLOSE_LIST_ITEM', 'GARBAGE')
t_ignore = '\t'

############### Tokenizer Rules ################


def t_CONTENT(t):
    r'[A-Za-z0-9, #"–/s//./-]+'   # [A-Za-z0-9, –//./-]+'
    return t


def t_OPEN_LINK(t):
    r'<a[^>]*>'
    return t


def t_CLOSE_LINK(t):
    r'</a[^>]*>'
    return t


def t_OPEN_LIST_ITEM(t):
    r'<li[^>]*>'
    return t


def t_CLOSE_LIST_ITEM(t):
    r'</li[^>]*>'
    return t


def t_GARBAGE(t):
    r'<[^>]*>'


def t_error(t):
    t.lexer.skip(1)


####################################################################################################################################################################################################
# GRAMMAR RULES


def p_start(p):
    '''start : ordered_list'''
    p[0] = p[1]


def p_ordered_list(p):
    '''ordered_list : OPEN_LIST_ITEM OPEN_LINK CONTENT CLOSE_LINK'''

    global extracted_links
    if len(p) == 5:
        if (re.search(r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\b', p[3]) \
                and ('timeline' in p[2].lower() or 'response' in p[2].lower())) \
                and re.search(r'\b\d{4}\b', p[2]):
            match = re.search(r'href="([^"]+)"', p[2])
            if match:
                extracted_links.append(match.group(1))
        elif re.search(r'_of_the_COVID-19_pandemic_in_(\d{4})', p[2]):
            match = re.search(r'href="([^"]+)"', p[2])
            if match:
                extracted_links.append(match.group(1))


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

######### DRIVER FUNCTION ########
extracted_links = []


def main():
    global extracted_links
    file_handle = open('main.html', 'r', encoding="utf-8")
    data_content = file_handle.read()
    lexer_obj = lex.lex()
    lexer_obj.input(data_content)
    # with open('token.txt', 'w') as file:
    #     # Write the line to the file
    #     for token in lexer_obj:
    #         file.write("\n")
    #         file.write(str(token))
    parser = yacc.yacc()
    parser.parse(data_content)
    file_handle.close()

    # Save links to a text file
    return extracted_links
