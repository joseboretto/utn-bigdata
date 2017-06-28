import matplotlib.pyplot as plt
import numpy as np
import pydotplus
from IPython.display import Image
from sklearn import tree
from matplotlib.backends.backend_pdf import PdfPages


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
        graph.write_pdf(fileName + '- Arbol.pdf')

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
        graph.write_pdf(fileName + '- Arbol - max depth ' + str(maxdepth) +'.pdf')

    def decisionTreeClassifierMinLeaf(self, X, Y, feature_names, target_names, fileName,MinLeaf):
        # http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
        clf = tree.DecisionTreeClassifier(min_samples_leaf=MinLeaf)
        clf = clf.fit(X, Y)
        dot_data = tree.export_graphviz(clf, out_file=None,
                                        feature_names=feature_names,
                                        class_names=target_names,
                                        filled=True, rounded=True,
                                        special_characters=True)
        graph = pydotplus.graph_from_dot_data(dot_data)
        graph.write_pdf(fileName + '- Arbol - Min Leaf ' + str(MinLeaf) +'.pdf')

    def decisionTreeClassifierDesicionBoundaryStraigh(self, X, Y, feature_names, target_names, fileName, title, coloursList):
        # guardo pdf
        fig = plt.figure()
        # http://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_iris.html
        # Parameters
        n_classes = 3
        # plot_colors = "gbr"
        cmap = plt.cm.RdYlBu
        plot_step = 1  # fine step width for decision surface contours
        plot_step_coarser = 0.5  # step widths for coarse classifier guesses
        RANDOM_SEED = 1  # fix the seed on each iteration
        plot_idx = 1

        cant_tagert = len(target_names)
        plt.figure(figsize=(10, 10))
        for pairidx, pair in enumerate([[0, 0], [1, 0], [2, 0],
                                        [0, 1], [1, 1], [2, 1],
                                        [0, 2], [1, 2], [2, 2]]):
            # dont plot the diagonal
            if pair[0] == pair[1]:
                continue
            # We only take the two corresponding features
            X_2Features = X[:, pair]
            y = Y

            # Shuffle
            idx = np.arange(X_2Features.shape[0])
            np.random.seed(RANDOM_SEED)
            np.random.shuffle(idx)
            X_2Features = X_2Features[idx]
            # y = y[idx]

            # Standardize
            # mean = X_2Features.mean(axis=0)
            # std = X_2Features.std(axis=0)
            # X_2Features = (X_2Features - mean) / std

            # Train
            clf = tree.DecisionTreeClassifier().fit(X_2Features, y)

            # Save tree
            dot_data = tree.export_graphviz(clf, out_file=None,
                                            feature_names=feature_names,
                                            class_names=target_names,
                                            filled=True, rounded=True,
                                            special_characters=True)
            graph = pydotplus.graph_from_dot_data(dot_data)
            graph.write_pdf(fileName + '- Arbol - pos - ' + str(pair) + ' .pdf')


            scores = clf.score(X_2Features, y)
            # Create a title for each column and the console by using str() and
            # slicing away useless parts of the string
            plt.xlabel(feature_names[pair[0]])
            plt.ylabel(feature_names[pair[1]])


            plt.subplot(cant_tagert, cant_tagert, (pairidx + 1))


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
                plt.scatter(x_axis_values, y_axis_values, c=coloursList, label=target_names[i], cmap=plt.cm.Paired ,s=10)
            plt.axis("tight")


            plot_idx += 1  # move on to the next plot in sequence

        plt.suptitle(title)
        plt.axis("tight")

        print ('Generando PDF DesicionBoundary - straigh')
        pp = PdfPages(fileName + '- DesicionBoundary.pdf')
        plt.savefig(pp, format='pdf')
        pp.close()

        # maximizo el tamano
        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())
        plt.show()

    def decisionTreeClassifierDesicionBoundaryStraighDepth(self, X, Y, feature_names, target_names, fileName, title,
                                                      coloursList, maxDepth):
        # guardo pdf
        fig = plt.figure()
        # http://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_iris.html
        # Parameters
        n_classes = 3
        # plot_colors = "gbr"
        cmap = plt.cm.RdYlBu
        plot_step = 1  # fine step width for decision surface contours
        plot_step_coarser = 0.5  # step widths for coarse classifier guesses
        RANDOM_SEED = 1  # fix the seed on each iteration
        plot_idx = 1

        cant_tagert = len(target_names)
        plt.figure(figsize=(10, 10))
        for pairidx, pair in enumerate([[0, 0], [1, 0], [2, 0],
                                        [0, 1], [1, 1], [2, 1],
                                        [0, 2], [1, 2], [2, 2]]):
            # dont plot the diagonal
            if pair[0] == pair[1]:
                continue
            # We only take the two corresponding features
            X_2Features = X[:, pair]
            y = Y

            # Shuffle
            idx = np.arange(X_2Features.shape[0])
            np.random.seed(RANDOM_SEED)
            np.random.shuffle(idx)
            X_2Features = X_2Features[idx]
            # y = y[idx]

            # Standardize
            # mean = X_2Features.mean(axis=0)
            # std = X_2Features.std(axis=0)
            # X_2Features = (X_2Features - mean) / std

            # Train
            clf = tree.DecisionTreeClassifier(max_depth=maxDepth).fit(X_2Features, y)
            # Save tree
            dot_data = tree.export_graphviz(clf, out_file=None,
                                            feature_names=feature_names,
                                            class_names=target_names,
                                            filled=True, rounded=True,
                                            special_characters=True)
            graph = pydotplus.graph_from_dot_data(dot_data)
            graph.write_pdf(fileName + '- Arbol - max depth ' + str(maxDepth) + ' - pos -'+ str(pair) +'.pdf')

            scores = clf.score(X_2Features, y)
            # Create a title for each column and the console by using str() and
            # slicing away useless parts of the string
            plt.xlabel(feature_names[pair[0]])
            plt.ylabel(feature_names[pair[1]])

            plt.subplot(cant_tagert, cant_tagert, (pairidx + 1))

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
                plt.scatter(x_axis_values, y_axis_values, c=coloursList, label=target_names[i], cmap=plt.cm.Paired,
                            s=10)
            plt.axis("tight")

            plot_idx += 1  # move on to the next plot in sequence

        plt.suptitle(title + '- max depth ' + str(maxDepth))
        plt.axis("tight")

        print ('Generando PDF DesicionBoundary - straigh - max depth' , maxDepth)
        pp = PdfPages(fileName + '- DesicionBoundary - max depth'+ str(maxDepth) +'.pdf')
        plt.savefig(pp, format='pdf')
        pp.close()

        # maximizo el tamano
        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())
        plt.show()

    def decisionTreeClassifierDesicionBoundaryStraighMinLeaf(self, X, Y, feature_names, target_names, fileName, title,
                                                           coloursList, MinLeaf):
        # guardo pdf
        fig = plt.figure()
        # http://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_iris.html
        # Parameters
        n_classes = 3
        # plot_colors = "gbr"
        cmap = plt.cm.RdYlBu
        plot_step = 1  # fine step width for decision surface contours
        plot_step_coarser = 0.5  # step widths for coarse classifier guesses
        RANDOM_SEED = 1  # fix the seed on each iteration
        plot_idx = 1

        cant_tagert = len(target_names)
        plt.figure(figsize=(10, 10))
        for pairidx, pair in enumerate([[0, 0], [1, 0], [2, 0],
                                        [0, 1], [1, 1], [2, 1],
                                        [0, 2], [1, 2], [2, 2]]):
            # dont plot the diagonal
            if pair[0] == pair[1]:
                continue
            # We only take the two corresponding features
            X_2Features = X[:, pair]
            y = Y

            # Shuffle
            idx = np.arange(X_2Features.shape[0])
            np.random.seed(RANDOM_SEED)
            np.random.shuffle(idx)
            X_2Features = X_2Features[idx]
            # y = y[idx]

            # Standardize
            # mean = X_2Features.mean(axis=0)
            # std = X_2Features.std(axis=0)
            # X_2Features = (X_2Features - mean) / std

            # Train
            clf = tree.DecisionTreeClassifier(min_samples_leaf=MinLeaf).fit(X_2Features, y)
            # Save tree
            dot_data = tree.export_graphviz(clf, out_file=None,
                                            feature_names=feature_names,
                                            class_names=target_names,
                                            filled=True, rounded=True,
                                            special_characters=True)
            graph = pydotplus.graph_from_dot_data(dot_data)
            graph.write_pdf(fileName + '- Arbol - Min Leaf ' + str(MinLeaf) + ' - pos -' + str(pair) + '.pdf')

            scores = clf.score(X_2Features, y)
            # Create a title for each column and the console by using str() and
            # slicing away useless parts of the string
            plt.xlabel(feature_names[pair[0]])
            plt.ylabel(feature_names[pair[1]])

            plt.subplot(cant_tagert, cant_tagert, (pairidx + 1))

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
                plt.scatter(x_axis_values, y_axis_values, c=coloursList, label=target_names[i], cmap=plt.cm.Paired,
                            s=10)
            plt.axis("tight")

            plot_idx += 1  # move on to the next plot in sequence

        plt.suptitle(title + '- Min Leaf ' + str(MinLeaf))
        plt.axis("tight")

        print ('Generando PDF DesicionBoundary - straigh - Min Leaf', MinLeaf)
        pp = PdfPages(fileName + '- DesicionBoundary - Min Leaf' + str(MinLeaf) + '.pdf')
        plt.savefig(pp, format='pdf')
        pp.close()

        # maximizo el tamano
        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())
        plt.show()











