from myutils import ByteArrayToHexStr

# DataStructures
psem_responses = {

    0x00: { 'code' : '<ok>', 'name' : 'Acknowledge', 'desc' : 'No problems, request accepted.' },
    0x01: { 'code' : '<err>', 'name' : 'Error', 'desc' : 'This code is used to indicate rejection of the received service request.  The reason for the rejection is not provided.' },
    0x02: { 'code' : '<sns>', 'name' : 'Service Not Supported', 'desc' : 'This Application-level error response will be sent to the device when the requested service is not supported.  This error indicates that the message was valid, but the request could not be honored. The <sns> error response has special implications in the context of a response to a Logoff, Terminate or Disconnect service request.  Specifically, a C12.22 Node in the Session State shall not issue this error, but it is permitted if the C12.22 Node only supports sessionless communication.' },
    0x03: { 'code' : '<isc>', 'name' : 'Insufficient Security Clearance', 'desc' : 'This Application-level error indicates that the current authorization level is insufficient to complete the request.' },
    0x04: { 'code' : '<onp>', 'name' : 'Operation Not Possible', 'desc' : 'This Application-level error will be sent to the device which requested an action that is not possible.   This error indicates that the message was valid, but the message could not be processed and covers conditions such as: invalid <length> or invalid <offset>. It can also be issued if the operation is not possible under the current C12.22 Node configuration.' },
    0x05: { 'code' : '<iar>', 'name' : 'Inappropriate Action Requested', 'desc' : 'This Application-level error indicates that the action requested was inappropriate.  Covers conditions such as a Write Service request to a read-only Table or an invalid Table identifier.' },
    0x06: { 'code' : '<bsy>', 'name' : 'Device Busy', 'desc' : 'This Application-level error indicates that the request was not acted upon because the device was busy doing something else. The operation may be retried at a later time with success, as the data may then be ready for transportation during this active communication.' },
    0x07: { 'code' : '<dnr>', 'name' : 'Data Not Ready', 'desc' : 'This Application-level error indicates that request was unsuccessful because the requested data is not ready to be accessed.' },
    0x08: { 'code' : '<dlk>', 'name' : 'Data Locked', 'desc' : 'This Application-level error indicates that the request was unsuccessful because the data cannot be accessed.' },
    0x09: { 'code' : '<rno>', 'name' : 'Renegotiate Request', 'desc' : 'This Application-level error indicates that the responding device wishes to return to the identification or Base State and renegotiate communication parameters.' },

    0x0A: { 'code' : '<isss>', 'name' : 'Invalid Service Sequence State', 'desc' : 'This Application-level error indicates that the request cannot be accepted at the current service sequence state.  For more information on service sequence states, see Annex D.  This is an indication to the C12.22 Application not to reissue this request at this time because there is a service sequence state problem or an out-of-order operations problem.' },
    0x0B: { 'code' : '<sme>', 'name' : 'Security Mechanism Error', 'desc' : 'This Application-level error may be returned when a security mechanism error is detected. This code covers errors such as a security mechanism not being supported and invalid encryption key.' },
    0x0C: { 'code' : '<uat>', 'name' : 'Unknown Application Title', 'desc' : 'This Application-level error may be returned by a C12.22 Relay or the target node when an unknown or invalid <called-aptitle> is received.' },
    0x0D: { 'code' : '<nett>', 'name' : 'Network Time-out', 'desc' : 'This Application-level error may be returned when a Network Time-out is detected.' },
    0x0E: { 'code' : '<netr>', 'name' : 'Network Not Reachable', 'desc' : 'This Application-level error may be returned when a node is not reachable.' },
    0x0F: { 'code' : '<rqtl>', 'name' : 'Request Too Large', 'desc' : 'This Application-level error may be returned when the request size is too large.' },

    0x10: { 'code' : '<rstl>', 'name' : 'Response Too Large', 'desc' : 'This Application-level error may be returned when the response size of a response is too large.' },
    0x11: { 'code' : '<sgnp>', 'name' : 'Segmentation not possible', 'desc' : 'This Application-level error may be returned when a C12.22 Node received a segment and does not support the Application Segmentation Sub-Layer.' },
    0x12: { 'code' : '<sgerr>', 'name' : 'Segmentation error', 'desc' : 'This Application-level error may be returned when a C12.22 Node fail to segment or reassemble an <acse-pdu>.' },

}

# parsers

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

response_parsers = {
    0x20 : parser_default_response,

    0x30 : parser_read_response,
    0x31 : parser_read_response,
    0x32 : parser_read_response,
    0x33 : parser_read_response,
    0x34 : parser_read_response,
    0x35 : parser_read_response,
    0x36 : parser_read_response,
    0x37 : parser_read_response,
    0x38 : parser_read_response,
    0x39 : parser_read_response,
    0x3E : parser_read_response,
    0x3F : parser_read_response,

    0x40 : parser_default_response,
    0x41 : parser_default_response,
    0x42 : parser_default_response,
    0x43 : parser_default_response,
    0x44 : parser_default_response,
    0x45 : parser_default_response,
    0x46 : parser_default_response,
    0x47 : parser_default_response,
    0x48 : parser_default_response,
    0x49 : parser_default_response,
    0x4F : parser_default_response,

    0x50 : parser_default_response,
    0x51 : parser_default_response,
    0x52 : parser_default_response,
    0x21 : parser_default_response,
    0x22 : parser_default_response,
    0x70 : parser_default_response,
    0x27 : parser_default_response,
    0x24 : parser_default_response,
    0x25 : parser_default_response,
    0x26 : parser_default_response,

    0x60 : parser_default_response,
    0x61 : parser_default_response,
    0x62 : parser_default_response,
    0x63 : parser_default_response,
    0x64 : parser_default_response,
    0x65 : parser_default_response,
    0x66 : parser_default_response,
    0x67 : parser_default_response,
    0x68 : parser_default_response,
    0x69 : parser_default_response,
    0x6A : parser_default_response,
    0x6B : parser_default_response,

    0x72 : parser_default_response,
    0x73 : parser_default_response,
    0x74 : parser_default_response,
    0x77 : parser_default_response,
    0x75 : parser_default_response,
    0x76 : parser_default_response
}