import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os 


_file_list = os.listdir()# ['mc.csv', 'mb.csv', 'mf.csv']
file_list = []
for f in _file_list:
    if '.csv' in f:
        file_list.append(f)

print(file_list)

log = {'reward':[], 'epoch':[]}

min_len = 987654321
rel_val = []
for idx, f in enumerate(file_list):
    print('{}/{} processing...'.format(idx+1, len(file_list)))
    df = pd.read_csv(f)
    df_len = df.shape[0]
    if df_len != 1000:
        print(df_len)
        continue

    cum_rwd = 0

    for i in range(df_len):
        cum_rwd += df.iloc[i, 2]

        log['reward'].append(cum_rwd)
        log['epoch'].append(i)


    # mean & var - reliability
    # rel_val.append(round(df['Value'].iloc[:min_len].mean() / df['Value'].iloc[:min_len].var(), 3))

print('Creating Graph...')
_log = pd.DataFrame(log)
plt.clf()

sns.lineplot(data = _log, x = 'epoch', y = 'reward')

# title = 'Reliability - MC : ', rel_val[0], ' MB : ', rel_val[1], ' MF : ', rel_val[2]
plt.savefig('line.png')
plt.show()

    



