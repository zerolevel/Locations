from location import Location
from coordinates import Coordinates
import unittest

class TestLocationCoordinates(unittest.TestCase):
    def testMumbai(self):
        lc = Location()
        mumbai_cord = lc.getCoordinates(query="Mumbai")
        mumbai_expected = Coordinates(lat=19.017587, lng=72.856248, state="Maharashtra", sub_district="Mumbai",
                                      district="Mumbai", level="Town", name="MUMBAI")
        self.assertTrue((float(mumbai_cord.lat) - float(mumbai_expected.lat)) < 0.00001, "Latitude didnot Match for Mumbai")
        self.assertTrue((float(mumbai_cord.lng) - float(mumbai_expected.lng))< 0.00001, "Longitude didnot Match for Mumbai")
        self.assertEqual(mumbai_cord.state, mumbai_expected.state, "States didnot Match for Mumbai")
        self.assertEqual(mumbai_cord.district, mumbai_expected.district, "District didnot Match for Mumbai")
        self.assertEqual(mumbai_cord.sub_district, mumbai_expected.sub_district, "SUB District didnot Match for Mumbai")
        self.assertEqual(mumbai_cord.level, mumbai_expected.level, "Levels didnot Match for Mumbai")

    def testNehdaiJaisalmerRajasthan(self):
        lc = Location(state="Rajasthan", district="Jaisalmer")
        nehdai_cord = lc.getCoordinates(query="Nehdai")
        nehdai_expected = Coordinates(lat=27.402876,lng=70.995243, state="Rajasthan", district="Jaisalmer",
                                      sub_district="Jaisalmer", level="Village", name="NEHDAI")
        self.assertEqual(nehdai_cord,nehdai_expected,"Cordinates didnot Match for Nehdai, (JSM) Rajasthan")


