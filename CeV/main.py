from pen import Pen

c1 = Pen()
print('===Pen 1===')
c1.color = 'Blue'
c1.tip = 0.5
c1.close()
c1.brand = 'bic'
c1.load = 90
c1.status()
c1.write()
print()

c2 = Pen()
print('===Pen 2===')
c2.tip = 0.3
c2.brand = 'Unknown'
c2.color = 'Green'
c2.load = 98
c2.open()
c2.status()
c2.write()
