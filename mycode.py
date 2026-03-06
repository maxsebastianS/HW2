import pandas as pd
import os

data = {
    "name": ["alice", "bob", "alice"],
    "age": [25, 30, 25],
    "city": ["new york", "los angeles", "new york"]
}

df = pd.DataFrame(data)

# add new row
#new_row = {"name": "charlie", "age": 35, "city": "chicago"}
#df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

#new_row2 = {"name": "dave", "age": 40, "city": "san francisco"}
#df = pd.concat([df, pd.DataFrame([new_row2])], ignore_index=True)

data_dir_path = "data"
os.makedirs(data_dir_path, exist_ok=True)
file_path = os.path.join(data_dir_path, "people.csv")
df.to_csv(file_path, index=False)
print(f"DataFrame saved to {file_path}")