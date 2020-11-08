import trail

class vtmountain:

    def __init__(self, name, greenTrails, blueTrails, blackTrails, doubleBlackTrails, gladeTrails, totalTrails, distanceFromUVM, nightSkiing, dayPassPrice):
        # initialize variables
        self.greenTrailObjects = []
        self.blueTrailObjects = []
        self.blackTrailObjects = []
        self.doubleBlackTrailObjects = []
        self.gladeTrailObjects = []
        self.name = name
        self.greenTrails = greenTrails
        self.blackTrails = blackTrails
        self.blueTrails = blueTrails
        self.doubleBlackTrails = doubleBlackTrails
        self.totalTrails = totalTrails
        self.distanceFromUVM = distanceFromUVM
        self.nightSkiing = nightSkiing
        self.gladeTrails = gladeTrails
        self.dayPassPrice = dayPassPrice

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
        return self.gladeTrails

    def getAllGreenTrailObjects(self):
        return self.greenTrailObjects

    def getAllBlueTrailObjects(self):
        return self.blueTrailObjects

    def getAllBlackTrailObjects(self):
        return self.blackTrailObjects

    def getAllDoubleBlackTrailObjects(self):
        return self.doubleBlackTrailObjects

    def getAllGladeTrailObjects(self):
        return self.gladeTrailObjects

    def getTotalAmount(self):
        if self.dayPassPrice < 0:
            self.dayPassPrice = 0
        return self.dayPassPrice

    def nightSkiing(self):
        return self.nightSkiing

    def getHowFarFromUVM(self):
      if self.distanceFromUVM < 0:
        self.distanceFromUVM = 0
      return self.distanceFromUVM

    def setGreenTrailObjects(self, name, levelTrail, nightSkiing, nameOfMountain):
      newTrail = trail.Trail(name, levelTrail, nightSkiing, nameOfMountain)
      self.greenTrailObjects.append(newTrail)

    def setBlueTrailObjects(self, name, levelTrail, nightSkiing, nameOfMountain):
      newTrail = trail.Trail(name, levelTrail, nightSkiing, nameOfMountain)
      self.blueTrailObjects.append(newTrail)

    def setBlackTrailObjects(self, name, levelTrail, nightSkiing, nameOfMountain):
      newTrail = trail.Trail(name, levelTrail, nightSkiing, nameOfMountain)
      self.blackTrailObjects.append(newTrail)

    def setDoubleBlackTrailObjects(self, name, levelTrail,nightSkiing, nameOfMountain):
      newTrail = trail.Trail(name, levelTrail, nightSkiing, nameOfMountain)
      self.doubleBlackTrailObjects.append(newTrail)

    def setGladeTrailObjects(self, name, levelTrail, nightSkiing, nameOfMountain):
      newTrail = trail.Trail(name, levelTrail, nightSkiing, nameOfMountain)
      self.gladeTrailObjects.append(newTrail)
