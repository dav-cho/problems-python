"""
1396. Design Underground System (medium)
"""


# Two hashmaps, storing total time and count (no overflow handling)
class UndergroundSystem:
    def __init__(self):
        self.customers = {}
        self.times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = stationName, t

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.customers.pop(id)
        pair = self.times.setdefault(
            (start_station, stationName), {"time": 0, "count": 0}
        )
        pair["time"] += t - start_time
        pair["count"] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) not in self.times:
            return 0
        pair = self.times[(startStation, endStation)]
        return pair["time"] / pair["count"]
