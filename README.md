# Data-Identity
Student DataHack - Data Identity hackathon 2018 Hosted by Analytics Vidhya 

<h3>Tool:</h3>
<hr>
Python 3.5

<h3>Libraaries:</h3>
<hr>
numpy 1.12.1<br>
pandas 0.20.2<br>
catboost 0.8.1<br>

<h3>File-Folder structure:</h3>
<hr>

```
.
|-- code
|   |-- final_model.py 					# final code file to run
|-- data
|   |-- train.csv  						# Train dataset file
|   |-- test.csv   						# Test dataset file
|   |-- submissions
|       |-- sample_submission.csv 	# sample submission file
|-- docs
|   |-- document.docx               # document of what approach has been used to solve this problem.
|-- readme.md
```

<h3>How to run code file:</h3>
<hr>
1) run final_model.py python file which is in code directory.
   python final_model.py

This file will use 'train.csv' file for training a model and 'test.csv' file for prediction.<br>
After prediction 'sample_submission.csv' file will be used for submission file format.<br>
'cat_sub.csv' submission file will be created under data/submissions directory.<br>
