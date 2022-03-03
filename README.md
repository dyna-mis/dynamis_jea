## JEA_RCR Test
<ol>
<li>download the main branch </li>
<li>change current working directory : cd dynamis_jea </li>
<li>compile the C++ code in the main branch (see detailed instruction below) </li>
<li>run experiments: run test.sh (which run experiments on benchmarks in folder INPUT and store results in folder OUTPUT as json files.)</li>
<li>download the branch dynamis_jea_plots besides the main branch, as the following structure below</li>
<li>change current working directory : cd ../dynamis_jea_plots </li>
<li> install requirements.txt</li>
<li>generate plots: run plotting.sh</li>
<li>compare generated plots with figures in paper (see Evaluation below)</li>

```
evaluation project
│     
│
└───dynamis_jea 
│   │   test.sh
│   │  
│   │
│   └───OUTPUT
│    
│   
└───dynamis_jea_plots
    │   plotting.sh          
    │  
    │
    └───E*(-Rect)

```  


  

</ol>

# Branch Main (main code)

## Requirements 
(check the CMakeLists.txt and src/CMakeLists.txt)
<ol>
<li>CGAL (>= 4.11.2)</li>
<li>  g++ </li>
<li> maxhs  </li>  *check the installation instruction and detailed information: http://www.maxhs.org/
</ol>

## Compilation
Compile the source with the build/build_auto.sh



# Evaluation
For each set of experiments, we set up a folder as follows. Each folder 
contains one subfolder, "plots," which contains the generated plots of its corresponding experiment set.
Please refer to the following table to compare the generated plots with plots presented in the paper.

| Experiment Set      | Figures|
| :----------------------: | :----------------------: | 
| E1    | Fig. 8|
| E23   | Fig 9 & Fig.10|
| E4    | Fig. 11|
| E5   | Fig. 12 & Fig.13|
| E1-Rect| Fig. 14|
| E23-Rect| Fig 15 & Fig.16|
| E4-Rect| Fig. 17|
| E5-Rect| Fig. 18 & Fig.19|



**NOTE**


The benchmark data files (in the folder INPUT) were generated with the https://github.com/dyna-mis/labeling-instance-generator. 
However, since the four large rectangle files are lost, we generate new files with seed 0. 
The computed results are slightly different; however, the generated plots (Fig.14) have similar patterns as our paper. 

 
