# LogicerrorRepair

## Overview

LogicerrorRepair is a sophisticated machine learning system designed to localize and correct logic errors in code. It leverages state-of-the-art techniques, including graph neural networks and pseudocode analysis, to improve the accuracy of automated program repair. This repository includes scripts for data preparation, model training, and evaluation, reflecting the comprehensive methodology discussed in "Logic Error Localization and Correction with Machine Learning."

## Getting Started

### Prerequisites

- Linux or macOS
- Python 3.6+
- Conda environment

### Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/Arrtourz/LogicerrorRepair
cd LogicerrorRepair
```

### Setting Up the Environment

To set up the required environment, follow these steps:

```bash
conda create -n DrRepair python=3.6
conda activate DrRepair
# Install required Python packages
```

### Data Preparation

To download and prepare the raw and preprocessed data:

```bash
# Download raw data
sh download_raw_data.sh

# Download preprocessed data
sh download_preprocessed_data.sh
```

### Training Models

To train the models on the prepared data:

```bash
# Train on DeepFix dataset
sh model/run_deepfix.sh

# Train on SPOC dataset
sh model/run_spoc.sh
```

### Evaluation and Testing

To evaluate the models and start the server for testing:

```bash
# Evaluate and test DeepFix model
sh model/server.sh

# Evaluate and test SPOC model
# Similar to above, adjust the script for SPOC evaluation
```

To properly cite the paper associated with your GitHub repository in the README, you can add a "References" section at the end. Here is how you could format it:

---

## References

Xu, Z., Sheng, V. S., & Lu, K. (2023). Logic Error Localization and Correction with Machine Learning (Student Abstract). Proceedings of the AAAI Conference on Artificial Intelligence, 37(13), 16372-16373. [https://doi.org/10.1609/aaai.v37i13.27046](https://doi.org/10.1609/aaai.v37i13.27046)

---

This citation provides readers with the source of the academic foundation and insights that guided the development of your project.

## License

This project is released under the MIT License. See the LICENSE file for more details.

---
