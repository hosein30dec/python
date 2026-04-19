correct_password="admin"
Tedad_ramz=0
while Tedad_ramz<3 :
    ramz=input("Ramz vorod khoda ra vared konid :")
    if ramz==correct_password :
        print("Ramz Sahih ast khosh omadid")
        break
    else :
        Tedad_ramz=Tedad_ramz+1
        forsat_ramz=3-Tedad_ramz
        print(f"forsat vared kardan ramz shoma {forsat_ramz} ast pas ba deqat vared konid")
    if Tedad_ramz==3 :
        print("hesab shoma masdod shod.")