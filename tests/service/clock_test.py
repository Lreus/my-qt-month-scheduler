from src.service import Clock
from datetime import date

class TestClock:

    def test_now_returns_today(self) -> None:
        clock = Clock()

        assert date.today() == clock.now()
