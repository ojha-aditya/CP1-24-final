import os
import numpy as np
import pandas as pd
import scipy as sp

def filename_lister(directory, filename_filter, extension):
    '''
    Function to generate a list of files with the required extension
    containing the filename_filter

    Parameters:
    - directory: directory containing the files
    - filename_filter: string required to be searched
    - extension: file extension such as '.md'

    Returns:
    - file_list: list of filenames containing the given filter and extension
    '''
    file_list = []

    for filename in os.listdir(directory):
        if filename.endswith(extension) and filename_filter in filename:
            file_list.append(filename)

    return file_list

def get_coordinates(file_path, column_1='Distance_(microns)', column_2 = 'Gray_Value'):
    '''
    Function to read the CSV file and convert GPS data to x, y coordinates 
    using Mercator projection.
    
    Parameters:
    - file_path: path to the CSV file.
    
    Returns:
    - x: a numpy array of x values
    - y: a numpy array of y values
    '''
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Extract latitude and longitude columns
    time = df[column_1].values
    intensity = df[column_2].values

    return np.array(time), np.array(intensity)
