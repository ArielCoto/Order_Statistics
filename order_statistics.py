#!/usr/bin/env python
# coding: utf-8

# # Ejercicio.
# 
# # Ariel Coto Tapia

# #### Vamos a dar dos metodos para simular variables aleatorias Beta(α, β). Para ello supondremos que α y β son parametros en los números naturales, elige los que tú gustes.
# 
# #### Método 1. Simula  $\alpha + \beta -1$  variables aleatorias $U_{1},...,U_{\alpha+\beta-1}$ uniformes en el [0, 1], y toma el α- ́esimo estadístico de orden, es decir, $U_{(\alpha)}$ . Si defines $Z=U_{(\alpha)}$, entonces Z se distribuye Beta(α, β).
# 
# #### Método 2. Simula 2 variables $Y_{1}~Gamma(\alpha,1)$ y $Y_{2}~Gamma(\beta ,1)$. Si definimos $Z=\frac{Y_{1}}{Y_{1}+Y_{2}}$, entonces $Z$ se distribuye Beta(α, β).(Puedes hacer uso de la funcion $numpy.random.gamma$

# * Empezaremos con el Método $\textbf{2}$ para simular variables aleatorias Beta($\alpha,\beta$).
# #### Sean $\alpha=1$ y $\beta=2$

# In[2]:


import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
import random


# In[3]:


alpha=1
beta=2
Y_1=random.gammavariate(alpha,1)
Y_2=random.gammavariate(beta,2)


# ##### Definimos Z

# In[4]:


Z=Y_1/(Y_1+Y_2)


# $\to$ $Z$ se distribuye Beta($\alpha, \beta$)

# * Luego continuamos con el Método $\textbf{1}$ para simular variables aleatorias Beta($\alpha,\beta$).

# Como $\alpha=1$ y $\beta=2$ entonces, simularemos $\alpha+\beta-1=\mathbf{2}$ variables aleatorias. Siendo $U_{1}$ y $U_{2}$ uniformes en el [0,1]

# In[5]:


random_sample=stats.uniform.rvs(loc=0,scale=1,size=2)
random_sample


# 

# In[6]:


ordered_sample=sorted(random_sample)


# In[7]:


Z=ordered_sample[0]
print(Z)


# $\to$ $Z$ se distribuye Beta($\alpha,\beta$)

# #### Sabiendo esto, haz un programa que realice tres histogramas, el primero de n (por ejemplo $n=1000$ o la cantidad suficientemente grande que gustes) simulaciones de variables aleatorias $Beta(\alpha,\beta)$ obtenidas por el método 1, otro histograma de $n$ simulaciones de $Beta(\alpha,\beta)$  por el método 2 y el  ́ultimo histograma de n simulaciones usando la función $numpy.random.beta$ ¿Son parecidos? Si $\alpha, \beta$ son números naturales muy grandes¿tarda igual o tarda más el método 1?

# * Primer histograma $\textbf{Método 1}$

# In[10]:


n_1=100000
t_list_1=[]

for i in range(n_1):
    random_sample=stats.uniform.rvs(loc=0,scale=1,size=2)
    ordered_sample=sorted(random_sample)
    Z_1=ordered_sample[0]
    t_list_1.append(Z_1)
    
    


# In[12]:


plt.hist(x=t_list_1, density=True,color='#F2AB6D',rwidth=0.9,bins=1000)
plt.xlabel('$Z \sim \alpha,\beta $')
plt.ylabel('Frecuencia')
plt.title('Distribución Beta. Método 1')
plt.show()


# * Segundo histograma $\textbf{Método 2}$

# In[20]:


n_2=100000
t_list_2=[]

for i in range(n_2):
    alpha=1
    beta=2
    Y_1=np.random.gamma(alpha,1)
    Y_2=np.random.gamma(beta,2)
    Z_2=Y_1/(Y_1+Y_2)
    t_list_2.append(Z_2)
    


# In[21]:


plt.hist(x=t_list_2,density=True, color='tab:purple',rwidth=0.9,bins=1000)
plt.xlabel('$Z \sim (\alpha,\beta)$')
plt.ylabel('Frecuencia')
plt.title('Distribución Beta. Método 2')
plt.show()


# * Tercer histograma usando la función $\textbf{numpy.random.beta}$

# In[17]:


n_3=100000
t_list_3=[]

for i in range(n_3):
    alpha=1
    beta=2
    Z_3=np.random.beta(alpha,beta)
    t_list_3.append(Z_3)


# In[18]:


plt.hist(x=t_list_3,density=True, color='seagreen',rwidth=0.9,bins=1000)
plt.xlabel('$Z \sim (\alpha,\beta)$')
plt.ylabel('Frecuencia')
plt.title('Distribución Beta. Método 3')
plt.show()


# #### Respondiendo a la interrogante si ¿son parecidos los histogramas?. Si son parecidos, sobre todo el Método 1 con el Tercer histograma.

# * Ahora, Si  $\alpha$, $\beta$  son números naturales muy grandes¿tarda igual o tarda más el método 1?

# Veamos...
# Sea $\alpha=30,000$ y $\beta=100,000$, entonces simularemos $\alpha+\beta-1=129,999$ variables aleatorias. Siendo $U_{1},...,U_{129,999}$ uniformes en el intervalo [0,1].
# Tomamos α- ́esimo estadístico de orden, es decir, $U_{(\alpha)}$ 

# In[3]:


n_prueba=1000
t_list_prueba=[]

for i in range(n_prueba):
    random_sample_prueba=stats.uniform.rvs(loc=0,scale=1,size=129999)
    ordered_sample_prueba=sorted(random_sample_prueba)
    Z_prueba=ordered_sample_prueba[30001]
    t_list_prueba.append(Z_prueba)
    


# In[15]:


plt.hist(x=t_list_prueba, density=True,color='black',rwidth=0.95,bins=100)
plt.xlabel('$Z \sim (\alpha,\beta)$')
plt.ylabel('Frecuencia')
plt.title('Distribución Beta. Método ANEXO')
plt.show()


# #### Es evidente que tarda mucho más en cargar los datos con parametros mucho más grandes, además vemos que tiende a una distribución normal.
