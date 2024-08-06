import sys
from batteryml.pipeline import Pipeline
from batteryml.visualization.plot_helper import plot_capacity_degradation, plot_cycle_attribute, plot_result

# ------ Basic Usage Of BatteryML Pipeline ------
# Create a pipeline with a configuration file, specifying the device and workspace.
# Developers need to modify the data, feature, model and other related settings in the config file in advance.
pipeline = Pipeline(
    config_path='configs/baselines/sklearn/variance_model/matr_.yaml',
    workspace='workspaces'
)

## Train and evaluate
# model, dataset = pipeline.train(device='cuda', skip_if_executed=False)
model, dataset = pipeline.train(device='cpu', skip_if_executed=False)