# NLEIS-Ferri-Ferrocyanide-Modelling [<a href="https://doi.org/10.5281/zenodo.18452317"><img src="https://zenodo.org/badge/1138793657.svg" alt="DOI"></a>](https://doi.org/10.5281/zenodo.20132086)
### **Repository Author:** Lauren A. Frank
This repository contains the supplementary materials for the paper: **Second Harmonic Nonlinear Warburg Admittance Analysis Eliminates Information Loss from Linearization in Traditional EIS: Theory and Experimental Validation** by Frank et al. 2026. This includes all of the code used to create the paper's Figures and its associated model derivations.
* 📓 [Tutorial - Supplementary Theory (SymPy harmonic series expansions)](jupyter/Theory%20Derivations/Tutorial_Supplementary_SympyHarmonicExpansions.ipynb) - mathematical derivations of current $\tilde{\mathrm{I}}_{\mathrm{j}}$ and $h_j$(∆E) up to N-th order; evaluation of modulation-potential-dependent surface concentration coefficients ($C_j^{s,II}$ and $C_j^{s,III}$).
* 📓 [Processing Data Notebook](jupyter/Processed%20Data/preprocessing_data.ipynb) - processing of raw input voltages and output currents (i.e. instrument scaling factor, vector rotations, first harmonic capacitive corrections); results saved to `preprocessed_data_final.csv`

### ★ How to Cite:
**Publication**
> Frank, L. A., Babauta, J. T., & Schwartz, D. T. *Second Harmonic Nonlinear Warburg Admittance Analysis Eliminates Information Loss from Linearization in Traditional EIS: Theory and Experimental Validation.* **Analytical Chemistry** (2026). https://doi.org/10.1021/acs.analchem.6c01245

**GitHub (latest version; concept DOI)**
>Frank, L. A. *NLEIS-Ferri-Ferrocyanide-Modelling.* Zenodo (2026). https://doi.org/10.5281/zenodo.18452317

## Abstract
**Authors – Lauren A. Frank¹, Jerome T. Babauta², Daniel T. Schwartz¹**  
¹*Department of Chemical Engineering and Clean Energy Institute, University of Washington*  
²*Gamry Instruments, Inc.*

Low frequency impedance or admittance experiments of reversible redox couples in well-supported quiescent electrolyte are normally analyzed using a linearized semi-infinite Warburg element with a single lumped parameter. Because each species of a redox couple has a distinct diffusivity, one cannot determine individual diffusivities by fitting a spectrum with one parameter; linearization causes information loss. Weakly nonlinear theory and experiments presented here extend traditional Warburg admittance analysis to the higher harmonic currents generated from single-sine potential modulations at a Pt electrode in well-supported ferri-/ferro-cyanide electrolyte. Complex harmonic current data from our commercial instrument is processed to enable direct fitting of theory to measurements. We show that complex first and second harmonic currents are measurable for ∆E ≥ 5 $mV_{RMS}$, whereas a good compromise between experimental signal-quality and leading-order model accuracy is found at ∆E ≈ 10 $mV_{RMS}$. Higher-order corrections to theory are required at larger potential modulation amplitudes to remove amplitude-dependency from fits, until $\frac{∆E*F}{RT}$ > 1, when weakly nonlinear theory breaks down. Fitting the first and second harmonic experimental signals to theory provides the mean diffusivity and a diffusion asymmetry parameter (deviations from mean), respectively, enabling unique determination of the individual ferricyanide and ferrocyanide diffusivities. Theory also shows that even harmonics disappear in the high-symmetry case of equal species diffusivities. In short, analyzing the first and second harmonics generated with moderate amplitude modulations eliminates information loss from linear Warburg analysis of the first harmonic alone.  

## Installation
Required Dependencies w/ Versions Used:
* Python (3.11.14)
* SciPy (1.16.3)
* NumPy (2.4.0)
* Matplotlib (3.10.7)
* Pandas (2.3.3)
* Sympy (1.14.0)

The conda environment used for this work can be recreated with the following commands:
* `conda env create -f environment.yml`
* `conda activate FerriFerroExp`

## Folders
* `Raw Data - FeCN platinum 8`: contains the raw .DTA file outputs from a Gamry Interface 1010E potentiostat for RMS potential modulations of 1 mV, 5 mV, 10 mV, 20 mV, 50 mV, and 100 mV. Files ending in 1 are associated with the Run (or replicate) 1 and those ending in 2 are Run 2.
* `jupyter`:
  * `Figures`: contains the jupyter notebooks used to generate the Figures in the paper and supplementary materials, along with their .pdf images.
  * `Processed Data`: contains the jupyter notebook `preprocessing_data.ipynb` used to preprocess the raw data from the `Raw Data - FeCN platinum 8` folder into the file `preprocessed_data_final.csv`, according to the methods described in the paper. This .csv file was used to create all the resulting Figures.
  * `Theory Derivations`: contains the jupyter notebook `Tutorial_Supplementary_SympyHarmonicExpansions.ipynb` used to mathematically derive the ordered-models for the first and second harmonic current and admittances.

## Repository Structutre
```bash
├── Raw Data - FeCN platinum 8
│   ├── CV3.DTA
│   ├── EISPOT_fcn_100mV_1.DTA
│   ├── EISPOT_fcn_100mV_2.DTA
│   ├── EISPOT_fcn_10mV_1.DTA
│   ├── EISPOT_fcn_10mV_2.DTA
│   ├── EISPOT_fcn_1mV_1.DTA
│   ├── EISPOT_fcn_1mV_2.DTA
│   ├── EISPOT_fcn_20mV_1.DTA
│   ├── EISPOT_fcn_20mV_2.DTA
│   ├── EISPOT_fcn_50mV_1.DTA
│   ├── EISPOT_fcn_50mV_2.DTA
│   ├── EISPOT_fcn_5mV_1.DTA
│   ├── EISPOT_fcn_5mV_2.DTA
│   └── OCP3.DTA
├── environment.yml
└── jupyter
    ├── .DS_Store
    ├── Figures
    │   ├── .DS_Store
    │   ├── Cyclic Voltamagram
    │   │   ├── Cover_art_CV.pdf
    │   │   ├── Figure1_Pt_Cycle3_CV.pdf
    │   │   └── cyclic_volt_plot.ipynb
    │   ├── Frequency Normalized Current Magnitudes
    │   │   ├── Figure4_Freq_Normalized_Current_Magnitudes.pdf
    │   │   └── Frequency_Normalized_Current_Plot.ipynb
    │   ├── Harmonic Growth
    │   │   ├── Figure3_Harmonic_Growth_0.3004808_Hz_Run1.pdf
    │   │   ├── Harmonic_Growth_Plot.ipynb
    │   │   ├── S6_Harmonic_Growth_All_Frequencies_Run1.pdf
    │   │   └── S7_Harmonic_Growth_All_Frequencies_Run2.pdf
    │   ├── Nonlinearly Corrected Admittances
    │   │   ├── Corrected_Admittance_Plots.ipynb
    │   │   ├── Figure5_A1_Plot_Run1.pdf
    │   │   ├── Figure6_A2_Plot_Run1.pdf
    │   │   ├── S8_A1_Plot_Run2.pdf
    │   │   └── S9_A2_Plot_Run2.pdf
    │   ├── Rotation and Processed Currents
    │   │   ├── Rotation_and_Processed_Plots.ipynb
    │   │   ├── S1_First_Harmonic_Rot_Proc_Current_Comparison.pdf
    │   │   ├── S3_First_Harmonic_2nd_Order_Admittance_all_Freq.pdf
    │   │   ├── S4_First_Harmonic_2nd_Order_Admittance_Near_Origin.pdf
    │   │   └── S5_Second_Harmonic_2nd_Order_Admittance_Near_Origin.pdf
    │   └── Signal Analysis
    │       ├── Cover_art_signal_analysis.pdf
    │       ├── Figure2_Processed_Current_Signal_Analysis.pdf
    │       ├── S2_Processed_Voltage_Signal_Analysis.pdf
    │       └── Signal_Analysis_Plot.ipynb
    ├── Processed Data
    │   ├── preprocessed_data_final.csv
    │   ├── preprocessed_data_final_units.csv
    │   ├── preprocessing_data.ipynb
    │   ├── rotated_data_noCdl.csv
    │   ├── rotated_data_noCdl_units.csv
    │   └── unprocessed_data_modFactor.csv
    │   └── unprocessed_data_modFactor_units.csv
    └── Theory Derivations
        ├── Tutorial_Supplementary_SympyHarmonicExpansions.ipynb
        ├── sixth_order_filtered_terms.json
        └── sixth_order_script.py
```
