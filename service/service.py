from deepface import DeepFace
import os

representations_file = 'db/representations_vgg_face.pkl'
model_name = 'VGG-Face'
detector_backend = 'opencv'
needed_update = False

def update_database():
    global needed_update
    if (needed_update == False):
        return
    if (os.path.exists(representations_file) == True):
        os.remove(representations_file)
    needed_update = False
    DeepFace.find(
        img_path='temp_images/update_img.png',
        model_name=model_name,
        detector_backend=detector_backend,
        enforce_detection=False,
        align=True,
        db_path="db",
    )

def detect_face(img_path, detector_backend):
    try:
        detected_faces = DeepFace.extract_faces(
            img_path=img_path,
            detector_backend=detector_backend,
            enforce_detection=False
        )
        return detected_faces[0]['confidence'] > 0.1
    except Exception as e:
        return False

def recognize(img_path):
    detected_faces = DeepFace.find(
        img_path='./temp_images/' + img_path,
        model_name=model_name,
        detector_backend=detector_backend,
        enforce_detection=False,
        align=True,
        db_path="db",
    )
    return detected_faces

def represent(img_path):
    result = {}
    embedding_objs = DeepFace.represent(
        img_path=img_path,
        model_name=model_name,
        detector_backend=detector_backend,
        enforce_detection=False,
        align=True,
    )
    result["results"] = embedding_objs
    return result


def verify(
    img1_path, img2_path, model_name, distance_metric
):
    obj = DeepFace.verify(
        img1_path='./temp_images/' + img1_path,
        img2_path='./temp_images/' + img2_path,
        model_name=model_name,
        detector_backend=detector_backend,
        distance_metric=distance_metric,
        align=True,
        enforce_detection=False,
    )
    return obj


def analyze(img_path, actions, detector_backend):
    result = {}
    demographies = DeepFace.analyze(
        img_path='./temp_images/' + img_path,
        actions=actions,
        detector_backend=detector_backend,
        enforce_detection=False,
        align=True,
    )
    result["results"] = demographies
    return result
