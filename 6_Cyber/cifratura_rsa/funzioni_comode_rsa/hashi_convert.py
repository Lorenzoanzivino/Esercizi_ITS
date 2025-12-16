def hashi_convert(msg:str) -> int:

    return int(''.join([str(ord(x)) for x in msg]))


def s2n(s):
    tot = 0
    esp = 0

    for c in s:
        tot += 256**esp*ord(c)
        esp += 1

    return tot
    

def s2ne(s):
    tot = 0

    for c in s:
        tot = (tot<<8)|ord(c)  # | or binario

    return tot


# algoritmo di diffie helman
