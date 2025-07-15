# Wallet Score Analysis
## Overview
An analysis of the wallet scores produced using the Aave V2 transaction data is presented in this document. Score distribution and behavioral insights derived from the scoring ranges are included in the analysis.

## Score Distribution
The wallet scores were categorized into ranges for analysis:
- 0-100
- 101-200
- 201-300
- 301-400
- 401-500
- 501-600
- 601-700
- 701-800
- 801-900
- 901-1000

### Score Distribution Graph
```python
import matplotlib.pyplot as plt
import pandas as pd

# Assuming wallet_scores is a dictionary with wallet addresses as keys and scores as values
wallet_scores = { ... }  

# Convert scores to DataFrame
scores_df = pd.DataFrame(wallet_scores.items(), columns=['Wallet', 'Score'])

# Create bins for score ranges
bins = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
labels = ['0-100', '101-200', '201-300', '301-400', '401-500', 
          '501-600', '601-700', '701-800', '801-900', '901-1000']
scores_df['Score Range'] = pd.cut(scores_df['Score'], bins=bins, labels=labels, right=False)

# Count the number of wallets in each range
score_distribution = scores_df['Score Range'].value_counts().sort_index()

# Plotting the distribution
plt.figure(figsize=(10, 6))
score_distribution.plot(kind='bar', color='skyblue')
plt.title('Wallet Score Distribution')
plt.xlabel('Score Ranges')
plt.ylabel('Number of Wallets')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()