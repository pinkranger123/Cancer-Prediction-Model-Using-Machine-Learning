from sklearn.ensemble import GradientBoostingClassifier

# Assuming you have train data 'X_train' and 'y_train'
# Assuming you have test data 'X_test' and 'y_test'

# Initialize Gradient Boosting Classifier
gb_model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)

# Train the model
gb_model.fit(X_train, y_train)

# Evaluate the model
accuracy_gb = gb_model.score(X_test, y_test)
print("Gradient Boosting Accuracy:", accuracy_gb)

# Confusion Matrix for Gradient Boosting
plt.figure(figsize=(8, 6))
plt.title("Gradient Boosting Confusion Matrix")
plot_confusion_matrix(gb_model, X_test, y_test, cmap=plt.cm.Blues)
plt.show()

# Feature Importance for Gradient Boosting
plt.figure(figsize=(10, 8))
sns.barplot(x=gb_model.feature_importances_, y=X_train.columns)
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Gradient Boosting - Feature Importance")
plt.show()
