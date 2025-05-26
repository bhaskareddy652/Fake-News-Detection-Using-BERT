from flask import Flask, request, jsonify
import torch
from transformers import BertTokenizer, BertForSequenceClassification

app = Flask(__name__)

# Load model and tokenizer
model_path = "model"
bert_tokenizer = BertTokenizer.from_pretrained(model_path)
bert_model = BertForSequenceClassification.from_pretrained(model_path)

def predict_news(model, tokenizer, text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        print(f"Logits: {logits}")  # Debug: print raw logits
        prediction = torch.argmax(logits, dim=1).item()
        print(f"Predicted class index: {prediction}")  # Debug: print predicted class index
    return "Real News" if prediction == 1 else "Fake News"





@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    prediction = predict_news(bert_model, bert_tokenizer, text)
    return jsonify({"prediction": prediction})
from flask import render_template_string

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        text = request.form.get("text")
        prediction = predict_news(bert_model, bert_tokenizer, text)
    return render_template_string('''
        <h2>Fake News Detector</h2>
        <form method="POST">
            <textarea name="text" rows="5" cols="60" placeholder="Enter news article text..."></textarea><br><br>
            <input type="submit" value="Check">
        </form>
        {% if prediction %}
        <h3>Prediction: {{ prediction }}</h3>
        {% endif %}
    ''', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
