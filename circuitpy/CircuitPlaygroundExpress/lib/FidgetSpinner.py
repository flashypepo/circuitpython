# Circuit Playground Express CircuitPython Fidget Spinner
# Needs this LIS3DH module and the NeoPixel module installed:
#   https://github.com/adafruit/Adafruit_CircuitPython_LIS3DH
#   https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel
# Author: Tony DiCola
# License: MIT License (https://opensource.org/licenses/MIT)

# Define a class that represents the fidget spinner.  The spinner only has a
# concept of its current position, a continuous value from 0 to <10.  You can
# start spinning the spinner with an initial velocity by calling the spin
# function, then periodically call get_position to get the current spinner
# position.  Since the position moves between values 0 to 10 it can easily map
# to pixel positions around the Circuit Playground Express board.
import math

class FidgetSpinner:

    def __init__(self, decay=0.5):
        """Create an instance of the fidget spinner.  Specify the decay rate
        as a value from 0 to 1 (continuous, floating point)--lower decay rate
        values will cause the spinner to slow down faster.
        """
        self._decay = decay
        self._velocity = 0.0
        self._elapsed = 0.0
        self._position = 0.0

    def spin(self, velocity):
        """Start the spinner moving at the specified initial velocity (in
        positions/second).
        """
        self._velocity = velocity
        self._elapsed = 0.0

    def get_position(self, delta):
        """Update the spinner position after the specified delta (in seconds)
        has elapsed.  Will return the new spinner position, a continuous value
        from 0...<10.
        """
        # Increment elapsed time and compute the current velocity after a
        # decay of the initial velocity.
        self._elapsed += delta
        current_velocity = self._velocity*math.pow(self._decay, self._elapsed)
        # Update position based on the current_velocity and elapsed time.
        self._position += current_velocity*delta
        # Make sure the position stays within values that range from 0 to <10.
        self._position = math.fmod(self._position, 10.0)
        if self._position < 0.0:
            self._position += 10.0
        return self._position
