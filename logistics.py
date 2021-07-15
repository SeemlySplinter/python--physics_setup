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
    

def print_version_info(dependencies:List[str], py_full:bool=False):
    """
        Prints version info for python and related dependencies.

        --Parameters--
        * dependencies : List[str] //
            Contains additional dependencies (beyond python) 
            required to run the current script. e.g. 
            ['numpy', 'matplotlib'].
        * py_full : bool, optional //
            True corresponds to printing the python version 
            in its full form; False corresponds to printing 
            in the form: #.x.x,  
                * by default False.
    """    
    
    head = 'versions:'
    prefix = ' ' * (len(head)+1)
    py_vers_template = '3.x.x'
    py_vers_len = len(py_vers_template)
    py_vers = sys.version if py_full else sys.version[:py_vers_len]

    print(head + ' python--' + py_vers)
    if 'numpy' in dependencies:
        print(prefix + 'numpy--' + np.__version__)
    if 'matplotlib' in dependencies:
        print(prefix + 'matplotlib--' + mpl.__version__)


def print_file_info(filename:str=None, location:str=None, ):
    """
        Prints information about the current python file 
        to the terminal output.

        --Parameters--
        * filename : str, optional //
            Name of the current file,  
                * by default None.
        * location : str, optional //
            Path to the current file, not including filename,  
                * by default None.
    """    

    if location:
        print(f'location: "{location}"') 
    if filename:
        print(f'filename: "{filename}"') 


def seconds_to_timestring(t:float, full_str:bool=False)->str:
    """
        Converts a time in fractional seconds into a printable string.

        --Parameters--
        * t : float // 
            Time in fractional seconds. 
        * full_str : bool, optional // 
            Option used to force output string to be 
            of the form hh:mm:ss.ss, 
                * by default False. 

        --Returns--
        * out : str // 
            Printable string of one of the following forms:
            
                hh:mm:ss.ss if (full_str option is True) OR ((1 hour) < t) ; 
                mm:ss.ss otherwise.
    """    

    time_parts = reduce(
        lambda part_tuple, divisor:
            divmod(part_tuple[0], divisor) + part_tuple[1:], 
            [(int(t * 100),), 100, 60, 60]
    )
    h, m, s, cs = time_parts
    
    if full_str == True or h >= 1:
        out = f'{h:02d}:{m:02d}:{s:02d}.{cs:02d}'
    else:
        out = f'{m:02d}:{s:02d}.{cs:02d}'

    return out


def print_time_required(
    init_time:float, 
    prefix:str='', 
    full_str:bool=False, 
):
    """
        Prints the time elapsed from init_time according 
        to the python interpreter. Note that 
        time.perf_counter() is used rather than 
        time.process_time(), meaning that time is recorded 
        while python is asleep using time.sleep(). 

        --Parameters--
        * init_time : float // 
            A time which must be bound at the start of the user's 
            "stopwatch" (free choice of the user) using the time module. 
        * prefix: str, optional //
            Gets printed on the same line just before the displayed
            time-requirement message,
                * by default ''.
        * full_str : bool, optional // 
            Option used to force printed string to be 
            of the form hh:mm:ss.ss, 
                * by default False. 
    """    

    time_req = time.perf_counter() - init_time
    time_str = seconds_to_timestring(time_req, full_str=full_str)
    print(prefix + f'time required: {time_str:s}')
    

def print_total_time(start_time:float, full_str:bool=False):
    """
        Prints the total time for the current script. 

        --Parameters--
        * start_time : float // 
            Time of beginning NEW RUN for current script--should 
            be bound at the start of current script using the 
            time module. 
        * full_str : bool, optional // 
            Option used to force printed string to be 
            of the form hh:mm:ss.ss, 
                * by default False.  
    """    
    
    elapsed_time = time.perf_counter() - start_time
    time_str = seconds_to_timestring(elapsed_time, full_str=full_str)
    print(f'runtime: {time_str:s}')


def housekeeping_initial(
    ignore_warnings:bool=False, 
    location:str=None,
    filename:str=None,
    print_version:Union[bool, List]=False,
    dependencies:List[str]=None,
):
    """
        Initial setup to make terminal output more legible.

        --Parameters--
        * ignore_warnings : bool, optional // 
            Option to quiet all warnings from the terminal,  
                * by default False. 
        * location : str, optional // 
            Path to the current file,  
                * by default None. 
        * filename : str, optional // 
            Name of the current file,  
                * by default None. 
        * print_version : Union[bool, List], optional // 
            Option to print version info--if this option is 
            True, then one must provide strings of required 
            dependencies in the dependcies parameter, 
            e.g. ['numpy', 'matplotlib'];
            can also be set as [bool, bool] where the first bool 
            is the normal print_version option, and the second bool 
            controls whether the python version should be printed 
            in full (defaults to False if print_version is given 
            as a single bool),  
                * by default False. 
        * dependencies : List[str], optional // 
            List of required dependencies, 
            e.g. ['numpy', 'matplotlib'], 
                * only required if (print_version == True) 
                OR (print_version[0] == True), 
                * by default None. 
    """    
    
    line = '=' * 40
    
    global start_time
    start_time = time.perf_counter()
    
    if ignore_warnings:
        warnings.filterwarnings('ignore')
    
    print()
    
    py_full = print_version[1] if type(print_version) == list else False
    if print_version == True or print_version[0] == True:
        print_version_info(dependencies=dependencies, py_full=py_full)
    
    print_file_info(filename=filename, location=location)
    print('--NEW RUN--')
    print(line)
    print()


def housekeeping_final(
    location:str=None,
    filename:str=None,
    print_timing:bool=False,
):
    """
        Final cleanup to make terminal output more legible. 

        --Parameters--
        * location : str, optional // 
            Path to the current file,  
                * by default None. 
        * filename : str, optional // 
            Name of the current file,  
                * by default None. 
        * print_timing : bool, optional // 
            Option to print the total time required for the 
            current script, 
                * by default False. 
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
    print()
    

def print_loop_progress(
    index:int, 
    index_max:int, 
    prefix:str='', 
):
    """
        Goes inside the body of a (for/while) loop to 
        repeatedly print the current progress, along with 
        an optional message, as the interpreter steps 
        though the loop. 

        --Parameters--
        * index : int // 
            The integer index representing the current step 
            of the loop (one might need to create this using 
            enumerate() ). 
        * index_max : int // 
            The integer corresponding to the loop's (inclusive) stop 
            condition--often needs to be 1 less than the stop 
            parameter for a range iterable.s
        * prefix: str, optional //
            Gets printed on the same line just before the displayed
            progress, 
                * by default ''. 
    """    

    percent_complete = 100 * (index) // index_max
    print(
        '\r' + prefix + f'progress: {percent_complete:0.0f}%',
        flush=True, end=''
    )
    if index == index_max: # condition for last step in loop
        print() 
