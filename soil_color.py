import math
import json

def euclidean_distance(color1, color2):
    if len(color1) == 3:
        color1 = color1 + (255,)
    r1, g1, b1, a1 = color1
    r2, g2, b2, a2 = color2
    distance = math.sqrt((r1 - r2)**2 + (g1 - g2)**2 + (b1 - b2)**2 + (a1-a2)**2)
    return distance

def find_soil_color(target_color):
    with open('soil.json', 'r') as soils:
        soil_data = json.load(soils)
        min_distance = float('inf')
        closest_soil = None

        for soil in soil_data['soil_types']:
            color = (float(soil['color']['r']),float(soil['color']['g']),float(soil['color']['b']),255)
            distance = euclidean_distance(target_color, color)
            if distance < min_distance:
                min_distance = distance
                closest_soil = soil

    return closest_soil
