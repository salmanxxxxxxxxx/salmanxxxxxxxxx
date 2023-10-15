indeks={
    "celsius  " :"c",
    "reamur  "  :"r",
    "fahrenheit":"f",
    "kelvin  "  :"k",

}
print("==========indeks satuan skala suhu==========")
for i in indeks:
    print("satuan suhu :",i, "\t indeks: ", indeks[i])

suhu=float(input("masukan suhu:"))
satuan=input("masukan indeks satuan skala suhu:")

if(satuan == "c"):
    print(suhu , "drajat celsius:")
    print("reamur = ", (suhu*4/5),"drajat")
    print("fahrenheit = ", (suhu*9/5+32), "drajat")
    print("kelvin = ", suhu + 273,"drajat")
          
