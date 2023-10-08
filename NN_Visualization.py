# Assuming you have a trained Neural Network model called 'nn_model'
# and test data 'X_test' and 'y_test'

# Confusion Matrix for Neural Network
plt.figure(figsize=(8, 6))
plt.title("Neural Network Confusion Matrix")
plot_confusion_matrix(nn_model, X_test, y_test, cmap=plt.cm.Blues)
plt.show()

# We have history object after model training called 'history'
# Plotting Training & Validation Loss for Neural Network
plt.figure(figsize=(8, 6))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Neural Network Training & Validation Loss')
plt.legend()
plt.show()
