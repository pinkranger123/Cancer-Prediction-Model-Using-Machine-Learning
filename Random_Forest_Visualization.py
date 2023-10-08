import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import plot_confusion_matrix

# Assuming you have a trained Random Forest model called 'rf_model'
# and test data 'X_test' and 'y_test'

# Confusion Matrix for Random Forest
plt.figure(figsize=(8, 6))
plt.title("Random Forest Confusion Matrix")
plot_confusion_matrix(rf_model, X_test, y_test, cmap=plt.cm.Blues)
plt.show()

# Feature Importance for Random Forest
plt.figure(figsize=(10, 8))
sns.barplot(x=rf_model.feature_importances_, y=X_train.columns)
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Random Forest - Feature Importance")
plt.show()
