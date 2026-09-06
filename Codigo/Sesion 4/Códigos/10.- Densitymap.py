!pip install seaborn

# library & dataset
import seaborn as sns
df = sns.load_dataset('iris')

# Make default density plot
sns.kdeplot(df['sepal_width'])