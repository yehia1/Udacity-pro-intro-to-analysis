import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("please input one of the main cities : ")
    city = input().lower()
    mycities = ['chicago','new york city','washington']
    while(city not in mycities):
       print('invalid input please input one of the cities')
       city = input().lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    print("please input the month u want : ")            
    month = input()
    my_months = ['all','january','february','march' ,'april','may','june']
    while (month not in my_months):
          print("not in range please input in range month: ")
          month = input()
                            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print("please input the day : ")
    day = input()
    my_days = ['all','monday','tuesday','sunday' ,'wednesday','friday','saturday','thursday']
    while (day not in my_days):
           print("pleaze input name of day : ")
           day = input()      
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df ['Start Time'] = df['Start Time'] = pd.to_datetime(df['Start Time'])
    df ['month'] = df ['Start Time'].dt.hour
    df['day'] = df ['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = {'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6}
        month = months[month]
        # filter by month to create the new dataframe
        df =  df[df['month']== month]
    # filter by day of week if applicable
    if day != 'all':
          # filter by day of week to create the new dataframe
          day = day.capitalize()
          df =df[df['day']==day]
    
    return df
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    print ('the most common month is : ',df['month'].mode()[0])

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
                
    print('Most Popular Day:', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('Most Popular Start Hour:', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most popular start station : ',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most Popular end station : ',df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'].str.cat(df['End Station'], sep = ' towards ')
    print('most common trip : ',df['Trip'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total trips time :',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('average trips time in mintues : ',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())
    if(city != 'washington'):
        # TO DO: Display counts of gender
        print(df['Gender'].value_counts())

        # TO DO: Display earliest 
        print("biggest one to try ",int(df['Birth Year'].min()))
        # most recent
        print('youngest to try : ',int(df['Birth Year'].max())) 
        #and most common year of birth
        x = df['Birth Year'].mode()[0]
        print('most common age : ',int(x))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def raw_input(df):
    i = 5
    while(True):
        x = input('do you want see 5 lines of raw data ? Enter yes or no : ')
        if (x.lower() == 'yes'):
            print(df.iloc[:i])
            i+=5
        else :
            break
        


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_input(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()