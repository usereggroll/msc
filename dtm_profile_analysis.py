import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('profile.csv')

layers = {
    'DTM 2012': ('phase2#1_x', 'phase2#1_y'),  # distance, elevation
    'DTM 2017': ('dtm17#1_x', 'dtm17#1_y'),
    'DTM 2020': ('dtm20#1_x', 'dtm20#1_y'),
    'DTM 2025': ('focaled17#1_x', 'focaled17#1_y'),
}

colors = {
    'DTM 2012': '#f4a261',   # gray
    'DTM 2017': '#1f77b4',   # blue
    'DTM 2020': '#2ca02c',   # green
    'DTM 2025': '#d62728',   # red
}

plt.figure(figsize=(12, 6))
all_elevations = []

print("Valid points and distance range per layer:")

for label, (dist_col, elev_col) in layers.items():
    if dist_col in df.columns and elev_col in df.columns:
        distance = pd.to_numeric(df[dist_col], errors='coerce')
        elevation = pd.to_numeric(df[elev_col], errors='coerce')

        valid = (~distance.isna()) & (~elevation.isna())
        valid_distance = distance[valid]
        valid_elevation = elevation[valid]

        if valid.sum() > 0:
            print(f"{label}: {valid.sum()} valid points, distance range: {valid_distance.min()} to {valid_distance.max()}")
            plt.plot(valid_distance, valid_elevation, label=label, color=colors[label])
            all_elevations.append(valid_elevation)
        else:
            print(f"{label}: No valid points")

# Zone lines at distance 259 and 411
for xpos in [259, 411]:
    plt.axvline(x=xpos, color='black', linestyle='dotted', linewidth=1)

if all_elevations:
    combined_elev = pd.concat(all_elevations)
    y_min = combined_elev.min()
    y_max = combined_elev.max()
    plt.ylim(y_min - 0.1, y_max + 0.1)

    plt.text(150, y_max, 'Zone 1', ha='center', fontsize=10, color='gray')
    plt.text(335, y_max, 'Zone 2', ha='center', fontsize=10, color='gray')
    plt.text(450, y_max, 'Zone 3', ha='center', fontsize=10, color='gray')

plt.xlabel('Distance (m)')
plt.ylabel('Elevation (m)')
plt.title('Longitudinal Profile (2012–2025)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
