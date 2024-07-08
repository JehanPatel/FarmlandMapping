import sys
import soil_color
import dominant_image_color

if __name__ == '__main__':
    image_path = sys.argv[1]
    soil_match = soil_color.find_soil_color(dominant_image_color.dominant_color(image_path))
    print(soil_match)
