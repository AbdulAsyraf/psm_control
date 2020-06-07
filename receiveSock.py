import socket
from datetime import datetime
import json

s = socket.socket()

s.bind(('0.0.0.0', 8090))

s.listen(0)

def write_json(data, filename = 'data.json'):
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
            # print(content.decode("utf-8"))
            # stuff.append(content.decode("utf-8"))
            strrr = content.decode("utf-8")
            addresses.append(strrr[:12])
            distances.append(strrr[12:])
            # print(strrr[:12])
            # print(strrr[12:])

    print("Closing connection\n")
    client.close()

    # for x in range(len(stuff)):
    #     if x%2 == 1:
    #         distances.append(int(stuff[x]))
    #         print("RSSI: ", stuff[x])
    #     else:
    #         addresses.append(stuff[x])
    #         print("Address: ", stuff[x])

    for x in range(len(addresses)):
        print("Address: ", addresses[x])
        print("RSSI: ", distances[x])

    # for x in stuff:
    #     print(x)

    for x in range(len(distances)):
        if x == 0 or distances[x] < shortest:
            shortest = distances[x]
            index = x
    
    now = datetime.now()
    timeentry = now.strftime("%d-%m-%Y-%H-%M")
    # timeentry = now.day + "-" + now.month + "-" + now.year + " " + now.hour + ":" + now.minute

    print("Closest beacon is ", addresses[index])

    entry = dict(masa=timeentry, loc=addresses[index])
    print(entry)

    with open('data.json') as json_file:
        data = json.load(json_file)

        temp = data['entry']

        temp.append(entry)

    write_json(data)

