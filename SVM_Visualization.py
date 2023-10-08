# We have a trained SVM model called 'svm_model'
# and test data 'X_test' and 'y_test'

# Confusion Matrix for SVM
plt.figure(figsize=(8, 6))
plt.title("SVM Confusion Matrix")
plot_confusion_matrix(svm_model, X_test, y_test, cmap=plt.cm.Blues)
plt.show()
