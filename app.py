# app.py
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import os
import cv2
from ultralytics import YOLO

app = Flask(__name__)

# Load pre-trained YOLOv8 model
model_detect_path = "model/detect/best.pt"
model_detect = YOLO(model_detect_path)

# model_segment_path = "model/segment/best.pt"
model_segment_path = "new_model/best.pt"
model_segment = YOLO(model_segment_path)

# Apply Flask CORS
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = "static/uploads"

def create_upload_folder():
    upload_folder = app.config['UPLOAD_FOLDER']
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

def predict_image(img_path):
    frame = cv2.imread(img_path)
    results = model_detect(frame, save=False, imgsz=320, conf=0.5)
    return results, len(results[0].boxes)

def segment_image(img_path):
    frame = cv2.imread(img_path)
    results = model_segment(frame, save=False, imgsz=320)
    return results, len(results[0].boxes)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')

        file = request.files['file']

        if file.filename == '':
            return render_template('index.html', error='No selected file')

        create_upload_folder()

        if file:
            img_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(img_path)

            if 'segment' in request.form:
                results, num_objects = segment_image(img_path)
            else:
                results, num_objects = predict_image(img_path)

            for r in results:
                im_array = r.plot()  # plot a BGR numpy array of predictions
                # Save image using OpenCV
                cv2.imwrite(img_path, cv2.cvtColor(im_array, cv2.COLOR_BGR2RGB))

            if num_objects:
                return render_template('index.html', img_path=img_path, num_objects=num_objects)
            else:
                return render_template('index.html', msg='Can\'t predict !!!')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='6868')
