#!usr/bin/env python


###################################################################
#
# compareGeneProfiles_main.py
#
# Programmer:  Carol L. Ecale Zhou
# Last update: 5 March 2015
#
# This program compares the gene calls from 2 genomes and identifies genes that 
# match, are similar, or are unique in each genome. This code is a re-write of
# compareGeneProfiles.py, which was written using beginner's knowledge of Python.
# This new program implements the same functionality,  but is written
# as object-oriented, modular code.
#
# Input parameters, format specifications, and default values:
# Files:
#    genome sequence files (in multi-fasta format; -g1 and -g2)
#    annotation files (in RAST .gff or .gff3 format; -a1 and -a2)
# Match/similarity detection (integer 0-100) with default value:
#    %identity gene-match cutoff (default 95)
#    %coverage gene-match cutoff (default 95)
#    %identity gene-similarity cutoff (default 60)
#    %coverage gene-similarity cutoff (default 75)
#    %identity domain-match cutoff (default 95)
#    %coverage domain-match cutoff (default 45)
#    %identity domain-similarity cutoff (default 60)
#    %coverage domain-similarity cutoff (default 45)
#    %identity paralog-match cutoff (default 95)
#    %coverage paralog-match cutoff (default 95)
#    %identity paralog-domain similarity cutoff (default 60)
#    %coverage paralog-domain similarity cutoff (default 45) 
#    %identity protein-match cutoff (default 95)
#    %coverage protein-match cutoff (default 95)
#    %identity protein-similarity cutoff (default 60)
#    %coverage protein-similarity cutoff (default 75)
#    %identity protein-domain-match cutoff (default 95)
#    %coverage protein-domain-match cutoff (default 45)
#    %identity protein-domain-similarity cutoff (default 60)
#    %coverage protein-domain-similarity cutoff (default 45)
#    %identity protein-paralog-match cutoff (default 95)
#    %coverage protein-paralog-match cutoff (default 95)
#    %identity protein-paralog-domain similarity cutoff (default 60)
#    %coverage protein-paralog-domain similarity cutoff (default 45) 
#
###################################################################
'''
Copyright (c) 2015, Lawrence Livermore National Security, LLC. Produced at the Lawrence Livermore National Laboratory. Written by Carol L. Ecale Zhou, zhou4@llnl.gov; carol.zhou@comcast.net. CODE-OCEC-15-045 All rights reserved. This file is part of Qspp. Please also read this link – Our Notice and GNU General Public License. 
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
_ 0. This License applies to any program or other work which contains a notice placed by the copyright holder saying it may be distributed under the terms of this General Public License. The “Program,” below, refers to any such program or work, and a “work based on the Program” means either the Program or any derivative work under copyright law: that is to say, a work containing the Program or a portion of it, either verbatim or with modifications and/or translated into another language. (Hereinafter, translation is included without limitation in the term “modification”.) Each licensee is addressed as “you.” 
_ Activities other than copying, distribution and modification are not covered by this License; they are outside its scope. The act of running the Program is not restricted, and the output from the Program is covered only if its contents constitute a work based on the Program (independent of having been made by running the Program). Whether that is true depends on what the Program does. 
_ 1. You may copy and distribute verbatim copies of the Program’s source code as you receive it, in any medium, provided that you conspicuously and appropriately publish on each copy an appropriate copyright notice and disclaimer of warranty; keep intact all the notices that refer to this License and to the absence of any warranty; and give any other recipients of the Program a copy of this License along with the Program. 
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
3 Each time you redistribute the Program (or any work based on the Program), the recipient automatically receives a license from the original licensor to copy, distribute or modify the Program subject to these terms and conditions. You may not impose any further restrictions on the recipients’ exercise of the rights granted herein. You are not responsible for enforcing compliance by third parties to this License. 
4 If, as a consequence of a court judgment or allegation of patent infringement or for any other reason (not limited to patent issues), conditions are imposed on you (whether by court order, agreement or otherwise) that contradict the conditions of this License, they do not excuse you from the conditions of this License. If you cannot distribute so as to satisfy simultaneously your obligations under this License and any other pertinent obligations, then as a consequence you may not distribute the Program at all. For example, if a patent license would not permit royalty-free redistribution of the Program by all those who receive copies directly or indirectly through you, then the only way you could satisfy both it and this License would be to refrain entirely from distribution of the Program. 
If any portion of this section is held invalid or unenforceable under any particular circumstance, the balance of the section is intended to apply and the section as a whole is intended to apply in other circumstances. 
It is not the purpose to this section to induce you to infringe any patents or other property right claims or to contest validity of any such claims; this section has the sole purpose of protecting the integrity of the free software distribution system, which is implemented by public license practices. Many people have made generous contributions to the wide range of software distributed through that system in reliance on consistent application of that system; it is up to the author/donor to decide if he or she is willing to distribute software through any other system and a licensee cannot impose that choice. 
This section is intended to make thoroughly clear what is believed to be a consequence of the rest of this License. 
1 If the distribution and/or use of the Program is restricted in certain countries either by patents or by copyrighted interfaces, the original copyright holder who places the Program under this License may add an explicit geographical distribution limitation excluding those countries, so that distribution is permitted only in or among countries not thus excluded. In such case, this License incorporates the limitation as if written in the body of this License. 
9. The Free Software Foundation may publish revised and/or new versions of the General Public License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns. 
Each version is given a distinguishing version number. If the Program specifies a version number of this License which applies to it and “any later version,” you have the option of following the terms and conditions either of that version of any later version published by the Free Software Foundation. If the Program does not specify a version number of this License, you may choose any version ever published by the Free Software Foundation. 
2 If you wish to incorporate parts of the Program into other free programs whose distribution conditions are different, write to the author to ask for permission. For software which is copyrighted by the Free Software Foundation, write to the Free Software Foundation; we sometimes make exceptions for this. Our decision to grant permission will be guided by the two goals of preserving the free status of all derivatives of our free software and or promoting the sharing and reuse of software generally. 
NO WARRANTY 
11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM “AS IS” WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND 
FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF 
THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION. 
2 IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. 
END OF TERMS AND CONDITIONS
'''

#SERVER = False  # True if this version of the code is running on the Django server
SERVER = True

import sys, os, re, string, copy
from time import strftime
from time import gmtime
import datetime
from subprocess import call
import fastaSequence
import annotation
import genomeSequence
import blastAnalysis

##### ENVIRONMENT

EMBOSS_HOME = "/usr/local/emboss/bin/"  #*** should be in path!
# Note:  EMBOSS messes with fasta headers; therefore, I am putting minimal info in the header and using only '/'
#    as a separator. EMBOSS adds "_1" to the end of a simple fasta header--can't prevent this. Using other
#    separators wreaks havoc in terms of the header EMBOSS produces, and including free text, such as the RAST
#    annotation, is the kiss of death.

##### FILE names

##### FILES
CODE_BASE_DIR = os.environ["CODE_BASE_DIR"]
BASE_DIR = ""
EMAIL_DIR = BASE_DIR  # Move files to this dir for email results to user
OUT_DIR          = ""   # Default
GENOME_FILE1     = ""   # Input parameters... 
GENOME_FILE2     = ""   #  
ANNOTATION_FILE1 = ""   # 
ANNOTATION_FILE2 = ""   # 
OUT_FILE         = "compareGeneProfiles_main.out"
REPORT_FILE      = "compareGeneProfiles_main.report"
SUMMARY_FILE     = "compareGeneProfiles_main.summary"
LOG_FILE         = "compareGeneProfiles_main.log"
LOG_COPY         = "compareGeneProfiles_main.log.copy"
OUT              = ""   # File handles...
REPORT           = ""   #
SUMMARY          = ""   #
LOG              = ""   #
ERROR_LOG        = ""   #

##########################################################################
##### PATTERNS

p_fasta = re.compile('\.(fasta)|(fna)|(fas)|(fnt)|(fa)')
p_gff = re.compile('\.gff*')

########################################################################
##### DECLARATIONS 

##### CONSTANTS

HELP_STRING = "This script inputs 2 genome fasta files and 2 RAST annotation files and returns a file (compareGeneProfiles_main.report containing a report specifying a comparison between the gene profiles of the 2 genomes, including matching genes, gene homologs and paralogs, and putative domain-fusion events. Optionally you may provide percent identity and coverage cutoffs for gene matching at the nucleotide level. By default these values for matching genes are 95% identity and 95% coverage. (All identity and coverage values for gene/domain/paralog match and similarity detection are configurable. For complete information on input parameters, type: compareGeneProfiles_main -input)"

USAGE_STRING = "Usage:  compareGeneProfiles_main.py -g1 <genome1.fasta> -a1 <genome1.gff> -g2 <genome2.fasta> -a2 <genome2.gff>\nYou may enter parameters interactively by typing: compareGeneProfiles_main.py -interactive" 

INPUT_STRING = "You may enter parameters interactively (via prompt) by typing: compareGeneProfiles_main.py -interactive\nYou will then be promted for the following required command-line parameters: \n   genome1.fasta\n   genome2.fasta\n   annotation1.gff\n   annotation2.gff\nOptionally, you may provide any/all of the following cutoff values as integers ranging from 0 to 100, with restrictions, by entering them at the command line prompt, or you may accept the defaults:\n   gene match sequence identity\n   gene match minumum coverage\n   gene similarity identity\n   gene similarity coverage\n   domain match identity\n   domain match coverage\n   domain similarity identity\n   domain similarity coverage\n   paralog match identity\n   paralog match coverage\n   paralog domain similarity identity\n   paralog domain similarity coverage\nType: compareGeneProfiles_main.py -interactive"   

ACCEPTABLE_ARG_COUNT = (2,3,9,11) # 2 if "help", "input", or "interactive"; 9 if 4 files provided with command-line labels (ie, '-g1')
                               # 3 if "config" mode; 11 if also including projectDirectory

#DEBUG = True
DEBUG = False
BLAST_ON = True    # controls whether blast is performed
#BLAST_ON = False
#PROTEIN = True     # controls whether protein sequences are blasted 
PROTEIN = False

##### BLAST default parameters

GENETIC_CODE    = 11 # bacterial, by default
BLAST_IDENTITY  = 60 
SCORE_EDGE      = 0.05
MAX_TARGET_SEQS = 1
OVERHANG        = 0.25
OUTPUT_FORMAT   = 7  # 7 is tabbed list output format for blast
EVALUE          = 1 

##### VARIABLES: command-line arguments

argCount         = 0 # number of command-line arguments provided
argument         = ""
genomeFile1      = "" # g1
genomeFile2      = "" # g2
rootFilename     = ""
annotationFile1  = "" # a1
annotationFile2  = "" # a2
projectDirectory = "" # d

#### VARIABLES: files

outFile      = ""     # Contains misc output
reportFile   = ""     # Contains binary genome comparison data 
summaryFile  = ""     # Contains summary data pertaining to binary comparison
logFile      = ""     # script log

errorLog = os.path.join(CODE_BASE_DIR, "compareGeneProfiles_main.err") # error log (records prior to script main body)

##### VARIABLES: other

fileError       = False    # assume all is ok until proven otherwise
extensionString = ""       # for capturing file extension string

##### DATA STRUCTURES

parameters = { # data structure for input to class methods; defaults as indicated
"geneMatchIdentity"                      : 95, 
"geneMatchCoverage"                      : 95,
"geneSimilarityIdentity"                 : 60,
"geneSimilarityCoverage"                 : 75,
"domainMatchIdentity"                    : 95,
"domainMatchCoverage"                    : 45,
"domainSimilarityIdentity"               : 60,
"domainSimilarityCoverage"               : 45,
"paralogMatchIdentity"                   : 80,
"paralogMatchCoverage"                   : 80,
"paralogSimilarityIdentity"              : 60,
"paralogSimilarityCoverage"              : 75,
"paralogDomainMatchIdentity"             : 95,
"paralogDomainMatchCoverage"             : 45,
"paralogDomainSimilarityIdentity"        : 60,
"paralogDomainSimilarityCoverage"        : 45,
"proteinMatchIdentity"                   : 95, 
"proteinMatchCoverage"                   : 95,
"proteinSimilarityIdentity"              : 60,
"proteinSimilarityCoverage"              : 75,
"proteinDomainMatchIdentity"             : 95,
"proteinDomainMatchCoverage"             : 45,
"proteinDomainSimilarityIdentity"        : 60,
"proteinDomainSimilarityCoverage"        : 45,
"proteinParalogMatchIdentity"            : 95,
"proteinParalogMatchCoverage"            : 95,
"proteinParalogSimilarityIdentity"       : 60,
"proteinParalogSimilarityCoverage"       : 75,
"proteinParalogDomainMatchIdentity"      : 95,
"proteinParalogDomainMatchCoverage"      : 45,
"proteinParalogDomainSimilarityIdentity" : 60,
"proteinParalogDomainSimilarityCoverage" : 45,
"analysis"                               : None, # will fill in as "cross comparison" or "paralog"
"type"                                   : None # will fill in as "gene" or "protein"
}

files = { # User's input files and other generated files go here
"genomeFile1"          : "",  # user input
"genomeFile2"          : "",  # user input
"annotationFile1"      : "",  # user input
"annotationFile2"      : "",  # user input
"geneFile1"            : "",
"geneFile2"            : "",
"proteinFile1"         : "",
"proteinFile2"         : "",
"baseDir"              : "",  # user input
"geneFile1_root"       : "",  # file name sans all directory prefixing
"geneFile2_root"       : "",
"protFile1_root"       : "",
"protFile2_root"       : "",
"projectDirectory"     : "",  # if SERVER, input from wrapper code
}

##### FUNCTIONS ##############################################################

# For inserting "gene" or "prot" into genome filename, for new gene, protein fasta files
def ConstructFilename(inFile,infix):  # infix is typically "gene" or "prot"
    newFile = ""
    stringList = re.findall('\.\w*', inFile)
    extensionString = stringList[-1] # Take last element in list
    rootFilename = inFile.rstrip(extensionString)
    newFile = rootFilename + "_" + infix + extensionString
    print "newFile name: ", newFile
    return newFile

# FUNCTION GetRootFile - Captures file name from directory-path/filename string
def GetRootFile(inFile):   # strip the inFile of all directory prefixes
    print "inFile is", inFile
    rootFile = ""
    stringList = re.findall('\/[\w\d\.]*', inFile)
    if stringList:
        rootFile = stringList[-1]  # Take last element in list
    else:
        rootFile = inFile
    rootFile = rootFile.lstrip('/')
    return rootFile 

# FUNCTION GetConfig - parses a configuration string and assigns file names

def GetConfig(configString):
    stringList = []
    configString = configString.lstrip('\"')
    configString = configString.rstrip('\"')
    stringList = configString.split('#')
    BASE_DIR                 = stringList[0]
    files["genomeFile1"]     = stringList[1]
    files["genomeFile2"]     = stringList[2]
    files["annotationFile1"] = stringList[3]
    files["annotationFile2"] = stringList[4]

# FUNCTION GetArguments - gets all input parameters from user interactively 
def GetArguments(parameters,files):
    # get Files
    sys.stdout.write("Please enter the base directory where your files are located: ")
    files["baseDir"] = sys.stdin.readline().rstrip()
    #files["baseDir"] = files["baseDir"].rstrip('/')  # remove terminal slash if exsits
    #files["baseDir"] = files["baseDir"] + '/'        # and put it there for sure
    sys.stdout.write("Please enter the genome #1 filename:")
    files["genomeFile1"] = sys.stdin.readline().rstrip()
    sys.stdout.write("Genome #2 filename:")
    files["genomeFile2"] = sys.stdin.readline().rstrip()
    sys.stdout.write("Genome #1 annotation filename:")
    files["annotationFile1"] = sys.stdin.readline().rstrip()
    sys.stdout.write("Genome #2 annotation filename:")
    files["annotationFile2"] = sys.stdin.readline().rstrip()
    GET_PARAMS = False
    sys.stdout.write("Do you want to accept all defaults? enter y/n  ")
    decision = sys.stdin.readline().rstrip()
    if decision.lower() == "n" or decision.lower() == "no":
        GET_PARAMS = True 
    if GET_PARAMS:
        #GENE###########################################################
        sys.stdout.write("gene match sequence identity (default=")
        sys.stdout.write(str(parameters["geneMatchIdentity"]))
        sys.stdout.write("): ")
        new = sys.stdin.readline().rstrip()
        if new:
            if int(new) >= 0 and int(new) <= 100:
                parameters["geneMatchIdentity"] = new

        sys.stdout.write("gene match minimum coverage (default=")
        sys.stdout.write(str(parameters["geneMatchCoverage"]))
        sys.stdout.write("): ")
        new = sys.stdin.readline().rstrip()
        if new:
            if int(new) >= 0 and int(new) <= 100:
                parameters["geneMatchCoverage"] = new

        sys.stdout.write("gene similarity sequence identity (default=")
        sys.stdout.write(str(parameters["geneSimilarityIdentity"]))
        sys.stdout.write("): ")
        new = sys.stdin.readline().rstrip()
        if new:
            if int(new) >= 0 and int(new) <= 100:
                parameters["geneSimilarityIdentity"] = new

        sys.stdout.write("gene similarity coverage (default=")
        sys.stdout.write(str(parameters["geneSimilarityCoverage"]))
        sys.stdout.write("): ")
        new = sys.stdin.readline().rstrip()
        if new:
            if int(new) >= 0 and int(new) <= 100:
                parameters["geneSimilarityCoverage"] = new

        #PROTEIN###########################################################
        sys.stdout.write("protein match sequence identity (default=")
        sys.stdout.write(str(parameters["proteinMatchIdentity"]))
        sys.stdout.write("): ")
        new = sys.stdin.readline().rstrip()
        if new:
            if int(new) >= 0 and int(new) <= 100:
                parameters["proteinMatchIdentity"] = new

        sys.stdout.write("protein match minimum coverage (default=")
        sys.stdout.write(str(parameters["proteinMatchCoverage"]))
        sys.stdout.write("): ")
        new = sys.stdin.readline().rstrip()
        if new:
            if int(new) >= 0 and int(new) <= 100:
                parameters["proteinMatchCoverage"] = new

        sys.stdout.write("protein similarity sequence identity (default=")
        sys.stdout.write(str(parameters["proteinSimilarityIdentity"]))
        sys.stdout.write("): ")
        new = sys.stdin.readline().rstrip()
        if new:
            if int(new) >= 0 and int(new) <= 100:
                parameters["proteinSimilarityIdentity"] = new

        sys.stdout.write("protein similarity coverage (default=")
        sys.stdout.write(str(parameters["proteinSimilarityCoverage"]))
        sys.stdout.write("): ")
        new = sys.stdin.readline().rstrip()
        if new:
            if int(new) >= 0 and int(new) <= 100:
                parameters["proteinSimilarityCoverage"] = new

        return(0) 
 
########################################################################################################
# Get command-line arguments; open user input/output files
########################################################################################################

today = os.popen('date')
ERROR_LOG = open(errorLog,"a")
ERROR_LOG.write("%s%s\n" % ("Reading command-line input at ",today.read()))

argCount = len(sys.argv)
print "Number of command-line arguments:", argCount
if argCount in ACCEPTABLE_ARG_COUNT:
    match = re.search("help", sys.argv[1].lower())
    if match:
        print HELP_STRING
        print USAGE_STRING
        ERROR_LOG.close(); exit(0)

    match = re.search("input", sys.argv[1].lower())
    if match:
        print INPUT_STRING
        ERROR_LOG.close(); exit(0)

    match = re.search("interactive", sys.argv[1].lower())
    if match:
        GetArguments(parameters,files)

    match = re.search("config", sys.argv[1].lower())
    if match:
        configString = sys.argv[2]
        GetConfig(configString)

    if argCount == 9 or argCount == 11:
	print "Reading input parameters"
        for i in range(argCount):
            if sys.argv[i] == "-g1":
                files["genomeFile1"] = sys.argv[i+1]
            if sys.argv[i] == "-g2":
                files["genomeFile2"] = sys.argv[i+1]
            if sys.argv[i] == "-a1":
                files["annotationFile1"] = sys.argv[i+1]
            if sys.argv[i] == "-a2":
                files["annotationFile2"] = sys.argv[i+1]
            if sys.argv[i] == "-d":
                files["projectDirectory"] = sys.argv[i+1]
                BASE_DIR = files["projectDirectory"]
	print "genomeFile1 is", files["genomeFile1"]
	print "genomeFile2 is", files["genomeFile2"]
	print "annotationFile1 is", files["annotationFile1"]
	print "annotationFile2 is", files["annotationFile2"]
	print "BASE_DIR is", files["projectDirectory"]
	print "Done reading input parameters"
    else:
        print USAGE_STRING
        ERROR_LOG.close();  exit(0)
else:
    print USAGE_STRING
    ERROR_LOG.write("%s\n" % ("Incorrect number of command-line arguments provided"))
    ERROR_LOG.close(); exit(0)

# Check files
match = re.search(p_fasta, files["genomeFile1"])
if not match:
    fileError = True
match = re.search(p_fasta, files["genomeFile2"])
if not match:
    fileError = True
match = re.search(p_gff, files["annotationFile1"])
if not match:
    fileError = True
match = re.search(p_gff, files["annotationFile2"])
if not match:
    fileError = True
if fileError:
    print "Check the formats of your input files:"  
    print "   Genome file #1:         ", files["genomeFile1"]
    print "   Annotation file #1:     ", files["annotationFile1"]
    print "   Genome file #2:         ", files["genomeFile2"]
    print "   Annotation file #2:     ", files["annotationFile2"]
    print "   Project directory:      ", files["projectDirectory"]
    print USAGE_STRING
    ERROR_LOG.write("%s\n" % ("ERROR in input file parameter"))
    ERROR_LOG.close(); exit(0)
else:
    ERROR_LOG.close()

# Prepend filenames with projectDirectory

print "1: OUT_DIR is", OUT_DIR
if SERVER:
    OUT_DIR      = os.path.join(files["projectDirectory"], OUT_DIR)
    reportFile   = os.path.join(OUT_DIR, "compareGeneProfiles_main.report")
    profilesFile = os.path.join(OUT_DIR, "compareGeneProfiles_main.out")
    logFile      = os.path.join(OUT_DIR, LOG_FILE)

print "2: SERVER is", SERVER
print "3: OUT_DIR is", OUT_DIR

# Prepend file names with baseDir; ""/no change if not provided:
print "baseDir is", files["baseDir"]
files["genomeFile1"] = os.path.join(files["baseDir"], files["genomeFile1"])
files["genomeFile2"] = os.path.join(files["baseDir"], files["genomeFile2"])
files["annotationFile1"] = os.path.join(files["baseDir"], files["annotationFile1"])
files["annotationFile2"] = os.path.join(files["baseDir"], files["annotationFile2"])

##### Open files

try:
    GENOME_FILE1 = open(files["genomeFile1"],"r")
except IOError as e:
    fileError = True
    print e
try:
    GENOME_FILE2 = open(files["genomeFile2"],"r")
except IOError as e:
    fileError = True
    print e
try:
    ANNOTATION_FILE1 = open(files["annotationFile1"],"r")
except IOError as e:
    fileError = True
    print e
try:
    ANNOTATION_FILE2 = open(files["annotationFile2"],"r")
except IOError as e:
    fileError = True
    print e
if fileError:
    ERROR_LOG.write("%s\n" % ("ERROR with input filename"))
    ERROR_LOG.close(); exit(0)

dateTime = str(datetime.datetime.now().time()) # need time down to sub-seconds 
today    = os.popen('date')
if SERVER:
    OUT_DIR = os.path.join(files["projectDirectory"], "Results_" + dateTime + "/")  #
else:
    OUT_DIR = "./"

print "Making directory", OUT_DIR
command = "mkdir " + OUT_DIR
os.system(command)
outFile      = os.path.join(OUT_DIR, OUT_FILE)     # Contains misc output
reportFile   = os.path.join(OUT_DIR, REPORT_FILE)  # Contains binary genome comparison data
summaryFile  = os.path.join(OUT_DIR, SUMMARY_FILE )# Contains summary data pertaining to binary comparison
logFile      = os.path.join(OUT_DIR, LOG_FILE)

LOG          = open(logFile,"w")
LOG.write("%s%s\n" % ("Begin script log ",today.read()))
LOG.write("%s%s\n" % ("Result directory suffix is ",dateTime))

# Record to log and keep in touch with user 

LOG.write("%s\n" % ("Parameters are: "))
LOG.write("%s%s\n" % ("genome file #1: ",files["genomeFile1"]))
LOG.write("%s%s\n" % ("genome file #2: ",files["genomeFile2"]))
LOG.write("%s%s\n" % ("annotation file #1: ",files["annotationFile1"]))
LOG.write("%s%s\n" % ("annotation file #2: ",files["annotationFile2"]))
LOG.write("%s%s\n" % ("user directory is: ",files["projectDirectory"]))
LOG.write("%s%s\n" % ("outFile is: ",outFile))

print "Parameters are:"
print "Genome file #1:", files["genomeFile1"]
print "Genome file #2:", files["genomeFile2"]
print "Annotation file #1:", files["annotationFile1"]
print "Annotation file #2:", files["annotationFile2"]
print "User directory:", files["projectDirectory"]
print "Out file:", outFile
keys = list(parameters); keys.sort()
for key in keys:
    print key, "is", parameters[key]

#########################################################################################################
# Construct genome data structures
#########################################################################################################

fLines = GENOME_FILE1.read().splitlines() # read lines into list, removing newlines
genome1 = genomeSequence.genome()
genome1.filename = files["genomeFile1"]
genome1.addContigs(fLines)
GENOME_FILE1.close()

fLines = GENOME_FILE2.read().splitlines()
genome2 = genomeSequence.genome()
genome2.addContigs(fLines)
GENOME_FILE2.close()

#########################################################################################################
# Extract gene sequences from genome files based on gene calls from annotation files;
# Translate gene sequences to protein.
# Construct gene and protein fastas and add to multi-fasta objects for each.
# Create gene and protein blast databases. 
# Save gene and protein fasta sequences to files.
#########################################################################################################

# First, create names for gene/protein fasta and blast database files; inform user

files["geneFile1"]    = ConstructFilename(files["genomeFile1"], "gene")
files["proteinFile1"] = ConstructFilename(files["genomeFile1"], "prot")
files["geneFile2"]    = ConstructFilename(files["genomeFile2"], "gene")
files["proteinFile2"] = ConstructFilename(files["genomeFile2"], "prot")

if PROTEIN: 
    print "Blast databases for genome 1 genes & proteins will be:"
    print files["geneFile1"], "and"
    print files["proteinFile1"]
    print "Blast databases for genome 2 genes & proteins will be:"
    print files["geneFile2"], "and"
    print files["proteinFile2"]
else:
    print "Blast databases for genome 1 genes will be:"
    print files["geneFile1"]
    print "Blast databases for genome 2 genes will be:"
    print files["geneFile2"]

# prepare to reverse complement
complements = string.maketrans('acgtrymkbdhvACGTRYMKBDHV', 'tgcayrkmvhdbTGCAYRKMVHDB')

################################################################

def extractGeneCalls(genomeX,lines): 
    geneCount = 0
    geneCountCDS = 0
    geneTemplate = fastaSequence.fasta()  # generic gene object
    annotationTemplate = annotation.annotationRecord()  # generic annotation object  
    gff = {  # for passing data to annotation class
        "source"       : "RAST",  #***
        "method"       : "RAST",
        "type"         : "gene",
        "contig"       : "unknown",
        "start"        : 0,
        "end"          : 0,
        "strand"       : 0,
        "readingFrame" : 0,
        "annotation"   : ""
        }  
    gene = {  # for passing data to fasta class
        "header"         : "",
        "name"           : "",
        "sequence"       : "",
        "type"           : "nt",
        "parentSequence" : "",
        "order"          : 0,
        "annotationList" : []
        }
    lines.remove(lines[0]) # skip header line 
    for line in lines:  # Extract gene fastas; create fasta object for gene; add to genome's geneSet
        geneCount += 1  # Don't need this, but diagnostic
        fields = line.split('\t')
        geneCallType = fields[2]
        if geneCallType.lower() == "cds":  # ie, skip '*RNA' and other entries (for now)
            geneCountCDS += 1
            gff["contig"]          = fields[0]
            gff["start"]           = int(fields[3])
            gff["end"]             = int(fields[4])
            gff["strand"]          = fields[6]
            gff["readingFrame"]    = fields[7]
            gff["annotation"]      = fields[8]
            gene["order"]          = geneCountCDS
            gene["name"]           = "cds" + str(geneCountCDS)
            gene["parentSequence"] = fields[0]  # the contig this gene is on (a shortHeader if from RAST)
            gene["sequence"] = genomeX.getSubsequence(gff["start"],gff["end"],gene["parentSequence"])
            if gff["strand"] == '-':  # Reverse complement sequence if on reverse strand
                reverseComplement = gene["sequence"].translate(complements)[::-1]
                gene["sequence"] = reverseComplement
            header = gene["name"] + "/" + gff["strand"] + "/" + str(gff["start"]) + "/" + str(gff["end"]) + "/"
            gene["header"] = header
            newGene = copy.deepcopy(geneTemplate) # dynamically allocate memory for next gene object
            newGene.enterGeneData(gene)
            newAnnotation = copy.deepcopy(annotationTemplate)
            newAnnotation.enterGFFdata(gff)
            newGene.addAnnotation(newAnnotation)
            genomeX.addGene(newGene)

#########################################################################################
# Extract gene sequences from genomes based on annotation file gene calls...
# ...construct gene fasta sequence objects and insert into multiFasta objects;
# Write gene fastas to file.
#########################################################################################

printFastas2fileArgs = {  # for passing parameters to class genome/
    "mtype"      : "gene",   # "gene" (default), "protein", or "contig"
    "headerType" : "short",  # "full", "short" (default), "truncated", "compound" # compound header is header + contig
    "filename"   : ""
    }

import subprocess

##### Genome #1 genes
fLines = ANNOTATION_FILE1.read().splitlines()
extractGeneCalls(genome1,fLines)
ANNOTATION_FILE1.close()
#p = subprocess.Popen(['pwd'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
#pwd = p.stdout.read()[:-1]
#printFile1 = pwd + "/" + files["geneFile1"]
printFile1 = files["geneFile1"]
print "Printing to file", printFile1
print "based on annotationFile1:", files["annotationFile1"]
printFastas2fileArgs["filename"] = printFile1
success = genome1.printFastas2file(printFastas2fileArgs)
print "Success in printing gene fastas to file:", success
genome1.printAll()

##### Genome #2 genes
fLines = ANNOTATION_FILE2.read().splitlines()
extractGeneCalls(genome2,fLines)
ANNOTATION_FILE2.close()
#p = subprocess.Popen(['pwd'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
#pwd = p.stdout.read()[:-1]
#printFile2 = pwd + "/" + files["geneFile2"]
printFile2 = files["geneFile2"]
print "Printing to file", printFile2
print "based on annotationFile2:", files["annotationFile2"]
printFastas2fileArgs["filename"] = printFile2
success = genome2.printFastas2file(printFastas2fileArgs)
print "Success in printing gene fastas to file:", success


#########################################################################################
# Translate protein sequences from gene sequences for genomes 1 & 2
# EMBOSS will write translations to input filename
# Capture translations in genomes' protein lists
#########################################################################################

#*** Note: Translate genes even if not doing blast for protein

translationArgs = { # for passing parameters to class genomeSequence/genome.makeBlastDBs method
    "embossHome"  : EMBOSS_HOME,
    "geneticCode" : GENETIC_CODE,
    "geneFile"    : "",
    "proteinFile" : ""
    }

print "Translating genes for both genomes...."

translationArgs["geneFile"] = files["geneFile1"]
translationArgs["proteinFile"] = files["proteinFile1"]
genome1.translateGenes(translationArgs)            # EMBOSS writes protein translations to file
PROT_FILE = open(files["proteinFile1"],"r")
fLines = PROT_FILE.read().splitlines()             # read lines into list, removing newlines
genome1.write2proteinSet(fLines)                   # Store translations in genome object
genome1.cleanUpAfterEMBOSS(translationArgs)        # EMBOSS messes with headers...so fix them
printFastas2fileArgs["filename"] = files["proteinFile1"]
printFastas2fileArgs["mtype"] = "protein"
genome1.printFastas2file(printFastas2fileArgs)     # Replace EMBOSS's file of translated proteins w/fixed fastas
genome1.printGenomeData()
PROT_FILE.close()

translationArgs["geneFile"] = files["geneFile2"]
translationArgs["proteinFile"] = files["proteinFile2"]
genome2.translateGenes(translationArgs)            # EMBOSS writes protein translations to file
PROT_FILE = open(files["proteinFile2"],"r")   
fLines = PROT_FILE.read().splitlines()             # read lines into list, removing newlines
genome2.write2proteinSet(fLines)                   # Store translations in genome object
genome2.cleanUpAfterEMBOSS(translationArgs)        # EMBOSS messes with headers...so fix them
printFastas2fileArgs["filename"] = files["proteinFile2"]
genome2.printFastas2file(printFastas2fileArgs)     # Replace EMBOSS's file of translated proteins w/fixed fastas
genome2.printGenomeData()
PROT_FILE.close()

print "Translation complete."

#########################################################################################################
# Create blast databases for gene and protein multi-fasta files 
#########################################################################################################

blastDBargs = {  # for passing parameters to class genomeSequence/makeBlastDBs method
    "dbType"   : "nucl", # default
    "filename" : ""
    }

if PROTEIN:
    print "Creating blast databases for genome 1 and genome 2 gene and protein sets..."
else:
    print "Creating blast databases for genome 1 and genome 2 gene sets..."

myBlast = blastAnalysis.blast()                # Make blast object

blastDBargs["dbType"] = "nucl"         # Set up for nucleotide blast
blastDBargs["filename"] = files["geneFile1"]
myBlast.makeBlastDB(blastDBargs)
blastDBargs["filename"] = files["geneFile2"]
myBlast.makeBlastDB(blastDBargs)

if PROTEIN:
    blastDBargs["dbType"] = "prot"         # Set up for protein blast
    blastDBargs["filename"] = files["proteinFile1"]
    myBlast.makeBlastDB(blastDBargs)
    blastDBargs["filename"] = files["proteinFile2"]
    myBlast.makeBlastDB(blastDBargs)

print "Blast database creation complete."

#####################################################################################
# Perform blast of gene and protein sets between genomes and against self
#####################################################################################

# Prepare parameters for blast

blastArgs = {
    "query"         : "",
    "subject"       : "",
    "mtype"         : "nucl",
    "evalue"        : EVALUE, 
    "identity"      : BLAST_IDENTITY,
    "scoreEdge"     : SCORE_EDGE,
    "maxTargetSeqs" : MAX_TARGET_SEQS,
    "overhang"      : OVERHANG,
    "outputFormat"  : OUTPUT_FORMAT, 
    "outfile"       : ""
}

print "Blasting gene sets..."
blastArgs["mtype"]   = "nucl"

print "Genome 1 genes against genome 2 genes..."
blastArgs["query"]   = files["geneFile1"]
blastArgs["subject"] = files["geneFile2"]
blastArgs["maxTargetSeqs"] = 1 

# Need the raw filename (without directory information) to construct blast output filenames
files["geneFile1_root"] = GetRootFile(files["geneFile1"])
files["geneFile2_root"] = GetRootFile(files["geneFile2"])
files["protFile1_root"] = GetRootFile(files["proteinFile1"])
files["protFile2_root"] = GetRootFile(files["proteinFile2"])

### Genome 1 - Genome 2

outfile = OUT_DIR + files["geneFile1_root"] + "_" + files["geneFile2_root"] + "_" + "blastn_" +\
    str(blastArgs["evalue"]) + "_" + str(blastArgs["identity"]) + ".out"
blastArgs["outfile"] = outfile
files["g1_g2_blastn"] = outfile
if BLAST_ON:
    result = myBlast.performBlast(blastArgs)
    print "Result of blasting genes genome1-genome2:", result

### Genome 2 - Genome 1

print "Genome 2 genes against genome 1 genes..."
blastArgs["query"]   = files["geneFile2"]
blastArgs["subject"] = files["geneFile1"]
blastArgs["maxTargetSeqs"] = 1 
outfile = OUT_DIR + files["geneFile2_root"] + "_" + files["geneFile1_root"] + "_" + "blastn_" +\
    str(blastArgs["evalue"]) + "_" + str(blastArgs["identity"]) + ".out"
blastArgs["outfile"] = outfile
files["g2_g1_blastn"] = outfile
if BLAST_ON:
    result = myBlast.performBlast(blastArgs)
    print "Result of blasting genes genome2-genome1:", result

### Genome 1 - Genome 1

print "Genome 1 genes against self..."
blastArgs["query"]   = files["geneFile1"]
blastArgs["subject"] = files["geneFile1"]
blastArgs["maxTargetSeqs"] = 5 
outfile = OUT_DIR + files["geneFile1_root"] + "_" + files["geneFile1_root"] + "_" + "blastn_" +\
    str(blastArgs["evalue"]) + "_" + str(blastArgs["identity"]) + ".out"
blastArgs["outfile"] = outfile
files["g1_g1_blastn"] = outfile
if BLAST_ON:
    result = myBlast.performBlast(blastArgs)
    print "Result of blasting genes genome1-genome1:", result

### Genome 2 - Genome 2 

print "Genome 2 genes against self..."
blastArgs["query"]   = files["geneFile2"]
blastArgs["subject"] = files["geneFile2"]
blastArgs["maxTargetSeqs"] = 5 
outfile = OUT_DIR + files["geneFile2_root"] + "_" + files["geneFile2_root"] + "_" + "blastn_" +\
    str(blastArgs["evalue"]) + "_" + str(blastArgs["identity"]) + ".out"
blastArgs["outfile"] = outfile
files["g2_g2_blastn"] = outfile
if BLAST_ON:
    result = myBlast.performBlast(blastArgs)
    print "Result of blasting genes genome2-genome1:", result

print "Blasting of gene sets complete."

### Proteome 1 - Proteome 2
if PROTEIN:
    print "Blasting protein sets..."
    blastArgs["mtype"]   = "prot"

    print "Genome 1 proteins against genome 2 proteins..."
    blastArgs["query"]   = files["proteinFile1"]
    blastArgs["subject"] = files["proteinFile2"]
    blastArgs["maxTargetSeqs"] = 1 
    outfile = OUT_DIR + files["protFile1_root"] + "_" + files["protFile2_root"] + "_" + "blastn_" +\
        str(blastArgs["evalue"]) + "_" + str(blastArgs["identity"]) + ".out"
    blastArgs["outfile"] = outfile
    files["g1_g2_blastp"] = outfile
    if BLAST_ON:
        result = myBlast.performBlast(blastArgs)
        print "Result of blasting proteins genome1-genome2:", result

    ### Proteome 2 - Proteome 1

    print "Genome 2 proteins against genome 1 proteins..."
    blastArgs["query"]   = files["proteinFile2"]
    blastArgs["subject"] = files["proteinFile1"]
    blastArgs["maxTargetSeqs"] = 1 
    outfile = OUT_DIR + files["protFile2_root"] + "_" + files["protFile1_root"] + "_" + "blastn_" +\
        str(blastArgs["evalue"]) + "_" + str(blastArgs["identity"]) + ".out"
    blastArgs["outfile"] = outfile
    files["g2_g1_blastp"] = outfile
    if BLAST_ON:
        result = myBlast.performBlast(blastArgs)
        print "Result of blasting proteins genome2-genome1:", result

    ### Proteome 1 - Proteome 1
 
    print "Genome 1 proteins against self..."
    blastArgs["query"]   = files["proteinFile1"]
    blastArgs["subject"] = files["proteinFile1"]
    blastArgs["maxTargetSeqs"] = 5 
    outfile = OUT_DIR + files["protFile1_root"] + "_" + files["protFile1_root"] + "_" + "blastn_" +\
        str(blastArgs["evalue"]) + "_" + str(blastArgs["identity"]) + ".out"
    blastArgs["outfile"] = outfile
    files["g1_g1_blastp"] = outfile
    if BLAST_ON:
        result = myBlast.performBlast(blastArgs)
        print "Result of blasting proteins genome1-genome1:", result
 
    ### Proteome 2 - Proteome 2

    print "Genome 2 proteins against self..."
    blastArgs["query"]   = files["proteinFile2"]
    blastArgs["subject"] = files["proteinFile2"]
    blastArgs["maxTargetSeqs"] = 5 
    outfile = OUT_DIR + files["protFile2_root"] + "_" + files["protFile2_root"] + "_" + "blastn_" +\
        str(blastArgs["evalue"]) + "_" + str(blastArgs["identity"]) + ".out"
    blastArgs["outfile"] = outfile
    files["g2_g2_blastp"] = outfile
    if BLAST_ON:
        result = myBlast.performBlast(blastArgs)
        print "Result of blasting proteins genome2-genome2:", result

    print "Blasting of protein sets complete."

#########################################################################################################
# Parse blast output files; write hits to data structures 
#########################################################################################################

print "Recording gene hits...",

gene12hitList = myBlast.recordHits(files["g1_g2_blastn"])
gene21hitList = myBlast.recordHits(files["g2_g1_blastn"])
gene11hitList = myBlast.recordHits(files["g1_g1_blastn"])
gene22hitList = myBlast.recordHits(files["g2_g2_blastn"])

print "Done!"

if PROTEIN:

    print "Recording protein hits...",

    prot12hitList = myBlast.recordHits(files["g1_g2_blastp"])
    prot21hitList = myBlast.recordHits(files["g2_g1_blastp"])
    prot11hitList = myBlast.recordHits(files["g1_g1_blastp"])
    prot22hitList = myBlast.recordHits(files["g2_g2_blastp"])

    print "Done!"

#########################################################################################################
# Identify mutual best hits, singluar best hits, loners, homologs, and paralogs
##########################################################################################################

lonerArgs = {
    "seqList1"     : None,
    "seqList2"     : None,
    "comparedHits" : None  # homology object returned by blast.compareHits method
}
#**************************************************************
print "Identifying gene mutual best hits and singular hits...",
parameters["type"] = "gene"
geneComparison = myBlast.compareHits(gene12hitList,gene21hitList,parameters)
print "Done!"

print "Identifying gene loners...",
lonerArgs["seqList1"] = genome1.geneSet
lonerArgs["seqList2"] = genome2.geneSet
lonerArgs["comparedHits"] = geneComparison
geneComparison = myBlast.identifyLoners(lonerArgs)
print "Done!"

print "Identifying gene paralogs...",
myBlast.identifyParalogs(genome1.geneSet,gene11hitList,parameters)
myBlast.identifyParalogs(genome2.geneSet,gene22hitList,parameters)
print "Done!"

#**************************************************************

if PROTEIN:
    print "Identifying protein mutual best hits and singular hits...",
    parameters["type"] = "protein"
    proteinComparison = myBlast.compareHits(prot12hitList,prot21hitList,parameters)
    print "Done!"

    print "Identifying protein loners...",
    lonerArgs["seqList1"] = genome1.proteinSet
    lonerArgs["seqList2"] = genome2.proteinSet
    lonerArgs["comparedHits"] = proteinComparison
    proteinComparison = myBlast.identifyLoners(lonerArgs)
    print "Done!"

    print "Identifying protein paralogs...",
    myBlast.identifyParalogs(genome1.proteinSet,prot11hitList,parameters)
    myBlast.identifyParalogs(genome2.proteinSet,prot22hitList,parameters)
    print "Done!"

#######################################################################################################
# Tally and report genome1/2 gene/protein comparison statistics  
#######################################################################################################
#*** Testing:  are summary statistics correct?

geneComp_stats = geneComparison.reportStats()  # reminder: a homology object
genome1_gene_stats = genome1.geneSet.reportStats() # reminder: a multi-fasta object
genome2_gene_stats = genome2.geneSet.reportStats()

if PROTEIN:
    protComp_stats = proteinComparison.reportStats()
    genome1_prot_stats = genome1.proteinSet.reportStats()
    genome2_prot_stats = genome2.proteinSet.reportStats()

SUMMARY = open(summaryFile,"w")
SUMMARY.write("\n%s\n" % ("************Next Report************"))
SUMMARY.write("%s%s\n" % ("Genome: ",files["genomeFile1"]))
SUMMARY.write("%s%s\n" % ("Genome: ",files["genomeFile2"]))
for stat in geneComp_stats:
    SUMMARY.write("%s\n" % (stat))
if PROTEIN:
    for stat in protComp_stats:
        SUMMARY.write("%s\n" % (stat))
for stat in genome1_gene_stats:
    SUMMARY.write("%s\n" % (stat))

if PROTEIN:
    for stat in genome1_prot_stats:
        SUMMARY.write("%s\n" % (stat))
    for stat in genome2_gene_stats:
        SUMMARY.write("%s\n" % (stat))
    for stat in genome2_prot_stats:
        SUMMARY.write("%s\n" % (stat))

SUMMARY.close()
"""
geneComparison.reportStats()
proteinComparison.reportStats()
genome1.geneSet.reportStats()
genome1.proteinSet.reportStats()
genome2.geneSet.reportStats()
genome2.proteinSet.reportStats()
"""

#######################################################################################################
# Combine mutual and singular best hits and unique genes/proteins in order wrt genome1
#######################################################################################################

# Perform data line merging
geneMergeList = geneComparison.mergeAll(genome1.geneSet,genome2.geneSet)
if PROTEIN:
    proteinMergeList = proteinComparison.mergeAll(genome1.proteinSet,genome2.proteinSet)

# Write merged data lines for gene analysis to out file
OUT = open(outFile,"w")
OUT.write("%s" % ("GENE COMPARISON RESULTS:\n"))
for hitItem in geneMergeList:
    OUT.write("%s%s" % (hitItem,"\n"))

# Write merged data lines for protein analysis to out file
if PROTEIN:
    OUT.write("%s" % ("PROTEIN COMPARISON RESULTS:\n"))  #*** Skipping protein for now
    for hitItem in proteinMergeList:
        OUT.write("%s%s" % (hitItem,"\n"))

OUT.close()

#######################################################################################################
# Create report
#######################################################################################################

# Create gene report
REPORT = open(reportFile,"w")
REPORT.write("%s" % ("#GENE HITS\n"))
for line in geneMergeList:
    for item in line:
        REPORT.write("%s%s" % (item,"\t"))
    REPORT.write("%s" % ("\n"))

# Create protein report
if PROTEIN:
    REPORT.write("%s" % ("#PROTEIN HITS\n"))   #*** Skipping protein for now
    for line in proteinMergeList:
        for item in line:
            REPORT.write("%s%s" % (item,"\t"))
        REPORT.write("%s" % ("\n"))
REPORT.close()

#########################################################################################################
# Clean Up
#########################################################################################################

LOG.close()

##### Copy result files out from Results_xxx directory into base user directory
#***  For pairwise comparison, that means: out, summary, report files
#***  For NxN comparisons, that means overall results files (not yet generated) 

EMAIL_DIR   = BASE_DIR 
logCopy     = os.path.join(EMAIL_DIR, LOG_COPY)
outCopy     = os.path.join(EMAIL_DIR, OUT_FILE)
reportCopy  = os.path.join(EMAIL_DIR, REPORT_FILE)
summaryCopy = os.path.join(EMAIL_DIR, SUMMARY_FILE)
call(["cp", logFile,     logCopy])
call(["cp", outFile,     outCopy])
call(["cp", reportFile,  reportCopy])
call(["cp", summaryFile, summaryCopy])

print "done!"

#######################################################################################################
