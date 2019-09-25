class Point:
    
    i = 12345

    def __init__(self):
        #print('initialiser',self)
        self.x=0
        self.y=0
        
        def __str__(self):
             return f'({self.x},{self.y})'
p = Point()
#print(p.x,p.y)
print(p,str(p))


         
