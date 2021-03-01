from myMath import myStatistics 

x=int(input("請輸入第一個數:"))
y=int(input("請輸入第二個數:"))
z=int(input("請輸入第三個數:"))
r=int(input("請輸入第四個數:"))
k=int(input("請輸入第五個數:"))

A=[x,y,z,r,k]

print("5個數字的平均為",myStatistics.myMean(A)) 

