from sklearn.metrics import confusion_matrix

# Ground truth labels (actual)
y_true = [0, 1, 2, 3, 4, 5] 

# Predicted labels
y_pred = [0, 1, 2, 3, 3, 5]

# Create confusion matrix
conf_matrix = confusion_matrix(y_true, y_pred)

# Print confusion matrix
print("Confusion Matrix:")
print(conf_matrix)
