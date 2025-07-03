import folium, requests, webbrowser

response = requests.get("http://localhost:3030/map")
points = response.json()

m = folium.Map(location=[47.4979,19.04], zoom_start=10)

for point in points:
    folium.Marker([point["latitude"], point["longitude"]]).add_to(m)

m.save("map.html")
webbrowser.open("map.html", new=2)