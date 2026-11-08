import pandas as pd

df = pd.read_excel("t1.xlsx")

esm = input(" enter a name:")

shakhs = df[df['Name'].str.lower() == esm.lower()]

if not shakhs.empty:
    name = shakhs.iloc[0]['Name']
    family = shakhs.iloc[0]['family']
    time = shakhs.iloc[0]['time']
    hoghoogh = shakhs.iloc[0]['hoghoogh']
    
    total_hoghoogh = time * hoghoogh
    
    print("=" * 30)
    print(f"name : {name} {family}")
    print(f"saat kari : {time} saat")
    print(f"hoghoogh : {hoghoogh} tooman") 
    print(f"hoghoogh mahane : {total_hoghoogh} tooman") 
    print("=" * 30)

else:
    print("the name not to list !")