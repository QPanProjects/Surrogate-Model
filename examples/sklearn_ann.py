import warnings
warnings.filterwarnings(action="ignore", category=Warning)

from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.preprocessing import StandardScaler, MaxAbsScaler


X = [[0., 0.], [1., 1.], [10., 10.]]
y = [0.0, 1.0, 10.0]
x_preb = [[5., 5.], [-10., -2.]]
x_preb = X

print '\nMLPClassifier'
clf = MLPClassifier(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(X, y)
y_pred = clf.predict(x_preb)
print y_pred
y_prob = clf.predict_proba(x_preb)
print y_prob
print y_prob[:, 1]

print '\nMLPRegressor'
rgs = MLPRegressor(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
rgs.fit(X, y)
y_pred = clf.predict(x_preb)
print y_pred
y_prob = clf.predict_proba(x_preb)
print y_prob
print y_prob[:, 1]

print X
print '\nStandardScaler'
scaler_standard = StandardScaler(copy=True, with_mean=True, with_std=True).fit(X)
X_scal = scaler_standard.transform(X)
print scaler_standard.mean_
print scaler_standard.scale_
print X_scal

print '\nMaxAbsScaler'
scaler_max_abs = MaxAbsScaler(copy=True).fit(X)
X_scal = scaler_max_abs.transform(X)
print scaler_max_abs.mean_
print scaler_max_abs.scale_
print X_scal
