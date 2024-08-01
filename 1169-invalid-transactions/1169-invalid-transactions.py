class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        result = []
        Transaction = collections.namedtuple('Transaction', ['name','time','amount','city'])
        transaction_tuple = []
        for trans in transactions:
            _name, _time,_amt,_city = (int(val) if val.isdigit() else val for val in trans.split(','))
            transaction_tuple.append(Transaction(_name, _time, _amt, _city))
        n = len(transactions)
        validity = [True]*n
        for i in range(n):
            if transaction_tuple[i].amount > 1000:
                validity[i] = False
            for j in range(i + 1, n):
                if transaction_tuple[i].name == transaction_tuple[j].name and abs(transaction_tuple[i].time - transaction_tuple[j].time) <= 60 and transaction_tuple[i].city != transaction_tuple[j].city:
                    validity[i] = validity[j] = False
        for i in range(n):
            if not validity[i]:
                result.append(transactions[i])
        return result
    