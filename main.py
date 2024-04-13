import numpy as np
from matplotlib import pyplot as plt

save_path = "/Users/syfme/Desktop/pythonStudy/dSciencePro"
#########
def data_to_dict(data):
    data_dict = {}
    for i in range(1, len(data)):
        row = data[i]
        name = row[0]
        steps = np.array(data[i][1:], dtype = int)
        data_dict[name] = steps
    return data_dict

#########
def hourly_to_daily(hourly_steps):
    daily_steps = []
    for i in range(0, len(hourly_steps), 24):
        day_step = hourly_steps[i:i+24]
        daily_count = sum(day_step)
        daily_steps.append(daily_count)
    return daily_steps

#########
def coumpute_stats(data_dict):
    stats_dict = {}
    for key, value in data_dict.items():
       stats_dict[key] = {"Minimum": min(value), "Maximum": max(value), "Average": np.mean(value)}
    return stats_dict

#########
def choose_category(avg_list):
    categories = {"concerning": 0, "Average": 0, "Excellent": 0}
    for avg in avg_list:
        if avg < 5000:
            categories["concerning"] += 1
        elif avg < 10000:
            categories["Average"] += 1
        elif avg >= 10000:
            categories["Excellent"] += 1
        else:
            print("Invalid")
    return categories

#########
def daily_to_total(daily_steps):
    total_dict = {}
    for name, steps in daily_steps.items():
        total_dict[name] = sum(steps)
    return total_dict

#########
def find_min_index(input_list): # Use the helper function for mySort 
    
    current_min = input_list[0]
    index = 0
    for i in range(len(input_list)):
        if input_list[i] < current_min:
            current_min = input_list[i]
            index = i

    return index

#########
def my_sort(user_names, user_steps):
    sorted_user_names = []
    sorted_user_steps = []
    for i in range(len(user_steps)):
        min_index = find_min_index(user_steps)
        sorted_user_names.append(user_names[min_index])
        sorted_user_steps.append(user_steps[min_index])
        user_steps[min_index] = float('inf')
    return sorted_user_names, sorted_user_steps

#########
def plot_line(steps): 
    
    hour_list = range(24)
    plt.plot(hour_list, steps)
    plt.title("Performance over the day")
    plt.xlabel("Hour")
    plt.ylabel("Steps")
    plt.savefig(save_path+"plot4.png")
    plt.close()

def plot_pie(categories):
    # Write your code here
    plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%')
    plt.title("Pie chart for the categories")
    plt.savefig(save_path+"plot3.png")
    plt.close()

def plot_bar(sorted_names, sorted_steps):
    # Write your code here
    plt.bar(sorted_names, sorted_steps)
    plt.title("Bar chart for participants")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(save_path+"plot2.png")
    plt.close()

def plot_bubbles(daily_step_dict):
    # Write your code here
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
           
    for key in daily_step_dict:
        plt.scatter(days, [key]*7, np.array(daily_step_dict[key])/30)
    plt.title("Bubble chart for the participants")
    plt.xlabel("Day")
    plt.ylabel("Participants")
    plt.savefig(save_path+"plot1.png")
    plt.close()

#########
def main():

#########    
    data = np.loadtxt('steps.csv', delimiter=',', dtype = str)
    data_dict = data_to_dict(data)

    daily_step_dict = {}
    for key in data_dict:
        daily_steps = hourly_to_daily(data_dict[key])
        daily_step_dict[key] = daily_steps

    stats_dict = coumpute_stats(daily_step_dict)
    for key in stats_dict:
        print(key, stats_dict[key])

    avg_list = []
    for key in stats_dict:
        avg_list.append(stats_dict[key]["Average"])
    
    categories = choose_category(avg_list)
    print("Members in each category: ", categories)

    total_step_dict = daily_to_total(daily_step_dict)
    unserted_user_names = list(total_step_dict.keys())
    unserted_user_steps = list(total_step_dict.values())
    sorted_user_names, sorted_user_steps = my_sort(unserted_user_names, unserted_user_steps)

    for i in range(len(sorted_user_names)):
        print(sorted_user_names[i], sorted_user_steps[i])   

    steps = data_dict["Juliana"][0:24]
    plot_line(steps) 

    plot_pie(categories)


    plot_bar(sorted_user_names, sorted_user_steps)

    plot_bubbles(daily_step_dict)

#########
main()
