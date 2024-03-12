import sys
from flask import Flask, request, Response
from QoSResponse import QoSResponse
from QoSResponseWithPayload import QoSResponseWithPayload
import ast


application = Flask(__name__)

@application.route("/simple", methods=["GET"])
def simple_get():

    """This method receives a light HTTP GET Request and returns a
    light HTTP Response.
    
    Returns: an a light HTTP Response with a <QoSResponse>.
    """
    res = QoSResponse()
    res.send()
    return res.__dict__

@application.route("/with-payload/<int:payload_size>", methods=["GET"])
def with_payload_get(payload_size: int):

    """This method receives a light HTTP GET Request and returns a dict
    with the payload specified in the url parameter.
    
    Parameters:
    - payload_size: int = The size of the HTTP Response payload field.
    
    Returns: the HTTP Response with a payload of the given size.
    """

    res = QoSResponseWithPayload(payload_size)
    res.send()
    return res.__dict__

@application.route("/with-payload", methods=["POST"])
def with_payload_post():

    """This method receives a HTTP POST Request with a payload of a given
    size and returns an HTTP Response with a payload of the same size.
    
    Parameters:
    - payload_size: int = The size of the HTTP Response payload field.
    
    Returns: the HTTP Response with a payload of the given size.
    """

    req_data = ast.literal_eval(request.data.decode("UTF-8"))
    res = QoSResponseWithPayload(req_data["request_payload_size"])
    return res.__dict__
