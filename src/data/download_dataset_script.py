import pandas as pd
import urllib.request
import os

# Download the data
url = 'https://dataalchemist4593424263.blob.core.windows.net/azureml-blobstore-ce610cc6-35e1-4d2d-b762-f188ac1230dc/airlines.dat?sp=r&st=2023-04-25T13:13:01Z&se=2023-04-25T21:13:01Z&spr=https&sv=2021-12-02&sr=b&sig=HVwC3mrlEps4C7O3A07CQe2kzxRkk1G6dr%2BANC8f5ZM%3D'
local_file_name = '\PASD\PredictingFlightDelays\src\data/airlines.dat'
if not os.path.exists("\PASD\PredictingFlightDelays\src\data"):
    os.makedirs("\PASD\PredictingFlightDelays\src\data")
urllib.request.urlretrieve(url, local_file_name)

df = pd.read_csv(url)
print(df.head())