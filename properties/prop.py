import numpy as np
import os

# Sun properties
# from: https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html
mass_sun = 1988500e24 # Mass of Sun in kg

# Mercury properties
# from: https://nssdc.gsfc.nasa.gov/planetary/factsheet/mercuryfact.html and https://ssd.jpl.nasa.gov/horizons/app.html#/
mass_mercury = 0.33010e24 # Mass of Mercury in kg
mercury_initial_position = np.array([-4.227610797568034E+10,  2.461564789560287E+10,  1.748360510496309E+10])
mercury_initial_velocity = np.array([-3.864898908767687E+04, -3.446562017696801E+04, -1.440384777280466E+04])

# Venus properties
# from: https://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html and https://ssd.jpl.nasa.gov/horizons/app.html#/
mass_venus = 4.8673e24 # Mass of    Venus in kg
venus_initial_position = np.array([-1.081907314450878E+08, -1.331508778140792E+07,  8.192114637316635E+05])
venus_initial_velocity = np.array([3.521901293154280E+03, -3.183074167752113E+04, -1.454493003810148E+04])

# Earth properties
# from: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html and https://ssd.jpl.nasa.gov/horizons/app.html#/
mass_earth = 5.9722e24 # Mass of Earth in kg
earth_initial_position = np.array([-2.600745330322259E+10,  1.326237828764555E+11,  5.752511716959091E+10]) # Initial position of Earth in m
earth_initial_velocity = np.array([-2.983800155786667E+04, -4.724379075830139E+03, -2.047849455589723E+03]) # Initial velocity of Earth in m/s

# Mars properties
# from: https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html and https://ssd.jpl.nasa.gov/horizons/app.html#/
mass_mars = 0.64169e24 # Mass of Mars in kg
mars_initial_position = np.array([-4.507776377918092E+10, -1.982014470800611E+11, -8.968192116531172E+10])
mars_initial_velocity = np.array([2.467035556790299E+04, -2.245391192030446E+03, -1.695102811755501E+03])

# Jupiter properties
# from: https://nssdc.gsfc.nasa.gov/planetary/factsheet/jupiterfact.html and https://ssd.jpl.nasa.gov/horizons/app.html#/
mass_jupiter = 1898.13e24 # Mass of Jupiter in kg
jupiter_initial_position = np.array([5.213787916839414E+11,  4.930595483661216E+11,  1.986508040963638E+11])
jupiter_initial_velocity = np.array([-9.471106131757649E+03,  8.895259661965978E+03,  4.043350526801355E+03])

# L4 properties
# from Vinogradova, T.A., Chernetenko, Y.A. Total mass of the Jupiter Trojans. Sol Syst Res 49, 391–397 (2015). https://doi.org/10.1134/S0038094615060076
#  and https://ssd.jpl.nasa.gov/horizons/app.html#/
mass_L4 = 0.19E-10 * mass_sun
L4_initial_position = np.array([-2.441314152698758E+11,  6.773311675172310E+11,  2.962716265074904E+11])
L4_initial_velocity = np.array([-1.256124827427834E+04, -3.308022912279178E+03, -1.112101126943102E+03])

# Jupiter L5 Properties
# from Vinogradova, T.A., Chernetenko, Y.A. Total mass of the Jupiter Trojans. Sol Syst Res 49, 391–397 (2015). https://doi.org/10.1134/S0038094615060076
#  and https://ssd.jpl.nasa.gov/horizons/app.html#/
mass_L5 = 0.11E-10 * mass_sun
L5_initial_position = np.array([6.986405083034292E+11, -2.319214104683651E+11, -1.164147752198974E+11])
L5_initial_velocity = np.array([4.386372878157628E+03,  1.186232117548549E+04,  4.977818054669012E+03])

# Saturn properties
# from: https://nssdc.gsfc.nasa.gov/planetary/factsheet/saturnfact.html and https://ssd.jpl.nasa.gov/horizons/app.html#/
mass_saturn = 568.32e24 # Mass of Saturn in kg
saturn_initial_position = np.array([1.344601481340454E+12, -4.930070052366619E+11, -2.615508262476352E+11])
saturn_initial_velocity = np.array([3.153932310901134E+03,  8.283282120269398E+03,  3.285573832689920E+03])

# Uranus properties
# from: https://nssdc.gsfc.nasa.gov/planetary/factsheet/uranusfact.html and https://ssd.jpl.nasa.gov/horizons/app.html#/
mass_uranus = 86.811e24 # Mass of Uranus in kg
uranus_initial_position = np.array([1.836138718926769E+12,  2.106621323518811E+12,  8.966192157686862E+11])
uranus_initial_velocity = np.array([-6.933507094073330E+03,  4.620953798868459E+03,  2.346696882933535E+03])
# Neptune properties
# from: https://nssdc.gsfc.nasa.gov/planetary/factsheet/neptunefact.html and https://ssd.jpl.nasa.gov/horizons/app.html#/
mass_neptune = 102.409e24 # Mass of Neptune in kg
neptune_initial_position = np.array([4.464870909756847E+12, -2.065589784787017E+11, -1.957151017472855E+11])
neptune_initial_velocity = np.array([-1.279763984862197E+03,  6.092274083726405E+03,  2.763111018370586E+03])
# Moon properties
# from: https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html and https://ssd.jpl.nasa.gov/horizons/app.html#/
mass_moon = 0.07346e25 # Mass of Moon in kg
moon_initial_position = np.array([-2.637093499608123E+10,  1.327648230502377E+11,  5.761337388984415E+10])
moon_initial_velocity = np.array([-3.024279048864922E+04, -5.494701852227165E+03, -2.445635834561632E+03])