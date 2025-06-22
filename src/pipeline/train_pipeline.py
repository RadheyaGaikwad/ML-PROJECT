import os
import sys
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression

from src.exception import CustomException

def train():
    try:
        df = pd.read_csv("Notebook/data/stud.csv")  # adjust path if needed

        X = df.drop("math score", axis=1)
        y = df["math score"]

        num_cols = ["reading score", "writing score"]
        cat_cols = [
            "gender",
            "race/ethnicity",
            "parental level of education",
            "lunch",
            "test preparation course"
        ]

        num_pipeline = Pipeline([("scaler", StandardScaler())])
        cat_pipeline = Pipeline([("onehot", OneHotEncoder(handle_unknown="ignore"))])

        preprocessor = ColumnTransformer(transformers=[
            ("num", num_pipeline, num_cols),
            ("cat", cat_pipeline, cat_cols)
        ])

        pipeline = Pipeline([
            ("preprocessor", preprocessor),
            ("regressor", LinearRegression())
        ])

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        pipeline.fit(X_train, y_train)

        os.makedirs("artifacts", exist_ok=True)
        joblib.dump(pipeline.named_steps["regressor"], "artifacts/model.pkl")
        joblib.dump(pipeline.named_steps["preprocessor"], "artifacts/preprocessor.pkl")

        print("✅ Training complete. Artifacts saved.")

    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    train()
