# Fake News Detection Using BERT(Bidirectional Encoder Representationas from Transformers)

This project demonstrates a fake news detection system built with BERT fine-tuning and deployed using Flask.

# Project Overview

- Fine-tuned a BERT model for classifying news articles as Real or Fake.
- Achieved high accuracy and F1 scores on test data.
- Developed a Flask web app and REST API for interactive predictions.

# Dataset

The dataset used in this project includes:
- real.csv: Contains 21,417 real news articles.
- fake.csv: Contains 23,481 fake news articles.

# How to Run

- Clone this repository.
- Download and place the pre-trained model in the model/ directory.
- Install dependencies: pip install -r requirements.txt
- Run the Flask app: python app.py

# Challenges Faced
- Ensuring consistent label mapping between dataset, training, and inference.
- Managing overfitting during training despite high accuracy.
- Debugging unexpected classification outputs and refining preprocessing.
- Efficiently deploying a transformer-based model for quick predictions.

# Results
- Metric	                                Value
- Validation Accuracy	                  ~99.9%
- Test Accuracy	                        ~99.9%
- Precision, Recall, F1-Score	           ~1.0
# 📈 Future Improvements
- Try alternative models: DistilBERT,Long Short-Term Memory (LSTM), Convolutional Neural Network (CNN), Bidirectional LSTM, ResNet, COBRA, Gated Recurrent Unit (GRU)
- Improve dataset balance and coverage (different regions, topics).
- Add streamlit or Gradio interface for better UX.
- Integrate LIME/SHAP for model explainability.
# 🧠 Skills Practiced
- NLP with Transformers
- Deep Learning (fine-tuning pre-trained models)
- Model evaluation and deployment
- Flask API & Web Development
- Debugging real-world ML issues
