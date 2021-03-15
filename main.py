from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
from collections import defaultdict

BIRTH_YEAR = 1920


def read_file():
    wine_data = pandas.read_excel(
        'wine3.xlsx',
        sheet_name='Лист1',
        na_values='nan',
        keep_default_na=False)\
        .sort_values(by='Категория')
    return wine_data.to_dict(orient='records')


def group_wine_cards(wine_cards):
    wine_cards_groups = defaultdict(list)
    for wine_card in wine_cards:
        key = wine_card['Категория']
        wine_cards_groups[key].append(wine_card)
    return wine_cards_groups


def get_company_age():
    current_year = datetime.date.today().year
    age = current_year - BIRTH_YEAR
    return age


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    company_age = get_company_age()
    wine_cards = read_file()
    wine_cards_groups = group_wine_cards(wine_cards)

    template = env.get_template('template.html')
    rendered_page = template.render(
        company_age=company_age,
        wine_cards_groups=wine_cards_groups,
    )
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()