import numpy as np
import matplotlib as mpl
import time
import sys
import warnings
from typing import List, Union
from functools import reduce


if True:
    # suppress reportUnboundVariable:
    start_time = None 


def print_version_info(dependencies:List[str], py_full:str=None):
    """ "dependencies" should contain additional dependencies 
    (beyond 'python') required to run the current script.  
    e.g. ['numpy', 'matplotlib'];
    "py_full" should be any str (e.g. 'full'), which will 
    have the python version print in it's full form--this 
    defaults to False, where the python version will be of the
    form '#.x.x' """
    
    head = 'versions:'
    prefix = ' ' * (len(head)+1)
    py_vers_template = '3.x.x'
    py_vers_length = len(py_vers_template)
    py_vers = sys.version \
        if py_full else sys.version[:py_vers_length]

    print(head + ' python--' + sys.version[:py_vers_length])
    if 'numpy' in dependencies:
        print(prefix + 'numpy--' + np.__version__)
    if 'matplotlib' in dependencies:
        print(prefix + 'matplotlib--' + mpl.__version__)


def print_file_info(filename:str=None, location:str=None, ):
    """ "filename" and "location" are both optional. 
    "filename" should be the file basename. 
    "location" should be the relative patt without the file 
    basename, possibly with "~" for the HOME directory """

    if location:
        print(f'location: "{location}"') 
    if filename:
        print(f'filename: "{filename}"') 


def seconds_to_timestr(t:float, full_str:bool=False):
    """ converts a time "t" in fractional seconds into a
    time-string of one of the following forms--

        hh:mm:ss.ss if "full_str" == True ,
        hh:mm:ss if (1 hour) <= "t" ,
        mm:ss if (1 min) <= "t" <= (1 hour) ,
        mm:ss.ss if "t" <= (1 min) . """

    time_parts = reduce(
        lambda part_tuple, divisor:
            divmod(part_tuple[0], divisor) + part_tuple[1:], 
            [(t * 100,), 100, 60, 60]
    )
    time_parts = (int(p) for p in time_parts)
    h, m, s, cs = time_parts
    
    if full_str == True:
        out = f'{h:02d}:{m:02d}:{s:02d}.{cs:02d}'

    elif h >= 1:
        out = f'{h:02d}:{m:02d}:{s:02d}'

    elif m >= 1:
        out = f':{m:02d}:{s:02d}'

    else:
        out = f'{m:02d}:{s:02d}.{cs:02d}'

    return out


def print_time_required(
    init_time:float, 
    buffer:bool=False, 
    msg:str=None, 
    full_str:bool=False, 
):
    """ "init_time" should be bound at start of 'stopwatch' 
    using the time module,
    "buffer" is an option to replace "msg" with an equal amount
    of spaces (' '),
    "msg" should a status string (printed elsewhere if buffer is 
    False),
    "full_str" is an option to fix the time format as 
    hh:mm:ss.ss ."""

    if buffer:
        buffer_str = ' ' * (len(msg) + 1)
        print(buffer_str, end='')

    time_req = time.perf_counter() - init_time
    time_str = seconds_to_timestr(time_req, full_str=full_str)

    print(f'time required: {time_str:s}')


def print_total_time(start_time:float, full_str:bool=False):
    """ "start_time" should be bound at start of script using 
    the time module, then passed into this routine, 
    "full_str" is an option to fix the time format as 
    hh:mm:ss.ss . """
    
    elapsed_time = time.perf_counter() - start_time
    time_str = seconds_to_timestr(elapsed_time, full_str=full_str)
    print(f'runtime: {time_str:s}')


def housekeeping_initial(
    ignore_warnings:bool=False, 
    location:str=None,
    filename:str=None,
    print_version:Union[bool, List]=False,
    dependencies:List[str]=None,
):
    """ "ignore_warnings" is used to quiet all warnings from the
    terminal. 
    "location" should be the relative path of the current file 
    (without basename). 
    "filename" should be the name of the current file. 
    "print_version" is used to send version info to stdout; 
    if this option is True, then one must provide strings of 
    required dependencies in "dependency_list", e.g. ['numpy', 
    'matplotlib'] 

    One can also set "print_version" : [bool, str], where the  
    the bool is the normal print_version option, and the 
    str (e.g. 'full') indicates whether the python version 
    should be printed in full (defaults to None if "print_version" 
    is given as a single bool)"""
    global start_time
    
    line = '=' * 40
    start_time = time.perf_counter()

    if ignore_warnings:
        warnings.filterwarnings('ignore')
    
    print()
    if print_version:
        py_full = print_version[1] \
            if type(print_version) == list else False
        print_version_info(
            dependencies=dependencies, py_full=py_full
        )
    print_file_info(filename=filename, location=location)
    print('--NEW RUN--')
    print(line)
    print()
    

def housekeeping_final(
    location:str=None,
    filename:str=None,
    print_timing:bool=False,
):
    """ "location" should be the relative path of the current file 
    (without basename). 
    "filename" shoudld be the name of the current file. 
    "print_timing" is used to print the total runtime for the file.
    """
    
    line = '=' * 40

    print()
    print(line)
    print_file_info(filename=filename, location=location) 
    if print_timing:
        print_total_time(
            start_time=start_time, full_str=False
        )
    print('--DONE--')
    print('\n')
    

def print_loop_progress(
    index:int, 
    index_max:int, 
    msg:str=None, 
    buffer:bool=False, 
):
    """ Print "msg" to terminal if "buffer" is False, else n spaces 
    where n is the length of "msg"; 
    print the progress for ("index" + 1) 
    steps out of "index_max" total steps; 
    flush stdout while printing.  """

    percent_complete = 100 * (index+1) / index_max
    buffer_str = ' ' * (len(msg) + 1)
    prefix = '\r' + buffer_str if buffer else '\r' + msg
    
    print(
        prefix + f'progress: {percent_complete:0.0f}%',
        flush=True, end=''
    )
    if index + 1 == index_max: # condition for last step in loop
        print() 

           