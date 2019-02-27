import logging

class MyUser:
    user_ws = {}
    user_login = {}

    def __init__(self, max_user=3):
        self.max_user = max_user

    def add_user(self, name, ws):
        if (name in self.user_login):
            if (len(self.user_login[name]) < self.max_user):
                self.user_login[name].append(ws)
                return(True)
            else:
                return(False)
        else:
            self.user_login[name] = [ws]
            return(True)

    def get_user_ws(self, name):
        if name in self.user_login:
            return(self.user_login[name])
        else:
            return(None)

    def get_user_login(self, ws):
        if ws in self.user_ws:
            return(user[name])
        else:
            return(None)

    def check_by_name():
        pass

    def check_by_ws():
        pass

    def del_user_by_name(self, name):
        self.user_login.pop(name)

    def del_user_by_websocket(self, ws):
        self.user_ws.pop(ws)
