car_data = {

    "EV": {
        "Maruti": {"Baleno": [1200000, "xls"],"sCross": [2200000, "123"]
        },

        "Hundai": {"i10": [1000000, "megha"],"creta": [1900000, "iv12"]     
        },  
        
        "KIA":{"seltos": [1300000, ""],"sonate": [4400000,""]
        
        }                                
          }, 

     "Petrol" : {
         "Hundai" : {"i10" : [670000, "qqq"]}

     }                                          
           }
while True:
#print(car_data)
#print(car_data["EV"]["Maruti"]["sCross"])
    print("1. search by company")
    print("2. search by model")
    print("3. display all cars")
    print("4. exit")
    ch=int(input("enter choice"))
    match ch:
       case 1:

         company_name=input("Enter name of company")
         for i in car_data.keys():
           for j in car_data[i].keys():
             if j==company_name:
                print(i,"--->",car_data[i][j])
       case 2:
          model_name=input("enter model name")
          for k,v in car_data.items():
             for v1 in v.items:
              print(k,v)



         
