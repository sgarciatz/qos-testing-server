# QoS Testing server

This Flask based application is intended to be deployed in order to measure how network topology changes may affect the end2end latency.

## Execution guide

Execute the following code:

``` 
pip install -e requirement.txt
gunicorn -w 1 -b <IP address:PORT> QoSServer
```


The server's endpoints are the following:

- `http://<IP address:PORT>/simple through` GET
- `http://<IP address:PORT>/with-payload` through POST
- `http://<IP address:PORT>/with-payload/<payload-size>` through GET