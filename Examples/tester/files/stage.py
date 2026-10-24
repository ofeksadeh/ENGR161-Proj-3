class stage:
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.blank = True
        self.hline = '=' * width + '\n'
        self.rowstr = '*' + ' ' * (width - 2) +  ('*\n')
        self.titlestr = '*' + ' ' * ((int(width / 2) - int(len(title)/2)) - 1) + title + ' ' * (width - (int(width / 2) - int(len(title)/2)) - 1 - len(title)) + '*\n'
