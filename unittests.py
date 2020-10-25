import unittest
import vtmountain
import trail
import skierSnowboarder
import skiday


class TestSkiDay(unittest.TestCase):
  VTMountain = 0
  # set up classmethod
  @classmethod
  def setUpClass():
    mtn1 = vtmountain.vtmountain("Bolton",5,4,6,2,1,18,50,True,65)
    mtn2 = vtmountain.vtmountain("Stowe",2,3,2,1,1,9,120,True,105)
    mtn3 = vtmountain.vtmountain("Jay Peak",3,4,1,2,1,11,110,True,90)

    # Green Trails
    mtn1.setGreenTrailObjects("Round Robin","Green",True,"Bolton")
    mtn1.setGreenTrailObjects("Magic Carpet","Green",True,"Bolton")
    mtn1.setGreenTrailObjects("Slide","Green",True,"Bolton")
    mtn1.setGreenTrailObjects("Snowball","Green",True,"Bolton")
    mtn1.setGreenTrailObjects("Upper Villager","Green",True,"Bolton")
    mtn2.setGreenTrailObjects("Cross Over","Green",False,"Stowe")
    mtn2.setGreenTrailObjects("Inspiration","Green",False,"Stowe")

    mtn3.setGreenTrailObjects("Deer Run", "Green", False, "Jay Peak")
    mtn3.setGreenTrailObjects("Queen's Highway", "Green", True, "Jay Peak")
    mtn3.setGreenTrailObjects("Kangaroo Trail", "Green", True, "Jay Peak")
    
    # Blue trails
    mtn1.setBlueTrailObjects("Sure Shot", "Blue", False, "Bolton")
    mtn1.setBlueTrailObjects("Timberline Run", "Blue", True, "Bolton")
    mtn1.setBlueTrailObjects("Showtime", "Blue", True, "Bolton")
    mtn1.setBlueTrailObjects("Moonlight", "Blue", False, "Bolton")

    mtn2.setBlueTrailObjects("Lower Star", "Blue", True, "Stowe")
    mtn2.setBlueTrailObjects("Lower National", "Blue", False, "Stowe")
    mtn2.setBlueTrailObjects("Sunrise", "Blue", True, "Stowe")

    mtn3.setBlueTrailObjects("Northway","Blue",False,
    "Jay Peak")
    mtn3.setBlueTrailObjects("Willard","Blue",True,
    "Jay Peak")
    mtn3.setBlueTrailObjects("Lower Milk Run","Blue",False,"Jay Peak")
    mtn3.setBlueTrailObjects("Timbuktu","Blue",True,"Jay Peak")


    # Black Trails
    mtn1.setBlackTrailObjects("Cougar","Black",False,"Bolton")
    mtn1.setBlackTrailObjects("Bolton Outlaw","Black",False,"Bolton")
    mtn1.setBlackTrailObjects("Upper Crossover","Black",False,"Bolton")
    mtn1.setBlackTrailObjects("SpellBinder","Black",False,"Bolton")
    mtn1.setBlackTrailObjects("Upper Tattle Tale","Black",False,"Bolton")
    mtn1.setBlackTrailObjects("Hard Luck","Black",False,"Bolton")
    mtn2.setBlackTrailObjects("Midway","Black",False,"Stowe")
    mtn2.setBlackTrailObjects("Hayride","Black",False,"Stowe")
    mtn3.setBlackTrailObjects("The Jet", "Black", False,"Jay Peak")


    # Double Black Trails
    mtn1.setDoubleBlackTrailObjects("Five Corners","Double Black", True, "Bolton")
    mtn1.setDoubleBlackTrailObjects("Vermont 200", "Double Black", False, "Bolton")
    mtn2.setDoubleBlackTrailObjects("Spruce Line","Double Black",False,"Stowe")

    mtn3.setDoubleBlackTrailObjects("Cayonland","Double Black", False, "Jay Peak")
    mtn3.setDoubleBlackTrailObjects("Purgatory","Double Black", True, "Jay Peak")

    
    # Glade Trails
    mtn1.setGladeTrailObjects("Vista Glades","Glade",True,"Bolton")
    mtn2.setGladeTrailObjects("Upper Nose Dive","Glade",False,"Stowe")
    mtn3.setGladeTrailObjects("Stateside Glade","Glade",False,"Jay Peak")

    # Skiers/Snowboarders
    skier1 = skierSnowboarder.skierSnowboarder("Michelle",20,"Intermediate", 69, 60, True)    

    skier2 = skierSnowboarder.skierSnowboarder("Lauren", 20, "Advanced", 109, 140, True)

    skier3 = skierSnowboarder.skierSnowboarder("Jason", 25, "Beginner", 110, 59, False)

    skier4 = skierSnowboarder.skierSnowboarder("Zach", 21, "Beginner", 70, 141, False)

    # Add vt mountains to ski day
    skiDay = skiday.skiday()
    skiDay.addVermontMountains(mtn1)
    skiDay.addVermontMountains(mtn2)
    skiDay.addVermontMountains(mtn3)
    
    # add the skiers/snowboarders to the ski day
    skiDay.addSkierSnowboarder(skier1)
    skiDay.addSkierSnowboarder(skier2)
    skiDay.addSkierSnowboarder(skier3)
    skiDay.addSkierSnowboarder(skier4)



if __name__ == "__main__":
  print("YAY")
  unittest.main()
