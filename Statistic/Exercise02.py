import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy as np 
def mean(ls):
    return (sum(ls)/len(ls))
data = [
    [23,43],
    [14,59],
    [14,48],
    [0,77],
    [17,50],
    [20,52],
    [20,46],
    [15,51],
    [21,51],
    
    
]
x =np.array([i[0] for i in data])
y =np.array([i[1] for i in data])
a,b1,b2 = np.polynomial.polynomial.polyfit(x,y,deg=2)
e = f'y={round(a,4)}{"+" if b1>0 else ""}\
    {round(b1,4)}x{"+" if b2>0 else ""}{round(b2,4)}x^2'
print(e)
n = len(x)
#predict_value quadratic
predict_value = [round((a+(b1*i)+(b2*i**2)),4) for i in x]
#Residual
residual = [round((y[i]-predict_value[i]),4) for i in range(n)]
#SSResid
SSResid = sum([(y[i]-predict_value[i])**2 for i in range(n) ])
#SSTo
y_mean = mean(y)
SSTo = sum([(y[i] - y_mean)**2 for i in range(n)])
r_square = round((1-(SSResid/SSTo))*100,2)
se = round((SSResid/(n-2))**0.5,4)
data = list(zip(x,y,predict_value,residual))
data_table = tabulate(data,headers=["x","y","predicted_value","residual"])
print(data_table)
print(f'r = {r_square}%')
print(f'se = {se}')

plt.figure(figsize=(10,4))
ax1 = plt.subplot(1,2,1)
ax1.scatter(x,y)
ax1.plot(x,(a+b1*x+b2*(x**2)),'-',c='r',label=r'$\hat{y} = a + b_1x + b_2x^2$')
ax1.legend()
ax1.set_title('Data')
ax1.set_xlabel('Date')
ax1.set_ylabel('Fishing Time')

ax2 = plt.subplot(1,2,2)
ax2.scatter(x,residual,label=r'$x,residual$')
ax2.legend()
ax2.set_title('x, residual plot')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
plt.show()
