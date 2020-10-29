from requests_html import HTMLSession
from bs4 import BeautifulSoup
from gui import Gui


# Get the titles of the reddit page
class ParseUrl:
    def __init__(self, url):

        # Get the page content
        self.titles = dict()
        self.session = HTMLSession()
        self.page = self.session.get(url)
        self.parse_to_bs = BeautifulSoup(self.page.content, "html.parser")
        self.links = self.parse_to_bs.find_all("a")

        # Parse the values into a
        for link in self.links:
            content = link.findChildren("h3", text=True)
            if len(content) > 0:
                self.titles.update({content[0].getText(): "http://reddit.com/" + link.get("href")})


# Execute the parse url function
if __name__ == '__main__':
    get_titles = ParseUrl("http://reddit.com/r/news/")
    gui = Gui(get_titles.titles)
    gui.create_gui()
