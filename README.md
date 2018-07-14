# Data-Identity
Student DataHack - Data Identity hackathon 2018 Hosted by Analytics Vidhya 
https://datahack.analyticsvidhya.com/contest/the-data-identity-2/
<br>5th rank solution.
## Tool:
- Python 3.5

## Libraries:
- numpy 1.12.1
- pandas 0.20.2
- catboost 0.8.1

## File-Folder structure:
```
.
|-- code
|   |-- final_model.py                 # final code file to run
|-- data
|   |-- train.csv                      # Train dataset file
|   |-- test.csv                       # Test dataset file
|   |-- submissions
|       |-- sample_submission.csv      # sample submission file
|-- docs
|   |-- document.docx                  # document of what approach has been used to solve this problem.
|-- readme.md
```

### How to run code file:
1. run final_model.py python file which is in code directory.<br>
   <code>python final_model.py</code>

- This file will use <code>train.csv</code> file for training a model and <code>test.csv</code> file for prediction.
- After prediction <code>sample_submission.csv</code> file will be used for submission file format.
- <code>cat_sub.csv</code> submission file will be created under <code>data/submissions</code> directory.
