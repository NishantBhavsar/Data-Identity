# Data-Identity
Student DataHack - Data Identity hackathon 2018 Hosted by Analytics Vidhya 

Tool:
==================================
Python 3.5

Libraaries:
==================================
numpy 1.12.1
pandas 0.20.2
catboost 0.8.1

File-Folder structure:
------------------------
```
.
+-- code
|   +-- final_model.py 					    # final code file to run
+-- data
|   +-- train.csv  						      # Train dataset file
|   +-- test.csv   						      # Test dataset file
|   +-- submissions
|       +-- sample_submission.csv 	# sample submission file
+-- docs
|   +-- document.docx               # document of what approach has been used to solve this problem.
+-- readme.md
```

How to run code file:
==================================
1) run final_model.py python file which is in code directory.
   python final_model.py

This file will use 'train.csv' file for training a model and 'test.csv' file for prediction.
After prediction 'sample_submission.csv' file will be used for submission file format.
'cat_sub.csv' submission file will be created under data/submissions directory.
