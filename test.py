import numpy as np
import matplotlib.pyplot as plt
import logistics
import os
# import config
# import routines
import common


#* File Specifications:
if True:
    filename_main = os.path.basename(__file__)
    home = os.path.expanduser('~')
    path_home2main = os.path.relpath(__file__, start=home)
    location_main = os.path.join(
        '~', path_home2main[:-len(filename_main)]
    )


#* Assign Constants:
if True:
    pass


#*Body:


def begin():
    """ 
        Initial terminal housekeeping. 
        
        --Version info (2020-06-23)--
        * versions: 
                * python--3.8.5 
                (default, Sep  3 2020, 21:29:08) [MSC v.1916 64 bit (AMD64)];
                * numpy--1.19.2;
                * matplotlib--3.3.2;
    """

    logistics.housekeeping_initial(
        ignore_warnings=True, 
        filename=filename_main, 
        location=location_main,
        print_version= [False, False], 
        dependencies=['numpy',  'matplotlib']
    )


def end():
    """ 
        Final terminal housekeeping.
    """

    logistics.housekeeping_final(
        filename=filename_main, 
        location=location_main,
        print_timing=True,
    )


def main():
    begin()
    """ --Top of Stack-- """
    
    steps = int(np.pi**2)
    common.replica_job(steps, True, True)


    #* print results:
    if True:
        print()
        print('--Results--')
        print()
    """ --Bottom of Stack-- """
    end()
    plt.show()


if __name__ == '__main__':
    main()
