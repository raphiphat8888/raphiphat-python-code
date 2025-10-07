"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""
def get_temperatures():
    temp=[]
    for i in range(0,7):
        temp.append(float(input(f"Please enter the temperature for day {i+1} (degrees):")))
    return temp
def analyze_temps(temp_list):
    average_temp=sum(temp_list)/7
    hight_temp=max(temp_list)
    low_temp=min(temp_list)
    return (low_temp,hight_temp,average_temp)
    
def display_analysis(avg, high, low):
    print(f"Average:{avg}C")
    print(f"Highest:{high}C")
    print(f"Lowest:{low}C")
    
temp_list=get_temperatures()
resul=analyze_temps(temp_list)
low, high, avg = resul 
display_analysis(avg, high, low)
