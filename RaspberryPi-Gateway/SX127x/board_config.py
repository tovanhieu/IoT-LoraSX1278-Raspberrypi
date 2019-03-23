""" Defines the BOARD class that contains the board pin mappings and RF module HF/LF info. """
# -*- coding: utf-8 -*-

# Copyright 2015-2018 Mayer Analytics Ltd. and Rui Silva
#
# This file is part of rpsreal/pySX127x.
#
# pySX127x is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# pySX127x is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more
# details.
#
# You can be released from the requirements of the license by obtaining a commercial license. Such a license is
# mandatory as soon as you develop commercial activities involving pySX127x without disclosing the source code of your
# own applications, or shipping pySX127x with a closed source product.
#
# You should have received a copy of the GNU General Public License along with pySX127.  If not, see
# <http://www.gnu.org/licenses/>.


import RPi.GPIO as GPIO
import spidev

import time


class BOARD:
    """ Board initialisation/teardown and pin configuration is kept here.
        Also, information about the RF module is kept here.
        This is the Raspberry Pi board with one LED and a Ra-02 Lora.
    """
    # Note that the BCOM numbering for the GPIOs is used.
    DIO0 = 4   # RaspPi GPIO 4
    DIO1 = 17   # RaspPi GPIO 17
    DIO2 = 18   # RaspPi GPIO 18
    DIO3 = 27   # RaspPi GPIO 27
    RST  = 22   # RaspPi GPIO 22
    LED  = 13   # RaspPi GPIO 13 connects to the LED and a resistor (1kohm or 330ohm)
    #SWITCH = 4  # RaspPi GPIO 4 connects to a switch - not necessary

    # The spi object is kept here
    spi = None
    SPI_BUS=0
    SPI_CS=0
    
    # tell pySX127x here whether the attached RF module uses low-band (RF*_LF pins) or high-band (RF*_HF pins).
    # low band (called band 1&2) are 137-175 and 410-525
    # high band (called band 3) is 862-1020
    low_band = True

    @staticmethod
    def setup():
        """ Configure the Raspberry GPIOs
        :rtype : None
        """
        GPIO.setmode(GPIO.BCM)
        # LED
        GPIO.setup(BOARD.LED, GPIO.OUT)
        GPIO.setup(BOARD.RST, GPIO.OUT)
        GPIO.output(BOARD.LED, 0)
        GPIO.output(BOARD.RST, 1)
        # switch
        #GPIO.setup(BOARD.SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
        # DIOx
        for gpio_pin in [BOARD.DIO0, BOARD.DIO1, BOARD.DIO2, BOARD.DIO3]:
            GPIO.setup(gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        # blink 2 times to signal the board is set up
        BOARD.blink(.1, 2)

    @staticmethod
    def teardown():
        """ Cleanup GPIO and SpiDev """
        GPIO.cleanup()
        BOARD.spi.close()

    @staticmethod
    def SpiDev():
        """ Init and return the SpiDev object
        :return: SpiDev object
        :param spi_bus: The RPi SPI bus to use: 0 or 1
        :param spi_cs: The RPi SPI chip select to use: 0 or 1
        :rtype: SpiDev
        """
        spi_bus=BOARD.SPI_BUS
        spi_cs=BOARD.SPI_CS
        BOARD.spi = spidev.SpiDev()
        BOARD.spi.open(spi_bus, spi_cs)
        BOARD.spi.max_speed_hz = 5000000    # SX127x can go up to 10MHz, pick half that to be safe
        return BOARD.spi

    @staticmethod
    def add_event_detect(dio_number, callback):
        """ Wraps around the GPIO.add_event_detect function
        :param dio_number: DIO pin 0...5
        :param callback: The function to call when the DIO triggers an IRQ.
        :return: None
        """
        GPIO.add_event_detect(dio_number, GPIO.RISING, callback=callback)

    @staticmethod
    def add_events(cb_dio0, cb_dio1, cb_dio2, cb_dio3, cb_dio4, cb_dio5, switch_cb=None):
        BOARD.add_event_detect(BOARD.DIO0, callback=cb_dio0)
        BOARD.add_event_detect(BOARD.DIO1, callback=cb_dio1)
        BOARD.add_event_detect(BOARD.DIO2, callback=cb_dio2)
        BOARD.add_event_detect(BOARD.DIO3, callback=cb_dio3)
        # the modtronix inAir9B does not expose DIO4 and DIO5
        if switch_cb is not None:
            GPIO.add_event_detect(BOARD.SWITCH, GPIO.RISING, callback=switch_cb, bouncetime=300)

    @staticmethod
    def led_on(value=1):
        """ Switch the proto shields LED
        :param value: 0/1 for off/on. Default is 1.
        :return: value
        :rtype : int
        """
        GPIO.output(BOARD.LED, value)
        return value

    @staticmethod
    def led_off():
        """ Switch LED off
        :return: 0
        """
        GPIO.output(BOARD.LED, 0)
        return 0
    
    @staticmethod
    def reset():
        """ manual reset
        :return: 0
        """
        GPIO.output(BOARD.RST, 0)
        time.sleep(.01)
        GPIO.output(BOARD.RST, 1)
        time.sleep(.01)
        return 0

    @staticmethod
    def blink(time_sec, n_blink):
        if n_blink == 0:
            return
        BOARD.led_on()
        for i in range(n_blink):
            time.sleep(time_sec)
            BOARD.led_off()
            time.sleep(time_sec)
            BOARD.led_on()
        BOARD.led_off()
        

        
        
        
# BOARD2 configuration here -----------------------------------------------------------------------------
class BOARD2:
    """ Board2 initialisation/teardown and pin configuration is kept here.
        Also, information about the RF module is kept here.
        This is the Raspberry Pi board with one LED and a Ra-02 Lora.
    """
    # Note that the BCOM numbering for the GPIOs is used.
    DIO0 = 23   # RaspPi GPIO 23
    DIO1 = 24   # RaspPi GPIO 24                                                                                         
    DIO2 = 25   # RaspPi GPIO 25
    DIO3 = 5   # RaspPi GPIO 5
    RST  = 6   # RaspPi GPIO 6
    LED  = 19   # RaspPi GPIO 19 connects to the LED and a resistor (1kohm or 330ohm)
    #SWITCH = 4  # RaspPi GPIO 4 connects to a switch - not necessary

    # The spi object is kept here
    spi = None
    SPI_BUS=0
    SPI_CS=1
    
    # tell pySX127x here whether the attached RF module uses low-band (RF*_LF pins) or high-band (RF*_HF pins).
    # low band (called band 1&2) are 137-175 and 410-525
    # high band (called band 3) is 862-1020
    low_band = True

    @staticmethod
    def setup():
        """ Configure the Raspberry GPIOs
        :rtype : None
        """
        GPIO.setmode(GPIO.BCM)
        # LED
        GPIO.setup(BOARD2.LED, GPIO.OUT)
        GPIO.setup(BOARD2.RST, GPIO.OUT)
        GPIO.output(BOARD2.LED, 0)
        GPIO.output(BOARD2.RST, 1)
        # switch
        #GPIO.setup(BOARD2.SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
        # DIOx
        for gpio_pin in [BOARD2.DIO0, BOARD2.DIO1, BOARD2.DIO2, BOARD2.DIO3]:
            GPIO.setup(gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        # blink 2 times to signal the BOARD2 is set up
        BOARD2.blink(.1, 2)

    @staticmethod
    def teardown():
        """ Cleanup GPIO and SpiDev """
        GPIO.cleanup()
        BOARD2.spi.close()

    @staticmethod
    def SpiDev():
        """ Init and return the SpiDev object
        :return: SpiDev object
        :param spi_bus: The RPi SPI bus to use: 0 or 1
        :param spi_cs: The RPi SPI chip select to use: 0 or 1
        :rtype: SpiDev
        """
        spi_bus=BOARD2.SPI_BUS
        spi_cs=BOARD2.SPI_CS
        BOARD2.spi = spidev.SpiDev()
        BOARD2.spi.open(spi_bus, spi_cs)
        BOARD2.spi.max_speed_hz = 5000000    # SX127x can go up to 10MHz, pick half that to be safe
        return BOARD2.spi

    @staticmethod
    def add_event_detect(dio_number, callback):
        """ Wraps around the GPIO.add_event_detect function
        :param dio_number: DIO pin 0...5
        :param callback: The function to call when the DIO triggers an IRQ.
        :return: None
        """
        GPIO.add_event_detect(dio_number, GPIO.RISING, callback=callback)

    @staticmethod
    def add_events(cb_dio0, cb_dio1, cb_dio2, cb_dio3, cb_dio4, cb_dio5, switch_cb=None):
        BOARD2.add_event_detect(BOARD2.DIO0, callback=cb_dio0)
        BOARD2.add_event_detect(BOARD2.DIO1, callback=cb_dio1)
        BOARD2.add_event_detect(BOARD2.DIO2, callback=cb_dio2)
        BOARD2.add_event_detect(BOARD2.DIO3, callback=cb_dio3)
        # the modtronix inAir9B does not expose DIO4 and DIO5
        if switch_cb is not None:
            GPIO.add_event_detect(BOARD2.SWITCH, GPIO.RISING, callback=switch_cb, bouncetime=300)

    @staticmethod
    def led_on(value=1):
        """ Switch the proto shields LED
        :param value: 0/1 for off/on. Default is 1.
        :return: value
        :rtype : int
        """
        GPIO.output(BOARD2.LED, value)
        return value

    @staticmethod
    def led_off():
        """ Switch LED off
        :return: 0
        """
        GPIO.output(BOARD2.LED, 0)
        return 0
    
    @staticmethod
    def reset():
        """ manual reset
        :return: 0
        """
        GPIO.output(BOARD2.RST, 0)
        time.sleep(.01)
        GPIO.output(BOARD2.RST, 1)
        time.sleep(.01)
        return 0

    @staticmethod
    def blink(time_sec, n_blink):
        if n_blink == 0:
            return
        BOARD2.led_on()
        for i in range(n_blink):
            time.sleep(time_sec)
            BOARD2.led_off()
            time.sleep(time_sec)
            BOARD2.led_on()
        BOARD2.led_off()
