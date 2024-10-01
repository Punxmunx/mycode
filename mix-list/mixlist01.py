#!/usr/bin/env python3
def main():
    my_list = [ "192.168.0.5", 5060, "UP"]
    iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
    print("The IP items in the list (IP): " + my_list[0])
    print("the other IPs:" + str(iplist[3:5]))
    print("The second item in the list (port): " + str(my_list[1]) )
    print("The last item in the list (state): " + my_list[2] )
main()
