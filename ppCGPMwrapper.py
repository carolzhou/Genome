#!/usr/bin/env python

#######################################################
#
# ppCGPMwrapper.py
#
# This script has no required input files, but should be run in the
# directory contining a set of "Results_" directories containing output
# generated by compareGeneProfiles_main.py.
#
# How the script works:
# 1) ppCGPMwrapper.py constructs the necessary command-line arguments for 
# calling postProcessCGPM.py. The output of postProcessCGPM.py is written
# to the current working directory, so ppCGPMwrapper.py changes to the
# specific results directory for a comparison before executing. 
# 2) The directory list (i.e., list of directory names beginning with "Results_")
# is read into a 
# data structure, from which each specific results directory is read, and
# each cycle of postProcessCGPM.py is executed.
# 3) In each directory is located an output file from compareGeneProfiles_main.py, 
# called, compareGeneProfiles_main.log. This log file contains the fully
# qualified directory path/filename for genome1 and genome2. These are read
# by ppCGPMwrapper.py and used to determine which genome file should be #1
# and which #2. 
#
# Programmer:  Carol L. Ecale Zhou
# Last update:  25 March 2014
#
#################################################################
'''
Copyright (c) 2015, Lawrence Livermore National Security, LLC. Produced at the Lawrence Livermore National Laboratory. Written by Carol L. Ecale Zhou, zhou4@llnl.gov; carol.zhou@comcast.net. CODE-OCEC-15-045 All rights reserved. This file is part of Qspp. Please also read this link � Our Notice and GNU General Public License. 
This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License (as published by the Free Software Foundation) version 2, dated June 1991. 
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and conditions of the GNU General Public License for more details. 
You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA 
OUR NOTICE AND TERMS AND CONDITIONS OF THE GNU GENERAL PUBLIC LICENSE 
Our Preamble Notice 
A. This notice is required to be provided under our contract with the U.S. Department of Energy (DOE). This work was produced at the Lawrence Livermore National Laboratory under Contract No. DE-AC52-07NA27344 with the DOE. 
B. Neither the United States Government nor Lawrence Livermore National Security, LLC nor any of their employees, makes any warranty, express or implied, or assumes any liability or responsibility for the accuracy, completeness, or usefulness of any information, apparatus, product, or process disclosed, or represents that its use would not infringe privately-owned rights. 
C. Also, reference herein to any specific commercial products, process, or services by trade name, trademark, manufacturer or otherwise does not necessarily constitute or imply its endorsement, recommendation, or favoring by the United States Government or Lawrence Livermore National Security, LLC. The views and opinions of authors expressed herein do not necessarily state or reflect those of the United States Government or Lawrence Livermore National Security, LLC, and shall not be used for advertising or product endorsement purposes. 
The precise terms and conditions for copying, distribution and modification follows. 
GNU Terms and Conditions for Copying, Distribution, and Modification 
_ 0. This License applies to any program or other work which contains a notice placed by the copyright holder saying it may be distributed under the terms of this General Public License. The �Program,� below, refers to any such program or work, and a �work based on the Program� means either the Program or any derivative work under copyright law: that is to say, a work containing the Program or a portion of it, either verbatim or with modifications and/or translated into another language. (Hereinafter, translation is included without limitation in the term �modification�.) Each licensee is addressed as �you.� 
_ Activities other than copying, distribution and modification are not covered by this License; they are outside its scope. The act of running the Program is not restricted, and the output from the Program is covered only if its contents constitute a work based on the Program (independent of having been made by running the Program). Whether that is true depends on what the Program does. 
_ 1. You may copy and distribute verbatim copies of the Program�s source code as you receive it, in any medium, provided that you conspicuously and appropriately publish on each copy an appropriate copyright notice and disclaimer of warranty; keep intact all the notices that refer to this License and to the absence of any warranty; and give any other recipients of the Program a copy of this License along with the Program. 
_ You may charge a fee for the physical act of transferring a copy, and you may at your option offer warranty protection in exchange for a fee. 
2 You may modify your copy or copies of the Program or any portion of it, thus forming a work based on the Program, and copy and distribute such modifications or work under the terms of Section 1 above, provided that you also meet all of these conditions: 
a) You must cause the modified files to carry prominent notices stating that you changed the files and the date of any change. 
b) You must cause any work that you distribute or publish, that in whole or in part contains or is derived from the Program or any part thereof, to be licensed as a whole at no charge to all third parties under the terms of this License. 
c) If the modified program normally reads commands interactively when run, you must cause it, when started running for such interactive use in the most ordinary way, to print or display an announcement including an appropriate copyright notice and a notice that there is no warranty (or else, saying that you provide a warranty) and that users may redistribute the program under these conditions, and telling the user how to view a copy of this License. (Exception: if the Program itself is interactive but does not normally print such an announcement, your work based on the Program is not required to print an announcement.) 
These requirements apply to the modified work as a whole. If identifiable sections of that work are not derived from the Program, and can be reasonably considered independent and separate works in themselves, then this License, and its terms, do not apply to those sections when you distribute them as separate work. But when you distribute the same section as part of a whole which is a work based on the Program, the distribution of the whole must be on the terms of this License, whose permissions for other licensees extend to the entire whole, and thus to each and every part regardless of who wrote it. 
Thus, it is not the intent of this section to claim rights or contest your rights to work written entirely by you; rather, the intent is to exercise the right to control the distribution of derivative or collective works based on the Program. 
In addition, mere aggregation of another work not based on the Program with the Program (or with a work based on the Program) on a volume of a storage or distribution medium does not bring the other work under the scope of this License. 
3. You may copy and distribute the Program (or a work based on it, under Section 2) in object code or executable form under the terms of Sections 1 and 2 above provided that you also do one of the following: 
a) Accompany it with the complete corresponding machine-readable source code, which must be distributed under the terms of Sections 1 and 2 above on a medium customarily used for software interchange; or, 
b) Accompany it with a written offer, valid for at least three years, to give any third party, for a charge no more than your cost of physically performing source distribution, a complete machine-readable copy of the corresponding source code, to be distributed under the terms of Sections 1 and 2 above on a medium customarily used for software interchange; or, 
c) Accompany it with the information you received as to the offer to distribute corresponding source code. (This alternative is allowed only for noncommercial distribution and only if you received the program in object code or executable form with such an offer, in accord with Subsection b above.) 
The source code for a work means the preferred form the work for making modifications to it. For an executable work, complete source code means all the source code for all modules it contains, plus any associated interface definition files, plus the scripts used to control compilation and installation of the executable. However, as a special exception, the source code distributed need not include anything that is normally distributed (in either source or binary form) with the major components (compiler, kernel, and so on) of the operating system on which the executable runs, unless that component itself accompanies the executable. 
If distribution of executable or object code is made by offering access to copy from a designated place, then offering equivalent access to copy the source code from the same place counts as distribution of the source code, even though third parties are not compelled to copy the source along with the object code. 
4. You may not copy, modify, sublicense, or distribute the Program except as expressly provided under this License. Any attempt otherwise to copy, modify, sublicense or distribute the 
Program is void, and will automatically terminate your rights under this License. However, parties who have received copies, or rights, from you under this License will not have their licenses terminated so long as such parties remain in full compliance. 
2 You are not required to accept this License, since you have not signed it. However, nothing else grants you permission to modify or distribute the Program or its derivative works. These actions are prohibited by law if you do not accept this License. Therefore, by modifying or distributing the Program (or any work based on the Program), you indicate your acceptance of this License to do so, and all its terms and conditions for copying, distributing or modifying the Program or works based on it. 
3 Each time you redistribute the Program (or any work based on the Program), the recipient automatically receives a license from the original licensor to copy, distribute or modify the Program subject to these terms and conditions. You may not impose any further restrictions on the recipients� exercise of the rights granted herein. You are not responsible for enforcing compliance by third parties to this License. 
4 If, as a consequence of a court judgment or allegation of patent infringement or for any other reason (not limited to patent issues), conditions are imposed on you (whether by court order, agreement or otherwise) that contradict the conditions of this License, they do not excuse you from the conditions of this License. If you cannot distribute so as to satisfy simultaneously your obligations under this License and any other pertinent obligations, then as a consequence you may not distribute the Program at all. For example, if a patent license would not permit royalty-free redistribution of the Program by all those who receive copies directly or indirectly through you, then the only way you could satisfy both it and this License would be to refrain entirely from distribution of the Program. 
If any portion of this section is held invalid or unenforceable under any particular circumstance, the balance of the section is intended to apply and the section as a whole is intended to apply in other circumstances. 
It is not the purpose to this section to induce you to infringe any patents or other property right claims or to contest validity of any such claims; this section has the sole purpose of protecting the integrity of the free software distribution system, which is implemented by public license practices. Many people have made generous contributions to the wide range of software distributed through that system in reliance on consistent application of that system; it is up to the author/donor to decide if he or she is willing to distribute software through any other system and a licensee cannot impose that choice. 
This section is intended to make thoroughly clear what is believed to be a consequence of the rest of this License. 
1 If the distribution and/or use of the Program is restricted in certain countries either by patents or by copyrighted interfaces, the original copyright holder who places the Program under this License may add an explicit geographical distribution limitation excluding those countries, so that distribution is permitted only in or among countries not thus excluded. In such case, this License incorporates the limitation as if written in the body of this License. 
9. The Free Software Foundation may publish revised and/or new versions of the General Public License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns. 
Each version is given a distinguishing version number. If the Program specifies a version number of this License which applies to it and �any later version,� you have the option of following the terms and conditions either of that version of any later version published by the Free Software Foundation. If the Program does not specify a version number of this License, you may choose any version ever published by the Free Software Foundation. 
2 If you wish to incorporate parts of the Program into other free programs whose distribution conditions are different, write to the author to ask for permission. For software which is copyrighted by the Free Software Foundation, write to the Free Software Foundation; we sometimes make exceptions for this. Our decision to grant permission will be guided by the two goals of preserving the free status of all derivatives of our free software and or promoting the sharing and reuse of software generally. 
NO WARRANTY 
11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM �AS IS� WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND 
FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF 
THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION. 
2 IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. 
END OF TERMS AND CONDITIONS
'''

import sys, os, re, string, copy
from subprocess import call
import subprocess

#### CONFIGURABLE

PYTHON_CODE_HOME = "/home/zhou4/PythonCode/BetaCode_CGP/"
POST_PROCESS_CGPM_CODE = PYTHON_CODE_HOME + "postProcessCGPM.py"  # use current stable version or modify constant
CGPM_REPORT = "compareGeneProfiles_main.report"
CGPM_LOG    = "compareGeneProfiles_main.log"

# PATTERNS for recognizing genome 1's & 2's genome and annotation files

p_g1 = re.compile('\#1.*\.fasta')
p_g2 = re.compile('\#2.*\.fasta')
p_a1 = re.compile('\#1.*\.gff')
p_a2 = re.compile('\#2.*\.gff')

#### FILES

logFile = "ppCGPMwrapper.log"
LOGFILE = open(logFile,"w")
LOGFILE.write("%s\n" % ("Begin log file"))
LOGFILE.write("%s%s\n" % ("Version of postProcessCGPM.py being used:",POST_PROCESS_CGPM_CODE))
LOGFILE.write("%s%s\n" % ("PYTHON_CODE_HOME is ",PYTHON_CODE_HOME))

#### CONSTANTS

ACCEPTABLE_ARG_COUNT = (1,2) # "help", "input", or 0 arguments expected

HELP_STRING = "This script does not require input parameters, but should be run in the directory containing the output directories created by compareGeneProfiles_main.py. This script runs postProcessCGPM.py to process the .report files in each Results_ directory and reads the .out file in the current directory to identify the locations of the genome, gene, and protein files that were compared. For more information, type: ppCGPMwrapper.py usage"

USAGE_STRING = "Usage:  ppCGPMwrapper.py\nFor more information, type: ppCGPMwrapper.py help"

INPUT_STRING = "Input:  this program requires no input parameters."

##### Get command-line arguments

argCount = len(sys.argv)
if argCount in ACCEPTABLE_ARG_COUNT:
    if argCount == 2:
        match = re.search("help", sys.argv[1].lower())
        if match:
            print HELP_STRING
            exit(0)
        match = re.search("usage", sys.argv[1].lower())
        if match:
            print USAGE_STRING
            exit(0)
        match = re.search("input", sys.argv[1].lower())
        if match:
            print INPUT_STRING
            exit(0)
else:
    print "Invalid input parameters. For help, type: ppCGPMwrapper.py help"
    exit(0)

#####

genomeFiles1  = {
    "strain"     : "",  # name of strain (e.g., AmesAncestor)
    "genome"     : "",  # filename containing genome (multi-)fasta
    "annotation" : "",  # filename containing genome annotations
    "genes"      : "",  # filename containing gene sequences 
    "proteins"   : "",  # filename containing protein translations
    }
genomeFiles2  = {
    "strain"     : "",  # name of strain (e.g., AmesAncestor)
    "genome"     : "",  # filename containing genome (multi-)fasta
    "annotation" : "",  # filename containing genome annotations
    "genes"      : "",  # filename containing gene sequences 
    "proteins"   : "",  # filename containing protein translations
    }

# Get list of results directories from previous (compareGeneProfiles_main.py) calculations

command = "ls . | grep \'Results_\'"  # Get list of Results directories in current directory
proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
if err:
    print "ERROR:", err
dirsList = []
dirsList = out.split('\n')

# Walk through each directory name, capture the genome 1 & 2 genome and annotation path/filenames...
# ...then re-construct the gene and protein filenames, and finally, execute postProcessCGPM.py over
# the binary-comparison report file.

count = 0; fragments = []; lineFragments = []
for resultDir in dirsList:
    match = re.search('Results_',resultDir)  # Make sure it's a correct directory name
    if match:  #***                               # Process .report file in this directory
        cgpmReport = CGPM_REPORT  # Construct .report and .log path/filenames
        cgpmLog    = resultDir + '/' + CGPM_LOG 

        ### Get absolute path/filename for genome and annotation files of binary comparison
        CGPM_LOG_HANDLE = open(cgpmLog,"r")  # Log file contains names of genome fasta and annotation files
        fLines = CGPM_LOG_HANDLE.read().splitlines()
        for line in fLines:
            match = re.findall(p_g1,line)  # Genome 1 fasta path/filename in this line
            if match:
                lineFragments = line.split(' ')
                genomeFiles1["genome"] = lineFragments[3] # in 4th position, if you split on space
                fragments = genomeFiles1["genome"].split('.fasta')
                genomeFiles1["genes"]    = fragments[0] + '_gene.fasta' # reconstruct genes fasta filename
                genomeFiles1["proteins"] = fragments[0] + '_prot.fasta'
                continue 
            match = re.findall(p_g2,line)  # Genome 2 fasta path/filename in this line
            if match:
                lineFragments = line.split(' ')
                genomeFiles2["genome"] = lineFragments[3]
                fragments = genomeFiles2["genome"].split('.fasta')
                genomeFiles2["genes"]    = fragments[0] + '_gene.fasta'
                genomeFiles2["proteins"] = fragments[0] + '_prot.fasta'
                continue 
            match = re.findall(p_a1,line)  # Genome 1 annotation path/filename in this line
            if match:
                lineFragments = line.split(' ')
                genomeFiles1["annotation"] = lineFragments[3]
                continue 
            match = re.findall(p_a2,line)  # Genome 2 annotation path/filename in this line
            if match:
                lineFragments = line.split(' ')
                genomeFiles2["annotation"] = lineFragments[3]
                continue 
        CGPM_LOG_HANDLE.close() 
        
        # Run postProcessCGMP.py for the current binary comparison
        currentDir = os.getcwd()  # where are we now
        os.chdir(resultDir)       # change to current Results directory
        call(["python",POST_PROCESS_CGPM_CODE,"-g1",genomeFiles1["genes"],"-g2",genomeFiles2["genes"],"-r",cgpmReport])
        os.chdir(currentDir)      # return
        count += 1 
        LOGFILE.write("%s%s\n" % ("Completed post-processing in directory ",resultDir))

##### Clean up

LOGFILE.write("%s%s%s\n" % ("Execution complete. ",count," jobs completed." ))
print "Execution complete.", count, "jobs completed."
LOGFILE.close()
