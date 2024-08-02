# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import sys
from batteryml.pipeline import Pipeline
from batteryml.visualization.plot_helper import plot_capacity_degradation, plot_cycle_attribute, plot_result

# Create a pipeline with a configuration file,
# specifying the device and workspace.
# Developers need to modify the data, feature, model and other related settings in the config file in advance.
pipeline = Pipeline(
    config_path='configs/baselines/sklearn/variance_model/matr_1.yaml',
    workspace='workspaces'
)
model, dataset = pipeline.train(device='cuda', skip_if_executed=False)
model, dataset = pipeline.train(device='cpu', skip_if_executed=False)