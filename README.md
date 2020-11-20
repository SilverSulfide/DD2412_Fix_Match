# DD2412_fixmatch
DD2412 final project repository by markuz@kth.se &amp; amper@kth.se

## Note

Some of the code present in this repository has been adapted from [https://github.com/google-research/fixmatch]()
and [https://github.com/LeeDoYup/FixMatch-pytorch](). This has been appropriately indicated in the code.

## Requirements
Pytorch 1.6.0 with CUDA enabled

## Installation
```
git clone https://github.com/SilverSulfide/DD2412_Fix_Match.git
```
```
pip install -r requirements.txt
```

## Training
Training hyperparemeters can be adjusted in the **config.yaml** file.

### Basic training call
```
python train.py -hp path/to/config 
```
### Optional arguments
```
--save_dir path/to/save_location
--save_name name of the experiment
--resume enables resuming from checkpoint
--load_path path/to/checkpoint
--overwrite overwrite existing experiment with the same name
--seed 
```

### Experiment arguments

These arguments concern modifications to weak augmentation.
By default flip and crop are enabled. 
To adjust the strength of the transformations edit the functions in **ssl_dataset.py**.

```
-tr --translate Adds translation transform to weak augment
-n --noise Adds noise transform to weak augment
-c --contrast Adds contrast transform to weak augment
```

## Plotting

**plot_results.py** plots the training loss and test accuracies for a given experiment.
This function is hardcoded for our results (i.e. our data structure) and needs to be modified for general use.
