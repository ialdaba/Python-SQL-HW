#-------------------------------------------------------------------------------
# Name: Isabel Angela Rinonos Aldaba
# Project 5
# Due Date: 4/22/2018
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: TAs
#-------------------------------------------------------------------------------
# Comments and assumptions: Included below
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
#        10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------

def is_valid_mapping(mapping):
    
    # valid only if their keys are all the same length, their values are all the 
    # same length, their keys are unique, and their values are unique
    
    keys_list = []
    vals_list = []
    
    result = True
    # create keys_list
    for key in mapping.keys():
        keys_list.append(key)
    
    standard_key = len(keys_list[0])
    
    # create vals_list
    #for val in mapping.values():
        #vals_list.append(val)
    vals_list = list(mapping.values())
    
    standard_val = len(vals_list[0])
    
    for key in keys_list:
        # keys are same length
        if len(key) != standard_key:
            result = False
        # keys are unique
        count = 0
        for element in keys_list:
            if element == key:
                count += 1
        if count > 1:
            result = False
           
    for val in vals_list:
        # values are same length
        if len(val) != standard_val:
            result = False
        # values are unique
        count = 0
        for element in vals_list:
            if element == val:
                count += 1
        if count > 1:
            result = False
    
    return result

def is_valid_mapping_for_message(mapping, message): 
    # check if everything you need to encode in message is a 
    # key in mapping
    
    # create keys_list
    keys_list = list(mapping.keys())
    len_key = len(keys_list[0])
    result = True
    new_len_key = len_key
    start_pos = 0
    i = 0
    
    while i < len(keys_list):
        slice =  message[start_pos:new_len_key]
        no_match = 0
        for key in keys_list:
            if slice not in key:
                no_match += 1
        if no_match == len(keys_list):
            result = False
        i += 1
        start_pos += len_key
        new_len_key += len_key
                   
    return result


def reverse_mapping(mapping):
    reverse = {}
    keys_list = list(mapping.values())
    values_list = list(mapping.keys())
    
    for i in range(len(keys_list)):
        key = keys_list[i]
        value = values_list[i]
        reverse[key] = value
           
    return reverse

def combine_mapping(mapping1, mapping2):
    
    mapping = {}
    merged_keys = list(mapping1.keys()) + list(mapping2.keys())
    merged_values = list(mapping1.values()) + list(mapping2.values())
    
    for i in range(len(merged_keys)):
        key = merged_keys[i]
        value = merged_values[i]
        mapping[key] = value
    
    for key in mapping1.keys():
    	if mapping1[key] != mapping[key]:
    		return None
    
    for key in mapping2.keys():
    	if mapping2[key] != mapping[key]:
    		return None
        
    if is_valid_mapping(mapping) is False:
        return None

    if is_valid_mapping(mapping) is True:
        return mapping

def message_statistics(message, encoded_message):

    d = {}
    list(message)
    list(encoded_message)
    
    for letter in message:
        counta = 0
        countb = 0
        for element in message:
            if element == letter:
                counta += 1
        stat = [counta, countb]
        d[letter] = stat
    
    for letter in encoded_message:
        counta = 0
        countb = 0
        for item in message:
            if letter == item:  
                counta += 1
        for element in encoded_message:
            if element == letter:
                countb += 1
        stat = [counta, countb]
        d[letter] = stat
        
    return d

def substitution_encode(mapping, message):
    
    encode = ""
    keys_list = list(mapping.keys())
    len_key = len(keys_list[0])
    new_len_key = len_key
    start_pos = 0
    i = 0
    
    while i < len(message):
        slice =  message[start_pos:new_len_key] 
        if slice in mapping.keys():
            encode = encode + mapping[slice]
        i += len_key
        start_pos += len_key
        new_len_key += len_key
        
    return encode

def substitution_decode(mapping, message):
    
    decode = ""
    vals_list = list(mapping.values())
    len_val = len(vals_list[0])
    new_len_val = len_val
    start_pos = 0
    i = 0
    
    while i < len(message):
        slice =  message[start_pos:new_len_val]
        for key, value in mapping.items():
            if slice == value:
                decode = decode + key
        i += len_val
        start_pos += len_val
        new_len_val += len_val
        
    return decode

def get_caesar_mapping(shift, message): 

# return the smallest encoding dictionary needed to encode the message
    d = {}
    
    
    for element in message:
        num = ord(element) + shift
        if num > 126:
            num = 31 + (num - 126)
        if num < 32:
            num = 127 - (32 - num)
        d[element] = chr(num)
       
    return d

def caesar_encode(shift, message):


	mapping = get_caesar_mapping(shift, message)

	encoded_message = substitution_encode(mapping, message)
    
	return encoded_message

def caesar_decode(shift, message): 
    
    mapping = {}
    
    
    for element in message:
        num = ord(element) - shift
        if num > 126:
            num = 31 + (num - 126)
        if num < 32:
            num = 127 - (32 - num)
        mapping[element] = chr(num)

    decode = ""
    vals_list = list(mapping.values())
    len_val = len(vals_list[0])
    new_len_val = len_val
    start_pos = 0
    i = 0
    
    while i < len(message):
        slice =  message[start_pos:new_len_val]
        for key, value in mapping.items():
            if slice == key:
                decode = decode + value
        i += len_val
        start_pos += len_val
        new_len_val += len_val
    
    return decode

def vigenere_encode(secret, message):

    encode = ""
    list_shifts = []
    i = 0
    
    for letter in secret:
        shift = ord(letter) - ord('a')
        list_shifts.append(shift)
    
    for character in message:
        if i > len(list_shifts) - 1:
            i = 0
        shift = list_shifts[i]
        
        num = ord(character) + shift
        if num > 126:
            num = 31 + (num - 126)
        if num < 32:
            num = 127 - (32 - num)
            
        encode = encode + chr(num)
        
        if i <= len(list_shifts) - 1:
            i += 1
            
    return encode

def vigenere_decode(secret, message):

    decode = ""
    list_shifts = []
    i = 0
    
    for letter in secret:
        shift = ord(letter) - ord('a')
        list_shifts.append(shift)
    
    for character in message:
        if i > len(list_shifts) - 1:
            i = 0
        shift = list_shifts[i]
        
        num = ord(character) - shift
        if num > 126:
            num = 31 + (num - 126)
        if num < 32:
            num = 127 - (32 - num)
            
        decode = decode + chr(num)
        
        if i <= len(list_shifts) - 1:
            i += 1
            
    return decode


def rail_encode(num_rails, message):
    
    encode = ""
    cycle = (num_rails * 2) - 2
            
    # edit message
    message = message.upper()
    
    start_pos = 0
    add_cycle = 1
    i = 0
    
    while i <= num_rails:
        if add_cycle > len(message):
            i += 1
            if num_rails > 2:
                if i%2 == 0:
                    cycle = (num_rails * 2) - 2
                if i%2 != 0:
                    cycle = cycle - 2
            start_pos = i
            add_cycle = i + 1
            
        if i == num_rails:
            return encode

        slice =  message[start_pos:add_cycle]
        if slice.isalpha() is False:
            slice = "."
            
        encode = encode + slice
        
        if cycle == 0:
            start_pos = start_pos + 1
        
        if cycle != 0:
            start_pos += cycle
            
        add_cycle = start_pos + 1


def read_mapping_file(file_name): 
    
	d = {}
	f = open(file_name)
	for num, line in enumerate(f,2):
		line.strip("\n")
		for line in f:
			new = line.split(",")
			key = new[0]
			val = new[1]
			d[key] = val
	return d
    
   