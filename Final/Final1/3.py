"""
Input 
put: put key value timstamp
get: get key timestamp
---
Output

Print out the value such that the key was set 
at the closest timestamp less than or equal to the requested timestamp.
If there are no earlier timestamps, return “nil”.
""" 
from typing import Dict, List, Tuple

class TimeMap: 
    def __init__(self):
        self.store: Dict[str, List[Tuple[int, str]]] = {}
  
    def put(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
            self.store[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return "nil"
        
        values = self.store[key]
        
        # Binary search to find the right value
        left =  0
        right = len(values) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
                
            print(values)
        # If no exact match, check the closest previous timestamp
        if right >= 0:
            return values[right][1]
        return "nil"

def main():
    tm = TimeMap()
    result = []
    for command in commands:
        parts = command.split()
        if parts[0] == "put":
            key, value, timestamp = parts[1], parts[2], int(parts[3])
            tm.put(key, value, timestamp)
        elif parts[0] == "get":
            key, timestamp = parts[1], int(parts[2])
            result.append(tm.get(key, timestamp))
    return result


