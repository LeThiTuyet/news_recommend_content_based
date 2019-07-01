import json
import os
import pandas as pd
from processing_data import normalize_document
file_list = []
history = []
for (dirpath, dirname, filename) in os.walk('data/train_json/'):
    for f in filename:
        file_list.append(dirpath+'/'+f)
for f in file_list:
    with open(f,encoding='utf8', errors='ignore') as json_file:
        json_data = json.load(json_file)
        history_item= {"uid":json_data["uuid"],"tacgia":json_data["author"],"tieude":json_data["title"],"noidung":normalize_document(json_data["text"])}
    history.append(history_item)
df = pd.DataFrame(history)
history_csv = df.to_csv(r'C:\Users\Le Thi Tuyet\PycharmProjects\NLP\bag-of-word\data\train\history_reading.csv', index=None, header=True)