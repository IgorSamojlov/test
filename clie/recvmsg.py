def read_msg(msg):
    if (msg['cmd'] == 'auth'):
        print('Message from server: auth is:', msg['answer'])
    elif(msg['cmd'] == 'msg'):
        print('Message from', msg['from'], ' ', msg['text'])
    elif (msg['cmd'] == 'reg'):
        print ('Registration is ', msg['answer'])
