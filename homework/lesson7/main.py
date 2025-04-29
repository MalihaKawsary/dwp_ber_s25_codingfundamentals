items=[]
while True:
    x=input(" Enter an item or (done to finish): ").strip()
    if x=="":
        print("Empty Input: Just press enter")
        continue
    if x.casefold() =="done":
       break
    
        
    items.append(x)
items=list(dict.fromkeys(items))
items.sort()
print("\nyour list")
for i, x in enumerate(items, 1):
    print(f"{i}.{x}")
print(f"Total number of items:{len(items)}")
