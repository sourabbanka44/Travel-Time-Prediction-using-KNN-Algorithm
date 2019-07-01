# Importing libraries
import tkinter as tk
import pandas as pd
import numpy as np
import math
import operator

HEIGHT = 500
WIDTH = 950

# Importing data 
data = pd.read_csv("TRAIN_SET.csv")

data.head()

#Function to check whether the output Final string is valid
#check for any exceptions 
def format_response(time):
    try:

        final_str = 'Time Taken: %s minutes' % (time)
    except:
        final_str = 'There was a problem retrieving that information'

    return final_str


# Defining a function which calculates euclidean distance between two data points
def euclideanDistance(data1, data2, length):
    distance = 0
    for x in range(length):
        distance += np.square(data1[x] - data2[x])
    return np.sqrt(distance)


# Defining our KNN model
def knn(trainingSet, testInstance, k):
 
    distances = {}
    sort = {}
    #print(testInstance)
    length = testInstance.shape[1]
    
    #### 
    # Calculating euclidean distance between each row of training data and test data
    for x in range(len(trainingSet)):
        
        #### 
        dist = euclideanDistance(testInstance, trainingSet.iloc[x], length)

        distances[x] = dist[0]

        ####
 
    #### 
    # Sorting them on the basis of distance

    sorted_d = sorted(distances.items(), key=operator.itemgetter(1))

    #### 
 
    neighbors = []
    
    #### 
    # Extracting top k neighbors
    for x in range(k):
        neighbors.append(sorted_d[x][0])
    ####
    #print(neighbors)
    classVotes = {}
    
    ####
    # Calculating the most freq class in the neighbors
    for x in range(len(neighbors)):
        response = trainingSet.iloc[neighbors[x]][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1

    ####

    #### 
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)

    label['text'] = format_response(str(sortedVotes[0][0]))
    #return(sortedVotes[0][0], neighbors)
    #### 



print("DriverRanking - (61-121)")
print("RoadWorks -(2-6)")
print("Weather - 11 to 30 (Cold to High Temperature)")
print("Temperature - (48 - 70)")
root = tk.Tk()
root.resizable(width=False, height=False)
# Code to add widgets...

#Creating a rectangular area
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#attaching a background image
background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

#creating a frame for labels,entrys and button
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=1, relheight=0.3, anchor='n')


#creating 4 labels
label1 = tk.Label(frame,text="Driver Ranking")
label1.grid(row=0,column=0)

label2 = tk.Label(frame,text="Road Works")
label2.grid(row=0,column=1)

label3 = tk.Label(frame,text="Weather")
label3.grid(row=0,column=2)

label4 = tk.Label(frame,text="Temperature")
label4.grid(row=0,column=3)


#creating 4 entry widgets
entry = tk.Entry(frame, font=40)
entry.grid(row=1,column=0)

entry2 = tk.Entry(frame, font=40)
entry2.grid(row=1,column=1)

entry3 = tk.Entry(frame, font=40)
entry3.grid(row=1,column=2)

entry4 = tk.Entry(frame, font=40)
entry4.grid(row=1,column=3)

#print(type(entry.get()))
#declaring our parameter as 2
k=2


button = tk.Button(frame, text="Predict Time", font=40, command=lambda: knn(data, pd.DataFrame([[int(entry.get()),int(entry2.get()),int(entry3.get()),int(entry4.get())]]), k))
button.grid(row=1,column=4)


lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

#label for printing the predicted time
label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

#END
root.mainloop()