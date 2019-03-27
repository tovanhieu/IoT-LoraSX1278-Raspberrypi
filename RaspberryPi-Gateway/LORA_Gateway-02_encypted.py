#!/usr/bin/env python3

""" This program asks a client for data and waits for the response, then sends an ACK. """

# Copyright 2019 To Van Hieu.
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
import json
import configparser

# Use BOARD 2
from SX127x.LoRa import LoRa2 as LoRa
from SX127x.board_config import BOARD2 as BOARD

BOARD.setup()
BOARD.reset()
import mysql.connector
# Function insert data to google cloud from gateway
def insertGgClouddb(cabin_id,tem,humi,light,co):
  mycursor = mydb.cursor()
  sql = "INSERT INTO tbl_cabin (train_id, cabin_id, temp, humi, longitude, latitude, co) VALUES (%s,%s,%s,%s,%s,%s,%s)"
  val = [ (1,cabin_id, tem, humi,'100','120', co) ]
  mycursor.executemany(sql, val)
  mydb.commit()

class mylora(LoRa):
    def __init__(self, verbose=False):
        super(mylora, self).__init__(verbose)
        self.set_mode(MODE.SLEEP)
        self.set_dio_mapping([0] * 6)
        self.var=0
        self.key = b'1234567890123456'

    def on_rx_done(self):
        BOARD.led_on()
        #print("\nRxDone")
        self.clear_irq_flags(RxDone=1)
        payload = self.read_payload(nocheck=True)
        mens=payload[4:-1] #to discard \xff\xff\x00\x00 and \x00 at the end
        mens= bytes(mens).decode("utf-8",'ignore') + '='
        print(mens)
        print(len(mens))
        cipher = AES.new(self.key,AES.MODE_ECB)
        decodemens=base64.b64decode(mens)
        decoded = cipher.decrypt(decodemens)
        decoded = bytes(decoded).decode("utf-8",'ignore')
        print ("== RECEIVE: ", mens, "  s|  Decoded: ",decoded )
        msg = json.loads(decoded)
        print(msg)
        insertGgClouddb(msg['id'],msg['t'],msg['h'],msg['l'],msg['p'])
        BOARD.led_off()
        time.sleep(2) # Wait for the client be ready
        msg_text = 'ACK             ' # 16 char
        cipher = AES.new(self.key,AES.MODE_ECB)
        encoded = base64.b64encode(cipher.encrypt(msg_text))
        lista=list(encoded)
        lista.insert(0,0)
        lista.insert(0,0)
        lista.insert(0,255)
        lista.insert(0,255)
        lista.append(0)
        self.write_payload(lista)
        #self.write_payload([255, 255, 0, 0, 65, 67, 75, 0]) # Send ACK
        self.set_mode(MODE.TX)
        print ("== SEND: ", msg_text, "  |  Encoded: ", encoded.decode("utf-8",'ignore'))
        print ("\n")
        self.var=1

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
            while (self.var==0):
                msg_text = 'INF             '
                cipher = AES.new(self.key,AES.MODE_ECB)
                encoded = base64.b64encode(cipher.encrypt(msg_text))
                lista=list(encoded)
                lista.insert(0,0)
                lista.insert(0,0)
                lista.insert(0,255)
                lista.insert(0,255)
                lista.append(0)
                self.write_payload(lista)
                #self.write_payload([255, 255, 0, 0, 57, 90, 54, 118, 106, 71, 75, 51, 87, 75, 107, 79, 99, 55, 76, 122, 112, 65, 86, 88, 79, 81, 61, 61, 0]) # Send INF
                self.set_mode(MODE.TX)
                print ("== SEND: INF                |  Encoded: ", encoded)
                time.sleep(3) # there must be a better solution but sleep() works
                self.reset_ptr_rx()
                self.set_mode(MODE.RXCONT) # Receiver mode
                start_time = time.time()
                while (time.time() - start_time < 10): # wait until receive data or 10s
                    pass;
            self.var=0
            self.reset_ptr_rx()
            self.set_mode(MODE.RXCONT) # Receiver mode
            time.sleep(10)

lora = mylora(verbose=False)
# parse config parameter for node1 in gateway
config = configparser.ConfigParser()
config.read("config.ini")
#     Slow+long range  Bw = 125 kHz, Cr = 4/8, Sf = 4096chips/symbol, CRC on. 13 dBm
lora.set_pa_config(pa_select=1, max_power=21, output_power=15)
lora.set_freq(float(config['Node2']['frequency']))
lora.set_bw(int(config['Node2']['band_width']))
lora.set_coding_rate(int(config['Node2']['coding_rate']))
lora.set_spreading_factor(int(config['Node2']['spreading_factor']))
lora.set_rx_crc(True)
#lora.set_lna_gain(GAIN.G1)
#lora.set_implicit_header_mode(False)
lora.set_low_data_rate_optim(True)

#  Medium Range  Defaults after init are 434.0MHz, Bw = 125 kHz, Cr = 4/5, Sf = 128chips/symbol, CRC on 13 dBm
#lora.set_pa_config(pa_select=1)

mydb = mysql.connector.connect(
  host = config['Google cloud MySQL']['host'],
  user = config['Google cloud MySQL']['user'],
  passwd = config['Google cloud MySQL']['passwd'],
  database = config['Google cloud MySQL']['database']
)

assert(lora.get_agc_auto_on() == 1)

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
