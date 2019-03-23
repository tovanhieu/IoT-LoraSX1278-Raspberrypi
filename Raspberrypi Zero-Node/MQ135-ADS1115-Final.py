#!/usr/bin/python
"""
@name: MQ-135.py - MQ-135 GAS SENSOR
@disclaimer: Copyright 2017, KRIPT4
@lastrelease: Dic 27 2017 16:50
"""

"""
MQ135 gas sensor | ADS1115 (Analog-to-Digital Converter for Raspberry Pi)
Datasheet can be found here: https://www.olimex.com/Products/Components/Sensors/SNS-MQ135/resources/SNS-MQ135.pdf
Application
They are used in air quality control equipments for buildings/offices, are suitable for detecting of NH3, NOx, alcohol, Benzene, smoke, CO2, etc
Original creator of this library: https://github.com/GeorgK/MQ135
"""

import sys
import math
import operator
import Adafruit_DHT
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from gpiozero import Buzzer
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
RZERO = 76
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

def main():
  while True:
   value_pin = map((value_ads.value - 500), 0, 26690, 0, 1023) # 565 / 535 fix value
   print(value_pin)
   rzero = getRZero(value_pin,RLOAD,ATMOCO2,PARA,PARB)
   correctedRZero = getCorrectedRZero(t,h,CORA,CORB,CORC,CORD,CORE,CORF,CORG,value_pin,RLOAD,ATMOCO2,PARA,PARB)
   resistance = getResistance(value_pin,RLOAD)	
   ppm = getPPM(PARA,RZERO,PARB,value_pin,RLOAD)	
   correctedPPM = getCorrectedPPM(t,h,CORA,CORB,CORC,CORD,CORE,CORF,CORG,value_pin,RLOAD,PARA,RZERO,PARB)
   print("\n h,t: %s  %s \n" %(h,t))
   print("\n MQ135 Gas Sensor:\n")
   print("\t MQ135 RZero: %s" % round(rzero))
   print("\t Corrected RZero: %s" % round(correctedRZero))
   print("\t Resistance: %s" % round(resistance))
   print("\t PPM: %s" % round(ppm))
   print("\t Corrected PPM: %s ppm" % round(correctedPPM))
   #Alarm !!!!!!!!!!!!!!
   if ppm > 400:
       buzzer.beep()
   else: 
       buzzer.off()
   time.sleep(1)
if __name__ == "__main__":
	main()
