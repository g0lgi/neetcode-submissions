class TimeMap:

    def __init__(self):
        self.map = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((value, timestamp))
        print(self.map)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        values = self.map[key]
        if timestamp < values[0][1]:
            return ""
        for i in range(len(values)):
            if values[i][1] == timestamp:
                return values[i][0]
            if values[i][1] > timestamp:
                return values[i - 1][0]
        return values[-1][0]
        # left = 0
        # right = len(values) - 1
        # mid = int((right + left) / 2)
        # print(left, mid, right)
        # while left < right:
        #     mid = int((right + left + 1) / 2)
        #     if values[mid][1] <= timestamp:
        #         left = mid
        #     elif values[mid][1] > timestamp:
        #         right = mid - 1
        # print(values)
        # print(left, mid, right)
        # return values[left][0]