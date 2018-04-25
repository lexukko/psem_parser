import sys
from myutils import ByteArrayToHexStr
from psem_data import psem_responses, requests_types

def parser_default_request(data):
    print("Default Request Parser")
    print("")
    print("Raw Data [ Hex: {} ]".format(ByteArrayToHexStr(data)))
    print("")
    print("Request Type: {}".format(requests_types[data[0]]))

def parser_read_offset_octet_request(data):
    if data[0] == 0x3f and len(data) == 8:
        print("{}".format(requests_types[data[0]]))
        print("")
        print("Raw Data [ Hex: {} ]".format(ByteArrayToHexStr(data)))
        print("")
        print("tableid [ Hex {}, Int16 {} ]".format(ByteArrayToHexStr(data[1:3]), int.from_bytes(data[1:3], byteorder='big', signed=False)))
        print("offset [ Hex {}, Word24 {} ]".format(ByteArrayToHexStr(data[3:6]), int.from_bytes(data[3:6], byteorder='big', signed=False)))
        print("octet count [ Hex {}, Int16 {} ]".format(ByteArrayToHexStr(data[6:8]), int.from_bytes(data[6:8], byteorder='big', signed=False)))
    else:
        print("Error: Invalid Request Parser.")

def parser_default_response(data):
    print("Default Response Parser")
    print("")    
    print("Raw Data [ Hex: {} ]".format(ByteArrayToHexStr(data)))
    print("")
    print("Code: {}".format(psem_responses[data[0]]['code']))
    print("Name: {}".format(psem_responses[data[0]]['name']))
    print("Description: {}".format(psem_responses[data[0]]['desc']))

def parser_read_response(data):
    psem_code = data[0]
    count = data[1:3]
    data_serv = data[3:-1]
    chksum = data[-1]

    print("Read Response Parser")
    print("---")    
    print("Raw Data [ Hex: {} ]".format(ByteArrayToHexStr(data)))
    print("")
    print("Code: {}".format(psem_responses[psem_code]['code']))
    print("Name: {}".format(psem_responses[psem_code]['name']))
    print("Description: {}".format(psem_responses[psem_code]['desc']))   
    print("")
    count_int16 = int.from_bytes(count, byteorder='big', signed=False)
    print("Count [ Hex: {}, Int16 : {} ]".format(ByteArrayToHexStr(count), count_int16))
    print("")
    print("Data [ Hex: {} ]".format(ByteArrayToHexStr(data_serv)))
    print("")
    print("cksum [ Hex: {:02x}, Int8 : {} ]".format(chksum, chksum))
    print("")
    if count_int16 == len(data_serv):
        print("response status :) !!")
    else:
        print("response status :( !!")

# parsers
packet_data_parsers = {
    'request':{
        'default':{
            'default_request'  : parser_default_request
        },
        'custom':{
            'read_offset_octet' : parser_read_offset_octet_request
        }
    },
    'response':{
        'default':{
            'default_response' : parser_default_response,
        },
        'custom':{
            'read_response' : parser_read_response
        }
    }
}

def parser_packet(data, parser_type, parser_category, parser_name):

    # string parameter 1 to byte array
    packet_array = data.replace(" ","")
    packet_array = [packet_array[i:i+2] for i in range(0, len(packet_array), 2)]
    packet_array = [int(h,16) for h in packet_array]

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
    packet_data_parsers[parser_type][parser_category][parser_name](data_packet)
    print("")

    print("<crc>        = {}{:02x}".format('0x',packet_array[-2]))
    print("<crc>        = {}{:02x}".format('0x',packet_array[-1]))

def process_arguments():
    data = None
    parser_type = None
    parser_category = None
    parser_name = None
    no_params = len(sys.argv) - 1

    if  no_params in (2,3):

        data = sys.argv[1]
        
        if sys.argv[2] in packet_data_parsers.keys():
            parser_type = sys.argv[2]
            parser_category = 'default'
            if parser_type == 'request':
                parser_name = 'default_request'
            else:
                parser_name = 'default_response'    
        else:
            print("Error: Invalid parser type.")
            print("Usage: packet.py ARRAY [request|response]")
            print("Usage: packet.py ARRAY [request|response] parser_name")
            exit(0)    
        if no_params == 3:
            if sys.argv[3] in packet_data_parsers[parser_type]['custom']:
                parser_name = sys.argv[3]
                parser_category = 'custom'

    else:
        print("Error: Not Enought parameters.")
        print("Usage: packet.py ARRAY [request|response]")
        print("Usage: packet.py ARRAY [request|response] parser_name")
        exit(0)

    
    return (data, parser_type, parser_category, parser_name)

if __name__ == "__main__":
    print("")
    print("C1219 Packet Parser v1.1")
    print("")
    data, parser_type, parser_category, parser_name = process_arguments()
    parser_packet(data, parser_type, parser_category, parser_name)

