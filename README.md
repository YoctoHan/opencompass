# OpenCompass Model Evaluation
This repository contains a customized version of OpenCompass 0.4.2, tailored for model evaluation in our specific business scenarios.

## Overview
This project provides a comprehensive framework for evaluating language models using OpenCompass, with custom configurations and datasets relevant to our business use cases. The evaluation environment is containerized using Docker to ensure consistency and reproducibility.

## Prerequisites
* Docker with GPU support
* Git
* NVIDIA GPU drivers
* Sufficient disk space for models and datasets
## Getting Started
### 1. Clone the Repository
```bash
git clone git@github.com:YoctoHan/opencompass.git
cd opencompass
```
### 2. Build the Docker Image
Navigate to the docker directory and build the evaluation environment:

```bash
cd docker
docker build -t aix-opencompass-eval-250524:latest .
```
### 3. Launch the Container
Use the provided script to create and start a new container:
```bash
cd ../scripts
./launch_container.sh
```
This script will:

* Create a new container with GPU support
* Mount the parent directory as a workspace
* Set up the necessary network configurations
* Activate the pre-configured OpenCompass environment
### 4. Prepare Datasets
Once inside the container, run the data preparation script:

```bash
./workspace/scripts/prepare_data.sh
```
This script will download and organize all required datasets for evaluation.

### 5. Run Evaluations
After data preparation is complete, you're ready to start model evaluations. The OpenCompass environment is pre-configured and activated by default.

Example evaluation command:

```bash
python run.py evaluations/eval_aixcoder_debug.py
```
## Project Structure

```
opencompass/
├── docker/           # Docker configuration files
├── scripts/          # Utility scripts
├── configs/          # Evaluation configurations
├── data/             # Dataset storage (created after preparation)
├── outputs/          # Evaluation results
└── evaluations/      # Evaluation scripts
```
## Environment Details
* Base Image: PyTorch 2.6.0 with CUDA 12.6 and cuDNN 9
* Python Version: 3.10
* OpenCompass Version: 0.4.2
* Pre-configured proxy settings for package installation
## Support
* For questions or issues related to this evaluation framework, please open an issue in the repository.

## License
* This project follows the licensing terms of the original OpenCompass project. Please refer to the LICENSE file for more details.

