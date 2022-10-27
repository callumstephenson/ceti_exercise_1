import math

def reactor_cost(in_stream_flowrate, temperature):
    '''
    reactor operating cost per hour in USD.
    input arguments: in_stream_flowrate (kg / hr), temperature (deg C) 
    return: operating cost in USD per hour
    '''
    if in_stream_flowrate < 0 or temperature < -273.15:
        raise Exception("invalid input args")
    return ( in_stream_flowrate * (temperature - 20) ) / 10000

def column_cost(in_stream_flowrate, column_number = 0):
    '''
    column operating cost per hour in USD
    input arguments: in_stream_flowrate (kg / hr)
    return: column operating cost in USD per hour
    '''
    column_factor = [25, 100]
    if in_stream_flowrate < 0:
        raise Exception("invalid input args")
    return in_stream_flowrate / column_factor[column_number]

def acid_sep_cost(in_stream_flowrate):
    ''' returns the cost of running the acid separator
    inputs: in_stream_flowrate kg / hr
    outputs: cost per hour in USD '''
    return in_stream_flowrate*0.15

def filter_cost(in_stream_flowrate):
    ''' returns the cost of running the filter
    inputs: in_stream_flowrate kg / hr
    outputs: cost per hour in USD '''
    return in_stream_flowrate*40

def recycle_cost(in_stream_flowrate):
    ''' returns the cost of running the recycle
    inputs: in_stream_flowrate kg / hr
    outputs: cost per hour in USD '''
    return in_stream_flowrate / 10000