from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/image.jpg')
def get_image():
    image_path = os.path.join(app.root_path, 'static', 'image.jpg')
    if os.path.exists(image_path):
        return send_file(image_path, mimetype='image/jpeg')
    else:
        return 'Image not found', 404

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

