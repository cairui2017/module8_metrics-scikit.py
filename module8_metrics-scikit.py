
import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    # Ask for the number of points
    N = int(input("Enter the number of points N: "))
    
    # Initialize arrays to hold x and y values
    X = np.zeros(N, dtype=int)
    Y = np.zeros(N, dtype=int)
    
    # Read N points (x, y) from the user
    for i in range(N):
        X[i] = int(input(f"Enter x value for point {i+1}: "))
        Y[i] = int(input(f"Enter y value for point {i+1}: "))
        
    # Compute Precision and Recall
    precision = precision_score(X, Y)
    recall = recall_score(X, Y)
    
    # Output the results
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
    main()
