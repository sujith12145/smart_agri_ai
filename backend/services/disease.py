import tensorflow as tf
from PIL import Image
import numpy as np

model = tf.keras.models.load_model("models/disease_model.h5")

def predict_disease(file):
    img = Image.open(file.file).resize((224,224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)
    classes = ["Healthy", "Early Blight", "Late Blight"]

    return classes[np.argmax(pred)]