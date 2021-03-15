from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas

BIRTH_YEAR = 1920

def read_file():
    excel_data_df = pandas.read_excel('wine.xlsx', sheet_name='Лист1')
    return excel_data_df.to_dict(orient='records')

wine_cards = read_file()

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
