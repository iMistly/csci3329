# Imports (import any packages needed here!)
import pandas as pd
import matplotlib.pyplot as plt

### PART 1 - Loading Data
'''
# fill in the code to complete the function load_data().
# This function will take the CSV file from the filepath (the file should be in the current folder),
# and load it into a DataFrame using pandas function read_csv(). 
# In this function, be sure to use the options to set the index column to be the 'date.utc' column, 
# and parse the timestamps so that we can work with them as datetime objects, using the parse_dates=True option when calling read_csv().
'''

def load_data():
    # Data file URL, do not modify
    #filepath = 'W9/Lab 5a/air_quality_no2_long.csv'
    filepath = 'https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/air_quality_no2_long.csv'


    ### YOUR CODE GOES HERE!
    # Use pd.read_csv() with filepath given above
    # Be sure to use options parse_dates=True
    # and index_col='date.utc'
    data = pd.read_csv(filepath, parse_dates=True, index_col='date.utc')



    ### END YOUR CODE (DO NOT MODIFY BELOW)

    return data


### PART 2 - Looking for Patterns
'''
Next, you will complete 3 functions:
find_total_time() - This function should take the dataframe and use the difference between the  min() and max()
                    functions of our date.utc column data to return the total elapsed time in the dataset. 

analyze_months() - This function should group the data by months using the .groupby() method of our dataframe. 
                    It should contain the mean value of each month, using the mean() function.

analyze_weekdays() - This function should group the data by weekdays using the .groupby() method of our dataframe.
                    It should contain the maximum value on each weekday, using the max() function.
'''

def find_total_time(data):
    '''
    here "data" is available and is your dataframe completed in Part 1 of the assignment
    Since "date.utc" is our index column, to access its values, we will use data.index
    instead of data['date.utc']. For example, data.index.min() will return the first timestamp in the dataset
    '''
    ### YOUR CODE GOES HERE!
    # Fill in the start value (the earliest timestamp in the index)
    start = data.index.min()

    # Fill in the end value (the lastest timestamp in the index)
    end = data.index.max()

    # Fill in the elapsed time by finding the difference between the start and the end values
    time_elapsed = end-start

    ### END YOUR CODE (DO NOT MODIFY BELOW)

    return time_elapsed

def analyze_months(data):
    '''
    here "data" is available and is your dataframe completed in Part 1 of the assignment
    '''
    ### YOUR CODE GOES HERE!

    # 1. to access the months data of our index, we will use data.index.month.
    months = data.index.month

    # 2. We can then use .groupby() on the "months" to get our monthly data
    monthly_data = data.groupby(months)


    # 3. Lastly, we will use the mean() function to get the average value for each month
    monthly_mean_value = monthly_data.mean()

    ### END YOUR CODE (DO NOT MODIFY BELOW)
    
    return monthly_mean_value

def analyze_weekdays(data):
    '''
    here "data" is available and is your dataframe completed in Part 1 of the assignment
    '''
    ### YOUR CODE GOES HERE!

    # 1. Access the "weekday" attribute of the index (similar to the previous function!)
    weekdays = data.index.weekday

    # 2. We can then use .groupby() on the "weekdays" to get our weekday data
    weekday_data = data.groupby(weekdays)


    # 3. Lastly, we will use the max() function to get the average value for each weekday
    weekday_max_value = weekday_data.max()

    ### END YOUR CODE (DO NOT MODIFY BELOW)
    
    return weekday_max_value
    

# PART 3 - Visualizations
'''
Finally, you will use matplotlib (make sure to use the correct import at the top of the assignment in the imports section!)
to create some visualizations of your data in Part 2.
Your task will be to create visualizations for the following data:
    1. Plot all data - Create a scatter plot with all values (using the plt.scatter() function)
    2. monthly data (from part 2) - This will be available to you as a dataframe. Create a bar chart (using the plt.bar() function)
    3. weekday data (from part 2) - This will be available to you as a dataframe. Create a scatter plot (using the plt.plot() function)
'''

def plot_all_data(data):
    '''
    1. Plot all data - Create a scatter plot with all values (using the plt.scatter() function)
        X values - should be data.index
        Y values - should be data['value']

        Be sure to use annotations to add the following:
            - A title
            - X and Y axis labels
    '''
    ### YOUR CODE STARTS HERE!

    # Define X and Y data values
    X = data.index
    Y = data['value']

    # Generate a scatter plot of the X and Y values, using plt.scatter()
    plt.scatter(X, Y)

    # Create Annotations
    # Title ( use plt.title() )
    plt.title('All Data')

    # X axis label ( use plt.xlabel() )
    plt.xlabel('Date')

    # Y axis label ( use plt.ylabel() )
    plt.ylabel('Air Quality')

    # Display the graph
    plt.show()

    ### YOUR CODE ENDS HERE (DO NOT MODIFY BELOW)

def plot_month_data(monthly_data):
    '''
    * the 
    1. Plot montlhy mean data - Create a bar chart with the mean monthly values (using the plt.bar() function)
        X values - should be monthly_data.index
        Y values - should be monthly_data['value']

        Be sure to use annotations to add the following:
            - A title
            - X and Y axis labels
    '''
    ### YOUR CODE STARTS HERE!

    # Define X and Y data values
    X = monthly_data.index
    Y = monthly_data['value']

    # Generate a bar plot using X and Y
    plt.bar(X, Y)

    # Create Annotations
    # Title ( use plt.title() )
    plt.title('Monthly Data')

    # X axis label ( use plt.xlabel() )
    plt.xlabel('Month')

    # Y axis label ( use plt.ylabel() )
    plt.ylabel('Air Quality')


    # This annotation will change the X axis tick marks from 5, 6 to 'May' and 'June'
    plt.xticks(X, ['May', 'June'])

    
    #Display the graph
    plt.show()

    ### YOUR CODE ENDS HERE (DO NOT MODIFY BELOW)

def plot_weekday_data(weekday_data):
    '''
    * the 
    2. Plot weekday max data - Create a bar chart with the max weekday values (using the plt.plot() function)
        X values - should be weekday_data.index
        Y values - should be weekday_data['value']

        Be sure to use annotations to add the following:
            - A title
            - X and Y axis labels
    '''
    ### YOUR CODE STARTS HERE!
    
    # Define X and Y data values
    X = weekday_data.index
    Y = weekday_data['value']

    # Generate a line plot using X and Y ( using plt.plot() )
    plt.plot(X, Y)

    # Create Annotations
    # Title ( use plt.title() )
    plt.title('Weekday Data')

    # X axis label ( use plt.xlabel() )
    plt.xlabel('Day')

    # Y axis label ( use plt.ylabel() )
    plt.ylabel('Air Quality')

    # This annotation will change the X axis tick marks from Integers to days of the week
    plt.xticks(X, ['Sunday', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat'])

    
    #Display the graph
    plt.show()
    ### YOUR CODE ENDS HERE (DO NOT MODIFY BELOW)

# TESTS - DO not modify
data_result = load_data()
time_elapsed = find_total_time(data_result)
monthly_mean_value = analyze_months(data_result)
weekday_max_value = analyze_weekdays(data_result)

print(monthly_mean_value)
print(weekday_max_value)

plot_all_data(data_result)
plot_month_data(monthly_mean_value)
plot_weekday_data(weekday_max_value)
