from bs4 import BeautifulSoup
from util import print_time


class Parser:
    def __init__(self, html):
        print_time("Initializing parser")
        self.soup = BeautifulSoup(html, "html.parser")

    # Expects soup to be tbody and children
    def extract_data_from_table(self, template, pop=[], remove_last=False):
        print_time("Extracting data from table")
        data = []
        rows = self.soup.find_all("tr")
        for index in pop:
            print_time(f"Removing row by index {index}")
            rows.pop(index)  # Remove table header

        if(remove_last):
            print_time(f"Removing last element")
            rows.pop()

        current = 1
        elements = len(rows)
        for row in rows:
            print_time(f"Parsing row {current} of {elements}")
            new_dict = {}
            columns = row.find_all("td")
            for key, value in template.items():
                new_dict[value] = columns[key].text
            data.append(new_dict)
            current += 1
        print_time("Parser complete")
        return data


#from selectolax.parser import HTMLParser
# SELECTOLAX, Didn't work...
# TODO: Figure out how to parse with selectolax for max performance
""" class Parser:
    def __init__(self, html):
        self.tree = HTMLParser(html)
        print(self.tree.html)

    def get_list_items(self):
        return self.tree.css(u"li")

    def print_items_text(self):
        items = self.get_list_items()
        for item in items:
            print(item.text())

    def print_text_at_index(self, index):
        items = self.get_list_items()
        item = items[index]
        print(item.text())

    # struct is a dict where the keys are indexes and the value is the key of the created dict
    def extract_data_from_list(self, struct):
        data = []
        items = self.get_list_items()
        for item in items:
            new_dict = {}
            for key, value in struct.items():
                new_dict[value] = item[key].text()
            data.append(new_dict)

    def extract_data_from_table(self, struct):
        data = []
        print("Struct: ", struct)
        items = self.tree.css(u"html")
        print("Items: ", items)
        for item in items:
            print(item)
            new_dict = {}
            for key, value in struct.items():
                print(item[key].text())
                new_dict[value] = item[key].text()
            data.append(new_dict)
        return data """
