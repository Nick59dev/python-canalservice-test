import requests
import datetime

from xml.etree import ElementTree as ET


# prefix
PREFIX     = "https://cbr.ru/scripts/XML_daily.asp?date_req="
# USA dollar ID
CURRENT_ID = "R01235"

class Current():
    """Class for fetching and updating current
    information about dollar current
    """
    def __init__(self):
        self.date     = datetime.date.today()
        # making a string from current date
        self.date_str = self.strmake(self.date)
        self.current  = 0
        # print(self.date_str)

    # method for making a string to the like of "DD/MM/YYYY"
    # from any date from datetime package
    def strmake(self, date_):
        return str(date_)[8:] + "/" + str(date_)[5:7] + "/" + str(date_)[:4]

    # Fetching dollar current if we are outdated
    # else doing nothing but returning previous
    # dollar current value
    def update(self):
        if self.date < datetime.date.today() or not self.current:
            # updating our class' info
            self.date = datetime.date.today()
            self.date_str = self.strmake(self.date)
            # making a request for XML currents to
            # Central Bank
            request = requests.get(PREFIX + self.date_str)
            # starting to process the XML data
            root = ET.fromstring(request.text)
            # finding USA dollar current in the fetched XML
            for desc in root:
                if desc.attrib["ID"] == CURRENT_ID:
                    for desc2 in desc:
                        if desc2.tag == "Value":
                            self.current = float(desc2.text.replace(",",'.'))
                            print(self.current)
        else: pass

    def get_current(self):
        self.update()
        return round(self.current, 2)


# cur = Current()
# print(cur.cur())
# print(cur.get_current())
