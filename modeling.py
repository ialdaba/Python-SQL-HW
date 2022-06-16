"""
Name: Isabel Aldaba
"""
import statistics as stat
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
"""
Problem 1
"""
print("\n",40*"-","\n","Problem 1:\n",40*"-")
# Your code goes here:

def get_student_data(filename):
    """ 
    This function takes in a file name containing student data, 
    does some processing on its contents and returns two lists
    containing the students' heights and weights
    input: filename
    output: heights and weights
    """
    with open(filename) as f:
        data = f.readlines()
    sdata = data[9:]
    # Add missing code here (1 or 2 lines)
    heights = []
    weights = []
    for i in sdata:
        heights.append(float((i.strip().split())[3]))
        weights.append(float((i.strip().split())[4]))
    # Add missing code here (1 line)
    return heights, weights

        
def problem1():
    # get heights and weights (1 line)
    heights, weights = get_student_data("student-data.txt")
    # compute mean height and weight (2 to 4 lines)
    avg_height = stat.mean(heights)
    avg_weight = stat.mean(weights)
    # plot data in 2x1 subplot. Add titles and labels (~ 5 lines)
    fig, axs = plt.subplots(2)
    xs = [x for x in range(len(heights))]
    axs[0].plot(xs, heights)
    axs[1].plot(xs, weights)
    axs[1].set_xlabel('Students')
    axs[0].set_ylabel('Heights (m)')
    axs[1].set_ylabel('Weights (kg)')
    axs[0].set_title('Heights and Weights of Students')

    # Extra credit (5 points)
    # Set x-limits and draw horizontal lines in red depicting means (~4 lines)
    axs[0].set_xlim(0, len(heights))
    axs[1].set_xlim(0, len(heights))
    axs[0].axhline(y = avg_height, c = "red")
    axs[1].axhline(y = avg_weight, c = "red")
    plt.show()
    plt.close()

# The following function runs your solution to problem 1
problem1()


"""
Problem 2
"""
print("\n",40*"-","\n","Problem 2:\n",40*"-")
# Your code goes here:

real= [1250.862449,1339.27466,1105.662566,1285.836143,1103.109547,1612.339172,
1980.645671,1094.928631,1106.021095,1395.516017,1234.742802,1453.741622,
1877.775261,1735.760669,1061.105059,1141.61727,1232.546287,1485.125246,
1179.093054,1763.176488,1714.704881]

predicted1= [1182.606513,1307.566548,1090.355357,1201.72772,1018.931609,
1586.741282,2073.734861,1121.749607,1093.164682,1345.728877,1181.388135,
1448.568219,1969.430382,1814.077539,1049.854831,1082.983318,1180.202392,
1498.650818,1269.523802,1692.147555,1631.618131]

predicted2= [1133.551213,1513.707178,926.7290148,1209.725911,1162.997602,
1662.447832,2037.447472,1004.68639,1065.033088,1505.190448,1011.728527,
1404.182947,1791.450931,1890.973888,1258.784257,1046.073185,1447.674167,
1283.43618,1346.06017,1855.629737,1896.855581]

predicted3= [1289.241852,1299.489127,1111.466304,1291.57706,1089.332333,
1618.674814,1970.17006,1112.608575,1098.59952,1398.406631,1242.857086,
1440.71055,1904.378157,1726.489816,1074.062908,1154.1111,1205.761704,
1477.75526,1205.525527,1799.807165,1700.030472]

predicted4= [1239.101308,1368.323121,1153.675224,1360.178149,1100.856967,
1665.134624,1981.703675,1024.189308,1115.637818,1450.84443,1274.822387,
1413.251122,1895.693964,1781.094654,1055.899244,1124.727968,1204.491513,
1546.700815,1179.661864,1821.171408,1653.113871]

predicted5= [1409.626015,1453.250781,1128.692766,1253.232145,1011.672975,
1617.889011,2116.745579,1076.216619,1241.621266,1426.033861,1161.689203,
1405.614258,1970.826596,1738.837106,1214.056768,1277.983739,1347.514589,
1490.125462,1060.997381,1735.633865,1689.393989]

x_vals = [x for x in range(len(real))]

plt.plot(x_vals, predicted1, label = "Predicted 1")
plt.plot(x_vals, predicted2, label = "Predicted 2")
plt.plot(x_vals, predicted3, label = "Predicted 3")
plt.plot(x_vals, predicted4, label = "Predicted 4")
plt.plot(x_vals, predicted5, label = "Predicted 5")
plt.plot(x_vals, real, color = 'black', label = "Real", linewidth = 3)
plt.legend()
plt.show()

def performance(real, predicted):
	# take difference of real and predicted values then absolute value each
	abs_diff = abs(np.subtract(real,predicted))
	
	# find average difference
	answer = (np.sum(abs_diff)) / len(abs_diff)
	return answer
	
def problem2():

	preds = [predicted1, predicted2, predicted3, predicted4, predicted5]
	model_perform = []
	for i in preds:
		place = preds.index(i)
		print("Performance of Model", place+1, ":", performance(real,i))
		model_perform.append(performance(real,i))
	
	best = model_perform.index(min(model_perform)) + 1
	worst = model_perform.index(max(model_perform)) + 1
	print("The model that performs the best is:", best)
	print("The model that performs that worst is:", worst)

# The following function runs your solution to problem 2
problem2()

"""
Problem 3
"""
print("\n",40*"-","\n","Problem 3:\n",40*"-")
# Your code goes here:
def f(x):
	return ((((x**3) - (2*x))**2) / x) + 8
	
# add your solution here
def problem3():
    # PART A
    a = -2
    b = 2
    x = np.linspace(a,b)
    plt.plot(x, f(x))
    plt.grid()
    plt.xlim(a,b)
    plt.show()
    plt.close()
    
    exact_area = 2 * 16
    print("The exact area is", exact_area)
    
    # PART B
    N_areas = 100
    areas = np.zeros(N_areas)
    N_rand = 1000 # random points
    
    for i in range(N_areas):
    	xrand = np.random.uniform(a, b, N_rand)
    	my_sums = 0
    	# loop over xrand numbers
    	for j in range(N_rand):
    		my_sums += f(xrand[j])
    	# aggregate each area
    	areas[i] = (b-a) / N_rand * my_sums

    # PART C
    plt.title("Distribution of Areas")
    plt.hist(areas, bins = 50, ec = "black")
    plt.ylabel("Number of Areas")
    plt.xlabel("Area Values")
    plt.show()
    print("Mean of Distribution:", areas.mean())
    
    # PART D
    print(f"Absolute Error: {abs(exact_area - areas.mean()):.8f}")
    
    # PART E
    print("To improve the area estimate, I would increase the number of areas and random points.")
    print("Both would lead to an average area that is closer to the actual area.")
    print("This is because there would be an increase in trials and points approximating the curve.")
# The following function runs your solution to problem 3
problem3()

