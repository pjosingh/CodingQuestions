dicts_lists = [
  {
    "Name": "James",
    "Age": 20,
  },
  {
     "Name": "May",
     "Age": 14,
  },
  {
    "Name": "Katy",
    "Age": 23,
  }
]

#There are different ways to sort that list
#1- Using the sort/ sorted function based on the age
dicts_lists.sort(key=lambda item: item.get("Age"))

print(dicts_lists)