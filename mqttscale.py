# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 22:12:12 2021

@author: Henry
"""

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from __main__ import *
import os
import asyncio
from azure.iot.device.aio import IoTHubDeviceClient
import nest_asyncio
nest_asyncio.apply()

async def main(abc):
    # Fetch the connection string from an enviornment variable
    conn_str = "HostName=Pipeline.azure-devices.net;DeviceId=pipeline;SharedAccessKey=B4H7pH0uZBHwnx7m52O+kOHB3dDp7uQu0uvnlz6Igw8="

    # Create instance of the device client using the connection string
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    # Connect the device client.
    await device_client.connect()

    # Send a single message
    print("Sending message...")
    await device_client.send_message(abc)
    print("Message successfully sent!")

    # Finally, shut down the client
    await device_client.shutdown()



    # asyncio.run(main()) 

    # If using Python 3.6 or below, use the following code instead of asyncio.run(main()):
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main(123))

   #  loop = asyncio.get_event_loop()
   # loop.run_until_complete(main("test"))
   #loop.close()