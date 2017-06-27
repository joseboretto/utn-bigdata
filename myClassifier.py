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


    def decisionTreeClassifierDesicionBoundary(self, X, Y, feature_names, target_names,fileName):
        # Parameters
        n_classes = 3
        plot_colors = "bry"
        plot_step = 1
        for pairidx, pair in enumerate([[0, 1], [0, 2], [1, 2]]):

            print "pair",pair
            print "paidx",pairidx
            print "feature 1 , eje X", feature_names[pair[0]]
            print "feature 2 , eje Y", feature_names[pair[1]]

            # We only take the two corresponding features
            X_2features = X[:, pair]


            # Train
            clf = tree.DecisionTreeClassifier().fit(X_2features, Y)

            # Plot the decision boundary
            plt.subplot(1, 3, pairidx + 1)

            x_min, x_max = 0, 30
            y_min, y_max = 0 ,30
            xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                                 np.arange(y_min, y_max, plot_step))

            Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
            Z = Z.reshape(xx.shape)
            cs = plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)

            plt.xlabel(feature_names[pair[0]])
            plt.ylabel(feature_names[pair[1]])
            plt.axis("tight")
            # plt.show()

            # Plot the training points
            for i, color in zip(range(n_classes), plot_colors):
                idx = np.where(Y == i)
                plt.scatter(X[idx, 0], X[idx, 1], c=color, label=target_names[i],
                            cmap=plt.cm.Paired)

            plt.axis("tight")
            # plt.show()

        plt.suptitle("Equipo " + fileName)
        plt.legend()
        plt.show()










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

