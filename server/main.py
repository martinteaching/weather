from simulation_server import SimulationServer
from http.server import HTTPServer

print("Serving...");

# Address + Port combination, along with HTTP handler.
server = HTTPServer(("0.0.0.0", 8888), SimulationServer);

try:
    server.serve_forever();
# CLARIFY: Catching the exception
# A: Allows us to proceed to the server close (the interrupt is handled and passed, rather than stopping execution).
# B: Neatens things up; ensures we don't print details of the exception to the console when we exit.
except KeyboardInterrupt:
    pass;

server.server_close();
