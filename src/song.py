class Song:
    def __init__(self, title, runtime, genre):
        self.title = title
        self.runtime = runtime
        self.genre = genre
        self. artist = None
        self.record = None


    def get_title(self):
        return self.title.title()

    def get_runtime(self):
        return self.runtime

    def get_genre(self):
        return self.genre

    def get_artist(self):
        return self.artist

    def get_record(self):
        return self.record

    def __repr__(self):
        return f'<Song title={self.title} runtime={self.runtime} genre={self.genre} >'