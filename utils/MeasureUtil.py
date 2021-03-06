#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu Nguyen" at 14:33, 25/03/2020                                                        %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Thieu_Nguyen6                                  %
#       Github:     https://github.com/thieunguyen5991                                                  %
#-------------------------------------------------------------------------------------------------------%

from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, mean_squared_log_error, median_absolute_error, r2_score
from numpy import round, sqrt, abs, where, mean, asscalar


class MeasureTimeSeries(object):
	def __init__(self, y_true, y_pred, multi_output=None, number_rounding=3):
		"""
		:param y_true:
		:param y_pred:
		:param multi_output:    string in [‘raw_values’, ‘uniform_average’, ‘variance_weighted’] or array-like of shape (n_outputs)
		:param number_rounding:
		"""
		self.y_true = y_true
		self.y_pred = y_pred
		self.multi_output = multi_output
		self.number_rounding = number_rounding
		self.score_ev, self.score_mae, self.score_mse, self.score_msle, self.score_meae = None, None, None, None, None
		self.score_r2, self.score_rmse, self.score_mape, self.score_smape = None, None, None, None

	def explained_variance_score(self):
		temp = explained_variance_score(self.y_true, self.y_pred, multioutput=self.multi_output)
		self.score_ev = asscalar(round(temp, self.number_rounding))

	def mean_absolute_error(self):
		temp = mean_absolute_error(self.y_true, self.y_pred, multioutput=self.multi_output)
		self.score_mae = asscalar(round(temp, self.number_rounding))

	def mean_squared_error(self):
		temp = mean_squared_error(self.y_true, self.y_pred, multioutput=self.multi_output)
		self.score_mse = asscalar(round(temp, self.number_rounding))

	def mean_squared_log_error(self):
		y_true = where(self.y_true < 0, 0, self.y_true)
		y_pred = where(self.y_pred < 0, 0, self.y_pred)
		temp = mean_squared_log_error(y_true, y_pred, multioutput=self.multi_output)
		self.score_msle = asscalar(round(temp, self.number_rounding))

	def median_absolute_error(self):
		if self.multi_output is not None:
			print("Median absolute error is not supported for multi output")
			return None
		temp = median_absolute_error(self.y_true, self.y_pred)
		self.score_meae = asscalar(round(temp, self.number_rounding))

	def r2_score_error(self):
		temp = r2_score(self.y_true, self.y_pred, multioutput=self.multi_output)
		self.score_r2 = asscalar(round(temp, self.number_rounding))

	def root_mean_squared_error(self):
		temp = sqrt(mean_squared_error(self.y_true, self.y_pred, multioutput=self.multi_output))
		self.score_rmse = asscalar(round(temp, self.number_rounding))

	def mean_absolute_percentage_error(self):
		temp = mean(abs((self.y_true - self.y_pred) / self.y_true), axis=0) * 100
		self.score_mape = asscalar(round(temp, self.number_rounding))

	def symmetric_mean_absolute_percentage_error(self):
		temp = mean(2 * abs(self.y_pred - self.y_true) / (abs(self.y_true) + abs(self.y_pred)), axis=0) * 100
		self.score_smape = asscalar(round(temp, self.number_rounding))

	def _fit__(self):
		self.explained_variance_score()
		self.mean_absolute_error()
		self.mean_squared_error()
		self.mean_squared_log_error()
		self.r2_score_error()
		self.root_mean_squared_error()
		self.mean_absolute_percentage_error()
		self.symmetric_mean_absolute_percentage_error()