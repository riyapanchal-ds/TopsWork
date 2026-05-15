import re
msg="contact number is 9898989898 and pincode number is 324532"
#ans=re.findall(r"\d+",msg)                              #r means row string
ans=re.findall(r"\d{6,10}",msg)
print(ans)

import re
msg="This is python class"
ans=re.findall(r"\b\w{4}\b",msg)
print(ans)