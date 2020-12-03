from simulation import Simulation

# Create a new object of our class, in order to call the appropriate methods.
simulation = Simulation();

# This time, user input comes before the loop, as the first input is a string.
location = input("Enter location: ");

# The second input still remains in a loop, as it needs to be parsed as an integer.
while True:
    try:
        # Cast the input as an integer.
        days = int(input("Days from now: "));
        # Break from our loop asking for input, once we have an acceptable value,
        # i.e. one that does not cause an exception
        break;
    except ValueError:
        # In the event of an exception, do nothing, and continue to top of loop,
        # in order to ask for input again.
        pass;

# Print the resulting simulation values.
print(simulation.weather(location, days));
