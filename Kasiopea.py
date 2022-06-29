start = list((input().split(":")))
end = list((input().split(":")))
def get_minutes(list):
    minutes = 0
    minutes = int(list[0])*60 + int(list[1])
    return int(minutes)

dif = get_minutes(end) - get_minutes(start)
m = dif%60
h = int((dif-m)/60)
if m==0:
    print("Misof slept for", str(h),"hour")
else:
    print("Misof slept for" ,str(h) ,"hours and",str(m), "minutes")
    

    