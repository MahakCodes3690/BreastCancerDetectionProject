# save as debug_load.py and run: python debug_load.py
import joblib, sklearn, numpy, sys, traceback

print("Python:", sys.version)
print("scikit-learn:", sklearn.__version__)
print("joblib:", joblib.__version__)
print("numpy:", numpy.__version__)

try:
    model = joblib.load("breast_cancer_pipeline.joblib")
    print("Loaded OK")
except Exception as e:
    print("ERROR loading model:")
    traceback.print_exc()