from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2


# http://scikit-learn.org/stable/modules/feature_selection.html
class myFeatureSelection(object):
    def pca(self, X, Y):
        pca = PCA(n_components=2)
        X_new = pca.fit_transform(X,Y)
        print 'PCA'
        print(pca.explained_variance_ratio_)
        print X_new


    def selectKBest(self,X, Y):
        X_new = SelectKBest(chi2, k=2).fit_transform(X, Y)
        print 'selectKBest'
        print X_new




