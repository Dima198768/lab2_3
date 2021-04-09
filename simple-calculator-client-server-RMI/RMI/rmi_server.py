#RMI
import Pyro4

@Pyro4.expose
class remote_service(object):

    def echo(self, text):
        return "You use echo with text: " + text

    def login(self, login, password):
        return login == "dima" and password == "123"

    def ping(self):
        return "localhost"


daemon = Pyro4.Daemon()                # make a Pyro daemon
uri = daemon.register(remote_service)   # register the greeting maker as a Pyro object

print("Server Uri =", uri)      # print the uri so we can use it in the client later
daemon.requestLoop()                   # start the event loop of the server to wait for calls