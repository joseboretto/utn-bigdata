import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn import svm
# Estos son nuestros datos
x = [1, 5, 1.5, 8, 1, 9]
y = [2, 8, 1.8, 8, 0.6, 11]
# los metenos en un array de 2 dimensiones (x,y)
X = np.array([[1,2],
             [5,8],
             [1.5,1.8],
             [8,8],
             [1,0.6],
             [9,11]])
# clasificacmos esos datos con el vector Y
y = [0,1,0,1,0,1]
#Creamos una clasificador
clf = svm.SVC(kernel='linear', C = 1.0)
#entrenamos el clasificador
clf.fit(X,y)
#Obtenemos los pesos
w = clf.coef_[0]
print 'Pesos: [W]: ' , w
#Obtenemos el valor de b (ordenada al origen)
b = clf.intercept_[0] / w[1]
# a es la inclinacion de la recta
a = -w[0] / w[1]
#ancho de la recta
xx = np.linspace(0,12)
# Formula de una recta: y = ax + b
yy = a * xx - b
#creamos la recta
h0 = plt.plot(xx, yy, 'k-', label="non weighted div")
# Hacemos un grafico de dispersion (scater) en x vs y
plt.scatter(X[:, 0], X[:, 1], c = y)
plt.legend()
plt.show()