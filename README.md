# Identifying-Severe-Community-Acquired-Pneumonia-Using-Radiomics-and-Clinical-Data

This warehouse stores the main process and key code of experiments in the paper. 
The overall process of the paper is as follows:

1. Medical image segmentation based on nnU-Net model
2. Medical image feature extraction based on Pyradiomics
3. Construction of clinical feature set, imaging feature set and mixed feature set
4. Feature screening process
5. Machine learning modeling
6. Model interpretability analysis based on SHAP method


Each process is described in detail below

------

#### Medical image segmentation based on nnU-Net model
nnU-Net is a fully automatic segmentation framework that can complete image segmentation without special processing by the user. For details, please refer to the warehouse: https://github.com/MIC-DKFZ/nnUNet 
It describes in detail the various storage locations of data set files

#### Medical image feature extraction based on Pyradiomics
Feature extraction using Pyradiomics requires downloading the toolkit from a third-party library https://github.com/AIM-Harvard/pyradiomics

After the download is complete, you can refer to the official sample code, or use ours
