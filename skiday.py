import vtmountain
import skierSnowboarder
from numpy.random import seed
from numpy.random import randint
seed(1)

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
    for skier in skierSnowboarderList:
      if skier.getName() == skierToAdd.getName():
        # TODO: Make sure the same random number is not generated twice
        value = randint(0, 100, 1)
        skierToAdd.setName(skierToAdd.getName() + str(value))
        skierSnowboarderList.append(skierToAdd)

  def addVermontMountains(self, mountainToAdd):
    vtMountains.append(mountainToAdd)

  def pickVermontMountain(self):
    global finalizedSkiDay
    addedNum = 0
    # go through each skier/snowboarder in the list
    for person in skierSnowboarderList:
      # get the price wanting to pay, distance willing to go, and skill level of the skier/snowboader
      keyName = person.getName()
      finalizedSkiDay[keyName]
      price = person.getPrice()
      distance = person.getHowFar()
      userMountainList = []
      
      # go through each mountain in the list of VT mountains to determine what 
      # trails on the mountains the skier/snowboader should go to
      for vtmtn in vtMountains:
        # goes into determineTrailsForDay
        # determine the skill level of the skier/snowboarder (what trails they should go on)
        userMountainList.append(vtmtn)
        # determine mountains in distance range
        if distance <= 60 and not vtmtn.distanceFromUVM() <= 60:
          userMountainList.remove(vtmtn)
        elif distance <= 140 and not vtmtn.distanceFromUVM() <= 140:
          userMountainList.remove(vtmtn)
    
        # determine mountains in price range
        if price < 70 and not vtmtn.dayPassPrice() < 70:
          userMountainList.remove(vtmtn)
        elif price < 110 and not vtmtn.dayPassPrice() < 110:
          userMountainList.remove(vtmtn)

      # organize the dictionary with mountains and trails    
      finalizedSkiDay[keyName]['VTMountain'] = userMountainList


  def determineTrailsForDay(self):
    userMountainList = []
    userTrailsGreen = []
    userTrailsBlue = []
    userTrailsBlack = []
    userTrailsDoubleBlack = []
    userTrailsGlade = []
    
    for person in skierSnowboarderList:
      finalizedSkiDay[person.getName()]['VTMountain'] = userMountainList
      skillLevel = person.getSkillLevel()
      nightSkiing = person.getNightSkiing()
      for vtmtn in userMountainList:
        # Skill level is beginner
        if skillLevel == "Beginner":
          greenTrails = vtmtn.getAllGreenTrails()
          # green trails
          for trailSelected in greenTrails:
            if nightSkiing and trailSelected.getNightSkiing():
              userTrailsGreen.append(trailSelected)
            elif not nightSkiing:
              userTrailsGreen.append(trailSelected)   
                
        # Skill level is intermediate
        elif skillLevel == "Intermediate":
          blueTrails = vtmtn.getAllBlueTrails()
          blackTrails = vtmtn.getAllBlackTrails()
            
          # blue trails
          for trailSelected in blueTrails:
            if nightSkiing and trailSelected.getNightSkiing():
              userTrailsBlue.append(trailSelected)
            elif not nightSkiing:
              userTrailsBlue.append(trailSelected)
                
          # black trails
          for trailSelected in blackTrails:
            userTrailsBlack.append(trailSelected)
            if nightSkiing and trailSelected.getNightSkiing():
              userTrailsBlack.append(trailSelected)
            elif not nightSkiing:
              userTrailsBlack.append(trailSelected)  
          
          # Skill Level is advanced
        elif skillLevel == "Advanced":
          gladeTrails = vtmtn.getAllGladeTrails()
          doubleBlackTrails = vtmtn.getAllDoubleBlackTrails()
            
          for trailSelected in gladeTrails:
            if nightSkiing and trailSelected.getNightSkiing():
              userTrailsGlade.append(trailSelected)
            elif not nightSkiing:
              userTrailsGlade.append(trailSelected) 
            
          for trailSelected in doubleBlackTrails:
            if nightSkiing and trailSelected.getNightSkiing():
              userTrailsDoubleBlack.append(trailSelected)
            elif not nightSkiing:
              userTrailsDoubleBlack.append(trailSelected)
            
      finalizedSkiDay[person]['GreenTrails'] = userTrailsGreen
      finalizedSkiDay[person]['BlueTrails'] = userTrailsBlue
      finalizedSkiDay[person]['BlackTrails'] = userTrailsBlack
      finalizedSkiDay[person]['DoubleBlackTrails'] = userTrailsDoubleBlack
      finalizedSkiDay[person]['GladeTrails'] = userTrailsGlade

# TODO: create getters for trails and dictionary