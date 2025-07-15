The goal of this project is to seek to develop a credit scoring model that, based on their historical transaction behavior in the Aave V2 protocol, assigns to each wallet a score between 0 and 1000. Higher scores are indicative of usage that is reliable and also responsible. Lower scores reflect exploitative or risky behavior.

The scoring model uses the following features transaction data provides.
- Transaction Frequency: Wallets each show this total for transactions.
- Transaction Types: Liquidations and repayments and borrows and count of deposits.
- Average Transaction Amount: The transactions involve an average amount that is present.
- Successful vs. Ratio of successful transactions versus failed ones: Failed Transactions.
- Time Between Transactions: Average time interval of transactions.
- Liquidity Utilization: Ratio from deposited amount to borrowed amount reversed.
- Repayment Behavior: Amount and frequency of repayments.
- Count of liquidation events: Liquidation Events too.
- Diversity of Interactions: The number of assets with which one interacts on.
- Risky Behavior Indicators: Flags are indicating of risky behaviors.

1. Data Loading: Transaction data must be loaded out of a JSON file.
2. Feature Engineering: Relevant features of each wallet must be calculated.
3. Score Calculation: Scores are something that should be assigned. Those will rely on planned attributes.
4. Output: A dictionary with wallet scores is generated.

1. The JSON file with user transactions must be loaded.
2. Convert the data. Processing requires a DataFrame.
3. Calculate scores in order for each wallet. The calculation is based upon such defined features.
4. Output the scores. They are intended for the purpose of further analysis.
