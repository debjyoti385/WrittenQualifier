from pandas import read_csv
from pandas import datetime
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.arima_model import ARMA
from sklearn.metrics import mean_squared_error

def parser_190(x):
	return datetime.strptime('190'+x, '%Y-%m')

def parser(x):
	return datetime.strptime(x, '%Y-%m')

def parser_year(x):
	return datetime.strptime(x, '%Y')

# series = read_csv('facebook_active_users.csv', header=0, parse_dates=[0], index_col=0,  squeeze=True, date_parser=parser)

series = read_csv('tweet_per_minute.csv', header=0, parse_dates=[0], index_col=0,  squeeze=True, date_parser=parser_year)

X = series.values
K = series.keys()
print (X)
size = int(len(X) * 0.6)
train, test = X[0:size], X[size:len(X)]
train_k, test_k = K[0:size], K[size:len(X)]
history = [x for x in train]
predictions = list()
for t in range(len(test)):
	# try:
	model = ARIMA(history, order=(0,1,0))
	# model = ARMA(history, order=(1,0))
	model_fit = model.fit(disp=0)
	output = model_fit.forecast(5)
	yhat = output[0]
	predictions.append(yhat)
	obs = test[t]
	date_k = test_k[t]
	history.append(obs)
	print('Prediction for %s is %f' % ( date_k.strftime('%Y-%m'), yhat))
	# except:
		# pass

error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)
# plot
pyplot.plot(test)
pyplot.plot(predictions, color='red')
fig = pyplot.figure()
fig.savefig("plot.png")
