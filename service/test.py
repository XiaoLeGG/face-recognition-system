from deepface import DeepFace

faces = DeepFace.find(
    img_path="./temp_images/1687436982290.png",
    db_path="./db",
    enforce_detection=False,
)
print(faces)