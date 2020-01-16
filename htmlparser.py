from bs4 import BeautifulSoup
from util import print_time

class Parser:
    def __init__(self, html, log_each_n = 10):
        print_time("Initializing parser")
        self.soup = BeautifulSoup(html, "html.parser")
        self.log_each_n = log_each_n

    # Expects soup to be tbody and children
    def extract_data_from_table(self, template, pop=[], remove_last=False):
        if(not template):
            raise Exception("No template added to parser")

        print_time("Extracting data from table")
        data = []
        rows = self.soup.find_all("tr")

        if(len(pop) > 0):
            sorted_pop = pop.sort(reverse=True)
            for index in sorted_pop:
                print_time(f"Removing row by index {index}")
                rows.pop(index)  # Remove table header

        if(remove_last):
            print_time(f"Removing last element")
            rows.pop()

        current = 1
        log_counter = 0
        elements = len(rows)

        #Iterate over every row in the table
        for row in rows:
            log_counter += 1
            if(log_counter == self.log_each_n or current == elements):
                print_time(f"Parsing row {current} of {elements}")
                log_counter = 0

            new_dict = {}
            columns = row.find_all("td")

            if(type(template) == "dict"):
                for key, value in template.items():
                    new_dict[value] = columns[key].text
            else:
                for index, value in enumerate(template):
                    new_dict[value] = columns[index].text
            
            data.append(new_dict)
            current += 1
        
        print_time("Parser complete")
        return data