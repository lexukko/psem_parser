
# psem responses
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

# request
requests_types = {
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

    0x72 : 'Get Configuration Service ',
    0x73 : 'Link Control Service',
    0x74 : 'Send Message Service',
    0x77 : 'Send Message Service (short)',
    0x75 : 'Get Status Service',
    0x76 : 'Get Registration Status Service'
}