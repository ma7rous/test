class Point:
    def __init__(self,x=0,y=0):
        #print('initialiser',self)
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'({self.x},{self.y})'
    
    def Add(self,r):
        return Point(self.x+r.x,self.y+r.y)    
    
p = Point(10,20)
q = Point(30,40)
def AddPoint(l,r):
    return Point(l.x+r.x, l.y+r.y)

#s = AddPoint(p,q)
#s = p.Add(q)
#m = p*a 
#print(m)    
#print(p.x,p.y)
#print(p,str(p))


         
