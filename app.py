from flask import Flask, request, jsonify
import cv2
import numpy as np
import base64
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # يسمح بـ CORS

@app.route('/enhance', methods=['POST'])
def enhance_image():
    file = request.files['image']
    img_array = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    # تحسين الصورة (تكبير بسيط)
    enhanced = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LANCZOS4)

    _, buffer = cv2.imencode('.jpg', enhanced)
    jpg_as_text = base64.b64encode(buffer).decode('utf-8')

    return jsonify({"enhanced_image": jpg_as_text})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
