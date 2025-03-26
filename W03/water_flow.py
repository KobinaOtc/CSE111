'''
Write a Python program that could help an engineer 
design a water distribution system. During this prove 
milestone, you will write three program functions and 
three test functions as described in the Steps section 
below.
'''

# Exceeding the Requirements
'''
Inside the functions of your water_flow.py program, you 
may have typed numbers for Earth’s acceleration of gravity, 
the density of water, and the dynamic viscosity of water. 
Instead of using the numbers inside your functions, define 
the following constants outside your functions. Then use the 
constant names in place of the numbers inside your functions.
'''
EARTH_ACCELERATION_OF_GRAVITY = 9.8066500
WATER_DENSITY = 998.2000000
WATER_DYNAMIC_VISCOSITY = 0.0010016
PSI_CONVERSION_FACTOR = 0.14503773773020923

def water_column_height(tower_height, tank_height):
    '''
    Write a function named water_column_height that 
    calculates and returns the height of a column of 
    water from a tower height and a tank wall height.
    '''
    height = tower_height + ((3 * tank_height) / 4)
    return height

def pressure_gain_from_water_height(height):
    '''
    Write a function named pressure_gain_from_water_height 
    that calculates and returns the pressure caused by Earth’s 
    gravity pulling on the water stored in an elevated tank.
    '''
    pressure = (WATER_DENSITY* EARTH_ACCELERATION_OF_GRAVITY * height) / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_lelngth, friction_factor, fluid_velocity):
    '''
    Write a function named pressure_loss_from_pipe that 
    calculates and returns the water pressure lost 
    because of the friction between the water and the walls 
    of a pipe that it flows through.
    '''
    lost_pressure = (-1 * (friction_factor * pipe_lelngth * WATER_DENSITY* fluid_velocity**2)) / (2000 * pipe_diameter)
    return lost_pressure

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    '''
    Write a function named pressure_loss_from_fittings that
    calculates the water pressure lost because of fittings 
    such as 45° and 90° bends that are in a pipeline.
    '''
    lost_preasure = (-0.04 * WATER_DENSITY* fluid_velocity**2 * quantity_fittings) / 2000
    return lost_preasure

def reynolds_number(hydraulic_diameter, fluid_velocity):
    '''
    Write a function named reynolds_number that calculates
    and returns the Reynolds number for a pipe with water 
    flowing through it. The Reynolds number is a unitless 
    ratio of the inertial and viscous forces in a fluid that 
    is useful for predicting fluid flow in different situations.
    '''
    rey_num = (WATER_DENSITY* hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY
    return rey_num

def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
    '''
    write a function named pressure_loss_from_pipe_reduction 
    that calculates the water pressure lost because of water 
    moving from a pipe with a large diameter into a pipe with 
    a smaller diameter.
    '''
    constant = (0.1 + (50 / reynolds_number)) * ((larger_diameter / smaller_diameter)**4 - 1)
    lost_pressure = ((-1 * constant) * WATER_DENSITY* fluid_velocity**2) / 2000
    return lost_pressure

# Exceeding the Requirements
'''
The functions that you wrote for this assignment, calculate 
water pressure in kilopascals (kPa). In the United States, 
water pressure is usually expressed in pounds per square inch 
(psi). Write a function in your water_flow.py program that 
converts kPa to psi. Then at the bottom of your main function, 
add code that calls your conversion function and prints the 
final pressure value in both kPa and psi.
'''
def convert_to_psi(kpa):
    psi = kpa * PSI_CONVERSION_FACTOR
    return psi

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    pressure_in_psi = convert_to_psi(pressure)
    # Exceeding the Requirements
    print(f"Pressure at house: {pressure:.1f} kilopascals\nPressure converted to pounds per square inch: {pressure_in_psi:.1f}psi")

if __name__ == "__main__":
    main()