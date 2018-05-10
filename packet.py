import sys
from myutils import HexStrToByteArray, IsValidHexStr
from request_parsers import request_parsers
from response_parsers import response_parsers

def parser_packet(data, parser_type, response_parser_id=None):
    # string parameter 1 to byte array
    packet_array = data 

    # validar si el primer byte es un ack = 0x16 y removerlo pre validacion
    if packet_array[0] == 0x06:
        print("\nPrimer byte es un <ack = 0x06> del servidor. a sido removido!\n")
        packet_array = packet_array[1:]

    # packet length
    packet_length = int.from_bytes(packet_array[4:6], byteorder='big', signed=False)
    print("Data length {}".format(packet_length))

    # packet payload (data)
    data_packet = packet_array[6:-2]

    print("")
    print("<stp>        = {}{:02x}".format('0x',packet_array[0]))
    print("<identity>   = {}{:02x}".format('0x',packet_array[1]))
    print("<ctrl>       = {}{:02x}".format('0x',packet_array[2]))
    print("<seq-nbr>    = {}{:02x}".format('0x',packet_array[3]))

    print("<length>     = {}{:02x}".format('0x',packet_array[4]))
    print("<length>     = {}{:02x}".format('0x',packet_array[5]))

    # llama un parser de packet_data_parsers
    print("")
    if parser_type == "request":
        if data_packet[0] in request_parsers.keys():
            request_parsers[data_packet[0]](data_packet)
    elif parser_type == "response":
        if response_parser_id in response_parsers.keys():
            response_parsers[response_parser_id](data_packet)
    print("")

    print("<crc>        = {}{:02x}".format('0x',packet_array[-2]))
    print("<crc>        = {}{:02x}".format('0x',packet_array[-1]))

if __name__ == "__main__":
    #data_str = IsValidHexStr("EE 88 20 00 00 08 3F 08 16 00 00 00 00 0A 1C E0")
    #data_arr = HexStrToByteArray(data_str)
    #parser_packet(data_arr,"request")

    data_str = IsValidHexStr("EE 00 20 00 00 0E 00 00 0A 00 04 08 14 0C 18 17 0A 13 17 71 90 BF")
    data_arr = HexStrToByteArray(data_str)
    parser_packet(data_arr,"response", 0x3f)