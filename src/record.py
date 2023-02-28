class Record:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year
        self.songs = []

    def get_title(self):
        return self.title.title()

    def get_year(self):
        return self.year

    def get_artist(self):
        return self.artist

    def get_songs(self):
        return self.songs

    def total_runtime(self):
        return sum([song.runtime for song in self.songs])

    def has_song(self, song):
        if song in self.songs:
            return True

    def get_longest_song(self):
        return sorted(self.songs, key=lambda song: song.runtime, reverse=True)[0]


    def __repr__(self):
        return f'<Record title={self.title} artist={self.artist} year={self.year} >'