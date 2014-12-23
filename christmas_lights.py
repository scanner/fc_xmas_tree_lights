#!/usr/bin/env python
#
# Copyright (c) 2014 Eric 'Scanner' Luce
#
"""
Various patterns for our Christmas tree lights
"""

# system imports
#
import time

# 3rd party imports
#
import opc

ADDRESS = 'localhost:7890'
NUM_PIXELS = 300

####################################################################
#
def color_wheel(wheel_pos):
    """
    Keyword Arguments:
    wheel_pos -- Return a color based on the specific position on the wheel
                 This is an integer between 0-255 inclusive.
    """
    if wheel_pos < 85:
        return (wheel_pos * 3, 255 - wheel_pos * 3, 0)
    elif wheel_pos < 170:
        wheel_pos -= 85
        return (255 - wheel_pos * 3, 0, wheel_pos * 3)
    else:
        wheel_pos -= 170
        return (0, wheel_pos * 3, 255 - wheel_pos * 3)


########################################################################
########################################################################
#
class Animation(object):
    """
    Base animation class
    """

    ####################################################################
    #
    def __init__(self, num_pixels):
        self.num_pixels = num_pixels
        pass

    ####################################################################
    #
    def one_frame(self, frame):
        """
        Produce one frame of animation. We return an array of the colors
        to light up.
        """
        raise NotImplemented


########################################################################
########################################################################
#
class LayerCake(Animation):
    """
    Layers of color going up or down the tree...
    """

    ####################################################################
    #
    def __init__(self, num_pixels, down=True, brightness=1.0):
        """
        If 'down' is True then the layers of color go from the top of the
        tree to the bottom of the tree.
        brightness is how bright the colors should be.
        """
        super(LayerCake, self).__init__(num_pixels)
        self.num_frames = 256
        return


#############################################################################
#
def main():
    """
    Find out which pattern they want to run and go with it..
    """
    client = opc.Client(ADDRESS)
    if client.can_connect():
        print('connected to %s' % ADDRESS)
    else:
        print('WARNING: could not connect to %s' % ADDRESS)
        return
    return

############################################################################
############################################################################
#
# Here is where it all starts
#
if __name__ == '__main__':
    main()
#
############################################################################
############################################################################
