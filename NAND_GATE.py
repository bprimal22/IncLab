"""         Simulation/Testing code for Nand_gate
            4-4-20
            Author: BP Rimal
 """

import statistics

#function for mean
# returns the mean for a list of numbers
# how to call: some_variable = mean(list_of_numbers)
def mean(values = []):
    return statistics.mean(values)


# function for standard deviation
# returns standard_deviation for a list of numbers
# calling the function: some_variable = standard_deviation(list_of_numbers)
def standard_deviation(values = []):
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
    numerator = (2*vin*rw_c)*((2*rv_b)+rw_b+(2*rv_a)+rw_a)
    denominator = ((2*rw_c)*((2*rv_b)+rw_b+(2*rv_a)+rw_a)) + (((2*rv_a)+rw_a)*((2*rv_b)+rw_b))
    return numerator/denominator


Device = ["Device1", "Device2", "Device3"]
Vin = [6, 6]                             # Voltage in for device 1 and 2
Rw = [6647, 5289, 4013]                     # Wire Resistance of each device
Rap = [35, 44, 32]                          # anti-parallel resistance for each device
Rp = [4.5, 11, 2]                           # parallel resistances for each device
Hb = [0.025, 0.025, 0.025]                  # mT, Bias Field
Vs1 = [4, 5, 5, 4.7, 4.4]                 # Critical switching voltage for Device 1
Vs2 = [1, 2, 3, 4, 5]                       # Critical switching voltage for Device 2
Vs3 = [1, 2, 3, 4, 5]                       # Critical switching voltage for Device 3
Vc = [mean(Vs1), mean(Vs2), mean(Vs3)]      # critical switching voltage for each device

# uncertainty of switching voltage of each device; uncertainty= standard deviation of switching voltages for each device
Vc_uncertainty = [standard_deviation(Vs1), standard_deviation(Vs2), standard_deviation(Vs3)]

# min switching voltage
Vc_min = [(Vc[0]-Vc_uncertainty[0]), (Vc[1]-Vc_uncertainty[1]), (Vc[2]-Vc_uncertainty[2])]

# max switching voltage
Vc_max = [(Vc[0]+Vc_uncertainty[0]), (Vc[1]+Vc_uncertainty[1]), (Vc[2]+Vc_uncertainty[2])]

# Cycle to cycle Variation given in percentage
c2c_variation = [Vc_uncertainty[0]/Vc[0], Vc_uncertainty[1]/Vc[1], Vc_uncertainty[2]/Vc[2]]

print("Cycle to Cycle Variation for Device 1= ", c2c_variation[0]*100, "%")
print("Cycle to Cycle Variation for Device 2= ", c2c_variation[1]*100, "%")
print("Cycle to Cycle Variation for Device 3= ", c2c_variation[2]*100, "%")

# Device to Device Variation
# given by the standard deviation of Mean switching voltage of each device
d2d_variation = standard_deviation(Vc)
print("Device to Device Variation (voltage) = ", d2d_variation)
print("Device to Device Variation (%) = ", d2d_variation*100/mean(Vc), "%")

# -----------------------NAND CASES ---------------------------------

# 00 = 1 case

# Inputs: Vin, Rw_a, Rw_b, Rw_c, Rv_a, Rv_b
V00 = v1(Vin[0], Rw[0], Rw[1], Rw[2], Rap[0], Rap[1])

# 01 = 1 case
V01 = v1(Vin[0], Rw[0], Rw[1], Rw[2], Rap[0], Rp[1])

# 10 = 1 case
V10 = v1(Vin[0], Rw[0], Rw[1], Rw[2], Rp[0], Rap[1])

# 11 = 0 case
V11 = v1(Vin[0], Rw[0], Rw[1], Rw[2], Rp[0], Rp[1])






