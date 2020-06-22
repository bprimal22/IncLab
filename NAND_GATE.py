"""         Simulation/Testing code for Nand_gate
            4-4-20
            Author: BP Rimal
 """

import statistics
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib import style

# ---------------------------------------------------------------------------------------------------
# -------------------- PUT DATA HERE ----------------------------------------------------------------
Device = ["Device1", "Device2", "Device3"]
Vin = [3.5, 3.5]  # Voltage in for device 1 and 2
Rw = [2230, 3998, 2950]  # Wire Resistance of each device
Rap = [589, 855, 913]  # anti-parallel resistance for each device
Rp = [275, 347, 575]  # parallel resistances for each device
Hb = [100, 100, 100]  # mT, Bias Field
Vs1 = [0.5, 1, 1.5, 1.5, 6]  # Critical switching voltage for Device 1
Vs2 = [0.4, 1, 1.5, 1.8, 2.5, 3.8, 5.8]  # Critical switching voltage for Device 2
Vs3 = [2, 2.5, 6, 6.5, 6.5]  # Critical switching voltage for Device 3


# ******************************************************************************************************
# ******************************************************************************************************
# functions


# function for mean
# returns the mean for a list of numbers
# how to call: some_variable = mean(list_of_numbers)
def mean(values=[]):
    return statistics.mean(values)


# function for standard deviation
# returns standard_deviation for a list of numbers
# calling the function: some_variable = standard_deviation(list_of_numbers)
def standard_deviation(values=[]):
    std = statistics.pstdev(values, mean(values))
    return std


# function
# Input: Vin (input voltage from the voltage source)
#       Rw_a (Resistance of wire for device A
#       Rv_a (Variable resistance [Rp or Rap] for device A
# Inputs: Vin, Rw_a, Rw_b, Rw_c, Rv_a, Rv_b

# Output: V1: voltage at the junction of Vouts of Device A and B and input to Device 3.
#             V1 can also be understood as input voltage for Device 3.
def v1(vin, rw_a, rw_b, rw_c, rv_a, rv_b):
    numerator = (2 * vin * rw_c) * ((2 * rv_b) + rw_b + (2 * rv_a) + rw_a)
    denominator = ((2 * rw_c) * ((2 * rv_b) + rw_b + (2 * rv_a) + rw_a)) + (((2 * rv_a) + rw_a) * ((2 * rv_b) + rw_b))
    return numerator / denominator


# function
# Input: v1 for a certain test case
# Output: 1 if the third device switches
#         0 if the third device doesn't switch
def output(v1):
    if (v1 > Vc_min[2]) and v1 < Vc_max[2]:
        return 1  # device 3 switches
    else:
        return 0

# function
# Input: Output Voltage, label
# Output: none
#        plots onto the graph
def plot_range(v, str):
    plt.plot([v, v, v, v], [0, 1, 2, 3], label=str)
    plt.xlabel(" Input Voltage to Output Device")
    plt.legend()



# function
# Input: Output Voltage, label
# Output: none
#        plots onto the graph
def plot(v, str):
 #   plt.plot([v, v, v, v], [0, 1, 2, 3], label=str)
    plt.plot([v,v], [1, 2], label=str)
    plt.xlabel(" Input Voltage to Output Device")
    plt.legend()


# ***************************************************************************************************************
# ***************************************************************************************************************


# critical switching voltage for each device
Vc = [mean(Vs1), mean(Vs2), mean(Vs3)]

# uncertainty of switching voltage of each device; uncertainty= standard deviation of switching voltages for each device
Vc_uncertainty = [standard_deviation(Vs1), standard_deviation(Vs2), standard_deviation(Vs3)]

# min switching voltage
Vc_min = [(Vc[0] - Vc_uncertainty[0]), (Vc[1] - Vc_uncertainty[1]), (Vc[2] - Vc_uncertainty[2])]
plot_range(Vc_min[2], "min Voltage to Switch")

# max switching voltage
Vc_max = [(Vc[0] + Vc_uncertainty[0]), (Vc[1] + Vc_uncertainty[1]), (Vc[2] + Vc_uncertainty[2])]
print("Vc_max = ", Vc_max)
plot_range(Vc_max[2], "max Voltage to Switch")

# Cycle to cycle Variation given in percentage
c2c_variation = [Vc_uncertainty[0] / Vc[0], Vc_uncertainty[1] / Vc[1], Vc_uncertainty[2] / Vc[2]]

print("Cycle to Cycle Variation for Device 1= ", c2c_variation[0] * 100, "%")
print("Cycle to Cycle Variation for Device 2= ", c2c_variation[1] * 100, "%")
print("Cycle to Cycle Variation for Device 3= ", c2c_variation[2] * 100, "%")

# Device to Device Variation
# given by the standard deviation of Mean switching voltage of each device
d2d_variation = standard_deviation(Vc)
print("Device to Device Variation (voltage) = ", d2d_variation)
print("Device to Device Variation (%) = ", d2d_variation * 100 / mean(Vc), "%")

# -----------------------NAND CASES ---------------------------------

# 00 = 0 case
# Inputs: Vin, Rw_a, Rw_b, Rw_c, Rv_a, Rv_b
V00 = v1(Vin[0], Rw[0], Rw[1], Rw[2], Rap[0], Rap[1])
print('V00 = ', V00)
if output(V00) == 1:
    print("00 case fails")
if output(V00) == 0:
    print("00 case works")
plot(V00, "V00")

# 01 = 0 case
V01 = v1(Vin[0], Rw[0], Rw[1], Rw[2], Rap[0], Rp[1])
print('V01 = ', V01)
if output(V01) == 1:
    print("01 case fails")
if output(V01) == 0:
    print("01 case works")
plot(V01, "V01")

# 10 = 0 case
V10 = v1(Vin[0], Rw[0], Rw[1], Rw[2], Rp[0], Rap[1])
print('V10 = ', V10)
if output(V10) == 1:
    print("10 case fails")
if output(V00) == 0:
    print("10 case works")
plot(V10, "V10")

# 11 = 1 case
V11 = v1(Vin[0], Rw[0], Rw[1], Rw[2], Rp[0], Rp[1])
print('V11 = ', V11)
if output(V11) == 0:
    print("11 case fails")
if output(V11) == 1:
    print("11 case works")
plot(V11, "V11")


# ----------------------------------------------------------------------------------------------------------
# **********************************************************************************************************

# Min TMR Calculation

# function
# figures out what Variable Resistance for Device A works
# Input: Resistance of the wire of New Device, Rp of the other device
def parallel_resistance(Rw_device, R_p):
    num_min = Rw[2] * ((2 * R_p) + Rw[1]) * (Vc_min[2] - Vin[1])
    num_max = Rw[2] * ((2 * R_p) + Rw[1]) * (Vc_max[2] - Vin[1])
    den_min = 2 * Rw[2] * (Vin[1] - Vc_min[2]) - Vc_min[2] * ((2 * R_p) + Rw[1])
    den_max = 2 * Rw[2] * (Vin[1] - Vc_max[2]) - Vc_max[2] * ((2 * R_p) + Rw[1])
    min_variable_resistance = (num_min / den_max) - (0.5 * Rw_device)
    max_variable_resistance = (num_max / den_min) - (0.5 * Rw_device)
    print("New Device A Rp min =", min_variable_resistance)
    print("New Device A Rp max =", max_variable_resistance)


parallel_resistance(Rw[0], Rp[0])


# function
# figures out what Variable Resistance for Device A works
# Input: Resistance of the wire of New Device, Rp of the other device
def antiparallel_resistance(Rw_device, R_ap):
    num_min = Rw[2] * ((2 * R_ap) + Rw[1]) * (0 - Vin[1])
    num_max = Rw[2] * ((2 * R_ap) + Rw[1]) * (Vc_min[2] - Vin[1])
    den_min = 2 * Rw[2] * (Vin[1])
    den_max = 2 * Rw[2] * (Vin[1] - Vc_min[2]) - Vc_min[2] * ((2 * R_ap) + Rw[1])
    min_variable_resistance = (num_min / den_max) - (0.5 * Rw_device)
    max_variable_resistance = (num_max / den_min) - (0.5 * Rw_device)
    print("New Device A Rap min =", min_variable_resistance)
    print("New Device A Rap max =", max_variable_resistance)


antiparallel_resistance(Rw[0], Rap[0])

plt.show()
