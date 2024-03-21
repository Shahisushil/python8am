# ntc to ntc = 2.5 
# ncell to ntc = 3.5
# ntc to ncell = 4.5
# ncell to ncell = 5.5
# 0-10 minutes interval
# find the bounous amount talking in certain Time

# KTM (27 KM)
# 5KM TO 5KM = KALANKI TO SWAYAMBHU
# 5KM TO 10KM = SWAYAMBHU TO BUS PARK
# 10KM TO 15KM = BUS PARK TO NARAYAN CHOWK
# 15KM TO 20KM = NARAYAN CHOWK TO TINKUNE
# 20KM TO 25KM = TINKUNE TO KALANKI
# NPR 15 PER 5KM
# 15% (STUDENT AND OLD AGE DISCOUNT)
# FIND KALANKI TO KALANKI PRICE ?


print("======================= BUS FAIR================")
print("1. kalanki to swayambhu 5 km (Rs. 15)")
print("2. swayambhuto bus park 10 km (Rs. 30)")
print("3. bus park to narayan chowk 15 km (Rs. 45)")
print("4. narayan chowk to tinkune 20 km (Rs. 60)")
print("5. tinkune to kalanki 25 km ( Rs.75 )")

option = int(input( "Enter your choice: "))

if option==1:
    travel_distance=int(input("Enter the travel area: "))
    if travel_distance>1 and travel_distance<5:
        print(f("you trave price: ",15))
    elif travel_distance>5 and travel_distance<10:
        print(f("your travel price: ",30))
        
