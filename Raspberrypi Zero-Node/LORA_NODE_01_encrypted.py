#!/usr/bin/env python3

""" This program sends a response whenever it receives the "INF" """

# Copyright 2018 Rui Silva.
#
# This file is part of rpsreal/pySX127x, fork of mayeranalytics/pySX127x.
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

import time, base64, sys
from Crypto.Cipher import AES
from SX127x.constants import add_lookup, MODE, BW, CODING_RATE, GAIN, PA_SELECT, PA_RAMP, MASK, REG
from SX127x.LoRa import set_bit, getter, setter
from SX127x.LoRaArgumentParser import LoRaArgumentParser
# Use BOARD 1
from SX127x.LoRa import LoRa
from SX127x.board_config import BOARD
import Adafruit_DHT
import sys
import math
import operator
import Adafruit_DHT
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from gpiozero import Buzzer
from gpiozero import LightSensor
import json
import _thread
from time import sleep

#Create light sensor object
ldr = LightSensor(6)
#Create buzzer object
buzzer = Buzzer(5)
# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
value_ads = AnalogIn(ads, ADS.P0)

"""
First version of an RaspBerryPi Library for the MQ135 gas sensor
TODO: Review the correction factor calculation. This currently relies on
the datasheet but the information there seems to be wrong.
"""

# The load resistance on the board
RLOAD = 10.0
# Calibration resistance at atmospheric CO2 level
RZERO = 76.63
# Parameters for calculating ppm of CO2 from sensor resistance
PARA = 116.6020682
PARB = 2.769034857

# Parameters to model temperature and humidity dependence
CORA = 0.00035
CORB = 0.02718
CORC = 1.39538
CORD = 0.0018
CORE = -0.003333333
CORF = -0.001923077
CORG = 1.130128205

# Atmospheric CO2 level for calibration purposes
ATMOCO2 = 397.13

"""
@brief  Get the correction factor to correct for temperature and humidity
@param[in] t  The ambient air temperature
@param[in] h  The relative humidity
@return The calculated correction factor
"""
#Configure DHT sensor parameter
sensor =  Adafruit_DHT.DHT11
pin = '21'
h, t = Adafruit_DHT.read_retry(sensor, pin)

def getCorrectionFactor(t,h,CORA,CORB,CORC,CORD,CORE,CORF,CORG):
	# Linearization of the temperature dependency curve under and above 20 degree C
	# below 20degC: fact = a * t * t - b * t - (h - 33) * d
	# above 20degC: fact = a * t + b * h + c
	# this assumes a linear dependency on humidity
	if t < 20:
		return CORA * t * t - CORB * t + CORC - (h-33.)*CORD
	else:
		return CORE * t + CORF * h + CORG

"""
@brief  Get the resistance of the sensor, ie. the measurement value
@return The sensor resistance in kOhm
"""

def getResistance(value_pin,RLOAD):
	return ((1023./value_pin) - 1.)*RLOAD

"""
@brief  Get the resistance of the sensor, ie. the measurement value corrected
        for temp/hum
@param[in] t  The ambient air temperature
@param[in] h  The relative humidity
@return The corrected sensor resistance kOhm
"""

def getCorrectedResistance(t,h,CORA,CORB,CORC,CORD,CORE,CORF,CORG,value_pin,RLOAD):
	return getResistance(value_pin,RLOAD) / getCorrectionFactor(t,h,CORA,CORB,CORC,CORD,CORE,CORF,CORG)

"""
@brief  Get the ppm of CO2 sensed (assuming only CO2 in the air)
@return The ppm of CO2 in the air
"""

def getPPM(PARA,RZERO,PARB,value_pin,RLOAD):
	return PARA * math.pow((getResistance(value_pin,RLOAD)/RZERO), -PARB)

"""
@brief  Get the ppm of CO2 sensed (assuming only CO2 in the air), corrected
        for temp/hum
@param[in] t  The ambient air temperature
@param[in] h  The relative humidity
@return The ppm of CO2 in the air
"""

def getCorrectedPPM(t,h,CORA,CORB,CORC,CORD,CORE,CORF,CORG,value_pin,RLOAD,PARA,RZERO,PARB):
	return PARA * math.pow((getCorrectedResistance(t,h,CORA,CORB,CORC,CORD,CORE,CORF,CORG,value_pin,RLOAD)/RZERO), -PARB)

"""
@brief  Get the resistance RZero of the sensor for calibration purposes
@return The sensor resistance RZero in kOhm
"""

def getRZero(value_pin,RLOAD,ATMOCO2,PARA,PARB):
	return getResistance(value_pin,RLOAD) * math.pow((ATMOCO2/PARA), (1./PARB))

"""
@brief  Get the corrected resistance RZero of the sensor for calibration
        purposes
@param[in] t  The ambient air temperature
@param[in] h  The relative humidity
@return The corrected sensor resistance RZero in kOhm
"""

def getCorrectedRZero(t,h,CORA,CORB,CORC,CORD,CORE,CORF,CORG,value_pin,RLOAD,ATMOCO2,PARA,PARB):
	return getCorrectedResistance(t,h,CORA,CORB,CORC,CORD,CORE,CORF,CORG,value_pin,RLOAD) * math.pow((ATMOCO2/PARA), (1./PARB))

"""
Re-maps a number from one range to another. That is, a value of fromLow would get mapped to toLow, 
a value of fromHigh to toHigh, values in-between to values in-between, etc.
# Arduino: (0 a 1023)
# Raspberry Pi: (0 a 26690)
More Info: https://www.arduino.cc/reference/en/language/functions/math/map/
"""

def map(x,in_min,in_max,out_min,out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

"""
@brief  Function parse input string message AES encryption 
@param[in] msg  The string message from Lora node
@return The string message divisible 16 
"""
def parse_msg(msg):
    n = len(msg) % 16
    if n == 0:
        return msg
    else:
        return msg.ljust(len(msg)+16-n)

"""
@brief  Function get input parameter from node 
@return The string parametter value from node
"""
def get_node_parameter(correctedPPM):
   # value_pin = map((value_ads.value - 565), 0, 26690, 0, 1023) # 565 / 535 fix value
    msg = json.dumps({'id' : 1 ,'t' : t ,'h' : h ,'l' : ldr.value , 'p' : round(correctedPPM)})
    if correctedPPM > 400:
       buzzer.beep()
    else: 
       buzzer.off()
    str_prs = parse_msg(msg)
    return(bytes(str_prs,'utf-8'))

###############
# h1 = 78
# t1 = 29
# l1 = 80
# p1 = 120    
###############
BOARD.setup()
BOARD.reset()
#parser = LoRaArgumentParser("LoRa sender node.")
class mylora(LoRa):
    def __init__(self, verbose=False):
        super(mylora, self).__init__(verbose)
        self.set_mode(MODE.SLEEP)
        self.set_dio_mapping([0] * 6)
        self.key = b'1234567890123456'

    def on_rx_done(self):
        BOARD.led_on()
        #print("\nRxDone")
        self.clear_irq_flags(RxDone=1)
        payload = self.read_payload(nocheck=True )
        mens=payload[4:-1] #to discard \xff\xff\x00\x00 and \x00 at the end
        mens=bytes(mens).decode("utf-8",'ignore')
        cipher = AES.new(self.key, AES.MODE_ECB)
        decodemens=base64.b64decode(mens)
        decoded = cipher.decrypt(decodemens)
        decoded = bytes(decoded).decode("utf-8",'ignore')
        print ("== RECEIVE: ", mens, "  |  Decoded: ",decoded )
        BOARD.led_off()
        if decoded=="INF             ":
            print("Received data request INF - going to send mens data from node:      ")
            time.sleep(4)
            value_pin = map((value_ads.value - 500), 0, 26690, 0, 1023) # 565 / 535 fix value
            rzero = getRZero(value_pin,RLOAD,ATMOCO2,PARA,PARB)
            correctedRZero = getCorrectedRZero(t,h,CORA,CORB,CORC,CORD,CORE,CORF,CORG,value_pin,RLOAD,ATMOCO2,PARA,PARB)
            resistance = getResistance(value_pin,RLOAD)	
            ppm = getPPM(PARA,RZERO,PARB,value_pin,RLOAD)	
            correctedPPM = getCorrectedPPM(t,h,CORA,CORB,CORC,CORD,CORE,CORF,CORG,value_pin,RLOAD,PARA,RZERO,PARB) 
            msg = get_node_parameter(correctedPPM) # Contain string char value divisable 16       
            print(len(msg))
            cipher = AES.new(self.key, AES.MODE_ECB)
            encoded = base64.b64encode(cipher.encrypt(msg))
            lista=list(encoded)
            lista.insert(0,0)
            lista.insert(0,0)
            lista.insert(0,255)
            lista.insert(0,255)
            lista.append(0)
            self.write_payload(lista)
            selfco.set_mode(MODE.TX)
            result =  '== SEND: DATA FROM NODE {} HUM: {} TEM: {}  LIGHT: {} PPM:  {}   |  Ended: {}'.format(1,h,t,ldr.value,round(correctedPPM), encoded.decode("utf-8",'ignore'))
            print(result)  
        if decoded=="ACK             ":
            print("\n")
            
        time.sleep(3)
        self.reset_ptr_rx()
        self.set_mode(MODE.RXCONT)

    def on_tx_done(self):
        print("\nTxDone")
        print(self.get_irq_flags())

    def on_cad_done(self):
        print("\non_CadDone")
        print(self.get_irq_flags())

    def on_rx_timeout(self):
        print("\non_RxTimeout")
        print(self.get_irq_flags())

    def on_valid_header(self):
        print("\non_ValidHeader")
        print(self.get_irq_flags())

    def on_payload_crc_error(self):
        print("\non_PayloadCrcError")
        print(self.get_irq_flags())

    def on_fhss_change_channel(self):
        print("\non_FhssChangeChannel")
        print(self.get_irq_flags())

    def start(self):          
        while True:
            self.reset_ptr_rx()
            self.set_mode(MODE.RXCONT) # Receiver mode
            while True:
                pass;
            
lora = mylora(verbose=False)
#args = parser.parse_args(lora)
#lora.set_mode(MODE.STDBY)
#lora.set_pa_config(pa_select=1, max_power=21, output_power=15)
# parse config parameter for node1 in gateway
config = configparser.ConfigParser()
config.read("config.ini")
#     Slow+long range  Bw = 125 kHz, Cr = 4/8, Sf = 4096chips/symbol, CRC on. 13 dBm
lora.set_pa_config(pa_select=1, max_power=21, output_power=15)
lora.set_freq(config['Node1']['frequency'])
lora.set_bw(config['Node1']['bandwidth'])
lora.set_coding_rate(config['Node1']['coding_rate'])
lora.set_spreading_factor(config['Node1']['spreading_factor'])
lora.set_rx_crc(True)
#lora.set_lna_gain(GAIN.G1)
#lora.set_implicit_header_mode(False)
lora.set_low_data_rate_optim(True)

#  Medium Range  Defaults after init are 434.0MHz, Bw = 125 kHz, Cr = 4/5, Sf = 128chips/symbol, CRC on Power 13 dBm
#lora.set_pa_config(pa_select=1)


# print(lora)
assert(lora.get_agc_auto_on() == 1)

# try: input("Press enter to start...")
# except: pass

try:
    print("START")
    lora.start()
except KeyboardInterrupt:
    sys.stdout.flush()
    print("Exit")
    sys.stderr.write("KeyboardInterrupt\n")
finally:
    sys.stdout.flush()
    print("Exit")
    lora.set_mode(MODE.SLEEP)
BOARD.teardown()

