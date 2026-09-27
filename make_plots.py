import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

fig_dir = os.path.join("Day_03", "figures")
os.makedirs(fig_dir, exist_ok=True)

df = pd.read_csv("Day_03/TB_Burden_Country.csv")

# 1. Pakistan TB Trend
pk_df = df[df["Country or territory name"] == "Pakistan"].sort_values("Year")
fig, ax1 = plt.subplots(figsize=(10, 5))
ax1.plot(pk_df['Year'], pk_df['Estimated prevalence of TB (all forms) per 100 000 population'], color='#1f77b4', marker='o', linewidth=2.5, label='TB Prevalence/100k')
ax1.set_xlabel('Year', fontweight='bold')
ax1.set_ylabel('TB Prevalence per 100k', color='#1f77b4', fontweight='bold')
ax2 = ax1.twinx()
ax2.plot(pk_df['Year'], pk_df['Estimated total population number'] / 1e6, color='#ff7f0e', marker='s', linestyle='--', linewidth=2.5, label='Population (M)')
ax2.set_ylabel('Population (Millions)', color='#ff7f0e', fontweight='bold')
plt.title('Pakistan: TB Prevalence Decline vs. Population Growth (1990-2013)', fontweight='bold')
plt.tight_layout()
p1 = os.path.join(fig_dir, "pakistan_tb_trend.png")
plt.savefig(p1, dpi=200)
plt.close()
print("Saved 1: " + p1)

# 2. Regional Comparison
plt.figure(figsize=(10, 5))
sns.barplot(data=df, x="Region", y="Estimated prevalence of TB (all forms) per 100 000 population", palette="Blues_d")
plt.title("Average Estimated TB Prevalence per 100k by WHO Region", fontweight='bold')
plt.tight_layout()
p2 = os.path.join(fig_dir, "regional_tb_comparison.png")
plt.savefig(p2, dpi=200)
plt.close()
print("Saved 2: " + p2)

# 3. Distribution Plot
plt.figure(figsize=(10, 5))
sns.histplot(df['Estimated prevalence of TB (all forms) per 100 000 population'], kde=True, color='teal', bins=35)
plt.title("Global TB Prevalence Distribution per 100,000 Population", fontweight='bold')
plt.xlim(0, 1500)
plt.tight_layout()
p3 = os.path.join(fig_dir, "tb_prevalence_distribution.png")
plt.savefig(p3, dpi=200)
plt.close()
print("Saved 3: " + p3)

# 4. Correlation Heatmap
plt.figure(figsize=(8, 6))
cols = ['Estimated total population number', 'Estimated prevalence of TB (all forms) per 100 000 population', 'Estimated mortality of TB cases (all forms, excluding HIV) per 100 000 population', 'Case detection rate (all forms), percent']
sns.heatmap(df[cols].corr(), annot=True, cmap="mako", fmt=".2f")
plt.title("Correlation Heatmap of Key Epidemiological Indicators", fontweight='bold')
plt.tight_layout()
p4 = os.path.join(fig_dir, "tb_metrics_correlation.png")
plt.savefig(p4, dpi=200)
plt.close()
print("Saved 4: " + p4)

print("COMPLETE_PLOT_GENERATION_SUCCESS")
