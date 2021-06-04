import numpy as np
import matplotlib.pyplot as plt
import logistics as lgs
import time
from typing import List, Union


def replica_job():
    """ dummy-job, replica loop with time.sleep()"""

    my_arr = np.zeros(75)
    stop = len(my_arr)
    msg = 'replicating job, '
    # print(msg)
    for i in range(stop):
        time.sleep(0.1)
        lgs.print_loop_progress(i, stop, msg=msg)


def build_plot(
    fig_label :       str                               ,
    x_arrs :          List[List[float]]                 ,
    y_arrs :          List[List[float]]                 ,
    plot_labels :     List[str]                         ,

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
    
        (--required arguments--)

        fig_label :       str                     ,
        x_arrs :          List[List[float]]       ,
        y_arrs :          List[List[float]]       ,
        plot_labels :     List[str]               ,

        (--optional arguments--)
        
        fig_loc :         [float, float]          ,
        fig_size :        [float, float]          ,
        x_label :         str                     ,
        y_label :         str                     ,
        plot_title :      str                     , 
        linestyles :      List[str]               , 
        plot_colors :     List[str]               , 
        plot_markers :    List[str]               , 
        legend :          bool | [bool, str]      ,
        axes :            bool | [bool, str, str] ,
        grid:             bool | [bool, float]    , 
        x_lim :           [float, float]          ,
        y_lim :           [float, float]          ,
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
        linestyle = linestyles[i] if linestyles else '-'
        color = plot_colors[i] if plot_colors else f'C{i}'
        marker = plot_markers[i] if plot_markers else None
        plt.plot(
            x_arrs[i], y_arrs[i], 
            label=plot_labels[i],
            linestyle=linestyle,
            color=color, 
            marker=marker
        )
    
    # labels:
    plt.xlabel(x_label)
    plt.xlabel(y_label)
    plt.title(plot_title)

    # options
    if legend:
        legend_loc = legend[1] if type(legend) == list else 'best'
        plt.legend(loc=legend_loc)
    if grid:
        opacity = grid[1] if type(grid) == list else 0.3
        plt.grid(alpha=opacity)
    if axes:
        axes_linestyle = axes[1] if type(axes) == list else '--'
        axes_color = axes[2] if type(axes) == list else 'k'
        plt.axhline(0, linestyle=axes_linestyle, color=axes_color)
        plt.axvline(0, linestyle=axes_linestyle, color=axes_color)
    if x_lim:
        plt.xlim(x_lim[0], x_lim[1])
    if y_lim:
        plt.ylim(y_lim[0], y_lim[1])


def abs_max(arrs:List)->float:
    """ Return the maximum from among the absolute values
    of all elements within several arrays (of any dimension).
    The arrays should be arranged along axis 0 of "arrs".  """

    maxes = [np.abs(arr).max() for arr in arrs]
    magnitude_max = np.amax(maxes)
    
    return magnitude_max

