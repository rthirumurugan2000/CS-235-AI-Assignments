""" Travelling salesman Problem Using A*- 1801185 Thirumurugan Ramar """
import random
import time

class TSP(object):

    # For finding distance between 2 points
    def getdistance(self,P1,P2): 
        self.P1 = P1
        self.P2 = P2
        distance = ((self.P1[0]-self.P2[0])**2 + (self.P1[1]-self.P2[1])**2)**(1/2)
        return distance

    # For generating random co-ordinates for the point between 0 and 25
    def randc(self):
        x = random.randint(0,25)
        y = random.randint(0,25)
        return [x,y]

    # For calculating total distance in current path
    def calculatedist(self,s,n): 
        self.calD = s
        self.nu = n
        dist = 0
        total = 0
        for i in range(self.nu):
            point1 = self.calD[i]
            point2 = self.calD[i+1]
            dist = self.getdistance(self.coord[point1],self.coord[point2])
            total+=dist    
        return total

    # Calculates h'(n)+g(n) cost (total: f(n)) Minimum spanning tree 
    def heuristic(self,chosenlist,citylist):
        check = citylist[:]  # shallow copies the list
        spl = chosenlist[:]
        dl = 999999999     # some max value
        fCost =[]
        l=[]
            
        for i in chosenlist:
            check.remove(i)
            
        for e in check:
            l.clear()
            l.append(e)
            rest = citylist[:]
            totaldist = 0
            
            while len(rest) > 0:
                dl=99999
                for i in l:
                    if i in rest:
                        rest.remove(i)
                
                for n in l:
                    for m in rest:
                        d = self.getdistance(self.coord[n],self.coord[m])
                        if d<dl:
                            dl = d
                            c = m
                
                if c not in l:
                    l.append(c)
                    
                totaldist += d
            
            g = self.getdistance(self.coord[e],self.coord[spl[-1]])
            k = self.getdistance(self.coord['0'],self.coord[e])
            f = g+totaldist+k
 
            fCost.append((f,e))
            
        fCost.sort()

        return (fCost[0][1])
    def solver(self):
        
        number = input("Input the number of citites to be generated: ")
        self.coord ={}
        citylist = []
        chosenlist = ['0']
        self.number = int(number)
        for i in range(self.number):
            a = str(i)
            l = self.randc()
            self.coord[a] = l
            citylist.append(a)
        
        currentState = citylist[:]
                
        for i in range(len(citylist)-1):        
            x = self.heuristic(chosenlist,citylist)
            chosenlist.append(x)
        
    
        final = chosenlist+['0']
        il = citylist +['0']
        
        fd = self.calculatedist(final,len(final)-1)
        id = self.calculatedist(il,len(il)-1)
        
        print("Coordinates" , self.coord)
        print("Initial state: ",il,"\n")
        print("Initial distance: %.2f km \n" %id)
        print("Final state : ",final,"\n" )
        print("Optimized distance: %.2f km \n" %fd)

def main():
    start = time.time()
    tsp = TSP() 
    tsp.solver()
    end = time.time()
    print("Time measure: %.2f sec" % (end-start))

if __name__ == "__main__":
    main()          
            
  
    
