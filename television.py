# television.py

class Television:
    # Class variables
    Min_volume = 0
    Max_volume = 2
    Min_channel = 0
    Max_channel = 3

    def __init__(self):
        # Instance variables (private)
        self._power_status = False
        self._muted = False
        self._volume = self.Min_volume
        self._channel = self.Min_channel

    def power(self):
        """Turn the TV on and off."""
        self._power_status = not self._power_status

    def channel_up(self):
        """Increase the TV channel. If on the maximum channel, set to the minimum."""
        if self._power_status:
            self._channel = (self._channel + 1) % (self.Max_channel + 1)

    def channel_down(self):
        """Decrease the TV channel. If on the minimum channel, set to the maximum."""
        if self._power_status:
            self._channel = (self._channel - 1) % (self.Max_channel + 1)

    def volume_up(self):
        """Increase the TV volume. If at the maximum volume, remain at the maximum."""
        if self._power_status and self._volume < self.Max_volume:
            self._volume += 1

    def volume_down(self):
        """Decrease the TV volume. If at the minimum volume, remain at the minimum."""
        if self._power_status and self._volume > self.Min_volume:
            self._volume -= 1

    def mute(self):
        """Mute and unmute the TV when it's on."""
        if self._power_status:
            self._muted = not self._muted
            if self._muted:
                self._volume = self.Min_volume

    def __str__(self):
        """String representation of the TV object."""
        return f"Power = {self._power_status}, Channel = {self._channel}, Volume = {self._volume}, Muted = {self._muted}"



