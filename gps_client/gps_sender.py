import  requests,time,random,os

SERVER_URL = os.getenv("SERVER_URL", "http://host.docker.internal:3030/coords")

def generate_coords():
    # Coordinates somewhere in Budapest
    lat = 47.50 + random.uniform(-0.01, 0.01)
    lon = 19.04 +random.uniform(-0.01, 0.01)
    return {"latitude": lat, "longitude": lon}

while True:
    coords = generate_coords()
    print("Sending GPS data", coords)
    try:
        requests.post(SERVER_URL, json=coords)
    except Exception as e:
        print("Exception: ",e)
    time.sleep(10)
