class Artist:
    def __init__(self, name):
        self.name = name
        self.records = []

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        
    def get_records(self):
        return self.records

    def get_first_record(self):
        return sorted(self.records, key=lambda record: record.year)[0]

    def __repr__(self):
        return f'<Artist name={self.name} >'