from flask import Blueprint, request
import service
import time
import os
import shutil
import json
import api

blueprint = Blueprint("routes", __name__)


@blueprint.route("/api")
def home():
    return "<h1>Welcome to DeepFace API, edited by Sakura Neko!</h1>"

@blueprint.route('/api/test', methods=['GET'])
def test():
    return { "message": 'test success'}

@blueprint.route("/api/upload", methods=["POST"])
def upload():
    if 'image' in request.files:
        image = request.files['image']
        file_id = str((int) (time.time() * 1000))
        file_id += os.path.splitext(image.filename)[1]
        image.save('temp_images/' + file_id)
        return { "status": 1, "message": "upload success", "img_id": file_id}
    return { "status": 0, "message": "upload failed"}

@blueprint.route("/api/register", methods=["POST"])
def register():
    input_args = request.get_json()
    if input_args is None:
        return {"status": 0, "message": "empty input set passed"}
    img_id = input_args.get("img_id")
    if img_id is None:
        return {"status": 0, "message": "you must pass img_id input"}
    if (os.path.exists('temp_images/' + img_id) == False):
        return {"status": 0, "message": "img_id not found"}
    name = input_args.get("name")
    if name is None:
        return {"status": 0, "message": "you must pass name input"}
    if (os.path.exists('temp_images/' + img_id) == False):
        return {"status": 0, "message": "img_id not found"}
    if (service.detect_face('temp_images/' + img_id, 'opencv') == False):
        return {"status": 0, "message": "Face not found"}
    users = {}
    with open('db/users.json', 'r') as file:
        users = json.load(file)
    if (users.get(name) is not None):
        return {"status": 0, "message": "user already exists"}
    user_image_file = name + os.path.splitext(img_id)[1]
    users[name] = {
        "user_image": user_image_file,
    }
    shutil.copy('temp_images/' + img_id, 'db/' + user_image_file)
    with open('db/users.json', 'w') as file:
        json.dump(users, file)
    with open('db/photos.json', 'r') as file:
        photos = json.load(file)
    with open('db/photos.json', 'w') as file:
        photos[user_image_file] = name
        json.dump(photos, file)
    service.needed_update = True
    return { "status": 1, "message": "Register success, your data will be updated in " + str(api.update_time()) + "s."}

@blueprint.route("/api/recognize", methods=["POST"])
def recognize():
    input_args = request.get_json()
    if input_args is None:
        return {"status": 0, "message": "empty input set passed"}
    img_id = input_args.get("img_id")
    if img_id is None:
        return {"status": 0, "message": "you must pass img_id input"}
    if (os.path.exists('temp_images/' + img_id) == False):
        return {"status": 0, "message": "img_id not found"}
    obj = service.recognize(
        img_path=img_id
    )
    if (len(obj[0]) > 0):
        print(obj)
        if (abs(obj[0]['VGG-Face_cosine'][0]) < 1):
            found_img = os.path.basename(obj[0]['identity'][0])
            with open('db/photos.json', 'r') as file:
                photos = json.load(file)
            return {"status": 1, "message": "Recognization success, Welcome back, " + photos[found_img] + " !",
                    "user": photos[found_img]}
        return {"status": 0, "message": "Recognization failed, no face found"}
    else:
        return {"status": 0, "message": "Recognization failed, no face found"}

@blueprint.route("/api/represent", methods=["POST"])
def represent():
    input_args = request.get_json()

    if input_args is None:
        return {"message": "empty input set passed"}

    img_path = input_args.get("img")
    if img_path is None:
        return {"message": "you must pass img_path input"}

    model_name = input_args.get("model_name", "VGG-Face")
    detector_backend = input_args.get("detector_backend", "opencv")
    enforce_detection = input_args.get("enforce_detection", True)
    align = input_args.get("align", True)

    obj = service.represent(
        img_path=img_path,
        model_name=model_name,
        detector_backend=detector_backend,
        enforce_detection=enforce_detection,
        align=align,
    )

    return obj


@blueprint.route("/api/verify", methods=["POST"])
def verify():
    input_args = request.get_json()

    if input_args is None:
        return {"message": "empty input set passed"}

    img1_path = input_args.get("img_id1")
    img2_path = input_args.get("img_id2")

    if img1_path is None or img2_path is None:
        return {"message": "you must pass images input"}

    model_name = input_args.get("model_name", "VGG-Face")
    distance_metric = input_args.get("distance_metric", "cosine")

    verification = service.verify(
        img1_path=img1_path,
        img2_path=img2_path,
        model_name=model_name,
        distance_metric=distance_metric,
    )

    verification["verified"] = str(verification["verified"])
    return verification


@blueprint.route("/api/analyze", methods=["POST"])
def analyze():
    input_args = request.get_json()

    if input_args is None:
        return {"message": "empty input set passed"}

    img_path = input_args.get("img_id")
    if img_path is None:
        return {"message": "you must pass image input"}

    detector_backend = input_args.get("detector_backend", "opencv")
    actions = input_args.get("actions", ["age", "gender", "emotion", "race"])

    demographies = service.analyze(
        img_path=img_path,
        actions=actions,
        detector_backend=detector_backend,
    )

    return demographies
