# Amazon Dash Listener
Python scripts to listen for an Amazon Dash Button press and perform a custom action. In this case, toggle on/off a set of Philips Hue lights.

## Prerequisites
* Python 2.7
* scapy
* pycurl
* urllib2

## Instructions
* Follow [Amazon's instructions](https://www.amazon.com/gp/help/customer/display.html?nodeId=201746340) to set up a new Dash Button. Cancel the setup process before adding a product to purchase, or you'll end up buying something every time you perform your action!
* Find the MAC Address of your Amazon Dash Button. I used Wireshark with the "bootp" filter to find a BOOTP packet with source MAC address beginning with "AmazonTe_" or "74:75:48" whenever the Dash Button is pressed.
* Edit the `button_press.py` script to include the Dash Button's MAC address and perform your custom action.
* To use with Philips Hue, follow the [setup instructions](https://www.developers.meethue.com/documentation/getting-started). Update the `light.py` script with your Bridge's IP address, user ID, and light group IDs.
* Modify the `button_listener.service` file with the correct location of the python script.
* Place the `button_listener.service` in the `/etc/systemd/system folder`.
* Run `sudo systemctl enable button_listener.service` to enable the service to run on boot.
* Run `sudo systemctl start button_listener.service` to start the service.
* Verify the service is running with `systemctl status button_listener.service`.