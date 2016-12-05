# from sklearn import datasets
# iris = datasets.load_iris()
# X, y = iris.data, iris.target
# y_true = [0, 1, 2, 3]
# y_pred = [0, 2, 1, 3]
#
# from sklearn.metrics import fbeta_score, make_scorer
# ftwo_scorer = make_scorer(fbeta_score, beta=2)
#
#
# from sklearn.model_selection import GridSearchCV
# from sklearn.svm import LinearSVC
# grid = GridSearchCV(LinearSVC(), param_grid={'C': [1, 10]}, scoring=ftwo_scorer)


import warnings

from sklearn.neural_network import MLPClassifier

warnings.filterwarnings(action="ignore", category=Warning)

X = [[0., 0.], [1., 1.]]
y = [0, 1]
x_preb = [[1., 1.], [-10., -2.]]
clf = MLPClassifier(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(X, y)
y_pred = clf.predict(x_preb)
y_prob = clf.predict_proba(x_preb)

print y_pred
print y_prob
print y_prob[:, 1]
