import re

def ByteArrayToHexStr(arr,sep=' ', prefix='0x'):
    return sep.join( '{}{:02x}'.format(prefix,item) for item in arr)

def HexStrToByteArray(hex_str):
    byte_array = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]
    byte_array = [int(h,16) for h in byte_array]
    return byte_array

# valida si una cadena de valores Hexadecimales es correcta, quita espacios, '0x', ','
# valida que la cantidad de caracteres sea par
# valida que solo contenga valores Hexadecimales correctos [0-9] y ABCDEF
# devuelve la cadena de ser correcta de lo contrario devuelve None
def IsValidHexStr(hex_str):
    clean_hex_str = hex_str.replace("0x","").replace(" ","").replace(",","")
    match = re.search("^([0-9]|[ABCDEFabcdef])*",clean_hex_str)
    if len(clean_hex_str) > 0 and ( len(clean_hex_str) % 2 ) == 0 and match.end() == len(clean_hex_str):
        return clean_hex_str
    else: 
        return None 

if __name__ == "__main__":
    print(IsValidHexStr('0x33, 0xFF, 0xee'))
    print(HexStrToByteArray(IsValidHexStr('0x33, 0xFF, 0xee')))