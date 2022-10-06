import pandas as pd
from sklearn import model_selection
import os

from pathlib import Path

cwd = Path.cwd()
parent = cwd.parent

DATA_PATH = os.path.join(parent,'input','train.csv')
DIR_PATH = os.path.join(parent,'input','train_folds.csv')

if __name__ == '__main__':
    df = pd.read_csv(DATA_PATH)
    df["kfold"] = -1

    df  = df.sample(frac=1).reset_index(drop=True)
    
    kf = model_selection.StratifiedKFold(n_splits=5, shuffle=False)

    for fold, (train_idx, val_idx) in enumerate(kf.split(X=df, y=df.target.values)):
        print(len(train_idx), len(val_idx))
        df.loc[val_idx, 'kfold'] = fold

    df.to_csv(DIR_PATH, index=False)