#Task 1: The Personal Contact Book (Dictionaries)
contact = {"Abia":9008610063,"Sneha":7619190063,"Jaweriya":9731082310}
contact["Keerti"]=9281673367
contact["Sneha"]=8270056715
print(contact.get("Abia"))
print(contact.get("Megha","Contact not found"))
for name,number in contact.items():
    print(f"Contact: {name} | Phone: {number}.")

#Task 2: The "Duplicate Cleaner" (Sets)
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_logs = set(raw_logs)
print(unique_logs)
print("ID05" in unique_logs)
print(f"Length of logs as list: {len(raw_logs)}, Length of logs as set: {len(unique_logs)}")


#Task 3: The Interest Matcher (Set Operations)
friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
print("Common interests: ",(friend_a & friend_b))
print("All interests: ",(friend_a | friend_b))
print("Unique interests of a: ",(friend_a - friend_b))
