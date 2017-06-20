from sklearn import tree
from IPython.display import Image
import pydotplus


class myDecisionTree(object):
    def classifie(self, X, Y, feature_names, target_names, fileName):
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
