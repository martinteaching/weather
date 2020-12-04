from sample_server import SampleServer
from simulation import Simulation

# Inherit from SampleServer, as we did with the unit tests.
class SimulationServer(SampleServer):

    # This is a method I know exists from the parent class, that will
    # be called every time a post request is made.
    def do_POST(self):
        # Call the parent method (which is part of our class now, so self works),
        # in order to extract post data.
        postData = self.get_post_data();
        # Extract the keys. This almost forms a contract with the caller, dictating
        # the information that needs to be passed.
        location = postData["location"];
        days = postData["days"];
        # Call our original simulation class, and the weather method, to invoke our model.
        # Note we're creating an object of simulation here on the fly. Really this should
        # be done in a constructor.
        weather = Simulation().weather(location, days);
        # Once again invoke the parent method to send the data back.
        # Should really be encapsulated in a JSON string also for consistency, but
        # we're just doing things simply for now.
        self.send_post_response(weather);
