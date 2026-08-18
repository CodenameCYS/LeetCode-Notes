'''
# === 1169. Invalid Transactions === #

A transaction is possibly invalid if:
    - the amount exceeds $1000, or;
    - if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.
Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.

Example 1:
    Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
    Output: ["alice,20,800,mtv","alice,50,100,beijing"]
    - Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:
    Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
    Output: ["alice,50,1200,mtv"]
Example 3:
    Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
    Output: ["bob,50,1200,mtv"]
 
Constraints:
    1. transactions.length <= 1000
    2. Each transactions[i] takes the form "{name},{time},{amount},{city}"
    3. Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
    4. Each {time} consist of digits, and represent an integer between 0 and 1000.
    5. Each {amount} consist of digits, and represent an integer between 0 and 2000.
'''
# === 228ms & 14.4MB === #
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        tmp = {}
        ans = set([it for it in transactions if int(it.split(',')[2]) > 1000])
        for it in transactions:
            name, time, amount, city = it.split(',')
            if name not in tmp.keys():
                tmp[name] = [(time, amount, city)]
            else:
                tmp[name].append((time, amount, city))
        for name, records in tmp.items():
            l = len(records)
            for i in range(l-1):
                t0, a0, c0 = records[i]
                for j in range(i+1, l):
                    t1, a1, c1 = records[j]
                    if abs(int(t0)-int(t1)) <= 60 and c1 != c0:
                        ans.add('{},{},{},{}'.format(name, t0, a0, c0))
                        ans.add('{},{},{},{}'.format(name, t1, a1, c1))
        return list(ans)
            