class Clock:
    def __init__(self, hour: int, minute: int):
        # Normalize the time to handle overflow/underflow
        total_minutes = (hour * 60 + minute) % (24 * 60)
        if total_minutes < 0:
            total_minutes += 24 * 60
        self.hour = total_minutes // 60
        self.minute = total_minutes % 60

    def __repr__(self) -> str:
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self) -> str:
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other: 'Clock') -> bool:
        if not isinstance(other, Clock):
            return NotImplemented
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes: int) -> 'Clock':
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes: int) -> 'Clock':
        return Clock(self.hour, self.minute - minutes)
