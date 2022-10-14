from flask import Flask, render_template, request
from flask_wtf import FlaskForm   # pip install Flask-WTF
from flask_bootstrap import Bootstrap
from wtforms import widgets, Form, FloatField, IntegerField, SelectField, SelectMultipleField

import numpy as np
import random
from Input_Function import func_ML_Extra_Eval


# app = Flask(__name__)
# Bootstrap(app)

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class SimpleForm(FlaskForm):
    example = MultiCheckboxField('Label')

class StomachCancerForm(Form):
    age = IntegerField("Age at operation", description="year")
    gender = SelectField("Gender", choices=[('0', 'Male'), ('1', 'Female')])

    phy_height = FloatField("Height", description="cm")
    phy_weight_pre = FloatField("Preoperative weight", description="kg")
    phy_weight_post = FloatField("Postoperative one-year weight", description="kg")
    phy_weight_diff = FloatField("difference value of weight", description="kg")
    phy_weight_per = FloatField("difference percentage of weight", description="")
    phy_bmi_pre = FloatField("Preoperative BMI", description="")
    phy_bmi_post = FloatField("One-year postoperative BMI", description="")
    phy_bmi_diff = FloatField("difference value of BMI", description="")
    phy_bmi_per = FloatField("difference percentage of BMI", description="")

    lab_chol_pre = FloatField("Preoperative cholesterol", description="mg/dL")
    lab_chol_post = FloatField("One-year postoperative cholesterol", description="mg/dL")
    lab_chol_diff = FloatField("difference value of cholesterol", description="mg/dL")
    lab_chol_per = FloatField("difference percentage of cholesterol", description="")
    lab_hemog_pre = FloatField("Preoperative hemoglobin", description="g/dL")
    lab_hemog_post = FloatField("One-year postoperative hemoglobin", description="g/dL")
    lab_hemog_diff = FloatField("difference value of hemoglobin", description="g/dL")
    lab_hemog_per = FloatField("difference percentage of hemoglobin", description="")
    lab_albumin_pre = FloatField("Preoperative albumin", description="g/dL")
    lab_albumin_post = FloatField("One-year postoperative albumin", description="g/dL")
    lab_albumin_diff = FloatField("difference value of albumin", description="g/dL")
    lab_albumin_per = FloatField("difference percentage of albumin", description="")
    lab_protein_pre = FloatField("Preoperative protein", description="g/dL")
    lab_protein_post = FloatField("One-year postoperative protein", description="g/dL")
    lab_protein_diff = FloatField("difference value of protein", description="g/dL")
    lab_protein_per = FloatField("difference percentage of protein", description="")

    nri_pre = FloatField("Preoperative nutritional risk index", description="")
    nri_post = FloatField("One-year postoperative nutritional risk index", description="")
    nri_diff = FloatField("difference value of nutritional risk index", description="")
    nri_per = FloatField("difference percentage of nutritional risk index", description="")

    fm_sfat_pre = FloatField("Preoperative subsutaneous fat area", description="cm{}".format('\u00B2'))
    fm_sfat_post = FloatField("One-year postoperative subsutaneous fat area", description="cm{}".format('\u00B2'))
    fm_sfat_diff = FloatField("difference value of subsutaneous fat area", description="cm{}".format('\u00B2'))
    fm_sfat_per = FloatField("difference percentage of subsutaneous fat area", description="")
    fm_vfat_pre = FloatField("Preoperative visceral fat area", description="cm{}".format('\u00B2'))
    fm_vfat_post = FloatField("One-year postoperative visceral fat area", description="cm{}".format('\u00B2'))
    fm_vfat_diff = FloatField("difference value of visceral fat area", description="cm{}".format('\u00B2'))
    fm_vfat_per = FloatField("difference percentage of visceral fat area", description="")

    fm_muscle_pre = FloatField("Preoperative skeletal muscle area", description="cm{}".format('\u00B2'))
    fm_muscle_post = FloatField("One-year postoperative skeletal muscle area", description="cm{}".format('\u00B2'))
    fm_muscle_diff = FloatField("difference value of skeletal muscle area", description="cm{}".format('\u00B2'))
    fm_muscle_per = FloatField("difference percentage of skeletal muscle area", description="")

    fm_muH_pre = FloatField("Preoperative skeletal muscle index adjusted with height{} (SMA/height{})".format('\u00B2', '\u00B2'), description="cm{}/m{}".format('\u00B2', '\u00B2'))
    fm_muH_post = FloatField("One-year postoperative skeletal muscle index adjusted with height{} (SMA/height{})".format('\u00B2', '\u00B2'), description="cm{}/m{}".format('\u00B2', '\u00B2'))
    fm_muH_diff = FloatField("difference value of skeletal muscle index adjusted with height{} (SMA/height{})".format('\u00B2', '\u00B2'), description="cm{}/m{}".format('\u00B2', '\u00B2'))
    fm_muH_per = FloatField("difference percentage of skeletal muscle index adjusted with height{}".format('\u00B2'), description="")

    fm_muBMI_pre = FloatField("Preoperative skeletal muscle index adjusted with BMI (SMA/BMI)", description="")
    fm_muBMI_post = FloatField("Postoperative 1-year skeletal muscle index adjusted with BMI (SMA/BMI)", description="")
    fm_muBMI_diff = FloatField("difference value of skeletal muscle index adjusted with BMI (SMA/BMI)", description="")
    fm_muBMI_per = FloatField("difference percentage of skeletal muscle index adjusted with BMI", description="")

    value_choices = [('0', 'No'), ('1', 'Yes')]
    si_tyop = SelectField("Type of surgery", choices=[('None', '-----'), ('0', 'Total gastrectomy'), ('1', 'Distal gastrectomy'), ('2', 'Other gastrectomy')])
    # si_tyan = SelectField("Type of anastomosis", choices=[('None', '-----'), ('0', 'Gastroduodenostomy'), ('1', 'Roux-en-Y gastrojejunostomy'), ('2', 'Gastrojejunostomy without jejunojejunostomy'), ('3', 'Gastrojejunostomy with jejunojejunostomy'), ('4', 'Total gastrectomy'), ('5', 'Billoth 1'), ('6', 'Others')])
    si_tyan = SelectField("Type of anastomosis", choices=[('None', '-----'), ('0', 'Gastroduodenostomy'), ('1', 'Roux-en-Y gastrojejunostomy'), ('2', 'Gastrojejunostomy without jejunojejunostomy'), ('3', 'Gastrojejunostomy with jejunojejunostomy'), ('4', 'Total gastrectomy'), ('6', 'Others')])
    si_cureintent = SelectField("Intent of treatment", choices=[('None', '-----'), ('0', 'Curative'), ('1', 'Palliative')])
    si_gasophis = SelectField("Past history of gastric surgery", choices=value_choices)
    si_esdhis = SelectField("Past history of endoscopic submucosal dissection", choices=value_choices)
    si_lapvsopen = SelectField("Operation method", choices=[('None', '-----'), ('0', 'Laparoscopy'), ('1', 'Open')])
    si_LND = SelectField("Lymph Node Dissection", choices=[('None', '-----'), ('0', 'Less than D2'), ('1', 'D2')])
    si_prm = FloatField("Proximal resection margin", description="cm")
    si_drm = FloatField("Distal resection margin", description="cm")

    cp_ajcc7 = SelectField("Cancer stage (AJCC7)", choices=[('None', '-----'), ('0', 'Ia'), ('1', 'Ib'), ('2', 'IIa'), ('3', 'IIb'), ('4', 'IIIa'), ('5', 'IIIb'), ('6', 'IIIc'), ('7', 'IV')])
    cp_tunum = SelectField("Number of tumors", choices=[('None', '-----'), ('0', 'One'), ('1', 'Multiple')])
    cp_tusize = FloatField("Tumor size", description="cm")
    cp_nometaln = FloatField("Number of metastatic lymph nodes", description="")
    cp_noretnl = FloatField("Number of retrieved lymph nodes", description="")
    cp_ene = SelectField("The extranodal extension of metastatic lymph node (pathological findings)", choices=[('None', '-----'), ('0', 'Negative'), ('1', 'Positive')])
    cp_dia = FloatField("Diameter of extranodal extension of metastatic lymph node", description="mm")
    cp_lvinv = SelectField("Lymphovascular invasion", choices=[('None', '-----'), ('0', 'Negative'), ('1', 'Positive')])
    cp_depthinv = SelectField("T stage", choices=[('None', '-----'), ('0', 'T1'), ('1', 'T2'), ('2', 'T3'), ('3', 'T4a'), ('4', 'T4b')])
    cp_nstage = SelectField("N stage", choices=[('None', '-----'), ('0', 'N0'), ('1', 'N1'), ('2', 'N2'), ('3', 'N3a'), ('4', 'N3b')])
    cp_perininv = SelectField("Perineural invasion", choices=[('None', '-----'), ('0', 'Negative'), ('1', 'Positive'), ('2', 'Not evaluated')])
    cp_agc = SelectField("Gross appearance of advanced gastric cancer (AGC)", choices=[('None', '-----'), ('0', 'Bormann type 1'), ('1', 'Bormann type 2'), ('2', 'Bormann type 3'), ('3', 'Bormann type 4'), ('4', 'Bormann type 5')])
    cp_egc = SelectField("Gross appearance of early gastric cancer (EGC)", choices=[('None', '-----'), ('0', 'Type I'), ('1', 'Type II'), ('2', 'Type III')])
    cp_path = SelectField("Tumor histology", choices=[('None', '-----'), ('0', 'Papillary adenocarcinoma'), ('1', 'Well-differentiated tubular adenocarcinoma'), ('2', 'Moderately-differentiated tubular adenocarcinoma'), ('3', 'Poorly-differentiated tubular adenocarcinoma'), ('4', 'Signet-ring cell carcionma'), ('5', 'Mucinous adenocarcioma'), ('6', 'Others')])
    cp_lauren = SelectField("Lauren Classification", choices=[('None', '-----'), ('0', 'Intestinal'), ('1', 'Diffuse'), ('2', 'Mixed'), ('3', 'Indeterminate')])

    # cp_tulongloc = SelectField("Tumor longitudinal location", choices=[('None', '-----'), ('0', 'upper'), ('1', 'middle'), ('2', 'lower')])
    cp_tulongloc_upper = SelectField("Upper third", choices=value_choices)
    cp_tulongloc_middle = SelectField("Middle third", choices=value_choices)
    cp_tulongloc_lower = SelectField("Lower third", choices=value_choices)

    cp_comorbidity = MultiCheckboxField("Comorbidity", choices=[('0', 'Diabete mellitus'), ('1', 'Hypertension'), ('2', 'Chronic active hepatitis'), ('3', 'Liver cirrhosis'), ('4', 'Tuberculosis'), ('5', 'Myocardial infarction'), ('6', 'Cerebrovascular accident'), ('7', 'Valvular heart disease'), ('8', 'Chronic obstructive pulmonarydisease'), ('9', 'Asthma'), ('10', 'Chronic renal failure')])

def function_calculate_diff_per(vPre, vPost):
    if vPre:
        vPre = float(vPre)
    if vPost:
        vPost = float(vPost)

    if (vPre and vPost):
        vDiff = vPost - vPre
        vPer = vDiff / vPre * 100
    else:
        vDiff = ''
        vPer = ''
    return vDiff, vPer

def function_calculate_BMI(vWeight, vHeight):
    if vWeight:
        vWeight = float(vWeight)
    if vHeight:
        vHeight = float(vHeight)

    vBMI = ''
    if (vWeight and vHeight):
        vBMI = vWeight / ((vHeight * 0.01)**2)
    return vBMI

def function_calculate_NRI(vAlbumin, vWeight_pre, vWeight_current):
    if vAlbumin:
        vAlbumin = float(vAlbumin)
    if vWeight_pre:
        vWeight_pre = float(vWeight_pre)
    if vWeight_current:
        vWeight_current = float(vWeight_current)

    vNRI = ''
    if (vAlbumin and vWeight_pre and vWeight_current):
        vNRI = (1.519 * 10 * vAlbumin) + 0.417 * (vWeight_current / vWeight_pre) * 100
    return vNRI

def function_calculate_muH(vMuscle, vHeight):
    if vMuscle:
        vMuscle = float(vMuscle)
    if vHeight:
        vHeight = float(vHeight)

    vmuH = ''
    if (vMuscle and vHeight):
        vmuH = vMuscle / ((vHeight * 0.01)**2)
    return vmuH

def function_calculate_muBMI(vMuscle, vBMI):
    if vMuscle:
        vMuscle = float(vMuscle)
    if vBMI:
        vBMI = float(vBMI)

    vmuBMI = ''
    if (vMuscle and vBMI):
        vmuBMI = vMuscle / vBMI
    return vmuBMI

def make_basic_data(form):
    age = request.form['age']
    gender = request.form['gender']
    phy_height = request.form['phy_height']
    phy_weight_pre = request.form['phy_weight_pre']
    phy_weight_post = request.form['phy_weight_post']
    form.phy_weight_diff.data, form.phy_weight_per.data = function_calculate_diff_per(phy_weight_pre, phy_weight_post)
    phy_weight_diff, phy_weight_per = form.phy_weight_diff.data, form.phy_weight_per.data
    lab_chol_pre = request.form['lab_chol_pre']
    lab_chol_post = request.form['lab_chol_post']
    form.lab_chol_diff.data, form.lab_chol_per.data = function_calculate_diff_per(lab_chol_pre, lab_chol_post)
    lab_chol_diff, lab_chol_per = form.lab_chol_diff.data, form.lab_chol_per.data
    lab_hemog_pre = request.form['lab_hemog_pre']
    lab_hemog_post = request.form['lab_hemog_post']
    form.lab_hemog_diff.data, form.lab_hemog_per.data = function_calculate_diff_per(lab_hemog_pre, lab_hemog_post)
    lab_hemog_diff, lab_hemog_per = form.lab_hemog_diff.data, form.lab_hemog_per.data
    lab_albumin_pre = request.form['lab_albumin_pre']
    lab_albumin_post = request.form['lab_albumin_post']
    form.lab_albumin_diff.data, form.lab_albumin_per.data = function_calculate_diff_per(lab_albumin_pre, lab_albumin_post)
    lab_albumin_diff, lab_albumin_per = form.lab_albumin_diff.data, form.lab_albumin_per.data
    lab_protein_pre = request.form['lab_protein_pre']
    lab_protein_post = request.form['lab_protein_post']
    form.lab_protein_diff.data, form.lab_protein_per.data = function_calculate_diff_per(lab_protein_pre, lab_protein_post)
    lab_protein_diff, lab_protein_per = form.lab_protein_diff.data, form.lab_protein_per.data

    ###=== BMI와 NRI는 수식을 통해 계산됨.
    form.phy_bmi_pre.data = function_calculate_BMI(phy_weight_pre, phy_height)
    form.phy_bmi_post.data = function_calculate_BMI(phy_weight_post, phy_height)
    phy_bmi_pre, phy_bmi_post = form.phy_bmi_pre.data, form.phy_bmi_post.data
    form.phy_bmi_diff.data, form.phy_bmi_per.data = function_calculate_diff_per(phy_bmi_pre, phy_bmi_post)
    phy_bmi_diff, phy_bmi_per = form.phy_bmi_diff.data, form.phy_bmi_per.data

    form.nri_pre.data = function_calculate_NRI(lab_albumin_pre, phy_weight_pre, phy_weight_pre)
    form.nri_post.data = function_calculate_NRI(lab_albumin_post, phy_weight_pre, phy_weight_post)
    nri_pre, nri_post = form.nri_pre.data, form.nri_post.data
    form.nri_diff.data, form.nri_per.data = function_calculate_diff_per(nri_pre, nri_post)
    nri_diff, nri_per = form.nri_diff.data, form.nri_per.data

    data_basic = np.concatenate([[age], [gender], [phy_bmi_pre], [phy_bmi_post], [phy_bmi_diff], [phy_bmi_per], [phy_height],
    [phy_weight_pre], [phy_weight_post], [phy_weight_diff], [phy_weight_per], [nri_pre], [nri_post], [nri_diff], [nri_per], 
    [lab_hemog_pre], [lab_hemog_post], [lab_hemog_diff], [lab_hemog_per], [lab_albumin_pre], [lab_albumin_post], [lab_albumin_diff], [lab_albumin_per], 
    [lab_protein_pre], [lab_protein_post], [lab_protein_diff], [lab_protein_per], [lab_chol_pre], [lab_chol_post], [lab_chol_diff], [lab_chol_per]])

    data_basic = np.asarray([np.NaN if data_basic[ii] == '' else data_basic[ii] for ii in range(0, len(data_basic))], dtype=np.float64)
    return data_basic

def make_ct_data(form):
    fm_sfat_pre = request.form['fm_sfat_pre']
    fm_sfat_post = request.form['fm_sfat_post']
    form.fm_sfat_diff.data, form.fm_sfat_per.data = function_calculate_diff_per(fm_sfat_pre, fm_sfat_post)
    fm_sfat_diff, fm_sfat_per = form.fm_sfat_diff.data, form.fm_sfat_per.data
    fm_vfat_pre = request.form['fm_vfat_pre']
    fm_vfat_post = request.form['fm_vfat_post']
    form.fm_vfat_diff.data, form.fm_vfat_per.data = function_calculate_diff_per(fm_vfat_pre, fm_vfat_post)
    fm_vfat_diff, fm_vfat_per = form.fm_vfat_diff.data, form.fm_vfat_per.data
    fm_muscle_pre = request.form['fm_muscle_pre']
    fm_muscle_post = request.form['fm_muscle_post']
    form.fm_muscle_diff.data, form.fm_muscle_per.data = function_calculate_diff_per(fm_muscle_pre, fm_muscle_post)
    fm_muscle_diff, fm_muscle_per = form.fm_muscle_diff.data, form.fm_muscle_per.data

    ###=== MuH와 MuBMI는 수식을 통해 계산됨.
    form.fm_muH_pre.data = function_calculate_muH(fm_muscle_pre, form.phy_height.data)
    form.fm_muH_post.data = function_calculate_muH(fm_muscle_post, form.phy_height.data)
    fm_muH_pre, fm_muH_post = form.fm_muH_pre.data, form.fm_muH_post.data
    form.fm_muH_diff.data, form.fm_muH_per.data = function_calculate_diff_per(fm_muH_pre, fm_muH_post)
    fm_muH_diff, fm_muH_per = form.fm_muH_diff.data, form.fm_muH_per.data

    form.fm_muBMI_pre.data = function_calculate_muBMI(fm_muscle_pre, form.phy_bmi_pre.data)
    form.fm_muBMI_post.data = function_calculate_muBMI(fm_muscle_post, form.phy_bmi_post.data)
    fm_muBMI_pre, fm_muBMI_post = form.fm_muBMI_pre.data, form.fm_muBMI_post.data
    form.fm_muBMI_diff.data, form.fm_muBMI_per.data = function_calculate_diff_per(fm_muBMI_pre, fm_muBMI_post)
    fm_muBMI_diff, fm_muBMI_per = form.fm_muBMI_diff.data, form.fm_muBMI_per.data

    data_ct = np.concatenate([[fm_sfat_pre], [fm_sfat_post], [fm_sfat_diff], [fm_sfat_per], 
    [fm_vfat_pre], [fm_vfat_post], [fm_vfat_diff], [fm_vfat_per], [fm_muscle_pre], [fm_muscle_post], [fm_muscle_diff], [fm_muscle_per],
    [fm_muH_pre], [fm_muH_post], [fm_muH_diff], [fm_muH_per], [fm_muBMI_pre], [fm_muBMI_post], [fm_muBMI_diff], [fm_muBMI_per]])

    data_ct = np.asarray([np.NaN if data_ct[ii] == '' else data_ct[ii] for ii in range(0, len(data_ct))], dtype=np.float64)
    return data_ct

def function_one_hot_encoding(arrValue, arrSize):
    arrData = np.zeros((arrSize))
    if arrValue != 'None':
        arrData[int(arrValue)] = 1
    return arrData

def make_onehot_data(form):
    cp_tusize = request.form['cp_tusize']
    cp_nometaln = request.form['cp_nometaln']
    cp_noretnl = request.form['cp_noretnl']
    cp_dia = request.form['cp_dia']
    si_prm = request.form['si_prm']
    si_drm = request.form['si_drm']
    cp_ajcc7 = request.form['cp_ajcc7']
    cp_depthinv = request.form['cp_depthinv']
    cp_nstage = request.form['cp_nstage']

    cp_tunum = request.form['cp_tunum']
    si_cureintent = request.form['si_cureintent']
    si_lapvsopen = request.form['si_lapvsopen']
    si_gasophis = request.form['si_gasophis']
    si_esdhis = request.form['si_esdhis']
    cp_lvinv = request.form['cp_lvinv']
    cp_perininv = request.form['cp_perininv']
    onehot_perininv = function_one_hot_encoding(cp_perininv, arrSize=3)
    cp_ene = request.form['cp_ene']

    si_tyop = request.form['si_tyop']
    onehot_tyop = function_one_hot_encoding(si_tyop, arrSize=3)

    si_tyan = request.form['si_tyan']
    onehot_tyan = function_one_hot_encoding(si_tyan, arrSize=7)
    si_LND = request.form['si_LND']

    cp_tulongloc_upper = request.form['cp_tulongloc_upper']
    cp_tulongloc_middle = request.form['cp_tulongloc_middle']
    cp_tulongloc_lower = request.form['cp_tulongloc_lower']
    onehot_tulongloc = np.array([cp_tulongloc_upper, cp_tulongloc_middle, cp_tulongloc_lower])

    cp_agc = request.form['cp_agc']
    onehot_agc = function_one_hot_encoding(cp_agc, arrSize=5)
    cp_egc = request.form['cp_egc']
    onehot_egc = function_one_hot_encoding(cp_egc, arrSize=3)
    cp_path = request.form['cp_path']
    onehot_path = function_one_hot_encoding(cp_path, arrSize=7)
    cp_lauren = request.form['cp_lauren']
    onehot_lauren = function_one_hot_encoding(cp_lauren, arrSize=4)

    cp_comorbidity = form.cp_comorbidity.data    
    onehot_comorbidity = np.zeros((11))
    for ii in range(0, len(cp_comorbidity)):
        onehot_comorbidity[int(cp_comorbidity[ii])] = 1
    
    data_numeric = np.concatenate([[cp_tusize], [cp_nometaln], [cp_noretnl], [cp_dia], [si_prm], [si_drm], [cp_ajcc7], [cp_depthinv], [cp_nstage]])

    data_onehot = np.concatenate([[cp_tunum], [si_cureintent], [si_lapvsopen], [si_gasophis], [si_esdhis], [cp_lvinv],
    onehot_perininv, [cp_ene], onehot_tyop, onehot_tyan, [si_LND], onehot_comorbidity, onehot_tulongloc, onehot_agc, onehot_egc, onehot_path, onehot_lauren])

    data_numeric = np.asarray([np.NaN if (data_numeric[ii] == '' or data_numeric[ii] == 'None') else data_numeric[ii] for ii in range(0, len(data_numeric))], dtype=np.float64)
    data_onehot = np.asarray([np.NaN if (data_onehot[ii] == '' or data_onehot[ii] == 'None') else data_onehot[ii] for ii in range(0, len(data_onehot))], dtype=np.float64)
    return data_numeric, data_onehot

def processResult():
    form = StomachCancerForm(request.form)

    if request.method == 'POST':
        # 각 feature별로 grouping 
        data_basic = make_basic_data(form)
        data_ct = make_ct_data(form)
        data_numeric, data_onehot = make_onehot_data(form)

        # create all dataset (sort model 순서대로)
        input_data = np.concatenate([data_basic, data_ct, data_numeric, data_onehot])

        # pre-processing (fill-up Nan & Normalization) -> calculate XGBoost model
        SavePath = './'
        vProb = func_ML_Extra_Eval(SavePath, input_data)
        print('============> prob: ', vProb)

        # result_view.html에서 소수점 2자리까지 보여줌
        for vData in form.data.items():
            if type(vData[1]) is float:
                form[vData[0]].data = round(form[vData[0]].data, 4)

        rate_mortality = round(vProb * 100, 4)



