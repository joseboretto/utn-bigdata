from sklearn import tree
from IPython.display import Image
import pydotplus
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn import svm
from mlxtend.plotting import plot_decision_regions

# http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html
class myClassifier(object):
    def decisionTreeClassifier(self, X, Y, feature_names, target_names, fileName):
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(X, Y)
        dot_data = tree.export_graphviz(clf, out_file=None,
                                        feature_names=feature_names,
                                        class_names=target_names,
                                        filled=True, rounded=True,
                                        special_characters=True)
        graph = pydotplus.graph_from_dot_data(dot_data)

        graph.write_pdf(fileName + '- Arbol.pdf')
        Image(graph.create_png())

    def SVMClassifier(self, X, Y,feature_names):

        clf = svm.SVC(kernel='linear', C = 1.0)
        # entrenamos el clasificador
        clf.fit(X, Y)
        # Obtenemos los pesos
        # Obtenemos los pesos
        w = clf.coef_
        print 'Pesos: [W]: ', w
        # self.plot_coefficients(clf,feature_names)
        # Plot Decision Region using mlxtend's awesome plotting function
        # Y = np.array(Y)
        # plot_decision_regions(X=X,y=Y,clf=clf,legend=5)





    def plot_coefficients(self, classifier, feature_names, top_features=2):
        # feature_names = ['Stage', 'Cantidad de faltas', '% Posesion','Cantidad de tiros al arco','Mes jugado''Stage', 'Cantidad de faltas', '% Posesion','Cantidad de tiros al arco','Mes jugado''Stage', 'Cantidad de faltas', '% Posesion','Cantidad de tiros al arco','Mes jugado']
        # https://medium.com/@aneesha/visualising-top-features-in-linear-svm-with-scikit-learn-and-matplotlib-3454ab18a14d
        coef = classifier.coef_.ravel()
        top_positive_coefficients = np.argsort(coef)[-top_features:]
        top_negative_coefficients = np.argsort(coef)[:top_features]
        top_coefficients = np.hstack([top_negative_coefficients, top_positive_coefficients])
        # create plot
        plt.figure(figsize=(15, 5))
        colors = ['red' if c < 0 else 'blue' for c in coef[top_coefficients]]
        plt.bar(np.arange(2 * top_features), coef[top_coefficients], color=colors)
        feature_names = np.array(feature_names)
        plt.xticks(np.arange(1, 1 + 2 * top_features), feature_names[top_coefficients], rotation=60, ha='right')
        plt.show()

