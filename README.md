# DD2412_Fix_Match
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
python train.py -hp path/to/config.yaml
```
### Optional arguments
More thorough descriptions can be found at the end of **train.py**.
```
--save_dir path/to/save_location
--save_name Name of the experiment
--resume Enables resuming from checkpoint
--load_path path/to/checkpoint
--overwrite Overwrite existing experiment in the same save dir
--seed 0,1,2 ...
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

## Evaluation

**eval.py** script is provided to report final or best accuracy of a checkpoint

### Basic call
```
python eval.py --load_path path/to/checkpoint.pth -hp path/to/config.yaml
```

### Optional arguments
More thorough descriptions can be found at the end of **eval.py**.
```
--batch_size Add evaluation batch size that is differs from the config
--use_train_model Uses training model, instead of EMA evaluation model
-tr --translate Add translate test images
-n --noise Add noise to test images
-c --contrast Add contrast to test images
```

## Plotting

**plot_results.py** plots the training loss and test accuracies from the logs of a given experiment.
This function is hardcoded for our results (i.e. our data structure) and needs to be modified for general use.
