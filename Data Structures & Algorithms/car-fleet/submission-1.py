class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        for i in range(len(position)):
            combined.append([position[i], speed[i]])
        combined.sort(reverse=True)
        times = []
        for j in range(len(combined)):
            time = (target - combined[j][0]) / combined[j][1]
            if j and time < times[j - 1]:
                times.append(times[j-1])
            else:
                times.append(time)
        # print(combined)
        # print(times)
        return len(set(times))