# Genome
This is a repository for comparative genomics

Summary
Compare Gene Profiles (CGP) performs pairwise gene content comparisons among a relatively large set of related bacterial genomes. CGP performs pairwise BLAST among gene calls from a set of input genome and associated annotation files, and combines the results to generate lists of common genes, unique genes, homologs, and genes from each genome that differ substantially in length from corresponding genes in the other genomes. CGP is implemented in Python and runs in a Linux environment in serial mode.
Code Specifics
CGP is a new bioinformatics tool that can be applied in automated comparison of gene content among an arbitrarily large set of bacterial genomes. Version 1.0.0 of the code runs in a Linux environment at the command line in serial mode. CGP can be used with as many genome and annotation files as can be accommodated on the user's system, with the limitation that the method scales with order N2. It should be feasible to compare up to 25 genomes in a matter of a few hours on a small Linux cluster (e.g., 96 processors).  CGP is written in Python 2.7.  CGP uses the transeq code from the Emboss package; this is the only external software dependency.
CGP comprises the following code files:
Annotation.py
blastAnalysis.py
CGPMdriver.py
CGPMwrapper.py
cleanUpFasta.py
compareGeneProfiles_main.py
constructConfigFile.py
constructPPcgpmConfigfile.py
fastaSequence.py
genomeSequence.py
postProcessCGPM.py
ppCGPMwrapper.py
queryCGPMcount.py
queryCGPMresults.py
summarizeCGPMresults.py

Processing is initiated by invoking CGPMdriver.py.  Code files can be found in folder CGPv1_codeFiles.

Included in this package are sample input files (see folder SampleInputfiles) and sample config files (see folder SampleConfigFiles). Sample output from CGP can be found in folder SampleOutputFiles.

