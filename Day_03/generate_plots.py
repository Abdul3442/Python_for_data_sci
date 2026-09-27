import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set stylish dark grid style
sns.set_theme(style="darkgrid")
plt.rcParams.update({'font.sans-serif': 'DejaVu Sans', 'font.size': 11})

# Output directory for figures
fig_dir = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(fig_dir, exist_ok=True)

# Load dataset
csv_path = os.path.join(os.path.dirname(__file__), "TB_Burden_Country.csv")
df = pd.read_csv(csv_path)

# ---------------------------------------------------------
# Figure 1: Pakistan TB Burden & Population Trend (1990 - 2013)
# ---------------------------------------------------------
pk_df = df[df["Country or territory name"] == "Pakistan"].sort_values("Year")

fig, ax1 = plt.subplots(figsize=(10, 6))

color = '#1f77b4'
ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('TB Prevalence (per 100k)', color=color, fontsize=12, fontweight='bold')
line1 = ax1.plot(pk_df['Year'], pk_df['Estimated prevalence of TB (all forms) per 100 000 population'], 
                 color=color, marker='o', linewidth=2.5, label='TB Prevalence per 100k')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  
color = '#ff7f0e'
ax2.set_ylabel('Population (Millions)', color=color, fontsize=12, fontweight='bold')
line2 = ax2.plot(pk_df['Year'], pk_df['Estimated total population number'] / 1e6, 
                 color=color, marker='s', linestyle='--', linewidth=2.5, label='Total Population (M)')
ax2.tick_params(axis='y', labelcolor=color)

# Title & Legend
plt.title('Pakistan: TB Prevalence Decline vs. Population Growth (1990–2013)', fontsize=14, fontweight='bold', pad=15)
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='center right', frameon=True, facecolor='white', edgecolor='none')

fig.tight_layout()
fig1_path = os.path.join(fig_dir, "pakistan_tb_trend.png")
plt.savefig(fig1_path, dpi=300)
plt.close()
print(f"Saved: {fig1_path}")

# ---------------------------------------------------------
# Figure 2: Regional TB Prevalence Comparison
# ---------------------------------------------------------
plt.figure(figsize=(10, 6))
region_order = df.groupby("Region")["Estimated prevalence of TB (all forms) per 100 000 population"].median().sort_values(ascending=False).index

palette = sns.color_palette("viridis", len(region_order))
ax = sns.barplot(
    data=df, 
    x="Region", 
    y="Estimated prevalence of TB (all forms) per 100 000 population", 
    order=region_order,
    palette=palette,
    capsize=0.1,
    err_kws={'linewidth': 1.5}
)

plt.title('Average TB Prevalence per 100,000 Population by WHO Region', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('WHO Region Code', fontsize=12, fontweight='bold')
plt.ylabel('Mean TB Prevalence per 100k', fontsize=12, fontweight='bold')

# Annotate bars with mean values
for p in ax.patches:
    height = p.get_height()
    if not pd.isna(height) and height > 0:
        ax.annotate(f'{height:.1f}',
                    (p.get_x() + p.get_width() / 2., height / 2),
                    ha='center', va='center', fontsize=10, color='white', fontweight='bold')

plt.tight_layout()
fig2_path = os.path.join(fig_dir, "regional_tb_comparison.png")
plt.savefig(fig2_path, dpi=300)
plt.close()
print(f"Saved: {fig2_path}")

# ---------------------------------------------------------
# Figure 3: Global TB Prevalence Distribution (Univariate Analysis)
# ---------------------------------------------------------
plt.figure(figsize=(10, 6))
sns.histplot(df['Estimated prevalence of TB (all forms) per 100 000 population'], kde=True, color='#2ca02c', bins=40)

plt.title('Global Distribution of TB Prevalence per 100,000 Population', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Estimated TB Prevalence per 100k Population', fontsize=12, fontweight='bold')
plt.ylabel('Frequency (Country-Years)', fontsize=12, fontweight='bold')
plt.xlim(0, 1500)

plt.tight_layout()
fig3_path = os.path.join(fig_dir, "tb_prevalence_distribution.png")
plt.savefig(fig3_path, dpi=300)
plt.close()
print(f"Saved: {fig3_path}")

# ---------------------------------------------------------
# Figure 4: Correlation Matrix Heatmap
# ---------------------------------------------------------
plt.figure(figsize=(9, 7))
corr_cols = [
    'Estimated total population number',
    'Estimated prevalence of TB (all forms) per 100 000 population',
    'Estimated mortality of TB cases (all forms, excluding HIV) per 100 000 population',
    'Estimated mortality of TB cases who are HIV-positive, per 100 000 population',
    'Case detection rate (all forms), percent'
]

short_names = ['Population', 'TB Prevalence/100k', 'TB Mortality/100k', 'HIV-TB Mortality/100k', 'Case Detection Rate %']
corr_df = df[corr_cols].corr()
corr_df.columns = short_names
corr_df.index = short_names

sns.heatmap(corr_df, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.8, cbar_kws={'label': 'Pearson Correlation'})
plt.title('Correlation Matrix of Key Epidemiological Indicators', fontsize=14, fontweight='bold', pad=15)
plt.xticks(rotation=30, ha='right')
plt.yticks(rotation=0)

plt.tight_layout()
fig4_path = os.path.join(fig_dir, "tb_metrics_correlation.png")
plt.savefig(fig4_path, dpi=300)
plt.close()
print(f"Saved: {fig4_path}")

print("All plots successfully generated and saved to Day_03/figures/")
