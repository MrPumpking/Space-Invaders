import time

class Timer:
  def __init__(self):
    self.start_time = self.current_time_ms()

  def current_time_ms(self):
    return int(round(time.time() * 1000))

  def restart(self):
    self.start_time = self.current_time_ms()

  def has_passed(self, time):
    current_time = self.current_time_ms()
    has_passed = (current_time - self.start_time) > time
    if (has_passed):
      self.start_time = current_time
    return has_passed