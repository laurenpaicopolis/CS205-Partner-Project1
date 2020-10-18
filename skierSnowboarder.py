class SkierSnowboarder:
    def __init__(self, name, age, skillLevel, length, price, howFar, nightSkiing):
      self.name = name
      self.age = age
      self.skillLevel = skillLevel
      self.length = length
      self.price = price
      self.howFar = howFar
      self.nightSkiing = nightSkiing
    
    def getName(self):
      return self.name
    
    def getAge(self):
      return self.age
    
    def getSkillLevel(self):
      return self.skillLevel
    
    def getLength(self):
      return self.length
    
    def getPrice(self):
      return self.price
    
    def getHowFar(self):
      return self.howFar

    def getNightSkiing(self):
      # verify that night skiing is a boolean
      return self.nightSkiing

    def setName(self):
      name = self.name
    
    

