from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
import pprint

BIRTH_YEAR = 1920

def read_file():
    excel_data_df = pandas.read_excel('wine2.xlsx', sheet_name='Лист1', na_values='nan', keep_default_na=False)
    return excel_data_df.to_dict(orient='records')

def group_wine_cards(wine_cards):
    wine_cards_groups = {}
    for wine_card in wine_cards:
        key = wine_card['Категория']
        wine_cards_groups.setdefault(key, []).append(wine_card)
    return wine_cards_groups

wine_cards = read_file()
wine_cards_groups = group_wine_cards(wine_cards)
pprint.pprint(wine_cards_groups)

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

current_year = datetime.date.today().year
delta_year = str(current_year - BIRTH_YEAR)

rendered_page = template.render(
    delta_year=delta_year,
    wine_cards=wine_cards,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
