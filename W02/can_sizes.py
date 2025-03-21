# Import libraries
import math

# Define pi variable
pi = math.pi
# Create can sizes directory
can_details = [
    {
        'name': '#1 Picnic',
        'radius': 6.83,
        'height': 10.16,
        'cost': 0.28,
    },
    {
        'name': '#1 Tall',
        'radius': 7.78,
        'height': 11.91,
        'cost': 0.43,
    },
    {
        'name': '#2',
        'radius': 8.73,
        'height': 11.59,
        'cost': 0.45,
    },
    {
        'name': '#2.5',
        'radius': 10.32,
        'height': 11.91,
        'cost': 0.61,
    },
    {
        'name': '#3 Cylinder',
        'radius': 10.79,
        'height': 17.78,
        'cost': 0.86,
    },
    {
        'name': '#5',
        'radius': 13.02,
        'height': 14.29,
        'cost': 0.83,
    },
    {
        'name': '#6Z',
        'radius': 5.40,
        'height': 8.89,
        'cost': 0.22,
    },
    {
        'name': '#8Z short',
        'radius': 6.83,
        'height': 7.62,
        'cost': 0.26,
    },
    {
        'name': '#10',
        'radius': 15.72,
        'height': 17.78,
        'cost': 1.53,
    },
    {
        'name': '#211',
        'radius': 6.83,
        'height': 12.38,
        'cost': 0.34,
    },
    {
        'name': '#300',
        'radius': 7.62,
        'height': 11.27,
        'cost': 0.38,
    },
    {
        'name': '#303',
        'radius': 8.10,
        'height': 11.11,
        'cost': 0.42,
    },
]
# Main function to compute the efficency of cans
def main():
    best_se = 0
    best_se_name = ''
    best_ce = 0
    best_ce_name = ''
    for can in can_details:
        volume = compute_volume(can['radius'], can['height'])
        surface_area = compute_surface_area(can['radius'], can['height'])
        storage_efficiency = compute_storage_efficiency(volume, surface_area)
        cost_efficiency = compute_cost_efficiency(volume, can['cost'])

        if cost_efficiency > best_ce:
            best_ce = cost_efficiency
            best_ce_name = can['name']
        else:
            best_ce
        
        if storage_efficiency > best_se:
            best_se = storage_efficiency
            best_se_name = can['name']
        else:
            best_se

        print(f'{can['name']} - SE: {storage_efficiency:.2f} || ' + \
              f'CE: {cost_efficiency:.2f}')
    print(f'\nBest storage efficiency: {best_se_name} - {best_se:.2f}\n' \
          f'Best cost efficiency: {best_ce_name} - {best_ce:.2f}\n')

# Compute volume for the cans
def compute_volume(radius, height):
    volume = pi * radius**2 * height
    return volume

# Compute surface area for the cans
def compute_surface_area(radius, height):
    surface_area = 2 * pi * radius * (radius + height)
    return surface_area

# Stretch challenge

# Compute storage efficiency
def compute_storage_efficiency(volume, surface_area):
    efficiency = volume / surface_area
    return efficiency

# Compute cost efficiency
def compute_cost_efficiency(volume, cost):
    cost_efficiency = volume / cost
    return cost_efficiency

main()