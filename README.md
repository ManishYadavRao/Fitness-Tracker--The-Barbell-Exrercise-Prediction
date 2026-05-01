# 🏋️ Barbell Exercise Tracker

A **Machine Learning-powered fitness tracking system** that analyzes wristwatch sensor data to classify barbell exercises, count repetitions, and provide intelligent workout insights.

---

## 🚀 Overview

The **Barbell Exercise Tracker** is designed for strength training enthusiasts and fitness tech innovation. It uses **accelerometer and gyroscope data** from wearable devices to:

* Detect exercise type
* Count repetitions automatically
* Track performance over time
* Suggest weight adjustments

This project demonstrates the power of **machine learning + signal processing** in real-world fitness applications.

---

## 🎯 Project Objective

* Classify barbell exercises:

  * Bench Press
  * Deadlift
  * Overhead Press
  * Barbell Row
  * Squat

* Accurately count repetitions

* Provide data-driven performance insights

* Enable real-time fitness tracking

---

## ⚙️ How It Works

1. 📡 **Data Collection**

   * Sensor data collected using wrist-worn device (MetaMotion)

2. 🧹 **Data Processing**

   * Cleaning, normalization, and outlier handling

3. 🧠 **Feature Engineering**

   * Temporal & frequency-based features
   * PCA for dimensionality reduction

4. 🤖 **Machine Learning Models**

   * Random Forest
   * Decision Tree
   * KNN
   * Naive Bayes
   * Neural Networks

5. 🔁 **Repetition Counting**

   * Signal smoothing (Low-pass filter)
   * Peak detection algorithm

6. 📊 **Output**

   * Exercise prediction
   * Rep count
   * Performance insights

---

## ✨ Features

* ✅ **Rep Counting** – Automatic detection of repetitions
* 📊 **Performance Tracking** – Logs workout history
* 🏋️ **Exercise Classification** – Identifies exercise type
* 🤖 **ML Integration** – High-accuracy predictive models
* 📈 **Data Visualization** – Insightful graphs and trends
* 💡 **Weight Suggestions** – Smart recommendations

---

## 📊 Dataset

* **Sensors**: Accelerometer + Gyroscope
* **Axes**: X, Y, Z
* **Participants**: 5
* **Exercises**: 5 types
* **Data Type**: Time-series sensor data

---

## 🧪 Project Workflow

```bash
Data Collection → Data Cleaning → Feature Engineering → Modeling → Evaluation → Deployment
```

### Steps:

* Load and merge CSV sensor data
* Handle missing values & outliers (IQR, LOF)
* Apply PCA & Fourier Transform
* Train ML models
* Evaluate using accuracy & confusion matrix
* Implement repetition counting algorithm

---

## 🧰 Tech Stack

* **Language**: Python

* **Libraries**:

  * Pandas
  * NumPy
  * Scikit-learn
  * Matplotlib
  * Seaborn
  * TensorFlow / PyTorch

* **Tools**:

  * VS Code
  * Jupyter Notebook
  * Git & GitHub
  * Anaconda

---

## 📈 Results

* ✅ **Accuracy**: ~99% (Random Forest best model)
* 🔁 **Rep Counting Error (MAE)**: ~0.3 reps
* 📊 Strong differentiation between exercises using sensor patterns

---

## 📌 Business Value

* Improves **fitness tracking accuracy**
* Enables **personalized workout plans**
* Enhances **user engagement & retention**
* Supports **next-gen wearable fitness devices**

---

## 🚀 Future Enhancements

* 🔵 Real-time sensor integration (Bluetooth)
* 🧍 Personalized models per user
* ➕ More exercises support
* 📱 Mobile app integration

---

## 📂 Project Structure

```
├── data/
│   ├── raw/
│   ├── processed/
├── src/
│   ├── data/
│   ├── models/
│   ├── visualization/
├── notebooks/
├── app.py
├── train_model.py
└── README.md
```

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit a pull request.

---

## 📜 References

* Machine Learning for the Quantified Self – Mark Hoogendoorn
* Barbell Tracking Project – Dave Ebbelaar

---

## 💬 Final Note

> This project showcases how **AI + Fitness** can revolutionize workout tracking.
> Let’s build smarter fitness systems together! 💪🚀

---
