# High-Throughput Screening of Piezoelectric Materials using Python

**Project Overview**
This project automates the high-throughput screening of **piezoelectric materials** using output files generated from VASP simulations.  
It extracts, cleans, and structures raw simulation data and computes key piezoelectric tensor properties to identify high-performance candidates for energy-harvesting applications.

**Skills Demonstrated**
- Data cleaning & preprocessing  
- Parsing unstructured VASP output files  
- Feature engineering  
- SQL-style data manipulation with Python (pandas)  
- Pipeline automation  
- Exploratory Data Analysis (EDA)  
- Data visualization (matplotlib / seaborn)  
- Materials informatics + scientific computing

**Project Structure**
```
pieozelectric_materials_screening
├──data/ # Raw & cleaned testcase datasets
├──notebooks/ # Preprocessing, Postprocessing and Visualization of results
├──scripts/ # Parsing & processing scripts
├──results_main/ # Final outputs and figures of complete dataset
├──results_testcase/ # Results CSVs of sample testcases
├──config.yaml
└──README.md
```

**Key Results**
- Processed **~3000** materials and extracted piezoelectric tensor for **75%** of them
- Extracted complete piezoelectric tensors from simulation outputs
- Computed key metrics (norm value of tensors, e_ij tensors)
- Identified **top 10** high-performance materials
- Found strong correlations between crystal symmetry and piezoelectric response