# 🌍 GeoTracker

**GeoTracker** is a Python project that simulates GPS coordinates and visualizes them on an interactive map. It uses `Flask` for the backend, `Docker` for containerization, and `folium` to generate map visualizations.
---

## 🚀 Features

- 🛰️ Simulates GPS location data
- 📡 Sends data to a Flask-based server
- 🗺️ Displays coordinates on an interactive map
- 🐳 Runs completely in Docker containers
- ⚙️ Easy orchestration with Docker Compose

---

## 📦 Tech Stack

- **Python 3.11**
- **Flask** – web server for receiving GPS data
- **Requests** – for sending simulated coordinates
- **Folium** – for generating interactive maps
- **Docker & Docker Compose** – for containerized environments

---

## 🧪 How It Works

1. The **GPS sender** generates random coordinates and sends them to the Flask server every 10 seconds.
2. The **Flask server** stores all received coordinates in memory.
3. The **map generator script** (`map_gen.py`) fetches the stored data and renders it into a map using `folium`.
4. The map is saved as `map.html` and opened in your browser.
