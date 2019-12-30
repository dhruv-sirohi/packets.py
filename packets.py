def packet_size(packet):
    '''
    (List[int]) -> int
    Returns length of packet in bits given as input
    >>> packet_size([0,1,0,1]) 
    4
    >>> packet_size([0,1,0,1,1,1]) 
    6
    >>> packet_size([0,1,0,1,1]) 
    5
    '''
    return(len(packet))

def error_indices(packet1, packet2):
    '''
    (List[int], List[int]) -> List[int]
    Returns list of all the indices of packet1 which do not match the equivalent indices in packet2
    >>> error_indices([0,1,1,1], [1,1,0,1]) 
    [0, 2] 
    >>> error_indices([1,1,0,1], [1,1,0,1]) 
    []
    >>> error_indices([1,0,0,1], [1,1,0,1]) 
    [1] 
    '''
    error = []
    for i in range(0,packet_size(packet1),1):
        if packet1[i] != packet2[i]:
            error.append(i)
    return error

def packet_diff(packet1, packet2):
    '''
    (List[int],List[int]) -> int
    Returns number of bit errors that occurred during transmission from packet1 to packet 2
    >>> packet_diff([0,1,0,1], [1,1,0,1]) 
    1 
    >>> packet_diff([0,1,1,0], [0,1,1,0])     
    0
    >>> packet_diff([0,1,1,1], [1,1,0,1]) 
    2
    '''
    errors = 0
    for i in range(0,packet_size(packet1),1):
        if packet1[i] != packet2[i]:
            errors += 1
    return errors

if __name__ == "__main__":
    # test your bit error rate detector here
    print("Testing Functions...")
