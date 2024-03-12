from QoSResponse import QoSResponse
import uuid
import datetime
import base64


class QoSResponseWithPayload(QoSResponse):


    """The same as QoSResponse but with a sizable payload.
    
    Attributes:
    - server_id: str = The id of the server. Currently the the name of
        the user of linux who deploys the server.
    - request_receival_time: str: The instance when the HTTP that 
        generates this response is received.
    - response_send_time: str = The instance when this object is sent
        to its destination.
    - response_payload: str = UTF-8 encoded sequence of '0' characters
        whose length is especified by the response_payload_size.
    """

    def __init__(self, request_payload_size: int) -> None:

        """Constructs a QoSResponseWithPayload
        
        Parameters:
        - request_payload_size: int = the size of the payload
            especified in bytes.
        """
        super().__init__()

        self.response_payload = "0" * request_payload_size
        self.response_payload_size = len(self.response_payload)
