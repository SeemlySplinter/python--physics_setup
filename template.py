import numpy as np
import matplotlib.pyplot as plt
import logistics as lgs
import os
# import config as cfg
# import routines as rts


#* File Specifications:
if True:
    filename_main = os.path.basename(__file__)
    dirname_main = os.path.dirname(__file__)
    relpath_main = os.path.relpath(__file__) 
    reldirname_main = os.path.join(
        '~', relpath_main[:-len(filename_main)]
    )


#* Assign Constants:
if True:
    pass


#*Body:


def begin():
    """ initial terminal housekeeping 
    
    --Version info (2020-06-04)--
    versions: python--3.8.5 
                (default, Sep  3 2020, 21:29:08) 
                [MSC v.1916 64 bit (AMD64)]; 
              numpy--1.19.2; 
              matplotlib--3.3.2;
    """

    lgs.housekeeping_initial(
        ignore_warnings=True, 
        filename=filename_main, 
        location=reldirname_main,
        print_version= [True, None], 
        dependencies=['numpy',  'matplotlib']
    )


def end():
    """ final terminal housekeeping """

    lgs.housekeeping_final(
        filename=filename_main, 
        location=reldirname_main,
        print_timing=True,
    )



def main():
    begin()
    """ --Top of Stack-- """
    
    
    
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
