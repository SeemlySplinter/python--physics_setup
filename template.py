import numpy as np
import matplotlib.pyplot as plt
import logistics as log
import os
# import config as cfg
# import routines as rt


#* File Specifications:
if True:
    filename_main = os.path.basename(__file__)
    dirname_main = os.path.dirname(__file__)
    relpath_main = os.path.relpath(__file__) 
    reldirname_main = os.path.join(
        '~', relpath_main[:-len(filename_main)]
    )


#* Assign Constants
if True:
    pass


def main():
    log.housekeeping_initial(
        ignore_warnings=False, 
        filename=filename_main, 
        location=reldirname_main,
        print_version=True,
        dependencies=['numpy', 'matplotlib'],
    )
    """ Begin Workspace """ 
    
    
    
    #* print results:
    if True:
        print()
        print(--Results--)
        print()
    """ End WorkSpace"""
    log.housekeeping_final(
        filename=filename_main, 
        location=reldirname_main,
        print_timing=True,
    )
    plt.show()


if __name__ == '__main__':
    main()
