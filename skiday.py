import vtmountain
import skierSnowboarder

class SkiDay:
  global skierSnowboarderList
  global vtMountains

  finalizedSkiDay = {}

  def __init__(self, vtMtn, skierSnowperson):
    self.vtMtn = vtMtn
    self.skierSnowperson = skierSnowperson

  def getVTMountain(self):
    return self.vtMtn
  def getSkierSnowboarder(self):
    return self.skierSnowperson

  def addSkierSnowboarder(self, skierToAdd):
    skierSnowboarderList.append(skierToAdd)

  def addVermontMountains(self, mountainToAdd):
    vtMountains.append(mountainToAdd)

  def pickVermontMountain(self):
    # price
    for person in skierSnowboarderList:
      price = person.getPrice()
      distance = person.getHowFar()
      skillLevel = person.getSkillLevel()
      for vtmtn in vtMountains:
        # goes into determineTrailsForDay
        if skillLevel == "Beginner":
          greenTrails = vtmtn.getAllGreenTrails()
        if skillLevel == "Intermediate":
          blueTrails = vtmtn.getAllBlueTrails()
          blackTrails = vtmtn.getAllBlackTrails()
        if skillLevel == "Advanced":
          gladeTrails = vtmtn.getAllGladeTrails()
          doubleBlackTrails = vtmtn.getAllBlackTrails()



        
    # distance

    # skill level
    
    