import socket
from datetime import datetime
import json

s = socket.socket()

s.bind(('0.0.0.0', 8090))

s.listen(0)

locations = {
    "d70574a2680b": 'bedroom',
    "d90776a46a0d": 'bathroom',
    # "23784e38f373": 'livingroom',
    # "26eb82a5e8d9": 'kitchen',
    "148c259dee68": 'playroom',
    "0fbe9e163089": 'livingroom'
}

def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

while True:
    client, addr = s.accept()
    stuff = []
    addresses = []
    distances = []

    while True:
        content = client.recv(14)
        

        if len(content) == 0:
            break

        else:
            strrr = content.decode("utf-8")
            try:
                addresses.append(locations[strrr[:12]])
                distances.append(strrr[12:])
            except KeyError:
                pass

    # print("Closing connection")
    client.close()

    for x in range(len(distances)):
        if x == 0 or distances[x] < shortest:
            shortest = distances[x]
            index = x
    
    now = datetime.now()
    timeentry = now.strftime("%H-%M")

    entryWeek = int(now.strftime("%U")) % 7
    timeFile = str(entryWeek) + now.strftime("-%d-%m") + ".json"

    try:
        entry = dict(masa=timeentry, loc=addresses[index])
    except NameError:
        entry = dict(masa=timeentry, loc="not found")

    print(entry)
    try:
        with open(timeFile) as json_file:
            data = json.load(json_file)
            temp = data['entry']
            temp.append(entry)
    except:
        data = {
            'entry':[
                {
                    'masa': timeentry,
                    'loc': addresses[index]
                }
            ]
        }

    write_json(data, timeFile)
