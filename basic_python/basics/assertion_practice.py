
def kelvin_to_farenheit(temp):
    assert (temp >= 0), "temp is zero"
    return ((temp -273)*1.8) + 32


print(kelvin_to_farenheit(-22222))