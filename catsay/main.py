from random import randint
import argparse
import requests
import urllib3
from bs4 import BeautifulSoup
from drawtable import Table
# from termcolor import colored  #print(colored('hello', 'red'), colored('world', 'green'))
from .animals import *
from .quotes import ret_random_quote
nam = ''
animal_choices_list = ['cat','dog','duck','camel','deer','dolphin','whale','snail','butterfly','hedgehog','fox','hippo','otter','rabbit','mouse']
animal_choices_dic = {'cat': 'cat[0]', 'dog': 'dog[0]', 'duck': 'duck[0]', 'camel': 'camel[0]', 'deer': 'deer[0]', 'dolphin': 'dolphin[0]', 'whale': 'whale[0]', 'snail': 'snail[0]', 'butterfly': 'butterfly[0]', 'hedgehog': 'hedgehog[0]', 'fox': 'fox[0]', 'hippo': 'hippo[0]', 'otter': 'otter[0]', 'rabbit': 'rabbit[0]', 'mouse': 'mouse[0]'}

tb = Table(margin_x=1, margin_y=1, align='left', max_col_width=40)
parser = argparse.ArgumentParser(description='Make cats say stuff.')
parser.add_argument('-a', '--animal', help='change the animal | default : catto', metavar='', choices=animal_choices)
parser.add_argument('-q', '--quote', help='make animal say your quote', metavar='')
args = parser.parse_args()


def lolcatzify(text_to_lcfy):
    html_doc = requests.get('https://speaklolcat.com/?' + urllib3.request.urlencode({"from": text_to_lcfy})).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    return soup.find(id='to').get_text()


if args.quote:
    full_quote = str(args.quote)
    full_quote.capitalize()
else:
    quote = ret_random_quote()
    full_quote = lolcatzify(quote['text']) + '\n\n\n'  # + (quote['author'])

if args.animal in animal_choices_list:
    args.animal = nam
    animal = eval(animal_choices_dic[args.animal])
else:
    animal = cat[0]


def main():
    tb.draw([[full_quote]])
    print('     |\n     |\n      \\' + animal)


if __name__ == '__main__':
    main()
