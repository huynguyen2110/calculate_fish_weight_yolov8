from flask import Flask, render_template, request
import os
from random import random
from ultralytics import YOLO
from features.get_history import get_history, predict_future_weight
from predict import predict
import json
from datetime import datetime

# Khởi tạo Flask
app = Flask(__name__, static_folder='static/upload')
app.config['UPLOAD_FOLDER'] = "static\images"
model = YOLO('modules/best.pt')


@app.template_filter('round_decimal')
def round_decimal(value, digits=1):
    return round(value, digits)


# Hàm xử lý request
@app.route("/", methods=['GET', 'POST'])
def home_page():
    # Nếu là POST (gửi file)
    if request.method == "POST":
        try:
            # Lấy file gửi lên
            image = request.files['file']
            print(image.filename)
            if image:
                # Lưu file
                path_to_save = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
                print("Save = ", path_to_save)
                image.save(path_to_save)

                # image = cv2.imread(path_to_save)

                print("Image = ", image.filename)
                fishes = predict(path_to_save)
                print('Image2 = ', image.filename)
                return render_template("index.html", user_image=image.filename, rand=str(random()), fishes=fishes,
                                       msg="Tải file lên thành công")

            else:
                # Nếu không có file thì yêu cầu tải file
                return render_template('index.html', msg='Hãy chọn file để tải lên')

        except Exception as ex:
            # Nếu lỗi thì thông báo
            print('ddddddddd', ex)
            return render_template('index.html', msg='Không nhận diện được vật thể')
    else:
        # Nếu là GET thì hiển thị giao diện upload
        return render_template('index.html')


@app.route("/history", methods=['GET'])
def history():
    fishes = get_history()
    return render_template('history.html', fishes=fishes)


@app.route('/api/history', methods=['POST'])
def history_api():
    day = json.loads(request.data)['day']

    dataReturn = predict_future_weight(day)

    return {'days': dataReturn}


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
