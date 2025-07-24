# app.py
from flask import Flask, render_template, request
import numpy as np
import pickle
import os
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tensorflow.keras.layers import GlobalAveragePooling2D

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load model and scaler
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('model/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Image feature extractor
base_model = MobileNetV2(weights='imagenet', include_top=False)
feature_model = Model(inputs=base_model.input, outputs=GlobalAveragePooling2D()(base_model.output))

def extract_image_features(img_path):
    try:
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        features = feature_model.predict(img_array)
        return features.flatten()
    except Exception as e:
        print(f"[Error] Feature extraction failed: {e}")
        return np.zeros(1280)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('image')
        if not file or file.filename == '':
            return "Please upload an image."

        try:
            sqft = float(request.form['sqft'])
            bed = float(request.form['bed'])
            bath = float(request.form['bath'])
        except:
            return "Please enter valid numbers for sqft, bed, and bath."

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        image_features = extract_image_features(filepath)
        combined_features = np.concatenate([image_features, [sqft, bed, bath]])

        features_scaled = scaler.transform([combined_features])
        prediction = model.predict(features_scaled)[0]

        return render_template('result.html', prediction=round(prediction, 2), image_path=filepath)

    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
