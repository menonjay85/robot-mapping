import numpy as np
import matplotlib.pyplot as plt
import math

scan = np.loadtxt('laserscan.dat')

angle = np.linspace(-math.pi/2, math.pi/2, len(scan), endpoint=True)
x_cood = scan * np.cos(angle)
y_cood = scan * np.sin(angle)

# Part A - Plots
plt.figure(figsize=(8, 6))
plt.scatter(x_cood, y_cood, c='blue', label='Laser End-Points')
plt.title('Laser Scan Points')
plt.xlabel('X-coordinates')
plt.ylabel('Y-coordinates')
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid(True)
plt.show()

# Part C
# Robots pose
x_robo, y_robo, theta_robo = 1.0, 0.5, math.pi/4

# Lasers pose relative to the robot
x_laser, y_laser, theta_laser = 0.2, 0.0, math.pi

# Transformation matrix for the robot
Rot_mat_robo = np.array([[np.cos(theta_robo), -np.sin(theta_robo)], [np.sin(theta_robo), np.cos(theta_robo)]])
T_robo = np.array([[Rot_mat_robo[0][0], Rot_mat_robo[0][1], x_robo],
                    [Rot_mat_robo[1][0], Rot_mat_robo[1][1], y_robo],
                    [0, 0, 1]])

# Transformation matrix for the laser in robot frame
R_laser = np.array([[np.cos(theta_laser), -np.sin(theta_laser)], [np.sin(theta_laser), np.cos(theta_laser)]])
T_laser = np.array([[R_laser[0][0], R_laser[0][1], x_laser],
                    [R_laser[1][0], R_laser[1][1], y_laser],
                    [0, 0, 1]])


T_total = np.dot(T_robo, T_laser)
global_coords = np.dot(T_total, np.vstack((x_cood, y_cood, np.ones(len(x_cood)))))

plt.figure(figsize=(8, 6))
plt.scatter(global_coords[0, :], global_coords[1, :], c='red', label='Global Laser Points')
plt.scatter(x_robo, y_robo, c='green', marker='o', label='Robot Center')
plt.scatter(T_total[0, 2], T_total[1, 2], c='orange', marker='^', label='Laser Center')
plt.title('Global Coordinates of Laser Scan Points')
plt.xlabel('X Coordinates')
plt.ylabel('Y Coordinates')
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid(True)
plt.show()
