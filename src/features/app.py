

# # # import pandas as pd

# # # df = pd.read_pickle("C:/Users/manis/Desktop/Fitness Tracker/data/interim/01_data_processed.pkl")
# # # df.to_csv("C:/Users/manis/Desktop/Fitness Tracker/data/processed/workout_data.csv", index=False)

# # # app.py — Streamlit App for Barbell Repetition Prediction
# # import DataTransformation
# # import streamlit as st
# # import pandas as pd
# # import numpy as np
# # import matplotlib.pyplot as plt
# # from sklearn.metrics import mean_absolute_error
# # import joblib
# # from scipy.signal import argrelextrema
# # from streamlit_lottie import st_lottie
# # import requests
# # from DataTransformation import LowPassFilter


# # # ----------------- LOTTIE LOADER -------------------
# # def load_lottieurl(url: str):
# #     r = requests.get(url)
# #     if r.status_code != 200:
# #         return None
# #     return r.json()

# # # ----------------- LOWPASS FILTER CLASS -------------
# # from DataTransformation import LowPassFilter
# # low_pass = LowPassFilter()

# # # ----------------- STREAMLIT CONFIG ------------------
# # st.set_page_config(page_title="Barbell Rep Tracker", page_icon="🏋️", layout="centered")
# # st.title("🏋️ Barbell Exercise Rep Tracker")

# # animation = load_lottieurl("https://lottie.host/62913c06-adbe-4f4c-83c1-8c9b3c10dea9/VIXwGjBPk.json")
# # if animation:
# #     st_lottie(animation, height=250, key="intro")

# # uploaded_file = st.file_uploader("C://Users//manis//Desktop//Fitness Tracker//data//processed//workout_data.csv")
# # if uploaded_file:
# #     df = pd.read_csv("C://Users//manis//Desktop//Fitness Tracker//data//processed//workout_data.csv")

# #     if not {"set", "label", "category", "acc_x", "acc_y", "acc_z", "gyr_x", "gyr_y", "gyr_z"}.issubset(df.columns):
# #         st.error("Your file must include required sensor and label columns.")
# #     else:
# #         # Add acc_r and gyr_r
# #         acc_r = df["acc_x"] ** 2 + df["acc_y"] ** 2 + df["acc_z"] ** 2
# #         gyr_r = df["gyr_x"] ** 2 + df["gyr_y"] ** 2 + df["gyr_z"] ** 2
# #         df["acc_r"] = np.sqrt(acc_r)
# #         df["gyr_r"] = np.sqrt(gyr_r)

# #         def count_reps(dataset, cutoff=0.4, order=10, column="acc_r"):
# #             fs = 1000 / 200
# #             data = low_pass.low_pass_filter(dataset, col=column, sampling_frequency=fs, cutoff_frequency=cutoff, order=order)
# #             indexes = argrelextrema(data[column + "_lowpass"].values, np.greater)
# #             peaks = data.iloc[indexes]
# #             return len(peaks)

# #         df = df[df["label"] != "rest"]
# #         df["reps"] = df["category"].apply(lambda x: 5 if x == "heavy" else 10)
# #         rep_df = df.groupby(["label", "category", "set"])["reps"].max().reset_index()
# #         rep_df["reps_pred"] = 0

# #         for s in df["set"].unique():
# #             subset = df[df["set"] == s]
# #             column = "acc_r"
# #             cutoff = 0.4

# #             if subset["label"].iloc[0] == "squat":
# #                 cutoff = 0.35
# #             if subset["label"].iloc[0] == "row":
# #                 cutoff = 0.65
# #                 column = "gyr_x"
# #             if subset["label"].iloc[0] == "ohp":
# #                 cutoff = 0.35

# #             reps = count_reps(subset, cutoff=cutoff, column=column)
# #             rep_df.loc[rep_df["set"] == s, "reps_pred"] = reps

# #         st.success("Prediction completed!")
# #         st.write(rep_df)

# #         error = mean_absolute_error(rep_df["reps"], rep_df["reps_pred"]).round(2)
# #         st.metric(label="Mean Absolute Error", value=error)

# #         st.subheader("Reps Prediction per Exercise")
# #         fig, ax = plt.subplots()
# #         rep_df.groupby(["label", "category"])[["reps", "reps_pred"]].mean().plot.bar(ax=ax)
# #         st.pyplot(fig)

# # else:
# #     st.info("Please upload a valid CSV file containing workout data to begin.")











# # import streamlit as st
# # import requests
# # from streamlit_lottie import st_lottie
# # import numpy as np
# # import joblib

# # # Load model
# # model = joblib.load("C://Users//manis//Desktop//Fitness Tracker//data\interim//01_data_processed.pkl")

# # # Feature list
# # feature_columns = [
# #     ['acc_x_freq_1.071_Hz_ws_14', 'acc_z_freq_0.714_Hz_ws_14', 'gyr_y_freq_0.714_Hz_ws_14', 'acc_x_freq_1.429_Hz_ws_14', 'acc_z_freq_2.5_Hz_ws_14', 'acc_r_freq_1.429_Hz_ws_14', 'gyr_y_freq_1.429_Hz_ws_14', 'gyr_y_freq_weighted', 'acc_y_freq_2.5_Hz_ws_14', 'gyr_r_freq_weighted', 'acc_y_temp_std_ws_5', 'gyr_y_freq_2.5_Hz_ws_14', 'acc_z_freq_0.357_Hz_ws_14', 'acc_y_freq_weighted', 'acc_r_freq_0.357_Hz_ws_14', 'gyr_y_freq_2.143_Hz_ws_14', 'gyr_x_max_freq', 'gyr_x_freq_1.071_Hz_ws_14', 'gyr_y_pse', 'acc_x_freq_1.786_Hz_ws_14', 'acc_x_temp_mean_ws_5', 'acc_r_freq_2.5_Hz_ws_14', 'gyr_y_freq_0.0_Hz_ws_14', 'gyr_z_freq_1.786_Hz_ws_14', 'gyr_r', 'acc_y_freq_0.357_Hz_ws_14', 'acc_x_temp_std_ws_5', 'acc_y_freq_0.0_Hz_ws_14', 'gyr_r_temp_mean_ws_5', 'acc_x_freq_0.0_Hz_ws_14', 'acc_z', 'acc_x_max_freq', 'acc_x_freq_2.143_Hz_ws_14', 'gyr_x_freq_weighted', 'acc_r_freq_weighted', 'acc_z_freq_1.786_Hz_ws_14', 'gyr_x_freq_0.714_Hz_ws_14', 'gyr_x_freq_1.786_Hz_ws_14', 'acc_r_freq_0.714_Hz_ws_14', 'acc_y', 'acc_r', 'acc_z_temp_mean_ws_5', 'gyr_z_temp_std_ws_5', 'gyr_r_freq_1.786_Hz_ws_14', 'acc_z_freq_0.0_Hz_ws_14', 'acc_x_freq_0.357_Hz_ws_14', 'gyr_y', 'gyr_x_temp_std_ws_5', 'acc_y_pse', 'acc_y_freq_1.429_Hz_ws_14', 'acc_r_freq_1.786_Hz_ws_14', 'gyr_r_freq_1.071_Hz_ws_14', 'acc_z_freq_weighted', 'gyr_x', 'gyr_y_freq_1.071_Hz_ws_14', 'acc_y_max_freq', 'gyr_r_freq_2.5_Hz_ws_14', 'gyr_z_freq_0.357_Hz_ws_14', 'pca_1', 'gyr_r_max_freq', 'gyr_r_freq_2.143_Hz_ws_14', 'acc_x_freq_0.714_Hz_ws_14', 'gyr_y_freq_1.786_Hz_ws_14', 'acc_y_freq_1.786_Hz_ws_14', 'acc_y_freq_2.143_Hz_ws_14', 'gyr_x_temp_mean_ws_5', 'acc_r_temp_mean_ws_5', 'gyr_r_freq_1.429_Hz_ws_14', 'gyr_y_temp_std_ws_5', 'gyr_x_freq_1.429_Hz_ws_14', 'acc_z_freq_1.429_Hz_ws_14', 'gyr_y_freq_0.357_Hz_ws_14', 'acc_r_max_freq', 'acc_r_freq_0.0_Hz_ws_14', 'acc_r_freq_2.143_Hz_ws_14', 'gyr_r_freq_0.0_Hz_ws_14', 'gyr_z_freq_weighted', 'acc_z_freq_1.071_Hz_ws_14', 'acc_r_pse', 'gyr_z_freq_1.429_Hz_ws_14', 'acc_z_freq_2.143_Hz_ws_14', 'gyr_x_freq_2.143_Hz_ws_14', 'gyr_z_freq_2.5_Hz_ws_14', 'gyr_r_freq_0.714_Hz_ws_14', 'gyr_r_pse', 'acc_x_freq_weighted', 'acc_y_freq_0.714_Hz_ws_14', 'acc_z_temp_std_ws_5', 'pca_3', 'gyr_z_max_freq', 'acc_z_max_freq', 'gyr_z_freq_2.143_Hz_ws_14', 'gyr_x_freq_0.357_Hz_ws_14', 'acc_r_temp_std_ws_5', 'acc_x', 'cluster', 'gyr_z_freq_0.0_Hz_ws_14', 'gyr_y_temp_mean_ws_5', 'gyr_z_pse', 'pca_2', 'acc_r_freq_1.071_Hz_ws_14', 'gyr_x_freq_0.0_Hz_ws_14', 'gyr_z', 'acc_y_temp_mean_ws_5', 'gyr_r_temp_std_ws_5', 'acc_z_pse', 'gyr_x_pse', 'gyr_z_temp_mean_ws_5', 'acc_x_pse', 'gyr_y_max_freq', 'acc_y_freq_1.071_Hz_ws_14', 'gyr_z_freq_0.714_Hz_ws_14', 'acc_x_freq_2.5_Hz_ws_14', 'gyr_r_freq_0.357_Hz_ws_14', 'gyr_x_freq_2.5_Hz_ws_14', 'gyr_z_freq_1.071_Hz_ws_14']

# # ]

# # # Prediction function
# # def predict_workout_type(features):
# #     X = np.array(features).reshape(1, -1)
# #     return model.predict(X)[0]

# # # Lottie loader
# # def load_lottieurl(url: str):
# #     r = requests.get(url)
# #     if r.status_code != 200:
# #         return None
# #     return r.json()

# # # Page config
# # st.set_page_config(page_title="Workout type prediction", page_icon="💪", layout="centered")

# # # CSS
# # st.markdown("""
# # <style>
# # body {
# #     background-color: #000;
# #     color: #fff;
# #     font-family: Raleway, sans-serif;
# # }
# # .main-header {
# #     font-size: 34px;
# #     text-align: center;
# #     color: #3E4C59;
# #     background-color: #9CA3AF;
# #     padding: 15px;
# #     border-radius: 8px;
# #     margin-bottom: 20px;
# # }
# # .instructions {
# #     font-size: 18px;
# #     margin-top: 20px;
# #     color: #6B7280;
# # }
# # .typewriter-text {
# #     font-size: 30px;
# #     font-weight: bold;
# #     animation: blink 1s steps(5, start) infinite;
# #     text-transform: uppercase;
# # }
# # @keyframes blink {
# #   to {
# #     visibility: hidden;
# #   }
# # }
# # </style>
# # """, unsafe_allow_html=True)

# # # Header
# # st.markdown('<div class="main-header"> 💪 Workout Type Prediction </div>', unsafe_allow_html=True)

# # # Load animations
# # initial_lottie = load_lottieurl("https://lottie.host/62913c06-adbe-4f4c-83c1-8c9b3c10dea9/VIXwGjBPk.json")
# # result_lottie = load_lottieurl("https://lottie.host/63337eda-24a2-4c2e-b3e4-67872c5fd855/hnh05v5t4N.json")
# # new_lottie = load_lottieurl("https://lottie.host/Bd982cda-7c49-4b1e-87c7-959b1a0b6f9a/E100UceyHQ.json")

# # if initial_lottie:
# #     st_lottie(initial_lottie, speed=1, height=300, key="initial")

# # # Instructions
# # st.markdown("<p class='instructions'>Adjust the sliders to set feature values and predict your workout type:</p>", unsafe_allow_html=True)

# # # Additional animation
# # if new_lottie:
# #     st_lottie(new_lottie, speed=1, height=300, key="mid")

# # # Input sliders
# # with st.expander("Adjust Feature Values"):
# #     col1, col2 = st.columns(2)
# #     for i, feature in enumerate(feature_columns):
# #         col = col1 if i < len(feature_columns) // 2 else col2
# #         col.slider(
# #             feature,
# #             min_value=-20.0,
# #             max_value=20.0,
# #             step=0.01,
# #             value=0.0,
# #             key=f"input_{feature}"
# #         )

# # # Prediction block
# # result_animation_placeholder = st.empty()

# # if st.button("Predict"):
# #     feature_values = [st.session_state[f"input_{feature}"] for feature in feature_columns]
# #     prediction = predict_workout_type(feature_values)

# #     workout_type_colors = {
# #         "bench": "#A5B4FC",
# #         "deadlift": "#FDBA74",
# #         "OHP": "#FCA5A5",
# #         "rest": "#D1D5DB",
# #         "row": "#6EE7B7",
# #         "squat": "#93C5FD",
# #     }
# #     prediction_color = workout_type_colors.get(prediction, "#6B7280")

# #     st.markdown(
# #         f"""
# #         <div class="typewriter-container">
# #             <div class="typewriter-text">
# #                 Predicted Workout Type: <span style="color: {prediction_color};">{prediction.upper()}</span>
# #             </div>
# #         </div>
# #         """, unsafe_allow_html=True
# #     )

# #     if result_lottie:
# #         result_animation_placeholder.lottie(
# #             result_lottie,
# #             speed=1,
# #             loop=True,
# #             quality="low",
# #             height=300,
# #             key="result_animation"
# #         )





# import streamlit as st
# import requests
# from streamlit_lottie import st_lottie
# import numpy as np
# import joblib

# # ------------------------- LOAD MODEL -------------------------
# model = joblib.load("C://Users//manis//Desktop//Fitness Tracker//models//model.pkl")

# # ------------------------- FEATURES ---------------------------
# feature_columns = [
#    'pca_1',
#   'duration',
#   'acc_x_freq_0.0_Hz_ws_14',
#   'acc_z_freq_0.0_Hz_ws_14',
#   'acc_y_temp_mean_ws_5',
#   'acc_x_temp_mean_ws_5',
#   'gyr_x_freq_1.071_Hz_ws_14',
#   'gyr_z_freq_0.0_Hz_ws_14',
#   'gyr_y_freq_0.0_Hz_ws_14',
#   'acc_y_freq_1.429_Hz_ws_14']

# # ------------------------ PREDICT FUNCTION --------------------
# def predict_workout_type(features):
#     X = np.array(features).reshape(1, -1)
#     return model.predict(X)[0]

# # ------------------------- LOAD ANIMATIONS --------------------
# def load_lottieurl(url: str):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# # ------------------------ PAGE CONFIG --------------------------
# st.set_page_config(page_title="Workout Predictor", page_icon="💪", layout="centered")
# st.markdown('<h1 style="text-align:center; color:#6EE7B7;">Barbell Workout Type Predictor</h1>', unsafe_allow_html=True)

# # Load Lottie animations
# intro_anim = load_lottieurl("https://lottie.host/62913c06-adbe-4f4c-83c1-8c9b3c10dea9/VIXwGjBPk.json")
# result_anim = load_lottieurl("https://lottie.host/63337eda-24a2-4c2e-b3e4-67872c5fd855/hnh05v5t4N.json")

# if intro_anim:
#     st_lottie(intro_anim, height=250, key="intro")

# st.markdown("<p style='color:gray;'>Use the sliders below to set the sensor-based feature values. Click predict to know which workout type it is!</p>", unsafe_allow_html=True)

# # -------------------------- SLIDERS ----------------------------
# with st.expander("Adjust Sensor Feature Values"):
#     col1, col2 = st.columns(2)
#     for i, feature in enumerate(feature_columns):
#         col = col1 if i < len(feature_columns) // 2 else col2
#         col.slider(
#             feature,
#             min_value=-20.0,
#             max_value=20.0,
#             value=0.0,
#             step=0.01,
#             key=f"input_{feature}"
#         )

# # ----------------------- PREDICTION ----------------------------
# if st.button("Predict Workout Type"):
#     feature_values = [st.session_state[f"input_{f}"] for f in feature_columns]
#     prediction = predict_workout_type(feature_values)

#     color_map = {
#         "bench": "#A5B4FC",
#         "deadlift": "#FDBA74",
#         "OHP": "#FCA5A5",
#         "rest": "#D1D5DB",
#         "row": "#6EE7B7",
#         "squat": "#93C5FD",
#     }
#     color = color_map.get(prediction, "#6B7280")

#     st.markdown(f"""
#     <div style='text-align:center; margin-top:30px;'>
#         <h2 style='color:{color};'>Prediction: {prediction.upper()}</h2>
#     </div>
#     """, unsafe_allow_html=True)

#     if result_anim:
#         st_lottie(result_anim, height=250, key="result")

# # ------------------------ FOOTER -------------------------------
# st.markdown("<hr><p style='text-align:center;font-size:14px;'>Developed for Barbell Exercise Fitness Tracking 🏋️‍♂️</p>", unsafe_allow_html=True)









import streamlit as st
import numpy as np
import joblib
from streamlit_lottie import st_lottie
import requests

# ---------------- Load model ----------------
model = joblib.load("../../src/random_forest.pickle")

# ---------------- Feature columns ----------------
selected_features = [
    "pca_1",
    "duration",
    "acc_z_freq_0.0_Hz_ws_14",
    "acc_y_temp_mean_ws_5",
    "gyr_y_freq_1.071_Hz_ws_14",
    "acc_z_freq_weighted",
    "acc_y_freq_0.357_Hz_ws_14",
    "acc_x_freq_2.5_Hz_ws_14",
    "gyr_x_freq_0.357_Hz_ws_14",
    "acc_x_freq_1.071_Hz_ws_14"
]

# ---------------- Lottie loader ----------------
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---------------- Page setup ----------------
st.set_page_config(page_title="🏋️ Workout Type Predictor", layout="centered")

st.markdown("""
<style>
body {
    background-color: #f8f9fa;
    color: #212529;
    font-family: 'Segoe UI', sans-serif;
}
h1 {
    color: #343a40;
    text-align: center;
}
.slider-label {
    font-weight: 600;
    margin-top: 10px;
}
.prediction-text {
    font-size: 26px;
    font-weight: bold;
    margin-top: 20px;
    color: #1d3557;
}
</style>
""", unsafe_allow_html=True)

st.title("🏋️ Barbell Exercise Classifier")
st.markdown("### Predict workout type from wearable motion data")

lottie_url = "https://lottie.host/62913c06-adbe-4f4c-83c1-8c9b3c10dea9/VIXwGjBPk.json"
lottie_json = load_lottieurl(lottie_url)
if lottie_json:
    st_lottie(lottie_json, height=200)

# ---------------- Sliders for feature input ----------------
st.markdown("#### Adjust the values below to simulate sensor inputs:")

cols = st.columns(2)
input_values = []
for i, feature in enumerate(selected_features):
    col = cols[i % 2]
    value = col.slider(f"{feature}", min_value=-20.0, max_value=20.0, value=0.0, step=0.01)
    input_values.append(value)

# ---------------- Prediction ----------------
if st.button("🔍 Predict Workout Type"):
    X = np.array(input_values).reshape(1, -1)
    prediction = model.predict(X)[0]

    workout_colors = {
        "squat": "#6A5ACD",
        "bench": "#FF6B6B",
        "deadlift": "#20B2AA",
        "row": "#FFA07A",
        "ohp": "#87CEFA",
        "rest": "#B0BEC5"
    }

    color = workout_colors.get(prediction.lower(), "#333")

    st.markdown(f"""
        <div class="prediction-text">
            🎯 **Predicted Workout:** <span style="color:{color}">{prediction.upper()}</span>
        </div>
    """, unsafe_allow_html=True)
