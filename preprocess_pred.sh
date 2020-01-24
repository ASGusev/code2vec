DATASET_NAME=my_dataset
HISTOGRAM_DATASET_NAME=my_dataset
mkdir convert_data/$DATASET_NAME
python3 ./preprocess_pred.py --raw_data ${DATASET_NAME}.raw.txt --raw_names ${DATASET_NAME}.raw.names.txt -mc 300 -wvs 500000 -pvs 500000 -tvs 500000 -wh data/$HISTOGRAM_DATASET_NAME/${HISTOGRAM_DATASET_NAME}.histo.ori.c2v -ph data/$HISTOGRAM_DATASET_NAME/${HISTOGRAM_DATASET_NAME}.histo.path.c2v -th data/$HISTOGRAM_DATASET_NAME/${HISTOGRAM_DATASET_NAME}.histo.path.c2v -o convert_data/$DATASET_NAME/$DATASET_NAME
