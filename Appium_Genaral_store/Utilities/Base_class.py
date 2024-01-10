import pytest
@pytest.mark.usefixtures("setup")
class BaseClass:
    def swipe(self, start_x, start_y, end_x, end_y, time_leap_in_ms):
        self.driver.swipe(start_x, start_y, end_x, end_y, time_leap_in_ms)