import vtmountain
import skierSnowboarder

class SkiDay:
  def __init__(self, vtmountain, skierSnowboarder):
    self.vtmountain = vtmountain
    self.skierSnowboarder = skierSnowboarder

  def getVTMountain(self):
    return self.vtmountain
  
  def getSkierSnowboarder(self):
    return self.skierSnowboarder

  def addSkierSnowboarder(self):
    self.skierSnowboarder = skierSnowboarder