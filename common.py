import numpy as np
import matplotlib.pyplot as plt
import logistics
import time
from typing import List, Union


def replica_job(
    steps:int, 
    print_progress:bool=False, 
    print_time:bool=False,
    time_full_str:bool=False 
):
    """
        Dummy-job -- replica-loop with time.sleep(); 
        prints the message 'replicating job, '.

        --Parameters--
        * steps : int // 
            Number of replica-actions (sleeps) to be 
            taken by the interpreter.
        * print_progress : bool, optional // 
            Option to print the progress of the replica job
            using the logistics.print_loop_progress() routine;
            the message 'replicating job' will always be printed, but
            will also followed by the progress indicator if 
            print_progress == True, 
                * by default False. 
        * print_time : bool, optional // 
            Option to print the time required (upon completion) 
            for the replica-job using the logistics.print_time_required()
            routine; this time will be preceded by a number of 
            spaces equivalent to the length of the message 
            'replicating job, ', if print_progress == True  
                * by default False. 
        * time_full_str : bool, optional // 
            Option to force the displayed time-string to be of the form:
            hh:mm:ss.cs,
                * only required if print_time == True, 
                * by default False. 
    """    
    
    init_time = time.perf_counter()
    msg = 'replicating job, '
    
    for i in range(steps):
        time.sleep(0.1)
        if print_progress:
            logistics.print_loop_progress(
                index=i, index_max=steps-1, prefix=msg
            )
        else: 
            print('\r' + msg, end='')
    
    buffer = ' ' * len(msg) if print_progress else ''
    if print_time:
        logistics.print_time_required(
            init_time=init_time, prefix=buffer,
            full_str=time_full_str
        )
    

def build_plot(
    fig_label :       str                               ,
    x_arrs :          List[List[float]]                 ,
    y_arrs :          List[List[float]]                 ,

    plot_labels :     List[str]             = None      ,
    fig_loc :         List[float]           = [600, 250],
    fig_size :        List[float]           = [640, 520],
    x_label :         str                   = ''        ,
    y_label :         str                   = ''        ,
    plot_title :      str                   = ''        , 
    linestyles :      List[str]             = None      , 
    plot_colors :     List[str]             = None      , 
    plot_markers :    List[str]             = None      , 
    legend :          Union[bool, List]     = False     ,
    axes :            Union[bool, List]     = False     ,
    grid:             Union[bool, List]     = False     , 
    y_lim :           List[float]           = None      ,
    x_lim :           List[float]           = None      ,   
):
    """
        Builds a plot using matplotlib.pyplot;
        "plt.show()" must be called elsewhere,

        --Parameters--
        * fig_label : str // 
            Title of the figure.
        * x_arrs : List[List[float]] // 
            Arrays (arranged along axis 0) 
            containing horizontal-axis values for points to be plotted; 
            each array in x_arrs should have exactly one counterpart
            in y_arrs. 
        * y_arrs : List[List[float]] // 
            Arrays (arranged along axis 0) 
            containing vertical-axis values for points to be plotted; 
        * plot_labels : List[str], optional // 
            Ordered labels for each plot 
            (i.e. each pair of x, y arrays). 
                * by default None. 
        * fig_loc : List[float], optional // 
            List with two elements giving the screen
            position [x, y] (in px) where the figure should be displayed. 
                * by default [600, 250]. 
        * fig_size : List[float], optional // 
            List with two elements giving the width and height (in px)
            of the displayed figure.  
                * by default [640, 520]. 
        * x_label : str, optional // 
            Horizontal axis label.  
                * by default ''. 
        * y_label : str, optional // 
            Vertical axis label.  
                * by default ''. 
        * plot_title : str, optional // 
            Title of set of plots (printed at top of figure). 
                * by default ''. 
        * linestyles : List[str], optional // 
            List of linestyles for each plot. 
                * by default None. 
        * plot_colors : List[str], optional // 
            List of colors for each plot.  
                * by default None. 
        * plot_markers : List[str], optional // 
            List of marker styles for each plot.  
                * by default None. 
        * legend : Union[bool, List], optional // 
            Option to enable legend for plots; 
            can also be set as a list containing a bool in position 0
            (corresponding the normal legend option) and a string in
            position 1 (corresponding to the loc option, specifying the 
            legend location, e.g. 'upper right'. 
                * requires plot_labels to be fully populated, 
                * by default False. 
        * axes : Union[bool, List], optional // 
            Option to enable axes; 
            can also be set as a list containing a bool in position 0 
            (corresponding to the normal axes option), a string in position
            1 (corresponding to the desired axes linestyle, 
            by default '--'), and a string in position 2 (corresponding to
            the desired axes color, by default 'k'),  
                * by default False. 
        * grid : Union[bool, List], optional // 
            Option to enable grid;
            can also be set as a list containing a bool in position 0 
            (corresponding to the normal grid option) and a float in position
            1 (corresponding to the opacity--i.e. alpha--level of 
            the gridlines), 
                * by default False. 
        * y_lim : List[float], optional // 
            List containing two floats--gives the vertical plot boundaries,  
                * by default None. 
        * x_lim : List[float], optional // 
            List containing two floats--gives the horizontal 
            plot boundaries,  
                * by default None. 
    """    
    
    plt.figure(fig_label)

    # Window geometry (type:int, units:px):
    fig_x_pos, fig_y_pos = fig_loc
    fig_width, fig_height = fig_size 
    mgr = plt.get_current_fig_manager()
    mgr.window.setGeometry(
        fig_x_pos, fig_y_pos, fig_width, fig_height
    )

    # Main plot call:
    for i in range(len(y_arrs)):
        label = plot_labels[i] if plot_labels else None
        linestyle = linestyles[i] if linestyles else '-'
        color = plot_colors[i] if plot_colors else f'C{i}'
        marker = plot_markers[i] if plot_markers else None
        plt.plot(
            x_arrs[i], y_arrs[i], 
            label=label,
            linestyle=linestyle,
            color=color, 
            marker=marker
        )
    
    # labels:
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(plot_title)

    # options
    if legend:
        legend_loc = legend[1] \
            if type(legend) == list else 'best'
        plt.legend(loc=legend_loc)
    if grid:
        opacity = grid[1] \
            if type(grid) == list else 0.3
        plt.grid(alpha=opacity)
    if axes:
        axes_linestyle = axes[1] \
            if type(axes) == list else '--'
        axes_color = axes[2] \
            if type(axes) == list else 'k'
        plt.axhline(
            0, linestyle=axes_linestyle, color=axes_color
        )
        plt.axvline(
            0, linestyle=axes_linestyle, color=axes_color
        )
    if x_lim:
        plt.xlim(x_lim[0], x_lim[1])
    if y_lim:
        plt.ylim(y_lim[0], y_lim[1])


def abs_max(arrs:List)->float:
    """
        Finds the maximum from among the absolute values 
        of all elements within several arrays 
        (where each array can be of any dimension).

        --Parameters--
        * arrs : List // 
            Contains (along axis 0) all arrays to be considered. 

        --Returns--
        * magnitude_max: float // 
            The desired maximum (from among the absolute maximums
            of the inputted arrays). 
    """    

    maxes = [np.abs(arr).max() for arr in arrs]
    magnitude_max = np.amax(maxes)
    
    return magnitude_max

