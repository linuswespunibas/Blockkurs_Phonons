#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Set of functions to plot figures, using the matplot python library
"""

import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
import math
from matplotlib.ticker import MaxNLocator

def c_scheme():
    # https://wpdatatables.com/data-visualization-color-palette/
    return ["#ffb400", "#d2980d", "#a57c1b", "#786028", "#363445", "#48446e", "#5e569b", "#776bcd", "#9080ff"]

def c_scheme_02():
    return ["#450d54", "#482878", "#3e4a89", "#30688e", "#25828e", "#1f9e89", "#35b779", "#6dcd59", "#b4de2c", "#fde725"]

def c_scheme_03():
    # twenty colors
    # https://sashamaps.net/docs/resources/20-colors/
    return ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff', '#000000']


def plot_with_one_axis(list_of_data:list, name_x="x", name_y="y", plot_title="", filename_to_save="nosvg", marker_size="5", font_size=16, offset_text_size=16, legend_local="best", legend_size=16, x_ticks_limit=5, x_ticks_numstyle="sci", line_width=1.5, y_lim = None): # [data_x, data_y, label, colorr, line_style, marker_type]

    """
    Plots multiple data series on a single axis.

    Args:
        list_of_data (list): Each entry should be [data_x, data_y, label, color, line_style, marker_type].
        name_x (str): Label for x-axis.
        name_y (str): Label for y-axis.
        plot_title (str): Title of the plot.
        filename_to_save (str): If not "nosvg", saves the plot as an SVG file.
        marker_size (int): Size of markers.
        font_size (int): Font size for axis labels and title.
        offset_text_size (int): Font size for scientific notation offset.
        legend_local (str): Position of the legend.
        legend_size (int): Font size for the legend.
        x_ticks_limit (int): Number of ticks on x-axis.
        x_ticks_numstyle (str): "sci", "plain", "scientific"
        y_lim (list): example: y_lim = [0, 250]
    """

    plt.figure()
    
    # [data_x, data_y, label, color, linestyle, marker_type]
    
    for l in list_of_data:
        data_x, data_y, label, colorr, line_style, marker_type = l
        plt.plot(data_x, data_y, label=label, marker=marker_type, linestyle=line_style, color=colorr, markersize=marker_size, linewidth=line_width) # color='red') 


    # Label the axes
    plt.xlabel(name_x, fontsize=font_size)
    plt.ylabel(name_y, fontsize=font_size)

    # Set title and legend
    plt.title(plot_title, fontsize=font_size)
    plt.legend(loc=legend_local, fontsize=legend_size)

    # Set font size for axis ticks and rotate x-axis labels
    plt.xticks(fontsize=font_size)
    plt.yticks(fontsize=font_size)

    # Use MaxNLocator for precise control over x-axis tick count
    plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=x_ticks_limit))

    # define y_lim
    if y_lim:
        plt.ylim(*y_lim)

    # Adjust scientific notation offset text size
    plt.ticklabel_format(style=x_ticks_numstyle, axis='x', scilimits=(0,0))
    plt.gca().xaxis.get_offset_text().set_fontsize(offset_text_size)

    # Save and show the plot
    if filename_to_save != "nosvg":
        fnts = filename_to_save + ".pdf"
        plt.savefig(fnts)

    plt.show()


def plot_with_one_axis_with_vertical_lines(list_of_data:list, name_x="x", name_y="y", plot_title="title", filename_to_save="nosvg", marker_size="5", font_size=16, offset_text_size=16, legend_local="best", legend_size=16, x_ticks_limit=5, vlines=None, y_lim = None): # [data_x, data_y, label, colorr, line_style, marker_type], [[x_val, color, linestyle], ...]
    """
    Plots multiple data series on a single axis.

    Args:
        list_of_data (list): Each entry should be [data_x, data_y, label, color, line_style, marker_type].
        name_x (str): Label for x-axis.
        name_y (str): Label for y-axis.
        plot_title (str): Title of the plot.
        filename_to_save (str): If not "nosvg", saves the plot as an SVG file.
        marker_size (int): Size of markers.
        font_size (int): Font size for axis labels and title.
        offset_text_size (int): Font size for scientific notation offset.
        legend_local (str): Position of the legend.
        legend_size (int): Font size for the legend.
        x_ticks_limit (int): Number of ticks on x-axis.
        y_lim (list): example: y_lim = [0, 250]
    """

    plt.figure()
    
    # [data_x, data_y, label, color, linestyle, marker_type]
    
    for l in list_of_data:
        data_x, data_y, label, colorr, line_style, marker_type = l
        plt.plot(data_x, data_y, label=label, marker=marker_type, linestyle=line_style, color=colorr, markersize=marker_size) # color='red') 

    # Label the axes
    plt.xlabel(name_x, fontsize=font_size)
    plt.ylabel(name_y, fontsize=font_size)

    # Set title and legend
    plt.title(plot_title, fontsize=font_size)
    plt.legend(loc=legend_local, fontsize=legend_size)

    # Set font size for axis ticks and rotate x-axis labels
    plt.xticks(fontsize=font_size)
    plt.yticks(fontsize=font_size)

    # Use MaxNLocator for precise control over x-axis tick count
    plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=x_ticks_limit))

    # Adjust scientific notation offset text size
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    plt.gca().xaxis.get_offset_text().set_fontsize(offset_text_size)

    # define y_lim
    if y_lim:
        plt.ylim(*y_lim)

    # Save and show the plot
    if filename_to_save != "nosvg":
        fnts = filename_to_save + ".pdf"
        plt.savefig(fnts)

    # Plot vertical lines based on vlines parameter
    if vlines:
        for x_val, color, linestyle in vlines:
            plt.axvline(x=x_val, color=color, linestyle=linestyle)

    plt.show()

def plot_with_one_axis_and_error_bars_BYLIST(ALLDATA:list, name_x, name_y, plot_title="title", filename_to_save="nosvg", line_style="", marker_type="o", marker_size="5", capsize_errorbars=5, transparency=1.0): # [data_x_1, data_y_1, data_y_1_error, label1, col1]
    """
    Plots data with error bars.

    Args:
        ALLDATA (list): List containing [data_x, data_y, data_y_error, label, color].
        name_x (str): Label for x-axis.
        name_y (str): Label for y-axis.
        plot_title (str): Title of the plot.
        filename_to_save (str): If not "nosvg", saves the plot as an SVG file.
        line_style (str): Style of the connecting lines.
        marker_type (str): Marker type for the data points.
        marker_size (int): Size of markers.
        capsize_errorbars (int): Size of error bar caps.
        transparency (float): Transparency level of plotted data.

    """

    plt.figure()
    
    # Plot data
    for d in ALLDATA:
        data_x_1, data_y_1, data_y_1_error, label1, col1 = d
        plt.errorbar(data_x_1, data_y_1, yerr=data_y_1_error, fmt=marker_type, label=label1, capsize=capsize_errorbars, color=col1, markersize=marker_size, linestyle="-", alpha=transparency)

    # Label the axes
    plt.xlabel(name_x)#rf"\textbf{{{name_x}}}", fontweight='bold') 
    plt.ylabel(name_y)#rf"\textbf{{{name_y}}}", fontweight='bold') #, color='red')
    
    # Set axis limits
    # plt.xlim([xmin, xmax])
    # plt.ylim([ymin, ymax])
    
    # Set title and legend
    plt.title(plot_title)#rf"\textbf{{{plot_title}}}" , fontweight='bold', fontsize=16)

    
    # Save and show the plot
    if filename_to_save != "nosvg":
        fnts = filename_to_save + ".pdf"
        plt.savefig(fnts)

    plt.show()


def plot_with_one_axis_with_points(list_of_data:list, list_of_points:list, name_x="x", name_y="y", plot_title="title", filename_to_save="nopdf", marker_type="o", marker_size="5"): # list_of_data: [[data_x, data_y, label, colorr, line_style]], list_of_points: [[x_val, y_val, labell, markerr, markersizee, colorr]]
    """
    Plots data with additional highlighted points.

    Args:
        list_of_data (list): List containing [data_x, data_y, label, color, line_style].
        list_of_points (list): List containing [x_val, y_val, label, marker, size, color].
        name_x (str): Label for x-axis.
        name_y (str): Label for y-axis.
        plot_title (str): Title of the plot.
        filename_to_save (str): If not "nopdf", saves the plot as an SVG file.
        marker_type (str): Marker type for main data points.
        marker_size (int): Size of markers.

    """
    
    plt.figure()

    # [data_x, data_y, label, color]
    
    for l in list_of_data:
        data_x, data_y, label, colorr, line_style = l
        plt.plot(data_x, data_y, label=label, marker=marker_type, linestyle=line_style, color=colorr, markersize=marker_size) # color='red')
    
    for p in list_of_points:
        x_val, y_val, labell, markerr, markersizee, colorr = p

        plt.plot(x_val, y_val, label=labell, marker=markerr, markersize=markersizee, color=colorr)

    # Label the axes
    plt.xlabel(name_x)#rf"\textbf{{{name_x}}}", fontweight='bold') 
    plt.ylabel(name_y)#rf"\textbf{{{name_y}}}", fontweight='bold') #, color='red')
    
    # Set axis limits
    # plt.xlim([xmin, xmax])
    # plt.ylim([ymin, ymax])
    
    # Set title and legend
    plt.title(plot_title)#rf"\textbf{{{plot_title}}}" , fontweight='bold', fontsize=16)

    
    # Save and show the plot
    if filename_to_save != "nopdf":
        fnts = filename_to_save + ".pdf"
        plt.savefig(fnts)

    plt.show()

def plot_with_two_axes_with_N_curves_with_VERTICAL_lines(data_y_one:list, data_y_two:list, name_x="name_x", name_y1="name_y1", name_y2="name_y2", col_ax1 = "red", col_ax2= "blue", plot_title="title", filename_to_save="nopdf", marker_size="5", font_size=18, legend_size=18, legend_local="best", vlines=None, x_ticks=True):

    """
        0: "best"
        1: "upper right"
        2: "upper left"
        3: "lower left"
        4: "lower right"
        5: "right"
        6: "center left"
        7: "center right"
        8: "lower center"
        9: "upper center"
        10: "center"
    """
    
    # font_size=18, offset_text_size=18, legend_local = 0, x_ticks_limit=5, legend_size=18*(4/6)

    # # Label the axes
    # plt.xlabel(name_x, fontsize=font_size)
    # plt.ylabel(name_y, fontsize=font_size)

    fig, ax1 = plt.subplots() 
    
    if x_ticks:
        ax1.set_xlabel(name_x, fontsize=font_size)
        ax1.tick_params(axis='x', labelsize=font_size)
    else:
        ax1.set_xticklabels([])
        ax1.tick_params(axis='x', labelsize=font_size, length=0)  # Removes the tick marks
        ax1.set_xlabel(name_x, fontsize=font_size)


    ax1.set_ylabel(name_y1, color=col_ax1, fontsize=font_size) 

    # Plot data on the first y-axis
    plot_1 = []
    for i, d1 in enumerate(data_y_one):
        x,y,lab, col, lins, linsh = d1
        plot_1.append(ax1.plot(x, y, color=col, label=lab, marker=linsh, linestyle=lins, markersize = marker_size)) #, marker=lins, linestyle=linsh))

    ax1.tick_params(axis='y', labelsize=font_size) 
    
    # Create the second y-axis
    ax2 = ax1.twinx() 
    ax2.set_ylabel(name_y2, color=col_ax2, fontsize=font_size)

    # Plot data on the second y-axis
    plot_2 = []
    for i, d2 in enumerate(data_y_two):
        x,y,lab, col, lins, linsh = d2 #                 [x_guess, fitted_y, "oct_15_no_comp_1 fit", c_scheme[7],  "-", ""]
        plot_2.append(ax2.plot(x, y, color=col, label=lab, marker=linsh, linestyle=lins, markersize = marker_size)) #, marker=lins, linestyle=linsh)2
            
    ax2.tick_params(axis='y', labelsize=font_size) 
    
    fig.tight_layout()

    # Flatten lists of plot lines to merge them for the legend
    lns = [line for sublist in plot_1 for line in sublist] + [line for sublist in plot_2 for line in sublist]
    labels = [l.get_label() for l in lns]
    
    plt.title(plot_title, fontsize=font_size)
    plt.legend(lns, labels, loc=legend_local, fontsize=legend_size)

    # Plot vertical lines based on vlines parameter
    if vlines:
        for x_val, color, linestyle in vlines:
            ax1.axvline(x=x_val, color=color, linestyle=linestyle)

    # Save and show the plot
    if filename_to_save != "nopdf":
        fnts = filename_to_save + ".pdf"
        plt.savefig(fnts)
    
    plt.show()

def one_axis__N_Y_with_error_bars__with_N_fits(list_of_data: list, list_of_fit: list, name_x="name_x", name_y="name_y", plot_title="title", filename_to_save="nopdf", marker_type="o", marker_size="5", capsize_errorbars=5, alpha_data=0.5, font_size=16, offset_text_size=16, legend_size=16, legend_local="best", x_ticks_limit=5):                                                      
    """
        0: "best"
        1: "upper right"
        2: "upper left"
        3: "lower left"
        4: "lower right"
        5: "right"
        6: "center left"
        7: "center right"
        8: "lower center"
        9: "upper center"
        10: "center"
    """
    
    plt.figure()


    # Plot data with error bars
    for d in list_of_data:
        # print(d[0],d[1],d[2],d[3],d[4],d[5])
        plt.errorbar(d[0], d[1], yerr=d[2], fmt=marker_type, label=d[3], capsize=capsize_errorbars, color=d[4], linestyle=d[5], markersize=marker_size, alpha=alpha_data)

    # Plot fit lines
    for f in list_of_fit:
        plt.plot(f[0], f[1], label=f[2], color=f[3])




    # Label the axes
    plt.xlabel(name_x, fontsize=font_size)
    plt.ylabel(name_y, fontsize=font_size)
    
    # Set title and legend
    plt.title(plot_title, fontsize=font_size)
    plt.legend(loc=legend_local, fontsize=legend_size)

    # Set font size for axis ticks and rotate x-axis labels
    plt.xticks(fontsize=font_size)
    plt.yticks(fontsize=font_size)

    # Use MaxNLocator for precise control over x-axis tick count
    plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=x_ticks_limit))

    # Adjust scientific notation offset text size
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    plt.gca().xaxis.get_offset_text().set_fontsize(offset_text_size)

    # Save and show the plot
    if filename_to_save != "nopdf":
        fnts = filename_to_save + ".pdf"
        plt.savefig(fnts)

    plt.show()

def plot_dynamic_subplots(list_of_data:list, name_x="x", name_y="y", filename_to_save="nosvg", marker_size=5, font_size=16, offset_text_size=16, legend_loc="best", legend_size=16, x_ticks_limit=5):

    
    plt.figure(figsize=(8, len(list_of_data) * 4))  # Dynamically scale figure height
    
    for i, data in enumerate(list_of_data, start=1):
        data_x, data_y, label, color, line_style, marker_type = data
        plt.subplot(len(list_of_data), 1, i)
        plt.plot(data_x, data_y, label=label, marker=marker_type, linestyle=line_style, color=color, markersize=marker_size)
        
        # Label the axes
        plt.xlabel(name_x, fontsize=font_size)
        plt.ylabel(name_y, fontsize=font_size)
                
        # Customize legend
        plt.legend(loc=legend_loc, fontsize=legend_size)

        # Use MaxNLocator for precise control over x-axis tick count
        plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=x_ticks_limit))

        # Customize tick label font size
        plt.tick_params(axis='both', which='major', labelsize=offset_text_size)

        # Adjust scientific notation offset text size
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        plt.gca().xaxis.get_offset_text().set_fontsize(offset_text_size)

        # Set font size for axis ticks and rotate x-axis labels
        plt.xticks(fontsize=font_size)
        plt.yticks(fontsize=font_size)

    # Adjust layout to prevent overlap
    plt.tight_layout()
    
    # Save the figure if needed
    if filename_to_save != "nosvg":
        plt.savefig(f"{filename_to_save}.pdf", format="pdf")
    
    # Show the plot
    plt.show()