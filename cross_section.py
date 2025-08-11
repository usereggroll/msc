import pandas as pd
import matplotlib.pyplot as plt
import glob

# Define the layers with new column names
layers = {
    'DTM 2012': ('2012#1_x', '2012#1_y'),  # distance, elevation
    'DTM 2017': ('2017#1_x', '2017#1_y'),
    'DTM 2020': ('2020#1_x', '2020#1_y'),
    'DTM 2025': ('2025#1_x', '2025#1_y'),
}

colors = {
    'DTM 2012': '#f4a261',   # orange
    'DTM 2017': '#cf295b',   # red     
    'DTM 2020': '#2ca02c',   # green
    'DTM 2025': '#1f77b4',   # blue
}

# Read all CSV files (assuming they have similar structure)
csv_files = glob.glob('cross_3.csv')  # You can specify exact filenames if needed
# Alternative: csv_files = ['file1.csv', 'file2.csv', 'file3.csv']

plt.figure(figsize=(12, 6))
all_elevations = []

print("Valid points and distance range per layer:")

for csv_file in csv_files:
    print(f"\nProcessing file: {csv_file}")
    df = pd.read_csv(csv_file)
    
    for label, (dist_col, elev_col) in layers.items():
        if dist_col in df.columns and elev_col in df.columns:
            distance = pd.to_numeric(df[dist_col], errors='coerce')
            elevation = pd.to_numeric(df[elev_col], errors='coerce')
            
            # Since you mentioned no empty values, we can still check for any potential issues
            valid = (~distance.isna()) & (~elevation.isna())
            valid_distance = distance[valid]
            valid_elevation = elevation[valid]
            
            if valid.sum() > 0:
                print(f"{label}: {valid.sum()} valid points, distance range: {valid_distance.min():.2f} to {valid_distance.max():.2f}")
                plt.plot(valid_distance, valid_elevation, label=f"{label}", 
                        color=colors[label], alpha=0.8)
                all_elevations.append(valid_elevation)
            else:
                print(f"{label}: No valid points")


if all_elevations:
    combined_elev = pd.concat(all_elevations)
    y_min = combined_elev.min()
    y_max = combined_elev.max()
    y_range = y_max - y_min
    plt.ylim(y_min - 0.1 * y_range, y_max + 0.1 * y_range)

plt.xlabel('Distance (m)')
plt.ylabel('Elevation (m)')
plt.title('Zone 3 Cross Section Profile (2012–2025)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()