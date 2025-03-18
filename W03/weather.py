def wind_chill(temp, wind_speed):
    chill_factor = 35.74 + 0.6215 * temp - 35.75 * wind_speed**0.16 + 0.4275 * temp * wind_speed**0.16
    rounded = round(chill_factor, 1)
    return rounded

def heat_index(temp, humidity):
    index = -42.379 + 2.04901523 * temp + 10.14333127 * humidity - 0.22475541 * temp * humidity \
    - 0.00683783 * temp**2 - 0.5481717 * humidity**2 + 0.00122874 * temp**2 * humidity + 0.00085282 \
    * temp * humidity**2 - 0.00000199 * temp**2 * humidity**2

    rounded = round(index, 1)
    return rounded

def cels_from_fahr(fahr):
    """Convert a temperature in Fahrenheit to
  Celsius and return the Celsius temperature.
  """
    cels = (fahr - 32) * 5 / 9
    return cels