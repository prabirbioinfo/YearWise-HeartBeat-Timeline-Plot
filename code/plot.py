# Save the plot as a PNG file
plt.figure(figsize=(14, 8))

# Create the gradient fill
for i in range(len(t) - 1):
    plt.fill_between(t[i:i+2], 0, heartbeat[i:i+2] * heartbeat_monthly[i:i+2], color=colors[i], alpha=0.8)

# Add plot enhancements
plt.plot(t, heartbeat * heartbeat_monthly, color='darkblue', linewidth=2, label='Yearly Timeline')
plt.title("Year2024", fontsize=16, color='navy', weight='bold')
plt.xlabel("Time", fontsize=12)
plt.ylabel("Intensity", fontsize=12)
plt.axhline(0, color="darkgray", linestyle="--", linewidth=0.8)
plt.legend(fontsize=12)
plt.grid(color='lightgray', linestyle='--', linewidth=0.5)
plt.gca().set_facecolor('#f5f5f5')  # Set background color

# Adjust y-axis limits to keep labels in frame
plt.ylim(-1, 1.2)

# Adding month labels to the plot
for i, label in enumerate(month_labels):
    pos = month_indices[i]
    label_y = heartbeat_monthly[np.searchsorted(t, pos)] + 0.1  # Adjust for better placement
    plt.text(pos, label_y, label, ha='center', fontsize=10, color='black')

# Save as PNG
plt.savefig("year_heartbeat_timeline_adjusted.png", dpi=300, bbox_inches='tight')
plt.show()

