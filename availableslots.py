import requests
import datetime
from tkinter import *
import tkinter as tk
root = Tk()
root.geometry("350x350")
root.title("Get available slot list in your district")


# for state_code in range(1,40):
#     response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_code))

def showdata():
    DIST_ID = data.get() #Bhopal
    numdays = 1


    base = datetime.datetime.today()
    date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
    date_str = [x.strftime("%d-%m-%Y") for x in date_list]
    print(date_str)

    for INP_DATE in date_str:

        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(DIST_ID, INP_DATE)
        response = requests.get(URL)
        if response.ok:
            resp_json = response.json()
            if resp_json["centers"]:
                print("You can book vaccine slots on {}".format(INP_DATE))
                l=[]
                for i in range(len(resp_json["centers"])):
                    temp_str=""
                
                    temp_str=temp_str+"Center Name : "+str(resp_json["centers"][i]["name"])+"\n"
                    temp_str=temp_str+"Address : "+str(resp_json["centers"][i]["address"])
                    temp_str=temp_str+"fees type : "+str(resp_json["centers"][i]["fee_type"])+"\n"
                    for j in range(len(resp_json["centers"][i]["sessions"])):
                        temp_str=temp_str+"minimum age limit : "+str(resp_json["centers"][i]["sessions"][j]["min_age_limit"])+"\n"
                        temp_str=temp_str+"date : "+str(resp_json["centers"][i]["sessions"][j]["date"])+"\n"
                        temp_str=temp_str+"available capacity : "+str(resp_json["centers"][i]["sessions"][j]["available_capacity"])+"\n"
                        temp_str=temp_str+"vaccine type : "+str(resp_json["centers"][i]["sessions"][j]["vaccine"])+"\n"
                        temp_str=temp_str+"slots : "+str(resp_json["centers"][i]["sessions"][j]["slots"])+"\n"
                        temp_str=temp_str+"Dose1 : "+str(resp_json["centers"][i]["sessions"][j]["available_capacity_dose1"])+"\n"
                        temp_str=temp_str+"Dose2 : "+str(resp_json["centers"][i]["sessions"][j]["available_capacity_dose2"])+"\n"
                    
                    l.append(temp_str)
                # for i in l:
                #   print(i)     
                out = "\n".join(l)
                
                # t=Text(root,height=100,width=100)
                # result = Label(root,textvariable="result")
                # result.pack() 
                # t.insert(tk.END,out)
                newwindow=Toplevel(root)
                newwindow.geometry("1000x1000")
                t=Text(newwindow,height=1000,width=1000)
                
                t.insert(tk.END,out)
                t.pack()
                newwindow.mainloop()
                
Label(root, text="Enter district code\n", font = "Console 15 bold").pack()

data = StringVar()
data.set("")
entry = Entry(root,textvariable=data,width=500).pack()
Button(root, text="Get Data", command = showdata).pack()
root.mainloop()
     



