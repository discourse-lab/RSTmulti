# RSTmulti

The corpus RSTmulti contains English and German texts which have two separate Rhetorical Structure Theory annotations, for the purpose of studying disagreement in the context of discourse structure. 

Repository with the dataset and scripts used in the The 19th Linguistic Annotation Workshop (LAW 2025) paper: [Disagreements in analyses of rhetorical text structure: A new dataset and first analyses](https://aclanthology.org/)

## Data

Our doubly annotated data can be found in the `data/` folder.

The files beginning with `maz-*` are from [PCC*](https://github.com/mohamadi-sara20/pcc/tree/main/double-annotated), with more information in the paper: [Discourse Parsing for German with new RST Corpora](https://aclanthology.org/2024.konvens-main.7/) (Shahmohammadi & Stede, KONVENS 2024).

The files beginning with `pcc-*` as well as `impfenpro.rs3` and `olympiacon.rs3` were doubly-annotated for the LAW paper. More information on the orignal PCC corpus can be found [here](https://angcl.ling.uni-potsdam.de/resources/pcc.html).

The files beginning with `UNSC-*` are previously unpublished doubly-annotated files from the UNSC-RST corpus. More information can be found in the paper: [Rhetorical Strategies in the UN Security Council: Rhetorical Structure Theory and Conflicts](https://aclanthology.org/2024.sigdial-1.2/) (Zaczynska & Stede, SIGDIAL 2024), as well as in the repository for the [UP Multilayer UNSC Corpus](https://github.com/discourse-lab/UMUC/tree/main).

The other files (which end with either `-a2`, `-b1`, or `-or`), are previously unpublished [APA-RST](https://github.com/fhewett/apa-rst) files. More information can be found in the paper: [APA-RST: A Text Simplification Corpus with RST Annotations](https://aclanthology.org/2023.codi-1.23/) (Hewett, CODI 2023).

The RST-DT is available from the [Linguistic Data Consortium](https://catalog.ldc.upenn.edu/LDC2002T07). We used the following files in our analysis: `wsj_0615, wsj_0624, wsj_0630, wsj_0639, wsj_0651, wsj_0669, wsj_0684, wsj_1100, wsj_1102, wsj_1114, wsj_1117, wsj_1123, wsj_1129, wsj_1132, wsj_1141, wsj_1153, wsj_1168, wsj_1304, wsj_1314, wsj_1358, wsj_1924, wsj_1998, wsj_2303, wsj_2328, wsj_2349, wsj_2367`.

## Tace output

The folder `tace_output/` contains the output from [RSTTace](https://github.com/tkutschbach/RST-Tace).
If you would like to use your own data, download Tace and parse your files accordingly.

## Scripts

The folder `scripts/` contains the scripts which are used to create the CSV files, which contain the categories which we use in our paper (interchangeable relations, etc.).
To run the scripts, first download the requirements as outlined in `requirements.txt`.
The CSV files can then be created as follows:
```
python create_categories.py 
```
If using your own data, or if you want to change the name of the output files, adapt the following arguments (run `python create_categories.py -h` for more details):
```
-tace_path
-corpus_path
-output_file
```



## More information and citation

More information on the files can be found in our paper. If you use any of the data please cite this paper:
...



