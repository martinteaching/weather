from unittest import TestCase
from simulation import Simulation

class WeatherTest(TestCase):

    def setUp(self):
        # Underscore indicating a 'private' variable (not literally private, this is achieved by double underscore,
        # just a convention);
        self._simulation = Simulation();

    # Use camel case here, to keep consistent with parent class which uses camel case (I believe?)
    def testBasic(self):
        assert self._simulation.weather("London", 5) == "snow";

    def testLarge(self):
        assert self._simulation.weather("London", 365) == "snow";

    def testNegative(self):
        result = self._simulation.weather("London", -1);
        assert not (result in ["sun", "wind", "rain", "snow", "cloud"]);
