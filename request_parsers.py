from myutils import ByteArrayToHexStr

# DataStructures

request_types = {
    0x20 : 'Identification Service',

    0x30 : 'Read Service (Full Read)',
    0x31 : 'Read Service (Index Read)',
    0x32 : 'Read Service (Index Read)',
    0x33 : 'Read Service (Index Read)',
    0x34 : 'Read Service (Index Read)',
    0x35 : 'Read Service (Index Read)',
    0x36 : 'Read Service (Index Read)',
    0x37 : 'Read Service (Index Read)',
    0x38 : 'Read Service (Index Read)',
    0x39 : 'Read Service (Index Read)',
    0x3E : 'Read Service (Default)',
    0x3F : 'Read Service (Octet/Offset Count)',

    0x40 : 'Write Service (Full)',
    0x41 : 'Write Service (Index Write)',
    0x42 : 'Write Service (Index Write)',
    0x43 : 'Write Service (Index Write)',
    0x44 : 'Write Service (Index Write)',
    0x45 : 'Write Service (Index Write)',
    0x46 : 'Write Service (Index Write)',
    0x47 : 'Write Service (Index Write)',
    0x48 : 'Write Service (Index Write)',
    0x49 : 'Write Service (Index Write)',
    0x4F : 'Write Service (Octet/Offset Count)',

    0x50 : 'Logon Service',
    0x51 : 'Security Service',
    0x52 : 'Logoff Service',
    0x21 : 'Terminate Service',
    0x22 : 'Disconect Service',
    0x70 : 'Wait Service',
    0x27 : 'Registration Service',
    0x24 : 'Deregistration Service',
    0x25 : 'Resolve Service',
    0x26 : 'Trace Service',

    0x60 : 'Negotiate Service',
    0x61 : 'Negotiate Service (Baud Rate included)',
    0x62 : 'Negotiate Service (Baud Rate included)',
    0x63 : 'Negotiate Service (Baud Rate included)',
    0x64 : 'Negotiate Service (Baud Rate included)',
    0x65 : 'Negotiate Service (Baud Rate included)',
    0x66 : 'Negotiate Service (Baud Rate included)',
    0x67 : 'Negotiate Service (Baud Rate included)',
    0x68 : 'Negotiate Service (Baud Rate included)',
    0x69 : 'Negotiate Service (Baud Rate included)',
    0x6A : 'Negotiate Service (Baud Rate included)',
    0x6B : 'Negotiate Service (Baud Rate included)',

    0x72 : 'Get Configuration Service',
    0x73 : 'Link Control Service',
    0x74 : 'Send Message Service',
    0x77 : 'Send Message Service (short)',
    0x75 : 'Get Status Service',
    0x76 : 'Get Registration Status Service'
}

# -- Parsers

def parser_default_request(data):
    print("Default Request Parser")
    print("")
    print("Raw Data [ Hex: {} ]".format(ByteArrayToHexStr(data)))
    print("")
    print("Request Type: {}".format(request_types[data[0]]))

def parser_read_offset_octet_request(data):
    if data[0] == 0x3f and len(data) == 8:
        print("{}".format(request_types[data[0]]))
        print("")
        print("Raw Data [ Hex: {} ]".format(ByteArrayToHexStr(data)))
        print("")
        print("tableid [ Hex {}, Int16 {} ]".format(ByteArrayToHexStr(data[1:3]), int.from_bytes(data[1:3], byteorder='big', signed=False)))
        print("offset [ Hex {}, Word24 {} ]".format(ByteArrayToHexStr(data[3:6]), int.from_bytes(data[3:6], byteorder='big', signed=False)))
        print("octet count [ Hex {}, Int16 {} ]".format(ByteArrayToHexStr(data[6:8]), int.from_bytes(data[6:8], byteorder='big', signed=False)))
    else:
        print("Error: Invalid Request Parser.")

# ---

request_parsers = {
    0x20 : parser_default_request,

    0x30 : parser_read_offset_octet_request,
    0x31 : parser_read_offset_octet_request,
    0x32 : parser_read_offset_octet_request,
    0x33 : parser_read_offset_octet_request,
    0x34 : parser_read_offset_octet_request,
    0x35 : parser_read_offset_octet_request,
    0x36 : parser_read_offset_octet_request,
    0x37 : parser_read_offset_octet_request,
    0x38 : parser_read_offset_octet_request,
    0x39 : parser_read_offset_octet_request,
    0x3E : parser_read_offset_octet_request,
    0x3F : parser_read_offset_octet_request,

    0x40 : parser_default_request,
    0x41 : parser_default_request,
    0x42 : parser_default_request,
    0x43 : parser_default_request,
    0x44 : parser_default_request,
    0x45 : parser_default_request,
    0x46 : parser_default_request,
    0x47 : parser_default_request,
    0x48 : parser_default_request,
    0x49 : parser_default_request,
    0x4F : parser_default_request,

    0x50 : parser_default_request,
    0x51 : parser_default_request,
    0x52 : parser_default_request,
    0x21 : parser_default_request,
    0x22 : parser_default_request,
    0x70 : parser_default_request,
    0x27 : parser_default_request,
    0x24 : parser_default_request,
    0x25 : parser_default_request,
    0x26 : parser_default_request,

    0x60 : parser_default_request,
    0x61 : parser_default_request,
    0x62 : parser_default_request,
    0x63 : parser_default_request,
    0x64 : parser_default_request,
    0x65 : parser_default_request,
    0x66 : parser_default_request,
    0x67 : parser_default_request,
    0x68 : parser_default_request,
    0x69 : parser_default_request,
    0x6A : parser_default_request,
    0x6B : parser_default_request,

    0x72 : parser_default_request,
    0x73 : parser_default_request,
    0x74 : parser_default_request,
    0x77 : parser_default_request,
    0x75 : parser_default_request,
    0x76 : parser_default_request
}