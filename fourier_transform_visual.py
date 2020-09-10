class Vec():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = sqrt(x**2 + y**2)
        self.update_angle()
        
    def __add__(self, v):
        return Vec(self.x + v.x, self.y + v.y)
    
    def update_angle(self):
        self.angle = atan2(self.y, self.x)

    def rotate(self, rad):
        self.x = self.magnitude * cos(-rad + self.angle) # "-" for counter clockwise rotation like in math
        self.y = self.magnitude * sin(-rad + self.angle)
        self.update_angle()
        

n = 100
res = 100 # resolution
scale_ = 100
f0 = 0.01
f1 = 0.05 
#func = [sin(TWO_PI * f0 * x) for x in range(0, int(f0 * 1000000) + 300)]
func = [sin(TWO_PI * f0 * x/res) + 0*cos(TWO_PI * 0.01 * x/res) + 0.5 for x in range(0, n * res)]


f = 0.00

l = Vec(1, 0)
ffs = []
checked_frequencies = []
maxff = 0
def setup():
    size(600, 600)

def draw():
    global f
    global maxff
    background(165)
    l = Vec(1, 0)
        
    #l.rotate(f * 1/frameRate)
    #line(width/2, height/2, l.x * scale_ + width/2, l.y * scale_ + height/2)
    strokeWeight(3)
    p = []
    for x in range(0, len(func)):
        p.append([l.x * func[x] * scale_ + width/2, l.y * func[x] * scale_ + height/2])
        l.rotate(TWO_PI * f/res)
        #print(l.angle)
        
    x_tot = p[0][0]
    y_tot = p[0][1]
    for i in range(1,len(p)):
        stroke(0, 0, 0, i*255/(len(p)-1))
        line(p[i][0], p[i][1], p[i-1][0], p[i-1][1])
        x_tot += p[i][0]
        y_tot += p[i][1]
    x_tot /= len(p)
    y_tot /= len(p)
    
    checked_frequencies.append(f)
    ffs.append(sqrt(x_tot**2 + y_tot**2))
    
    strokeWeight(10)
    
    #print(p[-1][0], p[-1][1])
    
    strokeWeight(3)
    stroke(0, 0, 200)
    line(width/2, height/2, p[-1][0], p[-1][1])
    stroke(0, 160, 0)
    strokeWeight(10)
    point(width/2, height/2)
    stroke(160, 0, 0)
    point(x_tot, y_tot)
    stroke(0)
    #print(f)
    strokeWeight(3)
    #line(0, 530, 600, 530)
    strokeWeight(5)
    
    #maxff = 0
    #if f > 0.01:
    maxff = min(ffs)#[10:])

    
    for i in range(len(ffs)):
        if ffs[i] == maxff:
            stroke(0, 200, 0)
            strokeWeight(12)
            textSize(32)
            text(str(checked_frequencies[i]), 50, 80)
        else:
            strokeWeight(3)
            stroke(0)
        point(float(i)/len(ffs)*width, ffs[i]+80)
    print(maxff)

        
    textSize(32)
    text(str(f), 50, 50)
    
    f += 0.005 * 1/frameRate
