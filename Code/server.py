import socket
from _thread import *
import pickle

server = "localhost"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection, Server Started")

players = {}
skins = ["MaskDude", "NinjaFrog"]  # List of available skins

def threaded_client(conn, player_id):
    print(f"Connection established with player {player_id}")
    skin = skins[player_id % len(skins)]  # Assign skin based on player_id
    conn.send(str.encode(str(player_id)))  # Send the player ID to the client
    players[player_id] = {
        "x": 100, "y": 100, 
        "x_vel": 0, "y_vel": 0, 
        "direction": "left", 
        "animation_count": 0, 
        "sprite_sheet": "idle", 
        "hit_count": 0, 
        "hit": False, 
        "id": player_id,
        "skin": skin  # Add skin to player data
    }

    conn.settimeout(10)  # Increase the timeout to 10 seconds

    while True:
        try:
            data = conn.recv(2048*4)
            if not data:
                #print(f"No data received from player {player_id}")
                break

            player_data = pickle.loads(data)
            #print(f"Received data from player {player_id}: {player_data}")
            players[player_id] = player_data

            reply = players
            conn.sendall(pickle.dumps(reply))
        except Exception as e:
            print(f"Error: {e}")
            break

    print(f"Lost connection with player {player_id}")
    del players[player_id]
    conn.close()

current_player_id = 0
num = 0

while True:
    conn, addr = s.accept()
    print(f"Connected to: {addr}")
    start_new_thread(threaded_client, (conn, current_player_id))
    
    if (num % 2 == 0):
        current_player_id += 1
        num += 1
    else:
        num += 1
