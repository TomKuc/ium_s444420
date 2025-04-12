from sacred import Experiment
from sacred.observers import FileStorageObserver
from datasets import load_dataset, DatasetDict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import joblib

ex = Experiment("ag_news_classifier")
ex.observers.append(FileStorageObserver.create('sacred_runs'))

@ex.config
def config():
    max_features = 5000
    hidden_units = 100
    max_iter = 10
    random_state = 42
    model_output = "ag_model.joblib"

@ex.capture
def load_data(_run):
    dataset = load_dataset('ag_news')
    _run.open_resource("dataset_info.txt", "w").write(str(dataset))
    split = dataset["train"].train_test_split(test_size=0.2, seed=42)
    dataset = DatasetDict({
        "train": split["train"],
        "dev": split["test"],
        "test": dataset["test"]
    })
    return dataset

@ex.automain
def train(max_features, hidden_units, max_iter, random_state, model_output, _run):
    dataset = load_data()

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
    print(acc)
    _run.log_scalar("accuracy", acc)
    _run.log_scalar("test_metric", 123.45)

    joblib.dump(pipeline, model_output)
    _run.add_artifact(model_output)
