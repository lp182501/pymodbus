# RUN AS ROOT, OTHERWISE YOU'LL HAVE NO ACCESS TO /dev/ttyUSB0....
# OR sudo chmod 666 /dev/ttyUSB0
# OR add ttyUSB0 to the rules.

from pymodbus.client.sync import ModbusSerialClient as ModbusClient

client = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=9600, parity='E', stopbits=1)
client.connect()

UNIT = 0x1

rr = client.read_holding_registers(1282,2,unit=UNIT)

print(rr.registers)

client.close()


#client.read_coils(1282,2,unit=1)
#client.read_coils(1282,2,unit=1).bits
#client.write_coils(2048,1,unit=1)
#client.read_coils(2048,1,unit=1).bits

#for x in range(2049,2066):
#    client.write_coil(x,0,unit=1)
