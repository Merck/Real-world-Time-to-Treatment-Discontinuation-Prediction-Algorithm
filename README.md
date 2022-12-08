# Real-world Time to Treatment Discontinuation Prediction

This is the code repository for Real-world Time to Treatment Discontinuation Prediction research project. The code reproduces the result in the paper "A machine learning approach to real-world time to treatment discontinuation prediction" accepted in the Journal of Advanced Intelligent Systems. https://doi.org/10.22541/au.166065465.59798123/v1

Authors: Weilin Meng, Xinyuan Zhang, Boshu Ru, Yuanfang Guan

Copyright © 2022 Merck & Co., Inc., Rahway, NJ, USA and its affiliates. All rights reserved.

Last updated: 11/29/2022


## 1 Dependency 
R 4.1.3
    library("survival")
    library("timeROC")
    library("Bolstad2")
    library("ROCR")
python 3.9
    scikit-learn
    keras
    tensorflow


## 2 Structure of code
|_ single_population #single homogeneous population rwToT validation with lightgbm as base learner
    |_ delta # test the effect of termination rate
    |_ delta_direct_aggregation # test the performance without propagation
    |_ simulate_new_feature_example_fixed # test the effect of feature number and example number
    |_ simulate_new_noise_example_fixed # test the effect of noise level and example number
    |_ simulate_scaling # test the effect of feature scaling
    |_ simulation_noisefactor_feature # test the effect of noise level and feature number

|_ single_population_dl #single homogeneous population rwToT validation with deep learning as base learner
    |_ delta
    |_ delta_direct_aggregation
    |_ simulate_new_feature_example_fixed
    |_ simulate_new_noise_example_fixed
    |_ simulate_scaling
    |_ simulation_noisefactor_feature
 
|_ single_population_linear  #single homogeneous population rwToT validation with linear regression as base learner
    |_ delta
    |_ delta_direct_aggregation
    |_ simulate_new_feature_example_fixed
    |_ simulate_new_noise_example_fixed
    |_ simulate_scaling
    |_ simulation_noisefactor_feature

|_ single_population_svm #single homogeneous population rwToT validation with SVM as base learner
    |_ delta
    |_ delta_direct_aggregation
    |_ simulate_new_feature_example_fixed
    |_ simulate_new_noise_example_fixed
    |_ simulate_scaling
    |_ simulation_noisefactor_feature

|_ two population # two/heterogeneous population rwToT validation with lightGBM as base learner
    |_ two_population_delta # test of the differences in termination rate
    |_ two_population_example # test the difference in training and test examples
    |_ two_population_noise # test the difference in feature noise levels
    |_ two_population_scaling # test the difference in feature scaling.


## 3 Running the code
In each of the above subdirectory, there is a base directory and a simulate_all.sh file.
The base directory contains the basic code to test each of the above parameters.
The simulate_all.sh file is the executable that test over a bunch of parameters.
Under each base directory:
|_ simulate.py # simulate the data that follows the distribution to be tested.
    when testing with your own data, please replace the datamatrix from simulate.py
|_ bash.sh # runs through a single cross-validation fold
|_ bash_all.sh # runs through five cross-validations
|_ python3 split.py # split data set into train and test
|_ guanrank.pl # calculate the ranking value in training set
|_ guanrank_time.pl # calculate the future time value for each ranked value
|_ prepare_train.pl # prepare training dataset, test dataset and validation dataset using the estimated future time
|_ train.py # train and interpolate prediction results


## 4 License

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS,WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
