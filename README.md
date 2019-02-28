# Raspberry-Bluetooth-Scanner
Scanner of nearby bluetooth devices

This is a project to provide an automated python script which scans nearby bluetooth devices and log it in a CSV file. Data includes:

    1. Device ID (unique physical address).
    2. Device Name.
The code is tested on a linux machine with python 2.7 but it will run on any Debian based environment, given that it has the following dependencies installed

## Dependencies & Installation
This python script invokes linux utility `hcitool` to get the device data and python data formatting library `pandas` to format retrieved data and finally log it.
To install the dependencies, you first need linux utiltiy `hcitool`. This executable utility can be installed with command:
    
    $ sudo apt-get install bluez
    $ sudo apt-get install blueman
    
Before proceeding any further, just make sure bluetooth is turned on. NEXT, Python script also require Pandas library, to install this:
    
    $ sudo pip install pandas
    
### How to Run
This python script does not take any command line arguments, so to run the script command is next:

    $ python ble_scan.py
    
This will print number of bluetooth devices found on the terminal and log retrived data in a csv file. That's it. Hope this helps.
