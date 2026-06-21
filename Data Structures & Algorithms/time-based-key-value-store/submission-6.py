class TimeMap:

    def __init__(self):
        self.dictionary = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key + str(timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        while timestamp >= 0 and key + str(timestamp) not in self.dictionary:
            timestamp -= 1
        return self.dictionary[key + str(timestamp)] if timestamp >= 0 else ""
