import test_packages as pardee_tests
import color_palletes as pardee_colors
import style_dictionaries as pardee_styles
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def load_COLT_data():
    data_directory = "C:/Users/coryv/Desktop/Work/Work-Projects/Pardee Visualization Guide/Data/COLT Data.xlsx"
    return pd.read_excel(data_directory)

def create_aggregation_dictionary():
    return {
            "Temporal Column" : "TripYear",
            "Groupby Columns" : "TripYear",
            "Aggregation Column" : "TripDuration"
            }

def create_pardee_pairplot(data):
    figure = plt.figure()
    sns.set_style(pardee_styles.standard_style)
    sns.set_palette(pardee_colors.crimson_color_gradient())
    sns.pairplot(data = data, hue = "RegionVisited")

def create_pardee_lineplot(data, aggregation_dictionary):
    figure = plt.figure()
    sns.set_style(pardee_styles.standard_style)
    sns.set_palette(pardee_colors.crimson_color_gradient())
    temporal = aggregation_dictionary["Temporal Column"]
    groupby = aggregation_dictionary["Groupby Columns"]
    aggregation = aggregation_dictionary["Aggregation Column"]
    
    sns.lineplot(x = data[temporal],
                 y = data.groupby(groupby)[aggregation].mean())
def main():
    COLT_data = load_COLT_data()
    pardee_tests.test_colors()
    create_pardee_pairplot(COLT_data)
    aggregation_dictionary = create_aggregation_dictionary()
    create_pardee_lineplot(COLT_data, aggregation_dictionary)

if __name__ == "__main__":
    main()


    