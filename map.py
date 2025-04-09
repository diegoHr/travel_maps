import folium

# Crear un mapa centrado en Hungría
mapa = folium.Map(location=[47.5, 19.5], zoom_start=7)

# Definir los puntos de interés con sus coordenadas aproximadas
destinos = {
    "Budapest": (47.4979, 19.0402),
    "Szentendre": (47.677, 19.072),
    "Visegrád": (47.785, 18.973),
    "Hollókő": (47.912, 19.595),
    "Eger": (47.902, 20.377),
    # Usamos las coordenadas de Lillafüred para representar el área del Parque Nacional de Bükk
    "Bükk National Park": (48.260, 20.350),
    "Lago Balatón": (46.85, 17.72),
    "Esztergom": (47.798, 18.739)
}

# Agregar marcadores al mapa
for lugar, coord in destinos.items():
    folium.Marker(coord, popup=lugar, tooltip=lugar, icon=folium.Icon(color='blue')).add_to(mapa)

# Definir rutas por día según el itinerario ajustado

# Día 1-2: Budapest (base; sin trazo adicional)
ruta1 = [destinos["Budapest"]]

# Día 3: Excursión a Szentendre y Visegrád, y regreso a Budapest
ruta2 = [
    destinos["Budapest"],
    destinos["Szentendre"],
    destinos["Visegrád"],
    destinos["Budapest"]
]
folium.PolyLine(ruta2, color="green", weight=4, opacity=0.7, tooltip="Día 3: Szentendre y Visegrád").add_to(mapa)

# Día 4: Ruta de Budapest a Hollókő y Eger (noche en Eger)
ruta3 = [
    destinos["Budapest"],
    destinos["Hollókő"],
    destinos["Eger"]
]
folium.PolyLine(ruta3, color="red", weight=4, opacity=0.7, tooltip="Día 4: Budapest - Hollókő - Eger").add_to(mapa)

# Día 5: Eger - Bükk National Park - Budapest
ruta4 = [
    destinos["Eger"],
    destinos["Bükk National Park"],
    destinos["Budapest"]
]
folium.PolyLine(ruta4, color="purple", weight=4, opacity=0.7, tooltip="Día 5: Eger - Bükk National Park - Budapest").add_to(mapa)

# Día 6: Budapest - Lago Balatón (noche en zona del Balatón)
ruta5 = [
    destinos["Budapest"],
    destinos["Lago Balatón"]
]
folium.PolyLine(ruta5, color="orange", weight=4, opacity=0.7, tooltip="Día 6: Budapest - Lago Balatón").add_to(mapa)

# Día 7: Lago Balatón - Esztergom - Budapest
ruta6 = [
    destinos["Lago Balatón"],
    destinos["Esztergom"],
    destinos["Budapest"]
]
folium.PolyLine(ruta6, color="blue", weight=4, opacity=0.7, tooltip="Día 7: Lago Balatón - Esztergom - Budapest").add_to(mapa)

# Guardar el mapa en un archivo HTML
mapa.save("itinerario_hungria_bukk.html")
print("Mapa generado y guardado como 'itinerario_hungria_bukk.html'")