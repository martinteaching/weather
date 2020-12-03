class Simulation:

    # Weather method tells us the weather based upon a simple model combining the location,
    # and the requested future date on which to make the prediction.
    def weather(self, location, days):

        # Our list of possible weather, as an array.
        possible_weather = ["sun", "wind", "rain", "snow", "cloud"];

        # Simple MOD example:
        # 9 % 3 = 0, because 3 goes into 9 3 times, without remainder.
        # 10 % 3 = 1, because 3 goes into 10 3 times, with remainder 1.
        # 11 % 3 = 2, because 3 goes into 10 3 times, with remainder 2.
        # 12 % 3 = 0, again, we've come full circle, because 3 goes into 12 4 times, without remainder.

        # 1. Use unicode (via the ordinal function), a coding system that gives each letter a number, to get a number from the first letter of our location.
        # 2. Mod this with 3, in order to get the first half of our index.
        index_first_half = ord(location[0]) % 3;

        # Repeat for days (minus ordinal, because already an integer).
        index_second_half = days % 3;

        # Index the array based upon our individual indexes combined: min value 0, max value 4.
        return possible_weather[index_first_half + index_second_half];
