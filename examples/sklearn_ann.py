import warnings

from sklearn.neural_network import MLPClassifier, MLPRegressor

warnings.filterwarnings(action="ignore", category=Warning)

X = [[0., 0.], [1., 1.], [10., 10.]]
y = [0.0, 1.0, 10.0]
x_preb = [[5., 5.], [-10., -2.]]
x_preb = X
print 'MLPClassifier'
clf = MLPClassifier(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(X, y)
y_pred = clf.predict(x_preb)
print y_pred
y_prob = clf.predict_proba(x_preb)
print y_prob
print y_prob[:, 1]

print 'MLPRegressor'
rgs = MLPRegressor(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
rgs.fit(X, y)
y_pred = clf.predict(x_preb)
print y_pred
y_prob = clf.predict_proba(x_preb)
print y_prob
print y_prob[:, 1]
