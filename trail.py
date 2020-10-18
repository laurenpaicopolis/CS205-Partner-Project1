class Trail:
    def __init__(self, name, levelTrail, nightSkiing, nameOfMountain):
      self.name = name
      self.levelTrail = levelTrail
      self.nightSkiing = nightSkiing
      self.nameOfMountain = nameOfMountain

    def getName(self):
      return self.name

    def getLevelTrail(self):
      return self.levelTrail

    def getNightSkiing(self):
      return self.nightSkiing
    
    def getNameOfMountain(self):
      return self.nameOfMountain