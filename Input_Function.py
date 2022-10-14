# -- coding:utf-8 --
import scipy.io as sio
import numpy as np
import _pickle as cPickle


def load_mat_data(file_name):
    contentsMat = sio.loadmat(file_name)
    arrMean = np.squeeze(contentsMat['arrMean'])
    arrStd = np.squeeze(contentsMat['arrStd'])
    return arrMean, arrStd

def normalize_dataset_test(input_data, input_features, arrMean, arrStd):
    # 수치형 변수: 0(Age), 2~59
    # Binary 변수[0-1]: 63-113
    # Binary 변수[1-2]: 1(Sex), 60-62

    ###=== Copy Input Data
    edit_data = input_data.copy()
    edit_data = np.reshape(edit_data, (1, input_features))

    ###=== Find Nan Values and Fill-up Nan Values
    for idx_col in range(0, input_features):
        edit_data[np.isnan(edit_data[:, idx_col]), idx_col] = arrMean[idx_col]

    ###=== Normalization Values
    for idx_col in range(0, input_features):
        if idx_col == 0:   ##=== Age
            edit_data[:, idx_col] = (edit_data[:, idx_col] - 50) / 100
        elif 2 <= idx_col <= 59:   ##=== 수치형 변수
            edit_data[:, idx_col] = (edit_data[:, idx_col] - arrMean[idx_col]) / arrStd[idx_col]
        else:  ##=== 0-1이라 수정이 필요 없는 데이터
            continue
    return edit_data

def preprocess_dataset(SavePath, input_data, input_features=114):
    ###=== Fill-up Nan Values & Normalization
    arrMean, arrStd = load_mat_data(SavePath + 'Mat_Normalization.mat')
    norm_data = normalize_dataset_test(input_data.copy(), input_features=input_features, arrMean=arrMean, arrStd=arrStd)
    return norm_data

def func_ML_Extra_Eval(SaveRootPath, input_data, input_features=114):
    norm_data = preprocess_dataset(SavePath=SaveRootPath, input_data=input_data, input_features=input_features)

    ###=== Predicted ML Model
    SavePath = SaveRootPath + 'Model_ML_Xgb/'
    arrProb = []
    for idx_repeat in range(1, 20 + 1):
        for idx_kfold in range(1, 5+1):
            model = cPickle.load(open(SavePath + 'model_Xgb_repeat' + str(idx_repeat) + '_fold' + str(idx_kfold) + '.pkl', 'rb'))
            extra_prob = model.predict_proba(norm_data)[:, 1]
            arrProb.append(extra_prob)

    ###=== Soft voting
    mean_prob = np.mean(arrProb)
    return mean_prob