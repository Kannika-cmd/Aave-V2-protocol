import pandas as pd
import json

# Load the JSON file
with open('user-wallet-transactions.json') as f:
    transactions = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(transactions)

# Feature Engineering
def calculate_scores(df):
    scores = {}
    for wallet in df['userWallet'].unique():
        wallet_data = df[df['userWallet'] == wallet]
        
        # Calculate features
        transaction_count = len(wallet_data)
        deposit_count = len(wallet_data[wallet_data['action'] == 'deposit'])
        borrow_count = len(wallet_data[wallet_data['action'] == 'borrow'])
        repayment_count = len(wallet_data[wallet_data['action'] == 'repay'])
        liquidation_count = len(wallet_data[wallet_data['action'] == 'liquidationcall'])
        
        # Example score calculation logic
        score = (transaction_count * 0.1 + deposit_count * 0.3 + 
                 borrow_count * 0.2 + repayment_count * 0.3 - 
                 liquidation_count * 0.5)
        
        # Normalize score to be between 0 and 1000
        score = max(0, min(1000, score))
        
        scores[wallet] = score
    
    return scores

# Generate wallet scores
wallet_scores = calculate_scores(df)

# Output scores
print(wallet_scores)
