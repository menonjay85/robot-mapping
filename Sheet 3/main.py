import math

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

# Command 1
v_l, v_r, t = 0.3, 0.3, 3
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
print(f"After command 1: x = {x}, y = {y}, theta = {theta}")

# Command 2
v_l, v_r, t = 0.1, -0.1, 1
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
print(f"After command 2: x = {x}, y = {y}, theta = {theta}")

# Command 3
v_l, v_r, t = 0.2, 0, 2
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
print(f"After command 3: x = {x}, y = {y}, theta = {theta}")
