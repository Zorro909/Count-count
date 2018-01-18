class Box:
    def __init__(self, lpad=1, rpad=1):
        self.fields = list()
        self.lpad = lpad
        self.rpad = rpad
        self.max_len = 0

    def add_field(self, content):
        self.fields.append(content)

        if self.max_len < len(content):
            self.max_len = len(content)
        
        return self

    def add_empty(self):
        self.fields.append('')
        return self

    def show_field(self, f):
        return '│'\
            + (' ' * self.lpad)\
            + f\
            + (' ' * (self.max_len - len(f)))\
            + (' ' * self.rpad)\
            + '│\n'

    def generate_box(self):
        total_len = self.lpad + self.rpad + self.max_len
        box = '┌' + ('─' * total_len) + '┐\n'

        for f in self.fields:
            box += self.show_field(f)

        box += '└' + ('─' * total_len) + '┘'
        return box
