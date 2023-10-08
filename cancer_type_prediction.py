# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

# Data Import
data = pd.read_csv('data_train.csv', sep='\t')

# Data Description
print("Dataset Description:")
print(data.info())

# Data Preparation
X = data.drop(columns=['Gene Description', 'Gene Accession Number', 'Target Variable'])
y = data['Target Variable']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# SVM Analysis
print("\nSVM Analysis:")
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)
svm_pred = svm.predict(X_test)
svm_accuracy = accuracy_score(y_test, svm_pred)
print("SVM Accuracy:", svm_accuracy)

# Random Forest Analysis
print("\nRandom Forest Analysis:")
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_pred)
print("Random Forest Accuracy:", rf_accuracy)

# Neural Network Analysis
print("\nNeural Network Analysis:")
parameters = {
    'hidden_layer_sizes': [(50, 50), (100,)],
    'activation': ['relu', 'tanh'],
    'solver': ['adam', 'sgd'],
}
mlp = MLPClassifier(max_iter=100)
grid_search = GridSearchCV(mlp, parameters, cv=3)
grid_search.fit(X_train, y_train)
mlp_pred = grid_search.predict(X_test)
mlp_accuracy = accuracy_score(y_test, mlp_pred)
print("Neural Network Accuracy:", mlp_accuracy)

# Model Comparison
print("\nModel Comparison:")
print("SVM Accuracy:", svm_accuracy)
print("Random Forest Accuracy:", rf_accuracy)
print("Neural Network Accuracy:", mlp_accuracy)

# Discussion and Conclusion
# Discuss strengths and weaknesses of SVM and Neural Networks
# Identify the most suitable model based on accuracy and efficiency
# Reflect on the broader implications and real-world applications
# Stress the importance of model selection and parameter tuning

# Saving the model with the best performance (choose the best model)
best_model = svm if svm_accuracy >= rf_accuracy and svm_accuracy >= mlp_accuracy else rf if rf_accuracy >= mlp_accuracy else grid_search

# Save the model to a file for future use
import joblib
joblib.dump(best_model, 'best_model.pkl')

