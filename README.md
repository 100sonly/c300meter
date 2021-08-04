# c300meter
Source code for SOI-Sem2-2021-0003

Installation of required python packages: 
pip3 install pymssql
pip3 install  opencv-python
pip3 install azure-iot-device
pip3 install nest-asyncio


ubuntu packages required:
sudo apt-get install libssl-dev

For running the script on PC:
Run analog_gauge_reader_pyodbc.py to test gauge-9.jpg
Run analog_gauge_reader_scale.py to test gauge-6.jpg

For running the script on Ubuntu:
Run analog_gauge_reader_jnano.py to test gauge-9.jpg
Run analog_gauge_reader_scale_jnano to test gauge-6.jpg

#mqttscale.py
A simple script to send a message to the IoT Hub
