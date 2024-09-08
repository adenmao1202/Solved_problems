"""
IO Format: 

Input Format:The first input is the amount of records. 
From the second line to the last line, each line containes an instruction, each instruction has it's own purpose.

insert: Add the stock id and the sequence of the stock price into the database

delete: Delete the stock id and the sequence of the stock from the database

update: Update the stock price sequence from the specific stock id

query: Print the mean value of the speific stock price sequence

Please also be aware that: since stock price cannot be a negative number (price must >= 0), 
so when there exists negative number in the input, change them to "NA".Output 

Format:The output will happened in instructions update, delete and query.

The output format in update will only be: Cannot find stock ID: {stockID}! If stockID does not exists in the database

The output format in delete will only be: Cannot find stock ID: {stockID}! If stockID does not exists in the database

The output format in query will be one of the below:

    {stockID} has mean value: {mean_value}

    Cannot find stock ID: {stockID}! If stockID does not exists in the database

    Stock sequence with NA value! If stockID's price sequence has NA value
    

example:
Input example 1:

4
insert 2330 10 9 8 7
update 00939 1 2 3
query 2330
delete 00940

Output example 1:

Cannot find stock ID: 00939!
2330 has mean value: 8.5
Cannot find stock ID: 00940!
"""


class StockData(object):
    def __init__(self):
        self.stock_data = {}

    def insert(self, stockID, *values):  # 傳入多個值需要使用 *
        prices = []
        for value in values:
            try:  # 新增
                if float(value) < 0:
                    prices.append(None)  # Use None for NA values
                else:
                    prices.append(float(value))  # Handle values as floats
            except ValueError:  # 如果value不是數字，但是'abc'，那就需要except然後return None
                prices.append(None)  # Handle invalid numbers as None
        
        if stockID in self.stock_data:
            return f"Stock ID {stockID} already exists. Use update to change the values."
        else:
            self.stock_data[stockID] = prices  # Add the list to the dictionary
        
    def delete(self, stockID):
        if stockID in self.stock_data:
            del self.stock_data[stockID]  # Special method of dictionary
        else:
            return f"Cannot find stock ID: {stockID}!"

    def update(self, stockID, *values):
        if stockID in self.stock_data:
            prices = []
            for value in values:
                try:  # 新增
                    price = float(value)
                    if price < 0:
                        prices.append(None)
                    else:
                        prices.append(price)
                except ValueError:  # 新增
                    prices.append(None)
            self.stock_data[stockID] = prices  # Update the prices in the dictionary
        else:
            return f"Cannot find stock ID: {stockID}!"

    def query(self, stockID):
        if stockID in self.stock_data:
            values = self.stock_data[stockID]
            if any(val is None for val in values):
                return "Stock sequence with NA value!"
            else:
                mean_value = sum(values) / len(values)
                return f"{stockID} has mean value: {mean_value:.1f}"
        else:
            return f"Cannot find stock ID: {stockID}!"

if __name__ == "__main__":
    num_of_command = input().strip()  # Process the first input
    total = int(num_of_command)

    data = StockData()  # being called so that I can use the class (data.insert, data.delete,...)

    for _ in range(total):  # 總共有幾組input # for_in range() is used when _ is not used below, just wanting to know how many times to iterate
        command = input().split(" ")  # 處理第一個以外的input
        cmd = command[0]
        stockID = command[1]
        values = command[2:]

        if cmd == "insert":
            result = data.insert(stockID, *values)  # Unpack the values 修改

        elif cmd == "delete":
            result = data.delete(stockID)

        elif cmd == "update":
            result = data.update(stockID, *values)  # Unpack the values 修改

        elif cmd == "query":
            result = data.query(stockID)

        if result is not None:
            print(result)

        
