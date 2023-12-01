#%%
import Sprinkle as sp
import numpy as np
import matplotlib.pyplot as plt
from importlib import reload
reload(sp)

#%%
causet1=sp.sprinkle(100)
causet2=sp.sprinkle2(100)
causet3=sp.sprinklem(100)
# print(causet2.maximal_chain())

#%%testing forgetting time filter
causet=sp.sprinklem(100)
causet.plot(1)
x=np.linspace(-0.6,0.6,500)
tau=0.1
y=np.sqrt(tau**2+x**2)
plt.plot(x,y)
causet.forgetting(tau,0,causet.Lorentz(0,0))
#%%testing trajectory
causet=sp.sprinklem(100)
causet.trajectory(0.1,0.6)

#%%testing plotting trajectory
plt.show()
causet=sp.sprinklem(100)
causet.plottraject(0.1,0.6)
plt.xlim(-0.7,0.7)
plt.ylim(0,1.4)
plt.show()
#%%taking sample over multiple causal sets
# sample=sp.sprinkle3(100,100)
# sample.list[0].plot()

# %%
