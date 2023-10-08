from skyfield.api import load, Topos, EarthSatellite,utc
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create lists to store satellite objects
satellites = []

# Open and read the TLE data text file
with open('CALSPHERE.txt', 'r') as file:
    lines = file.readlines()

# Loop through the lines in the file
for i in range(0, 12, 3):
    tle_line1 = lines[i+1].strip()
    tle_line2 = lines[i+2].strip()

    # Create EarthSatellite objects for each satellite
    satellite = EarthSatellite(tle_line1, tle_line2)
    satellites.append(satellite)

# Calculate and plot the orbits for each satellite
for satellite in satellites:
    times = []
    positions = []

    start_time = datetime.now().replace(tzinfo=utc)
    end_time = start_time + timedelta(days=1)
    delta_time = timedelta(minutes=10)

    ts = load.timescale()
    t = start_time

    while t <= end_time:
        times.append(t)
        position = satellite.at(ts.utc(t))
        positions.append(position)
        t += delta_time

    x = [pos.position.km[0] for pos in positions]
    y = [pos.position.km[1] for pos in positions]
    z = [pos.position.km[2] for pos in positions]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)

    ax.set_xlabel('X (km)')
    ax.set_ylabel('Y (km)')
    ax.set_zlabel('Z (km)')
    ax.set_title('Satellite Orbit')

    plt.show()