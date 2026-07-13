from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# Create model
model = KNeighborsClassifier()

# Train model
model.fit(X_train, y_train)

# Predict
prediction = model.predict(X_test)

# Show accuracy
print("Accuracy:", accuracy_score(y_test, prediction))

# Predict one flower
sample = [[5.1, 3.5, 1.4, 0.2]]
result = model.predict(sample)

print("Predicted Class:", iris.target_names[result][0])