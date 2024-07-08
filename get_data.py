import requests
from PIL import Image

apikey = '' 

def get_img(marker_coordinates,width,height,zoom):
    
    min_lat = min(coord[0] for coord in marker_coordinates)
    max_lat = max(coord[0] for coord in marker_coordinates)
    min_lon = min(coord[1] for coord in marker_coordinates)
    max_lon = max(coord[1] for coord in marker_coordinates)

    center_lat = (min_lat + max_lat) / 2
    center_lon = (min_lon + max_lon) / 2

    api_url = f"https://image.maps.ls.hereapi.com/mia/1.6/mapview?apiKey={apikey}&c={center_lat},{center_lon}&z={zoom}&w={width*2}&h={height*2}&t=1&nodot"
    response = requests.get(api_url)
    return response.content

def trim_to_dimensions(input_path, output_path, target_width, target_height):
    image = Image.open(input_path)
    original_width, original_height = image.size
    trim_left = (original_width - target_width) // 2
    trim_top = (original_height - target_height) // 2
    trim_right = original_width - trim_left
    trim_bottom = original_height - trim_top
    trimmed_image = image.crop((trim_left, trim_top, trim_right, trim_bottom))
    resized_image = trimmed_image.resize((target_width, target_height))
    resized_image.save(output_path)

def get_location(marker_coordinates):

    min_lat = min(coord[0] for coord in marker_coordinates)
    max_lat = max(coord[0] for coord in marker_coordinates)
    min_lon = min(coord[1] for coord in marker_coordinates)
    max_lon = max(coord[1] for coord in marker_coordinates)

    center_lat = (min_lat + max_lat) / 2
    center_lon = (min_lon + max_lon) / 2

    api_url = f"https://revgeocode.search.hereapi.com/v1/revgeocode?at={center_lat},{center_lon}&apiKey={apikey}"
    response = requests.get(api_url)
    return response.content.decode("utf-8")