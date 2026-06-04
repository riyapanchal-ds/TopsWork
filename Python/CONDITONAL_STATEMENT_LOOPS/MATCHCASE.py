'''marks=int(input("enter marks:--"))
match marks:
    case m if 70 <= m <=100:
        print("A")
    case m if 60 <= m <= 69:
        print("B")
    case m if 40 <= m <=59:
     print("C")
    case m if 30 <= m <=39:
      print("PASS")
    case _:
        print("FAIL")'''

month=input("enter month:--")
match month:
    case "february":
        print("28/29 days")
    case "april" | "june" | "september" | "november":
        print("30 days")
    case "january" | "march" | "may" | "july" | "august" | "october" | "december":
        print("31 days")
    case _:print("invalid month")