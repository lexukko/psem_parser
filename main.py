import sys
from myutils import IsValidHexStr, HexStrToByteArray
from response_parsers import response_parsers
from request_parsers import request_types
from packet import parser_packet


def list():
    print("response parsers")
    for k,v in response_parsers.items():
        print('{}{:02x} - {} - {}'.format('0x',k,v.__name__,request_types[k]))
        


if __name__ == '__main__':
    no_args = len(sys.argv)

    if no_args in (2,3,4):
        if no_args == 2 and sys.argv[1] == 'list':
            list()
        elif no_args == 3 and IsValidHexStr(sys.argv[1]) and sys.argv[2] == 'request':
            print("request <byte array> <request>")
            data_str = IsValidHexStr(sys.argv[1])
            if data_str is not None:
                data_arr = HexStrToByteArray(data_str)
                parser_packet(data_arr,"request")
        elif no_args == 4 and IsValidHexStr(sys.argv[1]) and sys.argv[2] == 'response' and int(sys.argv[3],16) in response_parsers.keys():
            data_str = IsValidHexStr(sys.argv[1])
            if data_str is not None:
                data_arr = HexStrToByteArray(data_str)
                parser_packet(data_arr,"response", int(sys.argv[3],16))
        else:
            print("Error Sintaxis incorrecta.")
            print("Uso: python main.py list")
            print("Uso: python main.py [Hex String] [request]")
            print("Uso: python main.py [Hex String] [response] [Hex response id]")
    else:
        print("Error numero de parametros incorrecto.")
        print("Uso: python main.py list")
        print("Uso: python main.py [Hex String] [request]")
        print("Uso: python main.py [Hex String] [response] [Hex response id]")

