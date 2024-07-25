import os
import pandas as pd
from radiomics import featureextractor, getFeatureClasses
folder_path_1 = r"E:\label-data\niigz\zhongzheng\zhongzheng"
folder_path_2 = r"E:\label-data\niigz\zhongzheng\zhong-label"

files = os.listdir(folder_path_1)

combined_df = pd.DataFrame()
for file in files:
    nrrd_array = file

    if file.endswith("_0000.nii.gz"):

        label_nrrd_array = file.replace("_0000.nii.gz", ".nii.gz")

        nrrd_array = "E:\label-data\\niigz\zhongzheng\zhongzheng\\"  + nrrd_array
        label_nrrd_array = "E:\label-data\\niigz\zhongzheng\zhong-label\\"  + label_nrrd_array
        print(label_nrrd_array,"\n",nrrd_array)


        settings = {}
        settings['binWidth'] = 25
        settings['resampledPixelSpacing'] = [1, 1, 1]
        params_file_path = "exampleCT.yaml"
        extractor = featureextractor.RadiomicsFeatureExtractor(params_file_path)#
        try:
            feature_1 = extractor.execute(nrrd_array, label_nrrd_array, voxelBased=False)
        except:
            continue
        pass

        featureA = pd.DataFrame([feature_1])
        featureA.insert(0, 'index', file)

        combined_df = combined_df.append(featureA, ignore_index=True)
        print(file, "Over！！")


combined_df.to_csv('重症.csv', index=False)