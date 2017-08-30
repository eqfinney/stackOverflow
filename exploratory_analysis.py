#
# exploratory_analysis
# My exploratory analysis of the 2017 Stack Overflow Developer Survey.
# Author: Emily Quinn Finney
#

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def import_data(filename):
    """
    Imports data from an external project into a format for exploratory analysis.
    :param filename: The name of the file to be imported.
    :return: data, a dataset.
    """

    data = pd.read_csv(filename, index_col=0, usecols=[0] + list(range(5,9)) + [18, 87, 145, 146, 147, 152])
    salary_data = data[np.isfinite(data['Salary'])]
    print(salary_data.head())
    print(salary_data.columns)
    return salary_data

def visualize_data_matplotlib(data_frame):
    """
    Visualizes a data frame based on its columns using matplotlib.
    :param data_frame: The data frame
    :return: A visualization
    """
    barplot_set_1d = data_frame.select_dtypes(exclude=['float', 'int'])
    hist_set_1d = data_frame.select_dtypes(include=['float', 'int'])
    # eventually I also want to plot each value against each other value or something
    # or use that zany visualization thingydoo

    barplot_matplotlib(barplot_set_1d)
    histogram_matplotlib(hist_set_1d)


def barplot_matplotlib(barplot_set_1d):
    for column in barplot_set_1d:
        plt.clf()
        num_counts = barplot_set_1d[column].dropna().value_counts()
        plt.bar(range(len(num_counts)), num_counts.values, label=num_counts.index)
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.title(column + " vs. frequency")
        plt.show()


def histogram_matplotlib(hist_set_1d):
    for column in hist_set_1d:
        plt.clf()
        plt.hist(hist_set_1d[column].dropna(), bins=50)
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.title(column + " vs. frequency")
        plt.show()


if __name__ == '__main__':
    survey_data = import_data('survey_results_public.csv')
    visualize_data_matplotlib(survey_data)
