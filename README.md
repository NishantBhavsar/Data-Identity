# Data-Identity
Student DataHack - Data Identity hackathon 2018 Hosted by Analytics Vidhya 

### Tool:
- Python 3.5

### Libraaries:
- numpy 1.12.1<br>
- pandas 0.20.2<br>
- catboost 0.8.1<br>

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

### How to run code file:
1. run final_model.py python file which is in code directory.<br>
   <code>python final_model.py</code>

- This file will use <code>train.csv</code> file for training a model and <code>test.csv</code> file for prediction.<br>
- After prediction <code>sample_submission.csv</code> file will be used for submission file format.<br>
- <code>cat_sub.csv</code> submission file will be created under <code>data/submissions</code> directory.<br>
