import matplotlib.pyplot as plt

itmax = sum(range(729))
print "Max it for loop2", itmax

it = range(729)
loop2it  = [itmax if (i%(3*int(i/30) + 1)==0) else 0 for i in it]
loop1it = [728 - i for i in it]
width = 1

plt.figure(1)
plt.bar(it, loop1it, width,color='green',edgecolor='none')
plt.xlabel('Outer loop iteration iterand (i)',fontsize=16)
plt.ylabel('Number of nested iterations',fontsize=16)
plt.title('Nested Iterations for Iteration Iterand of Loop 1',y=1.04,fontsize=20)

plt.figure(2)
plt.bar(it, loop2it, width,color='blue',edgecolor='none')
plt.xlabel('Outer loop iteration iterand (i)',fontsize=16)
plt.ylabel('Number of nested iterations',fontsize=16)
plt.title('Nested Iterations for Iteration Iterand of Loop 2',y=1.04,fontsize=20)

plt.show()

