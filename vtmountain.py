import trail

class vtmountain: 
    global greenTrailObjects
    global blueTrailObjects
    global blackTrailObjects
    global doubleBlackTrailObjects
    global gladeTrailObjects
    
    def __init__(self, name, greenTrails, blueTrails, blackTrails, doubleBlackTrails, totalTrails, distanceFromUVM, nightSkiing, gladeTrials):
      self.name = name
      self.greenTrails = greenTrails
      self.blackTrails = blackTrails
      self.blueTrails = blueTrails
      self.doubleBlackTrails = doubleBlackTrails
      self.totalTrails = totalTrails
      self.distanceFromUVM = distanceFromUVM
      self.nightSkiing = nightSkiing
      self.gladeTrials = gladeTrials

    def getName(self):
      return self.name

    def getAllGreenTrails(self):
      return self.greenTrails
    
    def getAllBlueTrails(self):
      return self.blueTrails
    
    def getAllBlackTrails(self):
      return self.blackTrails

    def getAllDoubleBlackTrails(self):
      return self.doubleBlackTrails

    def getAllGladeTrails(self):
      return self.gladeTrials
    
    def nightSkiing(self):
      return self.nightSkiing
    
    def distanceFromUVM(self):
      self.distanceFromUVM
    
    def setGreenTrailObjects(self, name, levelTrail, nightSkiing):
      newTrail = trail(name, levelTrail, nightSkiing)
      greenTrailObjects.append(newTrail)
    
    def setBlueTrailObjects(self, name, levelTrail, nightSkiing):
      newTrail = trail(name, levelTrail, nightSkiing)
      blueTrailObjects.append(newTrail)

    def setBlackTrailObjects(self, name, levelTrail, nightSkiing):
      newTrail = trail(name, levelTrail, nightSkiing)
      blackTrailObjects.append(newTrail)
    
    def setDoubleBlackTrailObjects(self, name, levelTrail,nightSkiing):
      newTrail = trail(name, levelTrail, nightSkiing)
      doubleBlackTrailObjects.append(newTrail)  

    def setGladeTrailObjects(self, name, levelTrail, nightSkiing):
      newTrail = trail(name, levelTrail, nightSkiing)
      gladeTrailObjects.append(newTrail)  
    
