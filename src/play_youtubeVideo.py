import clockwork
import webbrowser

class play_youtubeVideo(clockwork.clockwork):
    def __init__(self, URL = None, **kwargs):
        super().__init__(**kwargs)
        self.URL = URL

    def execute(self):
        webbrowser.open(self.URL)
        return