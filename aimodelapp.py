# app.py
from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import traceback

app = Flask(__name__)

# load pipeline once at startup
MODEL_PATH = "breast_cancer_pipeline (1).joblib"
pipeline = joblib.load(MODEL_PATH)

# (Optional) feature names from the dataset (30 numeric features)
FEATURE_NAMES = [
 "radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean",
 "compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean",
 "radius_se","texture_se","perimeter_se","area_se","smoothness_se",
 "compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se",
 "radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst",
 "compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"
]

@app.route("/")
def index():
    return render_template("index.html", features=FEATURE_NAMES)

def parse_features_from_request(req_json):
    """
    Accepts either:
    - {"features": [f1, f2, ..., f30]} (list order must match FEATURE_NAMES)
    - {"feature_dict": {"radius_mean": val, ...}} (dict with named features)
    - or a CSV string under "csv": "v1,v2,...,v30"
    Returns numpy array shape (1,30)
    """
    if not req_json:
        raise ValueError("Empty JSON")

    if "features" in req_json:
        feats = req_json["features"]
        arr = np.array(feats, dtype=float).reshape(1, -1)
        return arr

    if "feature_dict" in req_json:
        fd = req_json["feature_dict"]
        arr = [float(fd[name]) for name in FEATURE_NAMES]
        return np.array(arr, dtype=float).reshape(1, -1)

    if "csv" in req_json:
        vals = [float(x.strip()) for x in req_json["csv"].split(",")]
        return np.array(vals, dtype=float).reshape(1, -1)

    raise ValueError("No recognizable features found. Provide 'features' list, 'feature_dict', or 'csv'.")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)
        x = parse_features_from_request(data)   # your helper returns np.array shape (1,30)
        # validate shape
        if x.shape != (1, 30):
            return jsonify({"error": f"Invalid input shape {x.shape}, expected (1,30)"}), 400
        # predict
        pred = pipeline.predict(x)[0]
        proba = pipeline.predict_proba(x).tolist()[0] if hasattr(pipeline, "predict_proba") else None
        label_map = {0: "Benign", 1: "Malignant"}
        return jsonify({"prediction_label": label_map.get(int(pred), str(int(pred))), "prediction_value": int(pred), "probabilities": proba})
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": "Internal server error: "+str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

