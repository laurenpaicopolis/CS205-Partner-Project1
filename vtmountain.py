import trail

class vtmountain: 

    def __init__(self, name, greenTrails, blueTrails, blackTrails, doubleBlackTrails, gladeTrials, totalTrails, distanceFromUVM, nightSkiing,dayPassPrice):
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
      self.gladeTrials = gladeTrials
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
      return self.gladeTrials

    def getDayPassPrice(self):
      if self.dayPassPrice < 0:
        self.dayPassPrice = 0
        return self.dayPassPrice

    def nightSkiing(self):
      return self.nightSkiing

    def distanceFromUVM(self):
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
