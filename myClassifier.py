import matplotlib.pyplot as plt
import numpy as np
import pydotplus
from IPython.display import Image
from sklearn import tree
from matplotlib.backends.backend_pdf import PdfPages
import os

# http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html
class myClassifier(object):
    def decisionTreeClassifier(self, X, Y, feature_names, target_names, fileName):
        # http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(X, Y)
        dot_data = tree.export_graphviz(clf, out_file=None,
                                        feature_names=feature_names,
                                        class_names=target_names,
                                        filled=True, rounded=True,
                                        special_characters=True)
        graph = pydotplus.graph_from_dot_data(dot_data)
        graph.write_png(fileName + '/' + fileName + '- Arbol.png')

    def decisionTreeClassifierMaxDepth(self, X, Y, feature_names, target_names, fileName,maxdepth):
        # http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
        clf = tree.DecisionTreeClassifier(max_depth=maxdepth)
        clf = clf.fit(X, Y)
        dot_data = tree.export_graphviz(clf, out_file=None,
                                        feature_names=feature_names,
                                        class_names=target_names,
                                        filled=True, rounded=True,
                                        special_characters=True)
        graph = pydotplus.graph_from_dot_data(dot_data)
        graph.write_png(fileName + '/' +fileName + '- Arbol - max depth ' + str(maxdepth) +'.png')


    def decisionTreeClassifierDesicionBoundaryStraigh(self, X, Y, feature_names, target_names, fileName, title, coloursList):
        if not os.path.exists(fileName +'/clf-original'):
            os.makedirs(fileName +'/clf-original')
        # guardo pdf
        # fig = plt.figure()
        # http://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_iris.html
        # Parameters
        n_classes = 3
        # plot_colors = "gbr"
        cmap = plt.cm.RdYlBu
        plot_step = 1  # fine step width for decision surface contours
        plot_step_coarser = 0.5  # step widths for coarse classifier guesses
        RANDOM_SEED = 1  # fix the seed on each iteration
        plot_idx = 1

        cant_feature = len(feature_names)
        plt.figure(figsize=(10, 10))
        # ['Corners','Foules', 'Tiros al arco']
        # x_axis_values = X_2Features[:, 0]
        # y_axis_values = X_2Features[:, 1]
        for pairidx, pair in enumerate([
                                        [0, 0], [1, 0], [2, 0], [3, 0], [4, 0],
                                        [0, 1], [1, 1], [2, 1], [3, 1], [4, 1],
                                        [0, 2], [1, 2], [2, 2], [3, 2], [4, 2],
                                        [0, 3], [1, 3], [2, 3], [3, 3], [4, 3],
                                        [0, 4], [1, 4], [2, 4], [3, 4], [4, 4]
                                       ]):

            # select the sub plot
            plt.subplot(cant_feature, cant_feature, (pairidx + 1))
            if pair[0] == 0:
                plt.ylabel(feature_names[pair[1]])

            if pair[1] == (len(feature_names) - 1):
                plt.xlabel(feature_names[pair[0]])

            # dont plot the diagonal
            if pair[0] == pair[1]:
                continue

            # We only take the two corresponding features
            X_2Features = X[:, pair]
            y = Y
            y_2FeaturesName = [feature_names[pair[0]],feature_names[pair[1]]]



            # Train
            clf = tree.DecisionTreeClassifier().fit(X_2Features, y)

            # Save tree
            dot_data = tree.export_graphviz(clf, out_file=None,
                                            feature_names=y_2FeaturesName,
                                            class_names=target_names,
                                            filled=True, rounded=True,
                                            special_characters=True)
            graph = pydotplus.graph_from_dot_data(dot_data)
            graph.write_png(fileName + '/clf-original/' + '- Arbol original - pos - ' + str(pair) + ' .png')


            scores = clf.score(X_2Features, y)





            # Now plot the decision boundary using a fine mesh as input to a
            # filled contour plot
            x_min, x_max = X_2Features[:, 0].min() - 1, X_2Features[:, 0].max() + 1
            y_min, y_max = X_2Features[:, 1].min() - 1, X_2Features[:, 1].max() + 1
            xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                                 np.arange(y_min, y_max, plot_step))

            # Plot either a single DecisionTreeClassifier or alpha blend the
            # decision surfaces of the ensemble of classifiers

            Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
            Z = Z.reshape(xx.shape)
            cs = plt.contourf(xx, yy, Z, cmap=cmap)

            # Build a coarser grid to plot a set of ensemble classifications
            # to show how these are different to what we see in the decision
            # surfaces. These points are regularly space and do not have a black outline
            xx_coarser, yy_coarser = np.meshgrid(np.arange(x_min, x_max, plot_step_coarser),
                                                 np.arange(y_min, y_max, plot_step_coarser))
            Z_points_coarser = clf.predict(np.c_[xx_coarser.ravel(), yy_coarser.ravel()]).reshape(
                xx_coarser.shape)
            cs_points = plt.scatter(xx_coarser, yy_coarser, s=5, c=Z_points_coarser, cmap=cmap, edgecolors="none")

            # Plot the training points, these are clustered together and have a
            # black outline
            # for i, c in zip(xrange(n_classes), plot_colors):
            #     idx = np.where(y == i)
            #     plt.scatter(X[idx, 0], X[idx, 1], c=c, label=target_names[i],cmap=cmap)
            # Plot the training points
            for i in range(0, n_classes):
                # idx = np.where(Y == i)
                # plt.scatter(X[idx, 0], X_2features[idx, 1], c=color, label=target_names[i],cmap=plt.cm.Paired)
                x_axis_values = X_2Features[:, 0]
                y_axis_values = X_2Features[:, 1]
                plt.scatter(x_axis_values, y_axis_values, c=coloursList, label=target_names[i], cmap=plt.cm.Paired ,s=5)
            plt.axis("tight")


            plot_idx += 1  # move on to the next plot in sequence



        plt.suptitle(title)
        plt.axis("tight")
        print ('Generando PDF DesicionBoundary - straigh')
        plt.savefig(fileName + '/clf-original/' +fileName + '- original - surface - .png')
        # maximizo el tamano
        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())
        plt.show()

    def decisionTreeClassifierDesicionBoundaryStraighDepth(self, X, Y, feature_names, target_names, fileName, title,
                                                      coloursList, maxDepth):

        if not os.path.exists(fileName +'/clf-maxDepth' + str(maxDepth)):
            os.makedirs(fileName +'/clf-maxDepth' + str(maxDepth))
        # http://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_iris.html
        # Parameters
        n_classes = 3
        #surface color
        cmap = plt.cm.RdYlBu
        plot_step = 1  # fine step width for decision surface contours
        plot_step_coarser = 0.5  # step widths for coarse classifier guesses
        RANDOM_SEED = 1  # fix the seed on each iteration
        plot_idx = 1

        cant_feature = len(feature_names)

        plt.figure(figsize=(10, 10))

        for pairidx, pair in enumerate([
            [0, 0], [1, 0], [2, 0], [3, 0], [4, 0],
            [0, 1], [1, 1], [2, 1], [3, 1], [4, 1],
            [0, 2], [1, 2], [2, 2], [3, 2], [4, 2],
            [0, 3], [1, 3], [2, 3], [3, 3], [4, 3],
            [0, 4], [1, 4], [2, 4], [3, 4], [4, 4]
        ]):

            # select the sub plot
            plt.subplot(cant_feature, cant_feature, (pairidx + 1))
            if pair[0] == 0:
                plt.ylabel(feature_names[pair[1]])

            if pair[1] == (len(feature_names) - 1):
                plt.xlabel(feature_names[pair[0]])

            # dont plot the diagonal
            if pair[0] == pair[1]:
                continue



            # We only take the two corresponding features
            X_2Features = X[:, pair]
            y = Y
            y_2FeaturesName = [feature_names[pair[0]], feature_names[pair[1]]]

            # Train
            clf = tree.DecisionTreeClassifier(max_depth=maxDepth).fit(X_2Features, y)
            # Save tree
            dot_data = tree.export_graphviz(clf, out_file=None,
                                            feature_names=y_2FeaturesName,
                                            class_names=target_names,
                                            filled=True, rounded=True,
                                            special_characters=True)
            graph = pydotplus.graph_from_dot_data(dot_data)
            graph.write_png(fileName + '/clf-maxDepth' + str(maxDepth) +'/max depth '+ str(maxDepth)+ '- Arbol - pos - ' + str(pair) + ' .png')

            scores = clf.score(X_2Features, y)
            # Create a title for each column and the console by using str() and
            # slicing away useless parts of the string



            # plt.xlabel(feature_names[pair[0]])
            # plt.ylabel(feature_names[pair[1]])
            # Now plot the decision boundary using a fine mesh as input to a
            # filled contour plot
            x_min, x_max = X_2Features[:, 0].min() - 1, X_2Features[:, 0].max() + 1
            y_min, y_max = X_2Features[:, 1].min() - 1, X_2Features[:, 1].max() + 1
            xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                                 np.arange(y_min, y_max, plot_step))

            # Plot either a single DecisionTreeClassifier or alpha blend the
            # decision surfaces of the ensemble of classifiers
            Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
            Z = Z.reshape(xx.shape)
            cs = plt.contourf(xx, yy, Z, cmap=cmap)

            # Build a coarser grid to plot a set of ensemble classifications
            # to show how these are different to what we see in the decision
            # surfaces. These points are regularly space and do not have a black outline
            xx_coarser, yy_coarser = np.meshgrid(np.arange(x_min, x_max, plot_step_coarser),
                                                 np.arange(y_min, y_max, plot_step_coarser))
            Z_points_coarser = clf.predict(np.c_[xx_coarser.ravel(), yy_coarser.ravel()]).reshape(
                xx_coarser.shape)
            cs_points = plt.scatter(xx_coarser, yy_coarser, s=15, c=Z_points_coarser, cmap=cmap, edgecolors="none")


            # Plot the training points
            for i in range(0, n_classes):
                # idx = np.where(Y == i)
                # plt.scatter(X[idx, 0], X_2features[idx, 1], c=color, label=target_names[i],cmap=plt.cm.Paired)
                x_axis_values = X_2Features[:, 0]
                y_axis_values = X_2Features[:, 1]
                plt.scatter(x_axis_values, y_axis_values, c=coloursList, label=target_names[i], cmap=plt.cm.Paired,
                            s=10)
            plt.axis("tight")

            plot_idx += 1  # move on to the next plot in sequence

        plt.suptitle(title + '- max depth ' + str(maxDepth))
        plt.axis("tight")

        print ('Generando PDF DesicionBoundary - straigh - max depth' , maxDepth)
        plt.savefig(fileName +'/clf-maxDepth' + str(maxDepth) +'/'+fileName + '-surface- max depth'+ str(maxDepth) +'.png')

        # maximizo el tamano
        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())
        plt.show()












