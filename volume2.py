import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data preparation
data = {
    'Period': ['2017-2012', '2020-2017', '2025-2020'],
    'Zone 1 Erosion': [np.nan, -2410.73, -2061.48],
    'Zone 1 Accretion': [np.nan, 412.69, 0],
    'Zone 2 Erosion': [-588.44, -2275.09, -1304.55],
    'Zone 2 Accretion': [172.65, 258.63, 0],
    'Zone 3 Erosion': [-180.02, -705.66, -1885.17],
    'Zone 3 Accretion': [600.56, 1429.68, 0]
}

net_data = {
    'Period': ['2017-2012', '2020-2017', '2025-2020'],
    'Zone 1': [np.nan, -1998.04, -2061.48],
    'Zone 2': [-415.79, -2016.46, -1304.55],
    'Zone 3': [420.54, 724.02, -1885.17]
}

df = pd.DataFrame(data)
net_df = pd.DataFrame(net_data)

# Color schemes
erosion_colors = ['#1e40af', '#0891b2', '#0d9488']
accretion_colors = ['#dc2626','#ea580c', '#f59e0b']
net_colors = ['#1f77b4', '#2ca02c', '#ff7f0e']

def plot_erosion_accretion():
    fig, ax = plt.subplots(figsize=(14, 8))
    
    x = np.arange(len(df['Period']))
    width = 0.12
    spacing = 0.18  # Larger than width to create gap
    
    # Erosion bars
    ax.bar(x - 2.5*spacing, df['Zone 1 Erosion'], width, label='Zone 1 Erosion', color=erosion_colors[0])
    ax.bar(x - 1.5*spacing, df['Zone 2 Erosion'], width, label='Zone 2 Erosion', color=erosion_colors[1])
    ax.bar(x - 0.5*spacing, df['Zone 3 Erosion'], width, label='Zone 3 Erosion', color=erosion_colors[2])
    
    # Accretion bars
    ax.bar(x + 0.5*spacing, df['Zone 1 Accretion'], width, label='Zone 1 Accretion', color=accretion_colors[0])
    ax.bar(x + 1.5*spacing, df['Zone 2 Accretion'], width, label='Zone 2 Accretion', color=accretion_colors[1])
    ax.bar(x + 2.5*spacing, df['Zone 3 Accretion'], width, label='Zone 3 Accretion', color=accretion_colors[2])
    
    ax.set_xlabel('Period', fontsize=12, fontweight='bold')
    ax.set_ylabel('Volume Change (m³)', fontsize=12, fontweight='bold')
    ax.set_title('Erosion and Accretion by Period', fontsize=16, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(df['Period'])
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='black', linewidth=0.8)
    
    plt.tight_layout()
    plt.show()

def plot_net_change():
    fig, ax = plt.subplots(figsize=(12, 8))
    
    x = np.arange(len(net_df['Period']))
    width = 0.18
    spacing = 0.26

    for i, zone in enumerate(['Zone 1', 'Zone 2', 'Zone 3']):
        values = net_df[zone]
        color = net_colors[i]
        ax.bar(x + (i - 1) * spacing, values, width, label=zone, color=color, alpha=0.9)
    
    ax.set_xlabel('Period', fontsize=12, fontweight='bold')
    ax.set_ylabel('Net Volume Change (m³)', fontsize=12, fontweight='bold')
    ax.set_title('Net Volume Change by Period', fontsize=16, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(net_df['Period'])
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='black', linewidth=0.8)
    
    plt.tight_layout()
    plt.show()

def plot_both():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12))
    
    # Erosion/Accretion bars
    x = np.arange(len(df['Period']))
    width = 0.12
    spacing = 0.18

    ax1.bar(x - 2.5*spacing, df['Zone 1 Erosion'], width, label='Zone 1 Erosion', color=erosion_colors[0])
    ax1.bar(x - 1.5*spacing, df['Zone 2 Erosion'], width, label='Zone 2 Erosion', color=erosion_colors[1])
    ax1.bar(x - 0.5*spacing, df['Zone 3 Erosion'], width, label='Zone 3 Erosion', color=erosion_colors[2])

    ax1.bar(x + 0.5*spacing, df['Zone 1 Accretion'], width, label='Zone 1 Accretion', color=accretion_colors[0])
    ax1.bar(x + 1.5*spacing, df['Zone 2 Accretion'], width, label='Zone 2 Accretion', color=accretion_colors[1])
    ax1.bar(x + 2.5*spacing, df['Zone 3 Accretion'], width, label='Zone 3 Accretion', color=accretion_colors[2])
    
    ax1.set_xlabel('Period', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Volume Change (m³)', fontsize=12, fontweight='bold')
    ax1.set_title('Erosion and Accretion by Period', fontsize=14, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(df['Period'])
    ax1.legend(loc='upper left')  # Legend now inside the plot
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=0, color='black', linewidth=0.8)
    
    # Net Change bars
    x2 = np.arange(len(net_df['Period']))
    width2 = 0.15
    spacing2 = 0.26

    for i, zone in enumerate(['Zone 1', 'Zone 2', 'Zone 3']):
        values = net_df[zone]
        color = net_colors[i]
        ax2.bar(x2 + (i - 1) * spacing2, values, width2, label=zone, color=color, alpha=0.9)

    ax2.set_xlabel('Period', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Net Volume Change (m³)', fontsize=12, fontweight='bold')
    ax2.set_title('Net Volume Change by Period', fontsize=14, fontweight='bold')
    ax2.set_xticks(x2)
    ax2.set_xticklabels(net_df['Period'])
    ax2.legend(loc='upper left')
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=0, color='black', linewidth=0.8)

    plt.tight_layout()
    plt.show()


# Example usage
if __name__ == "__main__":
    # plot_erosion_accretion()
    # plot_net_change()
    plot_both()

    print("Erosion/Accretion Data:")
    print(df.to_string(index=False))
    print("\nNet Change Data:")
    print(net_df.to_string(index=False))
