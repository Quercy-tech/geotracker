FROM python:3.11
WORKDIR /app
COPY .. /app
RUN pip install flask requests folium
CMD ["python", "server.py"]