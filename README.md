# Seestar S50 Control from NINA running in a Windows 11 Virtual Machine on a Linux system

Peter D. Wilson
Mascot, New South Wales, Australia
2026-02-16 (last updated 2026-02-26)

Following the opening of access to ZWO Seestar S50 smart telescopes as ASCOM Alpaca devices, many on-line tutorials have been published (see a list of those I have viewed below). All assume that the user will be running NINA on a native Windows 11 platform.

Running NINA on a Windows virtual machine hosted on a Linux system appears to cause serious issues with the Alpaca discovery process. Specifically, I am running Windows 11 in a Docker container packaged by Winboat (https://www.winboat.app) hosted on a Linux Mint 22.3 platform.

This note documents a workflow that allowed my Seestar S50 to connect to my instance of NINA running on a Linux-hosted Windows 11 virtual machine.

## Connecting on my Linux machine

Using utilities on the Linux machine, I could identify the IP address of my Seestar S50 on my home LAN (note the Seestar must be started in “station mode”).

I adapted demonstration Python code from the documentation for Alpyca, the ASCOM Alpaca Python module. One script, *Seestar_discovery_test_alpyca.py*, provided information on the port used by my Seestar S50. A second script, *Seestar_server_info_alpyca.py*, was used to confirm that all the compomnent devices could be found. Finally a third script, *Seestar_connection_test_alpyca.py*, was used to confirm that connection could be made using the IP and port details, and that control commands would be correctly dealt with by the Seestar.

In addition, I could use Firefox to access and control the Seestar via Alpaca web interface hosted by the Seestar. I was able to control each of the component devices (camera, focusser, mount (or “telescope”), filter wheel, dew heater function) through this web interface.

## Windows 11 machine in a Linux-hosted container environment

Running NINA on the Windows implementation running in a container hosted by Linux failed to “see” the Seestar S50.

I could connect to the Seestar using the IP address and port number identified on the Linux host system in a Windows version of Firefox (i.e. 192.168.1.22:32323), and I could control the Seestar's device through the Alpaca web interface. However, running the Python discovery script on the Windows machine could not “see” LAN addresses. The only addresses resolved by this process were 172.0.0.1 (a bridge service?) and 127.0.0.1 (localhost on the Windows virtual machine).

Even though Firefox was successfully bridging from the container environment to access the Internet and LAN IP  addresses, the Alpaca discovery process could not find the Seestar S50 Alpaca server at address 192.168.1.22:32323.

So, definitely the problem is the Alpaca discovery process failing to find a bridge to LAN addresses. This explains why NINA could not find the Seestar and its devices. However, an additional question was “why doesn’t NINA list any Alpaca devices”. A number of tutorial videos suggested that his should be automatically available, but clearly the communication glitch NINA experiences on the Windows containerised machine is causing grief.

After many hours of research, trial and (much) error, this Google search, "is there any way alpaca device ip address can be set in nina", lead to a breakthrough. Listings shown by this query provided a number of methods for assigning a fixed IP address for each device and allowed me to generate ASCOM drivers which linked to the Alpaca services supplied by the Seestar S50.

This note documents a workflow that allowed my Seestar S50 to connect to my instance of NINA running on a Linux-hosted Windows 11 virtual machine.

### First steps:
   
On the **Linux** host, establish the correct IP address and port number for the device. To avoid chaos and confusion, you should be sure to have **only one** Seestar or other Alpaca-capable device active during these procedures.
   
+ Power up the Seestar S50 and make sure it is in "Station" mode
      
+ Find the S50's IP address on the network (i.e login to your router via the Linux host and find allocated IP address)
      
+ Run the Python script Seestar_discovery_test_alpyca.py and note the reported port number for the Seestar S50 Alpaca server. Typically, for a single device on the network this will port 32323 with the default discovery port 32227. However, note that the Alpaca documentation states that other port numbers may also be present, presumably to avoid conflicts when multiple Alpaca servers are discovered on the same LAN.
      
+ Test the IP and port combination using a web browser on the Linux host and also in the Windows virtual machine: You should see an Alpaca webpage which lets you connect each device within the S50 (eg camera, focuser, filter wheel, switch (dew heater) and telescope (aka mount)

+ Test that correct information about the Seestar's devices is listed by running the Python script *Seestar_server_info_alpyca.py*. (This step is optional but it does give you a complete understanding of the correct functioning of the ASCOM Aplaca interface).

+ Test connection on both Linux and Windows machines using the Python script *Seestar_connection_test_alpyca.py* and the IP address and port number combination.

### Next phase:

The next phase steps through the process of generating ASCOM Alpaca interface drivers on the **Windows** system for each device within the Seestar:

- Start ASCOM Diagnostics program: Click on the Start icon on the Windows 11 Task Bar, then click on the “All” option in the top right corner of the popup window. The ASCOM diagnostics program should appear at the top of the “A” section in the list of applications.
      
- Click on Choose Device
      
- Select Choose and Connect to Device
      
- For each Device Type (Camera, Telescope, Filter Wheel and Focuser):
      
   - Click Choose button to open a Chooser window:

      - Select the Alpaca tab

      - Make sure that Enable Alpaca Discovery is selected

      - Select Create Alpaca Driver from drop down list

      - Enter a name e.g. Seestar S50 in the popup dialog

      - Click on the Properties button to open a "Configuration" window:

                1. Select "IPv4 Only" in the "Supported IP Version(s)" control

                2. Change "Remote Device and Host or IP Address to the Seestar's IP address discovered earlier

                3. Change the "Alpaca Port Number" to the communications port number discovered earlier

                4. Click OK

       - Click OK in the Chooser Window

       - Click "Connect" button in Device Connection Tester window and check that connection is made and device attributes are correctly reported

### Final testing:

- Start NINA in the **Windows** machine and be sure that the Seestar S50 is powered on and in "Station" mode
      
- Select "Equipment" and test your connection to each device (Camera, Telescope, Filter Wheel, Switch (Dew Heater), and Focuser):

   - Click on the scan button for a selected device (it may take quite some time to complete a scan)
  
   - When scan is finished, look for a "Seestar S50" entry under ASCOM drivers
  
   - Test that connection is successful (eg that 3 filters are shown in Filter device and that you can hear the S50 change filters when you command a filter change; for the telescope (aka mount) the arm should move up and down using the N and S controls and close when the Park control is activated))
      
**Yeah! We can now do stuff!**
