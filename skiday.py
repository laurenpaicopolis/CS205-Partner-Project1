import vtmountain
import skierSnowboarder
import random


class SkiDay:

  def __init__(self):
    self.skierSnowboarderList = []
    self.vtMountains = []
    self.finalizedSkiDay = {}
    self.finalMountainObjects = {}

  def getVTMountains(self):
    return self.vtMountains

  def getSkierSnowboarder(self):
    return self.skierSnowperson

  def addSkierSnowboarder(self, skierToAdd):
    if len(self.skierSnowboarderList) == 0:
      self.skierSnowboarderList.append(skierToAdd)
    else:
      # go through each skier/snowboarder
      nameCount = 2
      for skier in self.skierSnowboarderList:
        # if two people have the same name, add a number to the end of their name
        if skier.getName() == skierToAdd.getName():
          newName1 = skierToAdd.getName()
          newName = str(newName1) + '_' + str(nameCount)
          fixedName = newName.split('_')
          newName = fixedName[0] + '_' + str(nameCount)
          skierToAdd.setName(newName)
          nameCount += 1

      self.skierSnowboarderList.append(skierToAdd)

  def addVermontMountains(self, mountainToAdd):
    self.vtMountains.append(mountainToAdd)

  def pickVermontMountain(self):
    addedNum = 0
    # go through each skier/snowboarder in the list
    for person in self.skierSnowboarderList:
      # get the price wanting to pay, distance willing to go, and skill level of the skier/snowboader
      keyName = person.getName()
      self.finalizedSkiDay[keyName] = {}
      price = person.getPrice()
      distance = person.getHowFar()
      self.userMountainList = []
      self.finalMountainList = []

      # go through each mountain in the list of VT mountains to determine what
      # trails on the mountains the skier/snowboader should go to
      for vtmtn in self.vtMountains:
        # goes into determineTrailsForDay
        # determine the skill level of the skier/snowboarder (what trails they should go on)
        self.userMountainList.append(vtmtn)
      # determine mountains in distance range
      for vtmtn in self.userMountainList:
        if distance < vtmtn.getHowFarFromUVM():
          self.userMountainList.remove(vtmtn)
      for vtmtn in self.userMountainList:
        # determine mountains in price range
        if price < vtmtn.getTotalAmount():
          self.userMountainList.remove(vtmtn)

      mountainObjectList = []
      # organize the dictionary with mountains and trails
      for mountain in self.userMountainList:
        self.finalMountainList.append(mountain.getName())
        mountainObjectList.append(mountain)
      self.finalMountainObjects[keyName] = mountainObjectList
      self.finalizedSkiDay[keyName]['VT Mountains'] = self.finalMountainList

  def determineTrailsForDay(self):
    self.userTrailsGreen = []
    self.userTrailsBlue = []
    self.userTrailsBlack = []
    self.userTrailsDoubleBlack = []
    self.userTrailsGlade = []

    for person in self.skierSnowboarderList:
      skillLevel = person.getSkillLevel()
      nightSkiing = person.getNightSkiing()
      self.userTrailsGreen = []
      self.userTrailsBlue = []
      self.userTrailsBlack = []
      self.userTrailsDoubleBlack = []
      self.userTrailsGlade = []

      mountainTime = self.finalMountainObjects[person.getName()]

      # go through each mountain that the user can go to, to select trails
      for vtmtn in mountainTime:
        # Skill level is beginner
        if skillLevel == "Beginner":
          greenTrails = vtmtn.getAllGreenTrailObjects()

          # green trails
          for trailSelected in greenTrails:
            if nightSkiing and trailSelected.getNightSkiing():
              self.userTrailsGreen.append(trailSelected.getName())
            elif not nightSkiing:
              self.userTrailsGreen.append(trailSelected.getName())

        # Skill level is intermediate
        elif skillLevel == "Intermediate":
          blueTrails = vtmtn.getAllBlueTrailObjects()
          blackTrails = vtmtn.getAllBlackTrailObjects()

          # blue trails
          for trailSelected in blueTrails:
            if nightSkiing and trailSelected.getNightSkiing():
              self.userTrailsBlue.append(trailSelected.getName())
            elif not nightSkiing:
              self.userTrailsBlue.append(trailSelected.getName())

          # black trails
          for trailSelected in blackTrails:
            if nightSkiing and trailSelected.getNightSkiing():
              self.userTrailsBlack.append(trailSelected.getName())
            elif not nightSkiing:
              self.userTrailsBlack.append(trailSelected.getName())

        # Skill Level is advanced
        elif skillLevel == "Advanced":
          gladeTrails = vtmtn.getAllGladeTrailObjects()
          doubleBlackTrails = vtmtn.getAllDoubleBlackTrailObjects()

          for trailSelected in gladeTrails:
            if nightSkiing and trailSelected.getNightSkiing():
              self.userTrailsGlade.append(trailSelected.getName())
            elif not nightSkiing:
              self.userTrailsGlade.append(trailSelected.getName())

          for trailSelected in doubleBlackTrails:
            if nightSkiing and trailSelected.getNightSkiing():
              self.userTrailsDoubleBlack.append(trailSelected.getName())
            elif not nightSkiing:
              self.userTrailsDoubleBlack.append(trailSelected.getName())

      self.finalizedSkiDay[person.getName()]['GreenTrails'] = self.userTrailsGreen
      self.finalizedSkiDay[person.getName()]['BlueTrails'] = self.userTrailsBlue
      self.finalizedSkiDay[person.getName()]['BlackTrails'] = self.userTrailsBlack
      self.finalizedSkiDay[person.getName()]['DoubleBlackTrails'] = self.userTrailsDoubleBlack
      self.finalizedSkiDay[person.getName()]['GladeTrails'] = self.userTrailsGlade

  def getFinalizedSkiDay(self):
    return self.finalizedSkiDay

  def getSkierSnowboarderList(self):
    return self.skierSnowboarderList

  def getVTMountainsList(self):
    return self.vtMountains

  def wrongPickVermontMountain(self):
    addedNum = 0
    # go through each skier/snowboarder in the list
    for person in self.skierSnowboarderList:
      # get the price wanting to pay, distance willing to go, and skill level of the skier/snowboader
      keyName = person.getName()
      self.finalizedSkiDay[keyName] = {}
      price = person.getPrice()
      distance = person.getHowFar()
      self.userMountainList = []
      self.finalMountainList = []

      # go through each mountain in the list of VT mountains to determine what
      # trails on the mountains the skier/snowboader should go to
      for vtmtn in self.vtMountains:
        # goes into determineTrailsForDay
        # determine the skill level of the skier/snowboarder (what trails they should go on)
        self.userMountainList.append(vtmtn)
        # determine mountains in distance range
      for vtmtn in self.userMountainList:
        if distance > vtmtn.getHowFarFromUVM():
          self.userMountainList.remove(vtmtn)
      for vtmtn in self.userMountainList:
        # determine mountains in price range
        if price > vtmtn.getTotalAmount():
          self.userMountainList.remove(vtmtn)

      # organize the dictionary with mountains and trails
      for mountain in self.userMountainList:
        self.finalMountainList.append(mountain.getName())
      self.finalizedSkiDay[keyName]['VT Mountains'] = self.finalMountainList
