class TimeMap:

    def __init__(self):
        self.time_map={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = [(0,""),(timestamp,value)]
        else:
            self.time_map[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.time_map:
            time_map = self.time_map[key]

            left = 0
            right = len(time_map)-1

            while left <= right:
                middle = (left+right)//2
                if time_map[middle][0]==timestamp:
                    return time_map[middle][1]
                
                if time_map[middle][0] < timestamp:
                    left = middle+1
                elif time_map[middle][0] > timestamp:
                    right = middle-1
                
            return time_map[right][1]
                
        else:
            return ""
        
