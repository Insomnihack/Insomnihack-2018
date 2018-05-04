
from mitmproxy import http
from subprocess import Popen

# This script launches a new instance of the vulnerable binary every time a "Set-Cookie" header is observed in a response
def response(flow: http.HTTPFlow) -> None:
    host = flow.request.host;
    cookie = flow.response.headers.get_all("Set-Cookie");
    if cookie:
        Popen(["./cookie_logger",host,';'.join(cookie)])
        # Uncomment the following to log to a file (disabled during the CTF)
        #with open("cookies.log","a") as log:
        #    Popen(["./cookie_logger",host,';'.join(cookie)],stdout=log)
