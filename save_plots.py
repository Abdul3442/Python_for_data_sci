import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("Day_03/figures", exist_ok=True)
df = pd.read_csv("Day_03/TB_Burden_Country.csv")

# Plot 1: Pakistan Trend
pk_df = df[df["Country or territory name"] == "Pakistan"].sort_values("Year")
fig, ax1 = plt.subplots(figsize=(10, 5))
ax1.plot(pk_df['Year'], pk_df['Estimated prevalence of TB (all forms) per 100 000 population'], color='#1f77b4', marker='o', linewidth=2, label='TB Prevalence per 100k')
ax1.set_xlabel('Year', fontweight='bold')
ax1.set_ylabel('TB Prevalence per 100k', color='#1f77b4', fontweight='bold')
ax2 = ax1.twinx()
ax2.plot(pk_df['Year'], pk_df['Estimated total population number'] / 1e6, color='#ff7f0e', marker='s', linestyle='--', linewidth=2, label='Population (M)')
ax2.set_ylabel('Population (Millions)', color='#ff7f0e', fontweight='bold')
plt.title('Pakistan: TB Prevalence Decline vs. Population Growth (1990-2013)', fontweight='bold')
plt.tight_layout()
plt.savefig("Day_03/figures/pakistan_tb_trend.png", dpi=200)
plt.close()

# Plot 2: Regional Comparison
plt.figure(figsize=(10, 5))
sns.barplot(data=df, x="Region", y="Estimated prevalence of TB (all forms) per 100 000 population", palette="Blues_d")
plt.title("Average Estimated TB Prevalence per 100k by WHO Region", fontweight='bold')
plt.tight_layout()
plt.savefig("Day_03/figures/regional_tb_comparison.png", dpi=200)
plt.close()

# Plot 3: Distribution
plt.figure(figsize=(10, 5))
sns.histplot(df['Estimated prevalence of TB (all forms) per 100 000 population'], kde=True, color='teal', bins=35)
plt.title("Global TB Prevalence Distribution per 100,000 Population", fontweight='bold')
plt.xlim(0, 1500)
plt.tight_layout()
plt.savefig("Day_03/figures/tb_prevalence_distribution.png", dpi=200)
plt.close()

# Plot 4: Heatmap
plt.figure(figsize=(8, 6))
cols = ['Estimated total population number', 'Estimated prevalence of TB (all forms) per 100 000 population', 'Estimated mortality of TB cases (all forms, excluding HIV) per 100 000 population', 'Case detection rate (all forms), percent']
sns.heatmap(df[cols].corr(), annot=True, cmap="mako", fmt=".2f")
plt.title("Correlation Heatmap of Key Epidemiological Indicators", fontweight='bold')
plt.tight_layout()
plt.savefig("Day_03/figures/tb_metrics_correlation.png", dpi=200)
plt.close()

print("SUCCESS: 4 plots generated in Day_03/figures/")
