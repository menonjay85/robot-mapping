import math
import matplotlib.pyplot as plt

def diffdrive(x, y, theta, v_l, v_r, t, l):
    # If both wheel velocities are equal, the robot moves straight
    if v_l == v_r:
        x_n = x + v_l * t * math.cos(theta)
        y_n = y + v_l * t * math.sin(theta)
        theta_n = theta
    else:
        # Compute the radius of the ICC (Instantaneous Center of Curvature)
        R = l / 2 * (v_l + v_r) / (v_r - v_l)
        # Compute the angular velocity
        omega = (v_r - v_l) / l
        # Compute the new orientation
        theta_n = theta + omega * t
        # Compute the center of the circle
        ICC_x = x - R * math.sin(theta)
        ICC_y = y + R * math.cos(theta)
        # Compute the new position
        x_n = ICC_x + R * math.sin(theta_n)
        y_n = ICC_y - R * math.cos(theta_n)

    return x_n, y_n, theta_n

# Initial position and orientation
x, y, theta = 1.5, 2.0, math.pi / 2
l = 0.5

# List to store trajectory for plotting
trajectory = [(x, y)]

# Command 1
v_l, v_r, t = 0.3, 0.3, 3
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
trajectory.append((x, y))

# Command 2
v_l, v_r, t = 0.1, -0.1, 1
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
trajectory.append((x, y))

# Command 3
v_l, v_r, t = 0.2, 0, 2
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
trajectory.append((x, y))

# Print final positions after each command
print(f"After command 1: x = {trajectory[1][0]}, y = {trajectory[1][1]}, theta = {theta}")
print(f"After command 2: x = {trajectory[2][0]}, y = {trajectory[2][1]}, theta = {theta}")
print(f"After command 3: x = {trajectory[3][0]}, y = {trajectory[3][1]}, theta = {theta}")

# Plotting the trajectory
x_vals, y_vals = zip(*trajectory)

plt.figure()
plt.plot(x_vals, y_vals, marker='o')
plt.title("Robot Trajectory")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.grid(True)
plt.axis('equal')

# Annotate the positions
for i, (x_val, y_val) in enumerate(trajectory):
    plt.annotate(f"P{i}", (x_val, y_val))

plt.show()
