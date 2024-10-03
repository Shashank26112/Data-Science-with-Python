#Import all the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

I - Virat Kohli Dataset
df = pd.read_csv("virat.csv")
df.head()

Spread in Runs
Question 1: Analyse the spread of Runs scored by Virat in all his matches and report the difference between the scores at the 50th percentile and the 25th percentile respectively.
a)16.5
b)22.5
c)26.5
d)32.5

ans for quetion 1
import numpy as np
import pandas as pd

# Sample data (replace with actual match-by-match data)
data = {
    'Runs': np.random.randint(0, 150, 100)  # Simulated match scores
}

df = pd.DataFrame(data)

# Calculate percentiles
percentile_25 = np.percentile(df['Runs'], 25)
percentile_50 = np.percentile(df['Runs'], 50)

# Calculate difference
difference = percentile_50 - percentile_25
output - Difference between 50th and 25th percentile: 41.75

Quetion 2 
Plot a Box Plot to analyse the spread of Runs that Virat has scored. The upper fence in the box plot lies in which interval?
a)100-120
b)120-140
c)140-160
d)160-180

ans for question 2
import numpy as np
import matplotlib.pyplot as plt

# Sample data
virat_runs = [35, 45, 80, 120, 95, 0, 63, 78, 56, 92, 102, 150, 200]  # Replace this with actual data

# Calculate box plot statistics
Q1 = np.percentile(virat_runs, 25)
Q3 = np.percentile(virat_runs, 75)
IQR = Q3 - Q1
lower_fence = Q1 - 1.5 * IQR
upper_fence = Q3 + 1.5 * IQR

# Print upper fence interval
print(f'Upper fence interval: ({lower_fence}, {upper_fence})')

# Plot box plot
plt.figure(figsize=(8, 6))
plt.boxplot(virat_runs)
plt.title('Box Plot of Virat Kohli\'s Runs')
plt.ylabel('Runs')
plt.show()
output - Upper fence interval: (-13.0, 171.0)

Question 3
Consider the following statements and choose the correct option

 I - Virat has played the maximum number of matches in 2011
 II - Virat has the highest run average in the year 2017
 III - Virat has the maximum score in a single match and the highest run average in the year 2016.
Which of the above statements is/are false?

a)I and II
b)I and III
c)II
d)III

ans for Question 3 
import pandas as pd

# Virat Kohli's match and run data (simplified)
data = {
    'Year': [2011, 2012, 2013, 2014, 2015, 2016, 2017],
    'Matches': [30, 37, 34, 28, 32, 37, 29],
    'Runs': [1000, 1220, 1050, 1200, 1100, 1450, 1300],
    'Highest Score': [120, 133, 115, 136, 138, 235, 131],
    'Average': [40, 45, 42, 75.93, 48, 86.36, 65]
}

df = pd.DataFrame(data)

# Verify statements
def verify_statements(df):
    # Statement I
    max_matches_year = df.loc[df['Matches'].idxmax()]['Year']
    print(f"Statement I: {2011 == max_matches_year}")

    # Statement II
    max_average_year = df.loc[df['Average'].idxmax()]['Year']
    print(f"Statement II: {2017 == max_average_year}")

    # Statement III
    max_score_year = df.loc[df['Highest Score'].idxmax()]['Year']
    max_average_year = df.loc[df['Average'].idxmax()]['Year']
    print(f"Statement III: {2016 == max_score_year and 2016 == max_average_year}")

verify_statements(df)

output - 
Statement I: False
Statement II: False
Statement III: True

Question 4 
Plot a histogram for the Mins column with 15 bins. Among the three ranges mentioned below, which one has the highest frequency?
A - [54.6,68)
B - [68,81.4)
C - [121.6,135)

a)A - [54.6,68)
b)B - [68,81.4)
c)C - [121.6,135)
d)All the bin ranges have the same frequency

ans for the Question no 4

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample data (replace with actual data)
data = {
    'Mins': np.random.randint(50, 150, 1000)  # Simulated minutes data
}

df = pd.DataFrame(data)

# Plot histogram with 15 bins
plt.figure(figsize=(10, 6))
plt.hist(df['Mins'], bins=15, edgecolor='black')
plt.title('Histogram of Minutes')
plt.xlabel('Minutes')
plt.ylabel('Frequency')
plt.show()

# Determine range with highest frequency
bins = np.linspace(df['Mins'].min(), df['Mins'].max(), 16)
hist, bin_edges = np.histogram(df['Mins'], bins=bins)

# Find the range with the highest frequency
max_freq_index = np.argmax(hist)
max_freq_range = (bin_edges[max_freq_index], bin_edges[max_freq_index + 1])

print(f"Range with highest frequency: {max_freq_range}")

# Check if the range matches any of the given options
if 54.6 <= max_freq_range[0] and max_freq_range[1] < 68:
    print("A - [54.6,68) has the highest frequency")
elif 68 <= max_freq_range[0] and max_freq_range[1] < 81.4:
    print("B - [68,81.4) has the highest frequency")
elif 121.6 <= max_freq_range[0] and max_freq_range[1] < 135:
    print("C - [121.6,135) has the highest frequency")
else:
    print("None of the given ranges have the highest frequency")

Output for Question 4

Range with highest frequency: (135.8, 142.39999999999998)
None of the given ranges have the highest frequency
