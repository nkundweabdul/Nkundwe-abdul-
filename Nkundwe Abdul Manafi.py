
def calculate_reduced_levels(data):
    RL = [0]  # The first station's RL is assumed to be zero

    for i in range(1, len(data)):
        backsight = data[i][0]
        intersight = data[i][1]
        foresight = data[i][2]

        RL.append(RL[i - 1] + backsight - intersight + foresight)

    return RL

# Station data: [Backsight, Intermediate Sight, Foresight]
station_data = [
    [1.325, 1.520, 1.200],
    [1.200, 1.400, 1.300],
    [1.300, 1.600, 1.250],
    [1.250, 1.450, 1.150],
    [1.150, 1.350, 1.100],
    [1.100, 1.300, 1.050],
    [1.050, 1.250, 1.000],
    [1.000, 1.200, 0.900],
    [0.900, 1.100, 0.850],
    [0.850, 1.050, 0.800]
]

reduced_levels = calculate_reduced_levels(station_data)

for i, rl in enumerate(reduced_levels):
    print(f"Station {chr(65 + i)} - Reduced Level: {rl:.3f}")


    def calculate_reduced_levels(data):
        RL = [0]  # The first station's RL is assumed to be zero

        for i in range(1, len(data)):
            backsight = data[i][0]
            intersight = data[i][1]
            foresight = data[i][2]

            RL.append(RL[i - 1] + backsight - intersight + foresight)

        return RL


    # Station data: [Backsight, Intermediate Sight, Foresight]
    station_data = [
        [1.325, 1.520, 1.200],
        [1.200, 1.400, 1.300],
        [1.300, 1.600, 1.250],
        [1.250, 1.450, 1.150],
        [1.150, 1.350, 1.100],
        [1.100, 1.300, 1.050],
        [1.050, 1.250, 1.000],
        [1.000, 1.200, 0.900],
        [0.900, 1.100, 0.850],
        [0.850, 1.050, 0.800]
    ]

    reduced_levels = calculate_reduced_levels(station_data)

    for i, rl in enumerate(reduced_levels):
        print(f"Station {chr(65 + i)} - Reduced Level: {rl:.3f}")

import matplotlib.pyplot as plt

# Road width and scale factor for illustration purposes
road_width = 10
scale_factor = 10

# Create cross-section points
cross_section = [(0, 0)]  # Starting point

for i, rl in enumerate(reduced_levels):
    x = i * scale_factor
    y = rl
    cross_section.append((x, y))

# Ending point
cross_section.append((len(reduced_levels) * scale_factor, 0))

# Extract X and Y coordinates for plotting
X = [point[0] for point in cross_section]
Y = [point[1] for point in cross_section]

# Create the cross-sectional diagram
plt.figure(figsize=(10, 6))
plt.plot(X, Y, marker='o', linestyle='-', color='b')
plt.fill_between(X, Y, color='lightgray')
plt.xlabel("Distance along Road")
plt.ylabel("Reduced Level")
plt.title("Cross-Sectional Diagram of the Road")
plt.grid()
plt.show()
