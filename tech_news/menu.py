import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)

from tech_news.analyzer.ratings import top_5_categories

option = {
    "0": "Digite quantas notícias serão buscadas:",
    "1": "Digite o título:",
    "2": "Digite a data no formato aaaa-mm-dd:",
    "3": "Digite a categoria:",
    "5": "Encerrando script\n",
}


def get_methods(value):
    options = {
        "0": lambda: get_tech_news(int(input(option[value]))),
        "1": lambda: search_by_title(input(option[value])),
        "2": lambda: search_by_date(input(option[value])),
        "3": lambda: search_by_category(input(option[value])),
    }

    selected_option = options.get(value)

    if not selected_option:
        return "Opção inválida"

    return selected_option()


def validate_option(value):
    options = ["0", "1", "2", "3", "4", "5"]
    if value not in options:
        sys.stderr.write("Opção inválida\n")
        return False
    return True


# Requisitos 11 e 12
def analyzer_menu():
    value = input(
        """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair.
"""
    )

    if not validate_option(value):
        return

    if value == "4":
        return top_5_categories()

    result = get_methods(value)
    if result:
        print(result)
        # print()
    print(option[value])
