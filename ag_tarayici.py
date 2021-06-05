import scapy.all as scapy
import optparse

def use_input():
    parse_obje = optparse.OptionParser()
    parse_obje.add_option("-i","--ipaddress",dest="ipadres",help="Taranacak ip address :")
    return parse_obje.parse_args()
def scan_natwork(ipadres):
    arp_request_packet = scapy.ARP(pdst=ipadres)
    brdoadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combinet_packet = brdoadcast_packet/arp_request_packet
    (cevaplanan_list,cevaplanmayan_list) = scapy.srp(combinet_packet,timeout=1)
    cevaplanan_list.summary()
(users_input,arguments) = use_input()
if not users_input.ipadres:
    print("IP ADRES GIRINIZ !")
scan_natwork(users_input.ipadres)
