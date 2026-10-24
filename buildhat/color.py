### DO NOT MODIFY CODE IN THIS FILE ###

'''
Lego Color Sensor:

    Description:
        This sensor can be used to detect the color in front of itself. This can be read as
        the name of the color as a string, the rgb representation of the color, or the hsv 
        code for the color. Additionally, functions can be used to wait until a certain color
        is observed.

    Hardware:
        These sensors can be connected to any of the BuildHAT motor ports. The letter associated 
        with each port can be seen just behind the ports, going from A to D counterclockwise.
        
        More info:
        https://www.raspberrypi.com/documentation/accessories/build-hat.html
    
    Initialization:
        sensor_name = ColorSensor('port')

        If you plug your sensor into port A and want to name it 'color', your initializaion
        will look like this:

        color = ColorSensor('A')

    ColorSensor.get_color():
        This function returns the color observed by the sensor, returning a string of the
        color name. This can be black, violet, blue, cyan, green, yellow, red, or white.If 
        your sensor's name is 'color', using this function will look like this:

        color_string = color.get_color()
        
    ColorSensor.get_color_rgbi():
        This function returns the color observed by the sensor, returning a tuple of the
        amount of red, green, blue, and the intensity of the color. Each of these values 
        ranges from 0 to 255 and intensity. If your sensor's name is 'color', using this 
        function will look like this:

        r, g, b, i = color.get_color_rgbi()

    ColorSensor.get_color_hsv():
        This function returns the color observed by the sensor, returning a tuple of the
        hue, saturation and value of the color. If your sensor's name is 'color', using 
        this function will look like this:

        hue, sat, val = color.get_color_hsv()

    ColorSensor.wait_until_color(color):
        This function pauses the execution of code until the observed color matches the 
        color input to the function. This is input as a string and must match black, 
        violet, blue, cyan, green, yellow, red, or white. If your sensor's name is 'color'
        and you want to wait until the color black is observed, using this function will 
        look like this:

        color.wait_until_color('black')

    ColorSensor.wait_for_new_color():
        This function pauses the execution of code until the color in front of the sensor
        changes. If your sensor's name is 'color', using this function will look like this:

        color.wait_for_new_color()
    
    ColorSensor_Example.py: 
        Usage of this code is demonstrated in the example file for this sensor in the Examples
        folder on your Pi's desktop.

'''

### DO NOT MODIFY CODE BELOW THIS LINE ###

import math
from collections import deque
from threading import Condition

from .devices import Device


class ColorSensor(Device):
    """Color sensor

    :param port: Port of device
    :raises DeviceError: Occurs if there is no color sensor attached to port
    """

    def __init__(self, port):
        """
        Initialise color sensor

        :param port: Port of device
        """
        super().__init__(port)
        self.reverse()
        self.mode(6)
        self.avg_reads = 4
        self._old_color = None

    def get_color(self):
        """Return the color

        :return: Name of the color as a string
        :rtype: str
        """
        r, g, b, _ = self.get_color_rgbi()
        return self.segment_color(r, g, b)

    def get_color_rgbi(self):
        """Return the color

        :return: RGBI representation
        :rtype: list
        """
        self.mode(5)
        reads = []
        for _ in range(self.avg_reads):
            reads.append(self.get())
        return self._avgrgbi(reads)

    def get_color_hsv(self):
        """Return the color

        :return: HSV representation
        :rtype: tuple
        """
        self.mode(6)
        readings = []
        for _ in range(self.avg_reads):
            read = self.get()
            read = [read[0], int((read[1] / 1024) * 100), int((read[2] / 1024) * 100)]
            readings.append(read)
        s = c = 0
        for hsv in readings:
            hue = hsv[0]
            s += math.sin(math.radians(hue))
            c += math.cos(math.radians(hue))

        hue = int((math.degrees((math.atan2(s, c))) + 360) % 360)
        sat = int(sum([hsv[1] for hsv in readings]) / len(readings))
        val = int(sum([hsv[2] for hsv in readings]) / len(readings))
        return (hue, sat, val)

    def wait_until_color(self, color):
        """Wait until specific color

        :param color: Color to look for
        """
        self.mode(5)
        self._cond = Condition()
        self._data = deque(maxlen=self.avg_reads)
        self._color = color
        self._cmp = lambda x, y: x == y
        self.callback(self._cb_handle)
        with self._cond:
            self._cond.wait()
        self.callback(None)

    def wait_for_new_color(self):
        """Wait for new color or returns immediately if first call

        :return: Name of the color as a string
        :rtype: str
        """
        self.mode(5)
        if self._old_color is None:
            self._old_color = self.get_color()
            return self._old_color
        self._cond = Condition()
        self._data = deque(maxlen=self.avg_reads)
        self._color = self._old_color
        self._cmp = lambda x, y: x != y
        self.callback(self._cb_handle)
        with self._cond:
            self._cond.wait()
        self.callback(None)
        return self._old_color

    def segment_color(self, r, g, b):
        """Return the color name from RGB

        :param r: Red
        :param g: Green
        :param b: Blue
        :return: Name of the color as a string
        :rtype: str
        """
        table = [("black", (0, 0, 0)),
                 ("violet", (127, 0, 255)),
                 ("blue", (0, 0, 255)),
                 ("cyan", (0, 183, 235)),
                 ("green", (0, 128, 0)),
                 ("yellow", (255, 255, 0)),
                 ("red", (255, 0, 0)),
                 ("white", (255, 255, 255))]
        near = ""
        euc = math.inf
        for itm in table:
            cur = math.sqrt((r - itm[1][0])**2 + (g - itm[1][1])**2 + (b - itm[1][2])**2)
            if cur < euc:
                near = itm[0]
                euc = cur
        return near

    def rgb_to_hsv(self, r, g, b):
        """Convert RGB to HSV

        Based on https://www.rapidtables.com/convert/color/rgb-to-hsv.html algorithm

        :param r: Red
        :param g: Green
        :param b: Blue
        :return: HSV representation of color
        :rtype: tuple
        """
        r, g, b = r / 255.0, g / 255.0, b / 255.0
        cmax = max(r, g, b)
        cmin = min(r, g, b)
        delt = cmax - cmin
        if cmax == cmin:
            h = 0
        elif cmax == r:
            h = 60 * (((g - b) / delt) % 6)
        elif cmax == g:
            h = 60 * ((((b - r) / delt)) + 2)
        elif cmax == b:
            h = 60 * ((((r - g) / delt)) + 4)
        if cmax == 0:
            s = 0
        else:
            s = delt / cmax
        v = cmax
        return int(h), int(s * 100), int(v * 100)

    def get_ambient_light(self):
        """Return the ambient light

        :return: Ambient light
        :rtype: int
        """
        self.mode(2)
        readings = []
        for _ in range(self.avg_reads):
            readings.append(self.get()[0])
        return int(sum(readings) / len(readings))

    def get_reflected_light(self):
        """Return the reflected light

        :return: Reflected light
        :rtype: int
        """
        self.mode(1)
        readings = []
        for _ in range(self.avg_reads):
            readings.append(self.get()[0])
        return int(sum(readings) / len(readings))

    def _avgrgbi(self, reads):
        readings = []
        for read in reads:
            read = [int((read[0] / 1024) * 255),
                    int((read[1] / 1024) * 255),
                    int((read[2] / 1024) * 255),
                    int((read[3] / 1024) * 255)]
            readings.append(read)
        rgbi = []
        for i in range(4):
            rgbi.append(int(sum([rgbi[i] for rgbi in readings]) / len(readings)))
        return rgbi

    def _cb_handle(self, lst):
        self._data.append(lst[:4])
        if len(self._data) == self.avg_reads:
            r, g, b, _ = self._avgrgbi(self._data)
            seg = self.segment_color(r, g, b)
            if self._cmp(seg, self._color):
                with self._cond:
                    self._old_color = seg
                    self._cond.notify()

    def on(self):
        """Turn on the sensor and LED"""
        self.reverse()
