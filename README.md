# Gastric_Cancer_Survival

***Paper***  
Prognostic AI Model to predict Five-year survival at One-Year after Gastric cancer Surgery based on nutrition and body morphometry.

***Abstract***  
***Background***:    
Personalized survival prediction is important in gastric cancer patients after gastrectomy based on large datasets with many variables including time-varying factors in nutrition and body morphometry. One-year after gastrectomy might be the optimal timing to predict long-term survival. We aimed to develop a personalized prognostic artificial intelligence (AI) model to predict five-year survival at one-year after gastrectomy.    

***Methods***:    
From a prospectively built gastric surgery registry from a tertiary hospital, 4,025 gastric cancer patients treated gastrectomy and survived more than a year were selected. Eighty-nine variables including clinical and derived time-varying variables were used as input variables. We proposed a multi-tree extreme gradient boosting (XGBoost) algorithm, an ensemble AI algorithm based on 100 datasets derived from repeated 5-fold cross-validation. Internal validation was performed in split datasets (n=1,121) by comparing our proposed model and six other AI algorithms. External validation was performed in patients in other hospital (n=590). We performed a sensitivity analysis to analyze the effect of the nutritional and fat/muscle indices using a leave-one-out method.    

***Results***::     
In the internal validation, our proposed model showed AUROC of 0.8237, which outperformed the other AI algorithms (0.7988 – 0.8165), 80.00% sensitivity, 72.34% specificity, and 76.17% balanced accuracy. In the external validation, our model showed AUROC of 0.8903, 86.96% sensitivity, 74.60% specificity, and 80.78% balanced accuracy. Sensitivity analysis demonstrated that the nutritional and fat/muscle indices influenced the balanced accuracy by 0.31% and 6.29% in the internal and external validation set, respectively. Our developed AI model was published on a website for personalized survival prediction.    

***Conclusions***:    
Our proposed AI model provides substantially good performance in predicting five-year survival at one-year after gastric cancer surgery.   

