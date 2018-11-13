import csv
import math
import collections
import sys

# Global Variable for K - Nearest Neighbour
# set K value
K = 10
save = True

# Function to read data train
# Input : -
# Output : array[0..n] of array[0..5] of float
def readDataTrain():
    with open('DataTrain_Tugas3_AI.csv') as file:
        reader = csv.reader(file, delimiter=',')
        # Skip header
        reader.next()
        # Initialize array for result
        data = []
        for row in reader:
            # Remove first column (Index column)
            # Convert other column to float
            data.append(map(lambda x: float(x), row[1:]))
        return data


# Function to read data test
# Input -
# Output : array[0..n] of array[0..5] of float
def readDataTest():
    with open('DataTest_Tugas3_AI.csv') as file:
        reader = csv.reader(file, delimiter=',')
        # skip header
        reader.next()
        # initialize array for result
        data = []
        for row in reader:
            # remove first column (Index column)
            # convert column 1 - 6 to float
            # set last column to -1 which mean not classed yet
            data.append(map(lambda x: float(x), row[1:6]))
        return data

# Function to measure distance between 2 data using euclidean distance algoritm
# Input : array of float, array of float
# Output : distance between 2 array of float
def euclideanDistance(inputX, inputY):
    # Check if equal length
    if(len(inputX) != len(inputY)):
        print "Wrong input size"
        return
    euclidean = map(lambda x,y: (x - y)**2, inputX, inputY)
    return math.sqrt(sum(euclidean))

def saveResult(results):
    with open('TebakanTugas3.csv', mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        i = 1
        for result in results:
            writer.writerow([i, result])
            i += 1

if __name__ == '__main__':
    if(len(sys.argv) > 1):
        K = int(sys.argv[1])
    if(len(sys.argv) > 2):
        save = sys.argv[2]
    # Load data
    training_data = readDataTrain()
    test_data = readDataTest()
    # Check if K > training_data length
    if(K > len(training_data)):
        print "K can't not greater than", len(training_data)
        exit(1)
    results = []
    for test in test_data:
        list_distance = []
        for train in training_data:
            # Get euclidean distance, and set last index as their class
            list_distance.append([euclideanDistance(test, train[:5]), train[5]])
        # Sort the distance Ascending
        list_distance.sort(key=(lambda x:x[0]))
        # Slice the list, get the K first data
        nearest_distance = list_distance[:K]
        # Slice between distance and class into individual list
        distance, class_type = zip(*nearest_distance)
        # Count the class type
        counter = collections.Counter(class_type)
        # Get the most common count
        result = counter.most_common(1)[0][0]
        print result
        # Append it to results
        results.append(result)
    # Save if save equal true
    if save:
        saveResult(results)

