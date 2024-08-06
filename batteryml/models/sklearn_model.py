# Licensed under the MIT License.
# Copyright (c) Microsoft Corporation.

import abc
import torch
import pickle
import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd

from batteryml.data.databundle import DataBundle

from .base import BaseModel


class SklearnModel(BaseModel, abc.ABC):
    def fit(self, dataset: DataBundle, timestamp: str = None) -> None:
        device = dataset.device
        dataset = dataset.to('cpu')
        feature = dataset.train_data.feature
        feature = feature.view(len(feature), -1)
        self.model.fit(feature, dataset.train_data.label.to('cpu'))

        timestamp = timestamp or 'UnknownTime'

        # Dump models
        if self.workspace is not None:
            filename = self.workspace / f'{timestamp}.ckpt'
            self.dump_checkpoint(filename)
            self.link_latest_checkpoint(filename)

        dataset = dataset.to(device)

    def predict(self, dataset: DataBundle, data_type: str='test') -> torch.Tensor:
        device = dataset.device
        dataset = dataset.to('cpu')
        if data_type == 'test':
            feature = dataset.test_data.feature
        else:
            feature = dataset.train_data.feature
        feature = feature.view(len(feature), -1)
        scores = self.model.predict(feature.numpy())

        scores = torch.from_numpy(scores).to(device).view(-1)
        dataset = dataset.to(device)
        return scores

    def dump_checkpoint(self, path: str):
        # with open(path, 'wb') as fout:
        #     pickle.dump(self.model, fout)
        # Convert model parameters to a dictionary
        model_params = {k: v.numpy() for k, v in self.model.state_dict().items()}

        # Convert dictionary to DataFrame
        df = pd.DataFrame({k: [v] for k, v in model_params.items()})

        # Save DataFrame to Parquet file
        table = pa.Table.from_pandas(df)
        pq.write_table(table, path)

    def load_checkpoint(self, path: str):
        # with open(path, 'rb') as fin:
        #     self.model = pickle.load(fin)
        # Read Parquet file into DataFrame
        table = pq.read_table(path)
        df = table.to_pandas()

        # Convert DataFrame back to dictionary
        model_params = {k: torch.tensor(v[0]) for k, v in df.items()}

        # Load parameters into model
        self.model.load_state_dict(model_params)
