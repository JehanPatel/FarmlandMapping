from flask import Flask, render_template,request
from io import BytesIO
from ml.crop_prediction.ZDecision_Tree_Model_Call import *
import soil_color
import dominant_image_color
import get_data
import ml.ph_prediction.ph_prediction
import uuid
import json

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/process_coordinates', methods=['POST'])

def process_coordinates():
    data = request.get_json()
    coordinates_dict = data.get('coordinates', [])
    coordinates = [(coord['lat'], coord['lng']) for coord in coordinates_dict]
    zoom = data.get('zoom', [])
    width = int(data.get('width',[]))
    height = int(data.get('height',[]))
    img = get_data.get_img(coordinates,width,height,zoom)
    img_path = f'./static/uploads/{str(uuid.uuid4())}_sat.png'
    get_data.trim_to_dimensions(BytesIO(img),img_path,width,height)
    address = get_data.get_location(coordinates)
    img_color = dominant_image_color.dominant_color(img_path)
    soil_data = soil_color.find_soil_color(img_color)
    ph = ml.ph_prediction.ph_prediction.predict_ph([list(img_color)])
    return ({
        'soil_data': soil_data,
        'file_path': img_path,
        'img_color': img_color,
        'ph': ph[0],
        'address': address
    })

@app.route('/soil_info', methods=['POST'])

def soil_info():
    try:
        soil_data = json.loads(request.form.get('soil_data'))
        file_path = request.form.get('file_path')
        img_color = request.form.get('img_color')
        ph = request.form.get('ph')
        season = request.form.get('season','Whole Year')
        try:
            address = json.loads(request.form.get('address'))
        except:
            #dt = request.form.get('district')
            #st = request.form.get('state')
            #address = {'items':[{'address':{'state':st,'county':dt}}]}
            pass
        state = address["items"][0]['address']['state']
        district = address["items"][0]['address']['county'].upper()
        crops = find_crops(state,district,season)
        return render_template('soil_data.html',soil_data=soil_data,file_path=file_path,img_color=img_color,ph=ph,state=state,district=district,season=season,crops=crops)
    except:
        uploaded_file = request.files['image']
        unique_filename = str(uuid.uuid4())
        file_extension = uploaded_file.filename.rsplit('.', 1)[-1].lower()
        file_path = f'./static/uploads/{unique_filename}_orignal.{file_extension}'
        uploaded_file.save(file_path)
        img_color = dominant_image_color.dominant_color(file_path)
        soil_data = soil_color.find_soil_color(img_color)
        ph = ml.ph_prediction.ph_prediction.predict_ph([list(img_color)])
        st = "Madhya Pradesh"
        dt="SEHORE"
        address = {'items':[{'address':{'state':st,'county':dt}}]}
        season = request.form.get('season','Whole Year')
        address = {'items':[{'address':{'state':st,'county':dt}}]}
        state = address["items"][0]['address']['state']
        district = address["items"][0]['address']['county'].upper()
        crops = find_crops(state,district,season)
        return render_template('soil_data.html', soil_data=soil_data,file_path=file_path,img_color=img_color,ph=ph,state=state,district=district,season=season,crops=crops)

@app.route('/process_season', methods=['POST'])

def process_season():
    data = request.get_json()
    season = data.get('season', [])
    print(season)
    state = data.get('state',[])
    district = data.get('district',[])
    crops = find_crops(state,district,season)
    return ({'crops':crops})
   
if __name__== '__main__':
    app.run(host='0.0.0.0',debug=True)