""" Python Package Support """
import random

""" Internal Package Support """
#Not Applicable

"""
    @author:     Matthew J Swann
    @version:    1.0, Last Update: 2012-11-08
    
    Program:     Particle Swarm Optimization for Continuous Function
    Integration: Tier 1A/B
    
    Six Camel Hump Function for optimization evaluation.   
 """

"""
-----------------------------
CLASS :: Hive
-----------------------------
 
 Serves as the group of particles.
 """
class Hive(object):
        
    """ 
     Constructor taking a parameter for the size of the
     population.
     
     @param popSize: Size of the hive cluster.
     """
    def __init__(self, popSize):
        self.populationSize = popSize
        self.population = list()
        """ Initialization """
        self.setup()
    
    
    """
     Initializes the hive cluster with particles containing
     random starting values. Best values are set within the
     appropriate values for the hive cluster itself.
     """
    def setup(self):
        for i in range (self.populationSize):
            particle = Particle()
            particle.setID(i)
            self.population.append(particle)
    
    
    """
     This was just to show my girlfriend some cool for-loop 
     stuff. So.... yeah.
     """
    def cleanList(self):
        for i in range (len(self.population)):
            self.population.pop(0)
    
    
    """
     Sorts the population based off fitness.
     """
    def sortListFitness(self):
        for i in range (len(self.population)):
            for j in range (len(self.population)):
                if (self.population[i].getCurrentCost()) < (self.population[j].getCurrentCost()):
                    swap = self.population.pop(i)
                    self.population.insert(j, swap)
                    
    
    """
     Adds a particle to the hive cluster.
     
     @param particle: Particle to be added to the hive
     cluster.
     """    
    def add(self, particle):
        self.population.append(particle)
    
    
    """
     Returns the population list.
     
     @return: Returns the population list.
     """    
    def getPopulation(self):
        return self.population
    
    """
     Calls particleAdmin() for each particle.
     """
    def hiveAdmin(self):
        for i in range (len(self.population)):
            self.population[i].particleAdmin()

"""
---------------------------------------
CLASS :: Particle
---------------------------------------

 Serves as a Hive entity.
 """
class Particle(object):

    """
     Constructor setting sentinel values. Also, calls
     for setup() generating random starting values and
     self evaluation. 
     """
    def __init__(self):
        self.bestCost = 10000
        self.particleID = None
        self.velocity = None
        self.xVelocity = 0
        self.yVelocity = 0
        """ Initialization """
        self.setup()
        
        
    """
     Initialization for the particle object. Sets random
     values within specified range, solves and sets the
     initial solved values for as the currently best values.
     """
    def setup(self):
        xParam = random.uniform(-2, 3)
        yParam = random.uniform(-2, 3)
        signature = random.randint(0, 1)
        if(signature == 1):
            xParam = 0 - xParam
        signature = random.randint(0, 1)
        if(signature == 1):
            yParam = 0 - yParam
        self.setVars(xParam, yParam)
        self.solve()
        

    """
    XXXXXXXXXXXXXXXXXXXXXXX
     """
    def processValues(self, xParam, yParam):
        self.checkSetX(xParam)
        self.checkSetY(yParam)
        self.solve()

    """
     Solves for current values of X and Y.
     
     @return: Returns function evaluation.
     """        
    def solve(self):
        x = self.x
        y = self.y
        solution = ( (4-(2.1*x*x) +((x*x*x*x)/3))*x*x + y*x +  
                  (-4+(4*y*y))*y*y )
        self.currentCost = solution
        if(solution < self.bestCost):
            self.bestCost = solution
            self.bestX = x
            self.bestY = y
        return solution
    
    
    """
     Sets x velocity value.    

     @param vel: X Velocity
     """
    def setXVelocity(self, vel):
        self.xVelocity = vel


    """
     Sets y velocity value.    

     @param vel: Y Velocity
     """
    def setYVelocity(self, vel):
        self.yVelocity = vel
    
    
    """
     Returns x velocity.
     
     @return: Returns the x velocity
     """
    def getXVelocity(self):
        return self.xVelocity
    
    
    """
     Returns y velocity.
     
     @return: Returns the y velocity
     """
    def getYVelocity(self):
        return self.yVelocity
    
    
    """
     Ensures the X value is between -2 & 3 per project
     specifications.
     
     @param newInput: New Input for X variable with wrap
     around boarder assurance.
     """
    def checkSetX(self, newInput):
        if newInput > 3:
            self.x = newInput-5
        elif newInput < -2:
            self.x = newInput+5
        else:
            self.x = newInput
    
    
    """
     Ensures the Y value is between -2 & 3 per project
     specifications.
     
     @param newInput: New Input for Y variable with wrap
     around boarder assurance.
     """
    def checkSetY(self, newInput):
        if newInput > 3:
            self.y = newInput-5
        elif newInput < -2:
            self.y = newInput+5
        else:
            self.y = newInput   
    
    
    """
     Sets the variables for the function without boarder
     assurance.
     
     @param newX: New X value.
     @param newY: New Y value.
     """
    def setVars(self, newX, newY):
        self.x = newX
        self.y = newY
    
        
    """
     Sets particle ID number
    
     @param value: Particle ID number
     """
    def setID(self, value):
        self.particleID = value
    
        
    """
     Returns particle ID number.
     
     @return: Returns particle ID number.
     """
    def getID(self):
        return self.particleID
    
    
    """
     Returns current X value.
     
     @return: Returns X value.
     """    
    def getX(self):
        return self.x


    """
     Returns current Y value.
     
     @return: Returns Y value.
     """        
    def getY(self):
        return self.y
 
    """
     Prints an admin output.
     """
    def particleAdmin(self):
        print("*** Particle Printout Start -->")
        print("Part ID: %s" % self.getID())
        print("BestSol: %s" % self.getBestCost())
        print("BestX:   %s" % self.getBestX())
        print("BestY:   %s" % self.getBestY())
        print("Vel X:   %s" % self.getXVelocity())
        print("Vel Y:   %s" % self.getYVelocity())
        print("CrntSol: %s" % self.getCurrentCost())
        print("CrntX:   %s" % self.getX())
        print("CrntY:   %s" % self.getY())
    
    """
     Returns bestCost, X and Y.
     
     @return: Best cost.
     @return: Best X
     @return: Best Y
     """
    def getBestCost(self):
        return self.bestCost
    
    def getCurrentCost(self):
        return self.currentCost
    
    def getBestX(self):
        return self.bestX
    
    def getBestY(self):
        return self.bestY