from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Charger le modèle
model = load_model('cell_classification_model.keras')

# Créer l'application Flask
app = Flask(__name__)


# Page principale avec formulaire d'upload
@app.route('/')
def home():
    return render_template('index.html')


# Endpoint pour effectuer la prédiction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']

    if file.filename == '':
        return "No file selected", 400

    # Prétraiter l'image
    img = load_img(file, target_size=(128, 128))  # Ajustez la taille selon votre modèle
    img_array = img_to_array(img) / 255.0  # Normaliser
    img_array = np.expand_dims(img_array, axis=0)  # Ajouter une dimension batch

    # Prédire
    predictions = model.predict(img_array)
    class_idx = np.argmax(predictions, axis=1)[0]  # Obtenir l'indice de classe
    class_names = ['Non infecté', 'Infecté']
    result = class_names[class_idx]

    return jsonify({'prediction': result})


# Lancer l'application
if __name__ == '__main__':
    app.run(debug=True)
