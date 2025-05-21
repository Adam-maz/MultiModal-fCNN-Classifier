# fCNN – Multimodal Neural Network Bioactivity Classifier

This repository presents the project **"fCNN – multimodal neural network bioactivity classifier, based on Morgan fingerprints and images of simulated (Docking, DFT) molecules."**

As part of this work, we developed a multimodal ligand bioactivity classifier targeting the 5-HT6R receptor. The model combines two types of molecular representations: Morgan fingerprints and images of ligands generated after simulation with **Maestro Schrödinger** (docking and DFT geometry optimization).  
This hybrid approach combines the predictive strength of fingerprints with the generalization ability of image-based inputs, resulting in a more robust binary classifier that performs well even with relatively small datasets.

To allow users to run the model locally, we provide a script that launches one of the four pre-trained models.  
Additionally, we offer a **plugin for Maestro Schrödinger** to automate the process of selecting molecules and generating screenshots for use with the model.

---

## 📁 Repository Contents

- **Compatibility_versions.txt** — describes compatible versions of required libraries/frameworks  
- **ChEMBL_Parser.ipynb** — notebook for parsing ligands from the ChEMBL database  
- **Spreadsheet_script** — script that generates a `.csv` file containing the "Entry ID" of the best-scoring conformer (based on Docking Score or State Penalty) per ligand  
- **fCNN_Maestro_Plugin/** — plugin for Maestro that automates molecule selection and screenshot capturing  
- **fCNN_launching_dir/** — directory containing example files (images and SMILES of two example ligands) and pre-trained models in the `trained_models/` subfolder  
- **CNN_notebook.ipynb** — notebook implementing the CNN-based model using images  
- **Fingerprints_notebook.ipynb** — notebook implementing the fingerprint-based model  
- **fCNN_MultiModal_Classifier.ipynb** — notebook combining both modalities (fingerprints + images)  
- **fCNN_launcher.ipynb** — script for launching the trained model on new data

---

## 🧪 Manual

### a) Installing and Running the Maestro Plugin

1. In Maestro, go to the **Scripts** tab and choose **Install**
2. Select the folder containing the plugin, confirm installation
3. After installation, the plugin will be visible in the Scripts panel  
   The plugin contains two modules:
   - **Module 1** – selects ligands with the lowest Docking Score or State Penalty. Requires a `.csv` file containing the "Entry ID" values for the best conformers
   - **Module 2** – generates molecule images (screenshots)

### b) Running the Classifier

To use the `fCNN_launcher.ipynb` script:

1. Place the notebook in the same folder as:
   - The `.joblib` file (a trained model)
   - A `.csv` file containing SMILES strings of the compounds to classify
2. In cell 5 of the notebook (the image loading step), provide the path to the folder containing subfolders with molecule images

---

## 🔗 Download Trained Models and Datasets

The following models and datasets are too large for GitHub (>50MB), so we provide them via **Google Drive**.  
> Content:
- [`CNN_docking_model_with_fps_architecture_I.joblib`](https://drive.google.com/uc?export=download&id=1yRvpoXy-rWkkOanDVh_lElgbVpl-9Yop)
- [`CNN_quanta_model_with_fps_architecture_I.joblib`](https://drive.google.com/uc?export=download&id=1laCxwhyFIoL4OQc5woNWkvESPL7hWRGR)
- [`CNN_docking_model_with_fps_architecture_II.joblib`](https://drive.google.com/uc?export=download&id=1f4SlOxRQHCDQiCXcJ-nJqoauLLmxows8)
- [`CNN_quanta_model_with_fps_architecture_II.joblib`](https://drive.google.com/uc?export=download&id=1kJoNoc_p4cGq4OsWfmK6xjgQSr5B5eK1)
- [`images_docking_dataset`](https://drive.google.com/drive/folders/1WUnSwanPpYyr6kFXQ8_V7coV-05ElDXI?usp=sharing)
- [`images_docking_dataset`](https://drive.google.com/drive/folders/1UUdqdmCkI5IUQm47YODi9390a9fiM45P?usp=sharing)    
---

## 📌 Notes

- The plugin and models were tested with specific versions of Maestro and Python packages. See `Compatibility_versions.txt` for more details.
- The example files provided in `fCNN_launching_dir/` can be used to test the pipeline end-to-end.
