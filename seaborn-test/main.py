
import seaborn as sns

data = sns.get_dataset_names()
print(data)
dataset = sns.load_dataset('fmri')

print(dataset)
