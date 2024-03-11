import os
# import ply.lex as lex
# import ply.yacc as yacc
from urllib.request import Request, urlopen
def main(name):
    # req = Request('https://en.wikipedia.org/wiki/2020_Summer_Olympics',headers ={'User-Agent':'Mozilla/5.0'})
    req = Request('https://en.wikipedia.org'+name,headers ={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    mydata = webpage.decode("utf8")
    f=open('webpage.html','w',encoding="utf-8")
    f.write(mydata)
    f.close

if __name__ == '__main__':
    main('/wiki/Responses_to_the_COVID-19_pandemic_in_August_2021')