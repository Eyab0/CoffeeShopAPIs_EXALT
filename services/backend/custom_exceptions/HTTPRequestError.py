class HTTPRequestError(Exception):
    """
     to handle the HTTP request errors
    """

    def __init__(self, msg, code):
        self.code = code
        self.msg = msg
