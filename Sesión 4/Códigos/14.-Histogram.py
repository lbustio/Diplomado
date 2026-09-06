# library & dataset
import seaborn as sns
df = sns.load_dataset('iris')

# Plot the histogram thanks to the histplot function
# (distplot fue eliminado de seaborn >= 0.14; histplot es su reemplazo)
sns.histplot(data=df, x="sepal_length", kde=False)