import kaggle 

kaggle.api.authenticate()

kaggle.api.dataset_download_files('djordjejov/serbian-real-estate-dataset', path='data/raw', unzip=True)



