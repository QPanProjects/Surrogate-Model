from sklearn import linear_model

# X = [[0., 0.], [1., 1.], [10., 10.]]
X = [[0.0], [1.0], [10.0]]
y = [0.0, 1.0, 10.0]
# x_preb = [[5., 5.], [-10., -10.]]
x_preb = [[5.], [-10.]]

clf = linear_model.Lars(n_nonzero_coefs=1)
clf.fit(X, y)
print(clf.coef_)
y_pred = clf.predict(x_preb)
print y_pred
