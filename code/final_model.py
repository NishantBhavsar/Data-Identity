import numpy as np
import pandas as pd
import catboost as cb


train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')

all_data = train_df.append(test_df, ignore_index=True)

# fill NaN values of 'trainee_engagement_rating' column based on trainee_id and program_id
for ue in all_data[all_data['trainee_engagement_rating'].isnull()]['trainee_id'].unique():
    te = all_data[all_data['trainee_id'] == ue]
    p_u = te['program_id'].unique()
    for p in p_u:
        pe = te[te['program_id'] == p]
        val = pe['trainee_engagement_rating'].dropna()
        if val.empty:
            val = te['trainee_engagement_rating'].dropna()
            if val.empty:
                val = int(all_data['trainee_engagement_rating'].mean())
            else:
                val = int(val.mean())
        else:
            val = int(val.mean())
        all_data.loc[pe.index, ['trainee_engagement_rating']] = val


# fill NaN values for 'age' column based on trainee_id
for ue in all_data[all_data['age'].isnull()]['trainee_id'].unique():
    te = all_data[all_data['trainee_id'] == ue]
    val = te['age'].dropna()
    if val.empty:
        val = int(all_data['age'].mean())
    else:
        val = int(val.mean())
    all_data.loc[te.index, ['age']] = val


train_df = all_data[0:train_df.shape[0]]
test_df = all_data[train_df.shape[0]:]
test_df.drop(['is_pass'], inplace=True, axis=1)

# features for catboost model and categorical features indices
features = [i for i in train_df.columns if i not in ['id', 'is_pass']]
categorical_features_indices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13]

# Cagtboost model
clf = cb.CatBoostClassifier(eval_metric="AUC", random_seed=877915463397741)

clf.fit(train_df[features], train_df['is_pass'], cat_features= categorical_features_indices)
preds = clf.predict_proba(test_df[features])[:, 1]

sub = pd.read_csv('sample_submission.csv')
sub['is_pass'] = preds
sub.to_csv('cat_sub.csv', index=False)
