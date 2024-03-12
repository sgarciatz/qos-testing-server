import os
import datetime

class QoSResponse(object):


    """This class is the payload of an HTTP response of the server.
    
    Parameters:
    - server_id: str = The id of the server. Currently the the name of
        the user of linux who deploys the server.
    - request_receival_time: str: The instance when the HTTP that 
        generates this response is received.
    - response_send_time: str = The instance when this object is sent
        to its destination.
    """ 

    def __init__(self) -> None:

        """Constructs a QoSResponse."""
        
        self.server_id: str = os.getlogin()
        self.request_receival_time: str = str(datetime.datetime.now())
        self.response_send_time: str = None


    def send(self):

        """This method must be called before sending the response in
        order to establish the dispatch_time.
        """

        self.response_send_time = str(datetime.datetime.now())