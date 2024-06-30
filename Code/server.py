import socket
from _thread import *
import pickle

server = "localhost"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

players = {}

def threaded_client(conn, player_id):
    conn.send(str.encode(str(player_id)))  # Send the player ID to the client
    players[player_id] = {
        "x": 100, "y": 100, 
        "x_vel": 0, "y_vel": 0, 
        "direction": "left", 
        "animation_count": 0, 
        "sprite_sheet": "idle", 
        "hit_count": 0, 
        "hit": False, 
        "id": player_id
    }

    while True:
        try:
            data = pickle.loads(conn.recv(2048*4))
            players[player_id] = data

            if not data:
                break
            else:
                reply = players
                conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    del players[player_id]
    conn.close()

current_player_id = 0
num = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, current_player_id))
    
    if (num % 2 == 0):
        current_player_id += 1
        num += 1
    else:
        num += 1
