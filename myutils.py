def ByteArrayToHexStr(arr,sep=' ', prefix='0x'):
    return sep.join( '{}{:02x}'.format(prefix,item) for item in arr)
