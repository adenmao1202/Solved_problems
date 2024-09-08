import sys


class StockData:
    def __init__(self):
        self.stock_data = {}

    def insert(self, stockID, *values):
        if stockID not in self.stock_data:
            self.stock_data[stockID] = []
            self.stock_data[stockID].extend(values)
        return None

    def delete(self, stockID):
        try:
            del self.stock_data[stockID]
        except KeyError:
            return f"Cannot find stock ID: {stockID}!"

    def update(self, stockID, *values):
        if stockID in self.stock_data:
            self.stock_data[stockID] = list(values)
        else:
            return f"Cannot find stock ID: {stockID}!"

    def query(self, stockID):
        try:
            values = self.stock_data[stockID]

            if any(val is None for val in values):
                raise TypeError("Stock sequence with NA value!")

            if all(val is not None for val in values):
                mean_value = sum(values) / len(values)
                return f"{stockID} has mean value: {mean_value:.1f}"
        except KeyError:
            return f"Cannot find stock ID: {stockID}!"
        except TypeError:
            return "Stock sequence with NA value!"

    def execute_commands(self):
        number_of_commands = int(input().strip())

        for i in range(number_of_commands):
            line = input().strip()
            parts = line.split()
            if len(parts) < 2:
                continue

            cmd = parts[0]
            stockID = parts[1]
            values = (
                [float(x) if float(x) > 0 else None for x in parts[2:]]
                if len(parts) > 2
                else []
            )

            if cmd == "insert":
                result = self.insert(stockID, *values)

            elif cmd == "update":
                result = self.update(stockID, *values)

            elif cmd == "query":
                result = self.query(stockID)

            elif cmd == "delete":
                result = self.delete(stockID)

            if result is not None:
                print(result)
                sys.stdout.flush()
        sys.stdout.flush()


if __name__ == "__main__":
    stock_data = StockData()
    stock_data.execute_commands()
