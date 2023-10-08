from console_gfx import *

dec_to_hex = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'
}


def to_hex_string(data: list, hex_string=''):
    for i in data:
        i = dec_to_hex[i]
        hex_string += i
    return hex_string

def count_runs(flat_data: list):
    num_runs = 1
    prev_val = flat_data[0]
    run_length = 0
    # loop through flat_data until the index value changes (this signifies the end of a run)
    # runs can be 15 pixels long MAX
    for val in flat_data:
        if run_length > 15:  # if run length is greater than 15, increment number of runs and make a new run
            num_runs += 1
            run_length = 0
        # in order to determine if the index value changes, store the previous index value then compare it with the current index value
        # if the values are the same, do nothing and move on to the next value in the list
        if val != prev_val:  # if the values change (prev_val is different from current val), add 1 to num_runs
            num_runs += 1
            run_length = 0
        prev_val = val  # the run ends when the value changes. We can keep track of this by storing the previous list val in a variable
        # increment run length by 1 for every loop
        run_length += 1
    return num_runs


def encode_rle(flat_data: list):
    '''count the length of the run, then put the length, value of the run into the next 2 spots of a list. Do this for an entire
    set of data'''
    encoded_data = []
    prev_val = flat_data[0]
    run_length = 0
    for i, val in enumerate(flat_data):
        if run_length == 15:
            encoded_data.extend([run_length, prev_val])
            run_length = 0
        # if data values change (curval != prevval), insert the length of the current run and prevval into encoded data list in that order
        if prev_val != val:
            encoded_data.extend([run_length, prev_val])
            run_length = 0
        prev_val = val
        run_length += 1
    encoded_data.extend([run_length, prev_val])
    return encoded_data
