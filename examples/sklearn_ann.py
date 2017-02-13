# MIT License
#
# Copyright (c) 2016 Daily Actie
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Author: Quan Pan <quanpan302@hotmail.com>
# License: MIT License
# Create: 2016-12-02

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
