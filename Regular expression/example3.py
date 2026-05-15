import re
text="User IDs are user1,user2, and user3,user11"
#msg=re.findall(r"user\d{1,2}",text)
msg=re.findall(r"user\d+",text)
print(msg)