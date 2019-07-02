#! /usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface that needs to be changed")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please Specify an interface to use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please Specify a new MAC to use --help for more info")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC Address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    result = subprocess.check_output(["ifconfig", interface])
    newmac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result)

    if newmac:
        return newmac.group(0)

    else:
        print("[-] No Such device")

    return


options = get_arguments()
current_mac = get_current_mac(options.interface)
print("CURRENT MAC = " + str(current_mac))
change_mac(options.interface, options.new_mac)
changed_mac = get_current_mac(options.interface)
if changed_mac == options.new_mac:
    print("[+} MAC ADDRESS was successfully changed to " + changed_mac)
else:
    print("[-] MAC Address could not be changed")

