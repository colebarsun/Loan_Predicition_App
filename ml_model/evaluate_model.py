import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pickle

def evaluate_model(test_data_filepath, model_filepath):
    """
    Loads a trained model and evaluates its performance on test data.
    """
    # Load test data
    df_test = pd.read_csv(test_data_filepath)
    X_test = df_test[['interest_rate', 'loan_term', 'max_loan_amount']]
    y_test = df_test['loan_approved']  # Assuming 'loan_approved' is the label column

    # Load the trained model
    with open(model_filepath, 'rb') as file:
        model = pickle.load(file)

    # Make predictions
    y_pred = model.predict(X_test)
    
    # Generate evaluation metrics
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy * 100:.2f}%")

    # Additional metrics if needed
    # You could include ROC AUC, Precision-Recall, etc.
    # roc_auc = roc_auc_score(y_test, y_pred)
    # print(f"ROC AUC: {roc_auc:.2f}")

if __name__ == "__main__":
    evaluate_model('data/test_loan_data.csv', 'ml_model/model.pkl')
