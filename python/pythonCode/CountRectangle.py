from itertools import combinations

def checkFormat(li):
    if len(li)==0:
        print ("Input is not formatted.")
        return False
    for x in li:
        if not isinstance(x,tuple):#points I use tuple
            print ("Input is not formatted.")
            return False#equals break
        else:
            if not len(x)==2 or not isinstance(x[0],int) or not isinstance(x[1],int):
                print ("Input is not formatted.")
                return False#equals break
    else:
        return True

def distance(p1,p2):
    return (p2[0]-p1[0])**2+(p2[1]-p1[1])**2#actually return is distance**2

def isRectangle(p1,p2,p3,p4):
    centerPoint_x = (p1[0]+p2[0]+p3[0]+p4[0])/4#cal centerPoint codinal x use two point of one diagonal,if we know p1 adn p2 is the points of one diagonal of rectangle,than 
    centerPoint_y = (p1[1]+p2[1]+p3[1]+p4[1])/4# if p2_x bigger than p1_x: center_x = p1_x+((p2_x-p1_x)/2),if p1_x bigger than p2_x : center_x = p2_x +((p1_x-p2_x)/2)
    centerPoint = (centerPoint_x,centerPoint_y)# so no matter p1,p2 who's x is bigger,center_x = (p1_x+p2_x)/2,end we do not need check which two is diagonal,just use both four points
    d1 = distance(p1,centerPoint)
    d2 = distance(p2,centerPoint)
    d3 = distance(p3,centerPoint)
    d4 = distance(p4,centerPoint)
    return d1 == d2 and d1 == d3 and d1 == d4 and d1 != 0#distance from center to 4 point is equal and != o,it is rectangle

def rect(pList):
    rectList =[]
    if not checkFormat(pList):
        rectList =[]
        return rectList
    else:
        for x in combinations(pList,4):#use combinations to get 4 elements combination
            if isRectangle(x[0],x[1],x[2],x[3])==True:
                print(x)
                rectList.append(x)
        return rectList  

a= [[1,3],'a']
a1 = [(1,3),(1,2),(2,2),(2,4),(4,3),(4,2),(6,3),(6,2),(3,1),(5,7),(7,5)] #point I use tuple 
a2 =[(1,3),(1,2),(2,2),(2,4),(4,3),(4,2),(6,3),(6,2)] #It is better to use set here,because if has duplicated points in list,it is nonsense,and i do not checkFormat if it is dupe points
print(checkFormat(a))
print(len(rect(a2)))
print("--------------------")
print(len(rect(a1)))