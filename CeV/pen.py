class Pen:
    # attributes
    def __init__(self, brand='', color='', tip=float, load=int, closed=bool):
        self.brand = str
        self.color = str
        self.tip = float
        self.load = int
        self.closed = bool

    # methods
    def status(self):
        if not self.closed:
            c = 'open'
        else:
            c = 'closed'
        print(f'The {self.color} {self.brand} pen has a {self.tip} tip size, is {self.load}% loaded and it is {c}')

    def write(self):
        if self.closed:
            print('Can\'t write')
        else:
            print('Writing...')

    def close(self):
        self.closed = True

    def open(self):
        self.closed = False
