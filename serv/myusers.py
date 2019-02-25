import logging

logging.basicConfig(filename='log_user.log', level=logging.INFO)

class MyUser():
    def __init__(self, max_user=3):
        self.max_user = max_user
        self.user_ws = {}
        self.user_log = {}

    def add_user(self, name, ws):
        if (name in self.user_log):
            if (len(self.user_log[name]) < self.max_user):
                self.user_log[name].append(ws)
                logging.info(self.user_log)
                return(True)
            else:
                return(False)
        else:
            self.user_log[name] = [ws]
            logging.info(self.user_log)
            return(True)

    def get_user_ws(self, name):
        if name in self.user_log:
            return(self.user_log[name])
        else:
            return(None)

    def get_user_log(self, ws):
        if ws in self.user_ws:
            return(user[name])
        else:
            return(None)

    def del_user_by_name(self, name):
        pass

    def del_user_by_websocket(self, ws):
        pass
