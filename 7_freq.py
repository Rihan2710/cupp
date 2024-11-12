import csv

def load_data(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    header = data[0][1:] 
    transactions = []
    for row in data[1:]:
        transaction = set(item for item in row[1:] if item)  
        transactions.append(transaction)
    return header, transactions

def generate_candidates(prev_frequent_itemsets, k):
    candidates = set()
    prev_frequent_itemsets = list(prev_frequent_itemsets)
    for i in range(len(prev_frequent_itemsets)):
        for j in range(i + 1, len(prev_frequent_itemsets)):
            union_set = prev_frequent_itemsets[i].union(prev_frequent_itemsets[j])
            if len(union_set) == k:
                candidates.add(frozenset(union_set))
    return candidates

def calculate_support(transactions, candidates, minsup, total_transactions):
    itemset_support = {}
    for transaction in transactions:
        for candidate in candidates:
            if candidate.issubset(transaction):
                itemset_support[candidate] = itemset_support.get(candidate, 0) + 1
    frequent_itemsets = {
        itemset: support / total_transactions
        for itemset, support in itemset_support.items()
        if support / total_transactions >= minsup
    }    
    return frequent_itemsets

def apriori(transactions, minsup):
    total_transactions = len(transactions)
    k = 1    
    candidates = [frozenset([item]) for item in set(item for transaction in transactions for item in transaction)]
    freq_itemset = []    
    while candidates:
        frequent_itemsets = calculate_support(transactions, candidates, minsup, total_transactions)        
        if not frequent_itemsets:
            break        
        freq_itemset.append(frequent_itemsets)
        candidates = generate_candidates(frequent_itemsets.keys(), k + 1)
        k += 1
    return freq_itemset

def write_itemsets(filename, freq_itemset):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Itemset', 'Support'])
        for k_itemsets in freq_itemset:
            for itemset, support in k_itemsets.items():
                writer.writerow([', '.join(itemset), support])

ip = './transaction.csv'  
op = './frequent_itemsets.csv'
minsup_percentage = float(input('Enter minimum support (as percentage): '))
minsup = minsup_percentage / 100  # Convert percentage to fraction
header, transactions = load_data(ip)
freq_itemset = apriori(transactions, minsup)
write_itemsets(op, freq_itemset)
print('Frequent itemsets are written to', op)
