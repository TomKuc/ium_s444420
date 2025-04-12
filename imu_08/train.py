import mlflow
from datasets import load_dataset, DatasetDict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import joblib

max_features = 5000
hidden_units = 100
max_iter = 10
random_state = 42
model_output = "ag_news_model.joblib"

with mlflow.start_run():

    mlflow.log_param("max_features", max_features)
    mlflow.log_param("hidden_units", hidden_units)
    mlflow.log_param("max_iter", max_iter)

    dataset = load_dataset('ag_news')
    split = dataset["train"].train_test_split(test_size=0.2, seed=42)
    dataset = DatasetDict({
        "train": split["train"],
        "dev": split["test"],
        "test": dataset["test"]
    })

    X_train = dataset["train"]["text"]
    y_train = dataset["train"]["label"]
    X_dev = dataset["dev"]["text"]
    y_dev = dataset["dev"]["label"]

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(max_features=max_features)),
        ("mlp", MLPClassifier(hidden_layer_sizes=(hidden_units,),
                              max_iter=max_iter,
                              random_state=random_state))
    ])

    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_dev)
    acc = accuracy_score(y_dev, y_pred)
    print("Accuracy:", acc)
    mlflow.log_metric("accuracy", acc)

    joblib.dump(pipeline, model_output)
    mlflow.log_artifact(model_output)
