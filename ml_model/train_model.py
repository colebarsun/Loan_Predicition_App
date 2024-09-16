import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pickle

def preprocess_data(filepath):
    """
    Loads and preprocesses loan data
    """
    df = pd.read_csv(filepath)
    df = df.dropna()
    df['interest_rate'] = df['interest_rate'].str.replace('%', '').astype(float)
    # Additional feature engineering...
    return df

def train_model(df):
    """
    Train RandomForestClassifier model with hyperparameter tuning
    """
    X = df[['interest_rate', 'loan_term', 'max_loan_amount']]
    y = df['loan_approved']  # Target variable
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [10, 20, 30]
    }
    rf = RandomForestClassifier(random_state=42)
    grid_search = GridSearchCV(rf, param_grid, cv=3, scoring='accuracy')
    grid_search.fit(X_train, y_train)

    print("Best parameters found: ", grid_search.best_params_)

    y_pred = grid_search.predict(X_test)
    print(classification_report(y_test, y_pred))

    with open('ml_model/model.pkl', 'wb') as f:
        pickle.dump(grid_search.best_estimator_, f)

if __name__ == "__main__":
    df = preprocess_data('data/loan_data.csv')
    train_model(df)
