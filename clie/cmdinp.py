import readline

class Cmd_inp(object):
    def __init__(self, cmd):
        self.cmd = sorted(cmd)

    def completer(self, text, state):

        if text:

            temp = [x for x in self.cmd if x and x.startswith(text)]
        else:
            temp = self.cmd[:]

        try:
            return temp[state]
        except IndexError:
            return None
