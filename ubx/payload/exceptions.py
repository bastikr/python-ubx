class PayloadError(Exception):
    def __init__(self, msg, buffer, context, suberror=None):
        if isinstance(suberror, Exception):
            submessage = "\n- " + str(suberror)
        elif isinstance(suberror, (tuple, list)):
            submessage = "\n- " + "\n- ".join(map(str, suberror))
        else:
            submessage = ""
        msg = msg + submessage.replace("\n", "\n  ")

        Exception.__init__(self, msg)
        self.msg = msg
        self.buffer = buffer
        self.context = context
        self.suberror = suberror
