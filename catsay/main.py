from random import randint
import argparse
import requests
import urllib3
from bs4 import BeautifulSoup
from drawtable import Table
# from termcolor import colored  #print(colored('hello', 'red'), colored('world', 'green'))
from .animals import doge, catto, birb
from .quotes import ret_random_quote

tb = Table(margin_x=1, margin_y=1, align='left', max_col_width=40)
parser = argparse.ArgumentParser(description='Make cats say stuff.')
parser.add_argument('-a', '--animal', help='change the animal | default : catto', metavar='', choices=['birb', 'doge'])
parser.add_argument('-m', '--myquote', help='make animal say your quote', metavar='')
args = parser.parse_args()


def lolcatzify(text_to_lcfy):
    html_doc = requests.get('https://speaklolcat.com/?' + urllib3.request.urlencode({"from": text_to_lcfy})).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    return soup.find(id='to').get_text()


if args.myquote:
    full_quote = str(args.myquote)
else:
    quote = ret_random_quote()
    full_quote = lolcatzify(quote['text']) + '\n\n\n'  # + (quote['author'])

if args.animal == 'doge':
    animal = doge[randint(0, len(doge) - 1)]
elif args.animal == 'birb':
    animal = birb[randint(0, len(birb) - 1)]
else:
    animal = catto[randint(0, len(catto) - 1)]


def main():
    tb.draw([[full_quote]])
    print('     |\n     |\n      \\' + animal)


if __name__ == '__main__':
    main()
