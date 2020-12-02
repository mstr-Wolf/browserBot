from clockwork import Clockwork
import webbrowser

class OpenNewTab(Clockwork):
    def __init__(self, URL = None, **kwargs):
        super().__init__(**kwargs)
        self.URL = URL

    def execute(self, **kwargs):
        webbrowser.open(self.URL)
        return