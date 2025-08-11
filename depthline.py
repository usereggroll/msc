import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data - in chronological order
periods = ['2017-2012', '2020-2017', '2025-2020']
zone1_data = [None, -0.71, -0.73]
zone2_data = [-0.21, -1.01, -0.65]
zone3_data = [0.21, 0.35, -0.91]

# Create x-axis positions for proper chronological ordering
x_positions = [0, 1, 2]

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot lines for each zone with smooth curves
# Create smooth curves using spline interpolation
x_smooth = np.linspace(0, 2, 100)

# Zone 1 - starts from second point since first is None
zone1_x = x_positions[1:]
zone1_y = zone1_data[1:]
if len(zone1_x) > 1:
    zone1_spline = make_interp_spline(zone1_x, zone1_y, k=1)  # k=1 for linear between 2 points
    zone1_smooth = zone1_spline(np.linspace(1, 2, 50))
    ax.plot(np.linspace(1, 2, 50), zone1_smooth, color='#3584bc', linewidth=2, label='Zone 1')
    ax.plot(zone1_x, zone1_y, 'o', color='#3584bc', markersize=8)

# Zone 2 - all points
zone2_spline = make_interp_spline(x_positions, zone2_data, k=2)  # k=2 for quadratic spline
zone2_smooth = zone2_spline(x_smooth)
ax.plot(x_smooth, zone2_smooth, color='#3faa40', linewidth=2, label='Zone 2')
ax.plot(x_positions, zone2_data, 'o', color='#3faa40', markersize=8)

# Zone 3 - all points
zone3_spline = make_interp_spline(x_positions, zone3_data, k=2)  # k=2 for quadratic spline
zone3_smooth = zone3_spline(x_smooth)
ax.plot(x_smooth, zone3_smooth, color='#ff983e', linewidth=2, label='Zone 3')
ax.plot(x_positions, zone3_data, 'o', color='#ff983e', markersize=8)

# Set x-axis labels
ax.set_xticks(x_positions)
ax.set_xticklabels(periods)

# Customize the plot
ax.set_xlabel('Time Period', fontsize=12)
ax.set_ylabel('Average Depth (m)', fontsize=12)
ax.set_title('Average Depth Changes Over Time', fontsize=14, fontweight='bold')

# Set y-axis limits to contain all curves
ax.set_ylim(-1.2, 0.5)
ax.set_yticks([-1.05, -0.7, -0.35, 0, 0.35])

# Add grid
ax.grid(True, alpha=0.3)

# Add legend
ax.legend(loc='center right', bbox_to_anchor=(1.0, 0.5))

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

# Optional: Save the plot
# plt.savefig('depth_changes_graph.png', dpi=300, bbox_inches='tight')