import unittest
import vtmountain
import trail
import skierSnowboarder
import skiday


class TestSkiDay(unittest.TestCase):
  VTMountain = 0

  # set up classmethod
  @classmethod
  def setUpClass(cls):
    print('setUpClass()')
    # distance, price
    cls.mtn1 = vtmountain.vtmountain("Bolton", 5, 4, 6, 2, 1, 18, 50, True, 65)
    cls.mtn2 = vtmountain.vtmountain("Stowe", 2, 3, 2, 1, 1, 9, 120, True, 105)
    cls.mtn3 = vtmountain.vtmountain("Jay Peak", 3, 4, 1, 2, 1, 11, 110, True, 90)

    # Green Trails
    cls.mtn1.setGreenTrailObjects("Round Robin", "Green", True, "Bolton")
    cls.mtn1.setGreenTrailObjects("Magic Carpet", "Green", True, "Bolton")
    cls.mtn1.setGreenTrailObjects("Slide", "Green", True, "Bolton")
    cls.mtn1.setGreenTrailObjects("Snowball", "Green", True, "Bolton")
    cls.mtn1.setGreenTrailObjects("Upper Villager", "Green", True, "Bolton")

    cls.mtn2.setGreenTrailObjects("Cross Over", "Green", False, "Stowe")
    cls.mtn2.setGreenTrailObjects("Inspiration", "Green", False, "Stowe")

    cls.mtn3.setGreenTrailObjects("Deer Run", "Green", False, "Jay Peak")
    cls.mtn3.setGreenTrailObjects("Queen's Highway", "Green", True, "Jay Peak")
    cls.mtn3.setGreenTrailObjects("Kangaroo Trail", "Green", True, "Jay Peak")

    # Blue trails
    cls.mtn1.setBlueTrailObjects("Sure Shot", "Blue", False, "Bolton")
    cls.mtn1.setBlueTrailObjects("Timberline Run", "Blue", True, "Bolton")
    cls.mtn1.setBlueTrailObjects("Showtime", "Blue", True, "Bolton")
    cls.mtn1.setBlueTrailObjects("Moonlight", "Blue", False, "Bolton")

    cls.mtn2.setBlueTrailObjects("Lower Star", "Blue", True, "Stowe")
    cls.mtn2.setBlueTrailObjects("Lower National", "Blue", False, "Stowe")
    cls.mtn2.setBlueTrailObjects("Sunrise", "Blue", True, "Stowe")

    cls.mtn3.setBlueTrailObjects("Northway", "Blue", False, "Jay Peak")
    cls.mtn3.setBlueTrailObjects("Willard", "Blue", True, "Jay Peak")
    cls.mtn3.setBlueTrailObjects("Lower Milk Run", "Blue", False, "Jay Peak")
    cls.mtn3.setBlueTrailObjects("Timbuktu", "Blue", True, "Jay Peak")


    # Black Trails
    cls.mtn1.setBlackTrailObjects("Cougar", "Black", True, "Bolton")
    cls.mtn1.setBlackTrailObjects("Bolton Outlaw", "Black", False, "Bolton")
    cls.mtn1.setBlackTrailObjects("Upper Crossover", "Black", False, "Bolton")
    cls.mtn1.setBlackTrailObjects("SpellBinder", "Black", False, "Bolton")
    cls.mtn1.setBlackTrailObjects("Upper Tattle Tale", "Black", True, "Bolton")
    cls.mtn1.setBlackTrailObjects("Hard Luck", "Black", False, "Bolton")

    cls.mtn2.setBlackTrailObjects("Midway", "Black", False, "Stowe")
    cls.mtn2.setBlackTrailObjects("Hayride", "Black", False, "Stowe")

    cls.mtn3.setBlackTrailObjects("The Jet", "Black", False, "Jay Peak")


    # Double Black Trails
    cls.mtn1.setDoubleBlackTrailObjects("Five Corners", "Double Black", True, "Bolton")
    cls.mtn1.setDoubleBlackTrailObjects("Vermont 200", "Double Black", False, "Bolton")
    cls.mtn2.setDoubleBlackTrailObjects("Spruce Line", "Double Black", True, "Stowe")

    cls.mtn3.setDoubleBlackTrailObjects("Cayonland", "Double Black", False, "Jay Peak")
    cls.mtn3.setDoubleBlackTrailObjects("Purgatory", "Double Black", True, "Jay Peak")


    # Glade Trails
    cls.mtn1.setGladeTrailObjects("Vista Glades", "Glade", True, "Bolton")
    cls.mtn2.setGladeTrailObjects("Upper Nose Dive", "Glade", False, "Stowe")
    cls.mtn3.setGladeTrailObjects("Stateside Glade", "Glade", False, "Jay Peak")

    # Skiers/Snowboarders
    # price, howFar
    cls.skier1 = skierSnowboarder.SkierSnowboarder("Michelle", 20, "Intermediate", 69, 60, True)

    cls.skier2 = skierSnowboarder.SkierSnowboarder("Lauren", 20, "Advanced", 109, 140, True)

    cls.skier3 = skierSnowboarder.SkierSnowboarder("Jason", 25, "Beginner", 105, 121, False)

    cls.skier4 = skierSnowboarder.SkierSnowboarder("Zach", 21, "Beginner", 95, 141, False)

    # Add vt mountains to ski day
    cls.skiDay = skiday.SkiDay()
    cls.skiDay.addVermontMountains(cls.mtn1)
    cls.skiDay.addVermontMountains(cls.mtn2)
    cls.skiDay.addVermontMountains(cls.mtn3)

    # add the skiers/snowboarders to the ski day
    cls.skiDay.addSkierSnowboarder(cls.skier1)
    cls.skiDay.addSkierSnowboarder(cls.skier2)
    cls.skiDay.addSkierSnowboarder(cls.skier3)
    cls.skiDay.addSkierSnowboarder(cls.skier4)
    cls.skiDay.getSkierSnowboarderList()


  def test_skiday(self):
    print("test_skiday()")
    # test pickVermontMountain in SkiDay

    self.skiDay.pickVermontMountain()
    mountains = self.skiDay.getFinalizedSkiDay()
    print(mountains)

    # Michelle - Bolton
    # Lauren - Bolton, Stowe, Jay Peak
    # Jason - Bolton, Stowe, Jay Peak
    # Zach - Bolton and Jay Peak
    mountainsSelected = {"Michelle": {"VT Mountains": ["Bolton"]}, "Lauren": {"VT Mountains": ["Bolton", "Stowe", "Jay Peak"]},
                         "Jason": {"VT Mountains": ["Bolton", "Stowe", "Jay Peak"]}, "Zach": {"VT Mountains": ["Bolton", "Jay Peak"]}}
    self.assertEqual(mountainsSelected, mountains)



    trailSelected = {'Michelle': {'VT Mountains': ['Bolton'], 'GreenTrails': [], 'BlueTrails': ['Timberline Run', 'Showtime'], 'BlackTrails': ['Cougar', 'Upper Tattle Tale'], 'DoubleBlackTrails': [], 'GladeTrails': []}, 'Lauren': {'VT Mountains': ['Bolton', 'Stowe', 'Jay Peak'], 'GreenTrails': [], 'BlueTrails': [], 'BlackTrails': [], 'DoubleBlackTrails': ['Five Corners', 'Spruce Line', 'Purgatory'],
                    'GladeTrails': ['Vista Glades']}, 'Jason': {'VT Mountains': ['Bolton', 'Stowe', 'Jay Peak'], 'GreenTrails': ['Round Robin', 'Magic Carpet', 'Slide', 'Snowball', 'Upper Villager', 'Cross Over', 'Inspiration', 'Deer Run', "Queen's Highway", 'Kangaroo Trail'], 'BlueTrails': [], 'BlackTrails': [], 'DoubleBlackTrails': [], 'GladeTrails': []}, 'Zach': {'VT Mountains': ['Bolton', 'Jay Peak'],
                    'GreenTrails': ['Round Robin', 'Magic Carpet', 'Slide', 'Snowball', 'Upper Villager', 'Deer Run', "Queen's Highway", 'Kangaroo Trail'], 'BlueTrails': [], 'BlackTrails': [], 'DoubleBlackTrails': [], 'GladeTrails': []}}
    # test determineTrailsForDay
    self.skiDay.determineTrailsForDay()
    trails = self.skiDay.getFinalizedSkiDay()
    print("\n Trails \n")
    self.assertEqual(trailSelected, trails)
    print(trails)

    correctSkiers = ["Michelle","Lauren","Jason","Zach"]
    skierList = self.skiDay.getSkierSnowboarderList()
    listReturned = []
    for object in skierList:
      listReturned.append(object.getName())
    self.assertEqual(correctSkiers,listReturned)

    correctMountains = ["Bolton","Stowe","Jay Peak"]
    mtnList = self.skiDay.getVTMountainsList()
    mtnReturned = []
    for vt in mtnList:
      mtnReturned.append(vt.getName())
    self.assertEqual(correctMountains,mtnReturned)

    skier5 = skierSnowboarder.SkierSnowboarder("Jackson", 24, "Beginner", 89, 138, False)
    self.skiDay.addSkierSnowboarder(skier5)
    correctSkiers = ["Michelle","Lauren","Jason","Zach","Jackson"]
    skierList = self.skiDay.getSkierSnowboarderList()
    listReturned = []
    for object in skierList:
      listReturned.append(object.getName())
    self.assertEqual(correctSkiers,listReturned)

    self.skiDay.pickVermontMountain()
    mountains = self.skiDay.getFinalizedSkiDay()
    print(mountains)

    addedSkierMountains = {'Michelle': {'VT Mountains': ['Bolton']}, 'Lauren': {'VT Mountains': ['Bolton', 'Stowe', 'Jay Peak']},
                        'Jason': {'VT Mountains': ['Bolton', 'Stowe', 'Jay Peak']}, 'Zach': {'VT Mountains': ['Bolton', 'Jay Peak']},
                        'Jackson': {'VT Mountains': ['Bolton', 'Jay Peak']}}
    self.assertEqual(addedSkierMountains, mountains)

    addedSkierNewTrails = {'Michelle': {'VT Mountains': ['Bolton'], 'GreenTrails': [], 'BlueTrails': ['Timberline Run', 'Showtime'], 'BlackTrails':
      ['Cougar', 'Upper Tattle Tale'], 'DoubleBlackTrails': [], 'GladeTrails': []}, 'Lauren': {'VT Mountains': ['Bolton', 'Stowe', 'Jay Peak'], 'GreenTrails':
      [], 'BlueTrails': [], 'BlackTrails': [], 'DoubleBlackTrails': ['Five Corners', 'Spruce Line', 'Purgatory'], 'GladeTrails': ['Vista Glades']}, 'Jason':
      {'VT Mountains': ['Bolton', 'Stowe', 'Jay Peak'], 'GreenTrails': ['Round Robin', 'Magic Carpet', 'Slide', 'Snowball', 'Upper Villager', 'Cross Over',
       'Inspiration', 'Deer Run', "Queen's Highway", 'Kangaroo Trail'], 'BlueTrails': [], 'BlackTrails': [], 'DoubleBlackTrails': [], 'GladeTrails': []},
       'Zach': {'VT Mountains': ['Bolton', 'Jay Peak'], 'GreenTrails': ['Round Robin', 'Magic Carpet', 'Slide', 'Snowball', 'Upper Villager', 'Deer Run',
      "Queen's Highway", 'Kangaroo Trail'], 'BlueTrails': [], 'BlackTrails': [], 'DoubleBlackTrails': [], 'GladeTrails': []}, 'Jackson': {'VT Mountains': ['Bolton', 'Jay Peak'],
       'GreenTrails': ['Round Robin', 'Magic Carpet', 'Slide', 'Snowball', 'Upper Villager', 'Deer Run', "Queen's Highway", 'Kangaroo Trail'], 'BlueTrails': [],
     'BlackTrails': [], 'DoubleBlackTrails': [], 'GladeTrails': []}}

    self.skiDay.determineTrailsForDay()
    trails = self.skiDay.getFinalizedSkiDay()
    self.assertEqual(addedSkierNewTrails, trails)

    mtn4 = vtmountain.vtmountain("Smugglers Notch", 3, 4, 1, 2, 1, 11, 110, True, 90)
    correctMountains = ["Bolton","Stowe","Jay Peak","Smugglers Notch"]
    self.skiDay.addVermontMountains(mtn4)
    mtnList = self.skiDay.getVTMountainsList()
    mtnReturned = []
    for vt in mtnList:
      mtnReturned.append(vt.getName())
    self.assertEqual(correctMountains,mtnReturned)

    self.skiDay.pickVermontMountain()
    mountains = self.skiDay.getFinalizedSkiDay()
    newMountainList = {'Michelle': {'VT Mountains': ['Bolton']},
                       'Lauren': {'VT Mountains': ['Bolton', 'Stowe', 'Jay Peak', 'Smugglers Notch']},
                       'Jason': {'VT Mountains': ['Bolton', 'Stowe', 'Jay Peak', 'Smugglers Notch']},
                       'Zach': {'VT Mountains': ['Bolton', 'Jay Peak', 'Smugglers Notch']},
                       'Jackson': {'VT Mountains': ['Bolton', 'Jay Peak']}}
    self.assertEqual(newMountainList, mountains)

    mtn4.setGreenTrailObjects("New Trail 1", "Green", True, "Smugglers Notch")
    mtn4.setBlueTrailObjects("New Trail 2", "Blue", True, "Smugglers Notch")
    mtn4.setBlackTrailObjects("New Trail 3", "Black", True, "Smugglers Notch")
    mtn4.setDoubleBlackTrailObjects("New Trail 4", "Double Black", True, "Smugglers Notch")
    mtn4.setGladeTrailObjects("New Trail 5", "Glade", True, "Smugglers Notch")

    self.skiDay.determineTrailsForDay()
    trails = self.skiDay.getFinalizedSkiDay()
    newAddedTrails = {'Michelle': {'VT Mountains': ['Bolton'], 'GreenTrails': [], 'BlueTrails': ['Timberline Run', 'Showtime'],
                                   'BlackTrails': ['Cougar', 'Upper Tattle Tale'], 'DoubleBlackTrails': [], 'GladeTrails': []},
                      'Lauren': {'VT Mountains': ['Bolton', 'Stowe', 'Jay Peak', 'Smugglers Notch'], 'GreenTrails': [], 'BlueTrails': [],
                                 'BlackTrails': [], 'DoubleBlackTrails': ['Five Corners', 'Spruce Line', 'Purgatory', 'New Trail 4'],
                                 'GladeTrails': ['Vista Glades', 'New Trail 5']}, 'Jason': {'VT Mountains': ['Bolton', 'Stowe', 'Jay Peak',
                                  'Smugglers Notch'], 'GreenTrails': ['Round Robin', 'Magic Carpet', 'Slide', 'Snowball', 'Upper Villager',
                                'Cross Over', 'Inspiration', 'Deer Run', "Queen's Highway", 'Kangaroo Trail', 'New Trail 1'], 'BlueTrails': [],
                                 'BlackTrails': [], 'DoubleBlackTrails': [], 'GladeTrails': []}, 'Zach': {'VT Mountains': ['Bolton', 'Jay Peak',
                                'Smugglers Notch'], 'GreenTrails': ['Round Robin', 'Magic Carpet', 'Slide', 'Snowball', 'Upper Villager', 'Deer Run', "Queen's Highway",
                          'Kangaroo Trail', 'New Trail 1'], 'BlueTrails': [], 'BlackTrails': [], 'DoubleBlackTrails': [], 'GladeTrails': []}, 'Jackson': {'VT Mountains':
                       ['Bolton', 'Jay Peak'], 'GreenTrails': ['Round Robin', 'Magic Carpet', 'Slide', 'Snowball', 'Upper Villager', 'Deer Run', "Queen's Highway", 'Kangaroo Trail'],
                       'BlueTrails': [], 'BlackTrails': [], 'DoubleBlackTrails': [], 'GladeTrails': []}}

    self.assertEqual(trails,newAddedTrails)

    #self.assertEqual(addedSkierNewTrails, trails)
    # Must uncomment this to fail, and comment this to pass
    #wrongTrails = self.skiDay.wrongPickVermontMountain()
    #self.assertEqual(wrongTrails, mountains)


if __name__ == "__main__":
  unittest.main()
