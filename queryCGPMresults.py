#!/usr/bin/env python


#######################################################
#
# queryCGPMresults.py
#
# Programmer:  Carol L. Ecale Zhou
# Last update:  08 September 2014
#
#################################################################
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

import sys, os, re, string, copy
#from subprocess import call
import subprocess

CODE_BASE_DIR = os.environ["CODE_BASE_DIR"]
#### FILES

inFile            = ""  # list of directories to query. By default all 'Results_' dirs in cwd are queried, but can be user designated subset 
outFile           = os.path.join(CODE_BASE_DIR, "queryCGPMresults.user.out")   # default, but should be user designated
queryFile         = os.path.join(CODE_BASE_DIR, "queryCGPMresults.query")     # holds intermediate results from grepping report file for genome_hitType
logFile           = os.path.join(CODE_BASE_DIR, "queryCGPMresults.log")
ppCGPM_logFile    = "postProcessCGPM.log"           # file by this name in each 'Results_' directory
ppCGPM_reportFile = "postProcessCGPM.report"        # file by this name in each 'Results_' directory
LOGFILE = open(logFile,"w")
LOGFILE.write("%s\n" % ("Begin log file"))

#### CONSTANTS

MAX_PARAMS = 7   # currently, user can specify up to 7 parameters (not counting the '-letter' preceding the parameter)

HELP_STRING = "Script queryCGPMresults.py searches results files generated by compareGeneProfiles_main.py/postProcessCGPM.py and returns a list of matches. For more information, type: queryCGPMresults.py usage, or queryCGPMresults.py input."

USAGE_STRING = "Usage:  python queryCGPMresults.py -g <1|2|3> -s <nt|aa> -h <loner|singular|mutual> -d <dirFile.lst> -o <outFile> -i <i1,i2,i3> -c <cds1,cds2,cds3> (optional parameters, comprising interpretation strings or cds numbers, separated by comma; use -i or -c but not both)"

INPUT_STRING = """Input:  The following parameters may be provided: 
   genome number (1 or 2, or 3 if both) (default: 3)
   sequence type (nt or aa) (default: nt)
   hit type (loner, singular, or mutual best) (default: loner)
   name of a file containing a list of the directories to search (default: none, will read from current directory)
       Note: directories need to be fully qualified (ie, full path provided), 
       or you may provide a common directory under which all directories are 
       located by specifying: baseDir=<dir> as a separate line in your input file. 
       For an example of a correctly formatted input file, see queryCGPMresults.infile.sample.txt. 
   name of the output file where query results will be written (default: queryCGPMresults.user.out)
   Format your input as follows:
       -g 1|2|3 -s nt|aa -h loner|singular|mutual -d <dirsfile> -o <outfile>
   You may also (optinally) provide one or more interpretation codes separated by comma (no spaces between): 
       -i <extra,split,reverse,paralog,alternate,overlap> Note: if more than one, separate with comma (no spaces)
         Meaning:  
           extra = extra or missing domain
           split = split gene call
           reverse = gene call is on reverse strand
           paralog = paralog or gene duplication
           alternate = alternate start codon
           overlap = overlapping genes
   You may also query all of the hits for one or more coding sequences by providing a comma-separated list of numbers:  
        -c <123,456,78910>
"""

GENOME = False; SEQUENCE_TYPE = False; HIT_TYPE = False; INFILE_PARAM = False; OUTFILE_PARAM = False; INTERPRETATION_PARAM = False
ANY = True; 
FLIP = False; 
SPLIT = False; 
XTRA = False; 
ALTERNATE = False; 
OVERLAP = False; 
PARALOG = False; 
NOT_ATG = False; 
CDS = False
# CDS is True if query is for all hits for a given coding sequence (cds number) #*** ???

##### Get command-line arguments

genomeOrdering = 3         # default:  both genomes
sequenceType = "nt"        # default:  nucleotide
hitType = "loner"          # default:  loners (i.e., unique genes)
interpretationString = ""  # from user input
interpretationCodes  = []  # user-input list split by ','
interpretationCode   = ""
cdsList = []
cdsString = ""
cdsNumber = ""

# This is rather complicated, but it filters some possible user error in
# providing the wrong number of command-line arguments, for example
# leaving out the "-letter" prefix for a parameter.
ACCEPTABLE_ARG_COUNT = []  
ACCEPTABLE_ARG_COUNT.append(2)      # if only argument is 'help' etc. 
for x in xrange((MAX_PARAMS+1)*2):  # otherwise, arguments come in pairs (eg, -d <dirsList>)
    if x % 2 == 1:  # x is odd      # recall: sys.argv[0] is the code itself
        ACCEPTABLE_ARG_COUNT.append(x)

argCount = len(sys.argv)
if argCount in ACCEPTABLE_ARG_COUNT:
    if argCount == 2:
        match = re.search("help", sys.argv[1].lower())
        if match:
            print HELP_STRING
            exit(0)
        match = re.search("input", sys.argv[1].lower())
        if match:
            print INPUT_STRING
            exit(0)
        match = re.search("usage", sys.argv[1].lower())
        if match:
            print USAGE_STRING
            exit(0)
    else:
        for i in xrange(argCount):
            if sys.argv[i] == "-g":  # 1 or 2, for genome1 or genome2, and 3 for both, 0 for a single cds, regardless of hit type
                if sys.argv[i+1] == "1" or sys.argv[i+1] == "2" or sys.argv[i+1] == "3" or sys.argv[i+1] == "0":
                    genomeOrdering = sys.argv[i+1].lower()
                    GENOME = True

            if sys.argv[i] == "-s":  # 'nt' or 'aa', for gene or protein
                match = re.search('nt|nucl|gene|dna|aa|prot|peptide|protein', sys.argv[i+1].lower())
                if match:
                    sequenceType = sys.argv[i+1].lower()
                    SEQUENCE_TYPE = True

            if sys.argv[i] == "-h":  # 'loner', 'singular', 'mutual_best', for type of hit
                match = re.search('loner|unique|singular|mutual|best|any|all', sys.argv[i+1].lower())
                if match:
                    hitType = sys.argv[i+1].lower()
                    HIT_TYPE = True

            if sys.argv[i] == "-d":  # directories list filename
                inFile = sys.argv[i+1]
                INFILE_PARAM = True
 
            if sys.argv[i] == "-o":  # output filename
                outFile = sys.argv[i+1]
                OUTFILE_PARAM = True

            if sys.argv[i] == "-i":  # interpretation code (optional)
                interpretationString = sys.argv[i+1]
                INTERPRETATION_PARAM = True
                interpretationCodes = interpretationString.split(',')
                for code in interpretationCodes:
                    match = re.search('extra',code.lower())       # extra or missing domain
                    if match:
                        XTRA = True; ANY = False
                    match = re.search('missing',code.lower())
                    if match:
                        XTRA = True; ANY = False
                    match = re.search('flip',code.lower())        # gene on reverse strand
                    if match:
                        FLIP = True; ANY = False
                    match = re.search('reverse',code.lower())
                    if match:
                        FLIP = True; ANY = False
                    match = re.search('alternate',code.lower())   # alternate start codon
                    if match:
                        ALTERNATE = True; ANY = False
                    match = re.search('overlap',code.lower())     # overlapping genes
                    if match:
                        OVERLAP = True; ANY = False
                    match = re.search('paralog',code.lower())     # paralog or gene duplication
                    if match:
                        PARALOG = True; ANY = False
                    match = re.search('dup',code.lower())         
                    if match:
                        PARALOG = True; ANY = False
                    match = re.search('start',code.lower())       # alternate start codon
                    if match:
                        ALTERNATE = True; ANY = False
                    match = re.search('not',code.lower())         # start codon not ATG
                    if match:
                        NOT_ATG = True; ANY = False

            if sys.argv[i] == "-c":  # coding sequence number provided
                cdsString = sys.argv[i+1]
                cdsList = cdsString.split(',')
                CDS = True

    print "Query will be run with the following parameters:"
    print "    genome ordering =", genomeOrdering
    print "    sequence type =", sequenceType
    print "    hit type =", hitType
    if inFile:
        print "    inFile =", inFile
    else:
        print "    inFile = none provided; using current directory list"
    print "    outFile =", outFile
    print "    cds number =", cdsList
    print "    interpretation codes are", interpretationCodes

    LOGFILE.write("%s\n"   % ("Parameter files are: "))
    LOGFILE.write("%s%s\n" % ("    genomeOrdering: ",genomeOrdering))
    LOGFILE.write("%s%s\n" % ("    sequenceType: ",sequenceType))
    LOGFILE.write("%s%s\n" % ("    hitType: ",hitType))
    if inFile:
        LOGFILE.write("%s%s\n" % ("    inFile: ",inFile))
    else:
        LOGFILE.write("%s\n" % ("    inFile: none provided; using current directory list"))
    LOGFILE.write("%s%s\n" % ("    outFile: ",outFile))
    LOGFILE.write("%s%s\n" % ("    interpretation codes: ",interpretationCodes))
    LOGFILE.write("%s%s\n" % ("    cds numbers: ",cdsList))

else:
    print HELP_STRING
    print USAGE_STRING
    print INPUT_STRING
    exit(0)

##### Open files and get list of Results directories to query

directoryList = []
baseDir = "./"  # default is current working directory

match = re.search('\w',inFile)  # If user provided infile w/dir names, then use it
if match:
    LOGFILE.write("%s%s\n" % ("Reading input file ",inFile))
    INFILE = open(inFile,"r")
    fLines = INFILE.read().splitlines()
    numLines = len(fLines)
    LOGFILE.write("%s%s\n" % ("Number of lines in input file with directories list is ", numLines)) 
    for i in xrange(0,numLines):
        line = fLines[i]
        match = re.search('baseDir',line)
        if match:
            (preamble,baseDir) = line.split('=')
        else:
            match = re.search('\w+', line)
            if match:
                directoryList.append(line)

else:  # If no infile w/dir names was provided, then assume Results dirs are in current working directory 
    command = "ls . | grep \'Results_\'"  # Get list of Results directories in current directory
    proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True) 
    (out, err) = proc.communicate()
    if err:
        print "ERROR:", err
    out = out.rstrip()  # remove pesky terminal newline character
    directoryList = out.split('\n')

# Check directoryList
print "directoryList is", directoryList

OUTFILE = open(outFile,"w")
#QUERY_FILE = open(queryFile,"w")

##### Construct and run queries

sysCommand = "> " + queryFile  # Reminder: queryFile holds intermediate results
os.system(sysCommand)          # create or initialize query.out file 

LOGFILE.write("%s\n" % ("Reading input directories and gathering information"))

ONE = False
TWO = False
if genomeOrdering == 1:
    ONE = True
if genomeOrdering == 2:
    TWO = True
if genomeOrdering == 3:
    ONE = True; TWO = True

print "Processing Results directories..."
for dir in directoryList:
    print "Next dir is", dir
    nextDir = baseDir + dir
    nextLog = nextDir + "/" + ppCGPM_logFile
    NEXT_LOG = open (nextLog,"r")
    fLines = NEXT_LOG.read().splitlines()
    for line in fLines:
        match = re.search('#1',line)
        if match:
            columns = line.split(' ')
            genome1 = columns[3]
        match = re.search('#2',line)
        if match:
            columns = line.split(' ')
            genome2 = columns[3]
    NEXT_LOG.close()

    #nextReport = nextDir + "/" + ppCGPM_reportFile
    sysCommand = "echo \'##### Querying directory\' " + nextDir + " >> " + queryFile
    os.system(sysCommand)
    sysCommand = "echo \'# Gene Set 1 is\' " + genome1 + " >> " + queryFile
    os.system(sysCommand)
    sysCommand = "echo \'# Gene Set 2 is\' " + genome2 + " >> " + queryFile
    os.system(sysCommand)

    print "CDS is", CDS
    if CDS and cdsList != []:
        for cds in cdsList:
            nextCDS = "cds" + cds + "/"
            sysCommand = "grep \'" + nextCDS + "' " + nextDir + "/" + "postProcessCGPM.report >> " + queryFile
            os.system(sysCommand) 
    else:
        if ONE:
            queryString = "genome1_" + hitType  #
            sysCommand = "grep \'" + queryString + "' " + nextDir + "/" + "postProcessCGPM.report >> " + queryFile
            os.system(sysCommand)
        if TWO:
            queryString = "genome2_" + hitType  # 
            sysCommand = "grep \'" + queryString + "' " + nextDir + "/" + "postProcessCGPM.report >> " + queryFile
            os.system(sysCommand)

##### Process raw query text and write to users output file

fields = []  # holds column values from .report file
POS            = 0
GENOME_TYPE    = 1
Q_START        = 2
Q_END          = 3
S_START        = 4
S_END          = 5
IDENTITY       = 6
EVALUE         = 7
QLS1           = 8
G1HEADER       = 9
G1CONTIG       = 10
G1ANNOTATION   = 11
G1GENE_START   = 12
G1GENE_END     = 13
G1STRAND       = 14
QLS2           = 15
G2HEADER       = 16
G2CONTIG       = 17
G2ANNOTATION   = 18
G2GENE_START   = 19
G2GENE_END     = 20
G2STRAND       = 21
G1COVERAGE     = 22
G2COVERAGE     = 23
ALIGN_LENGTH   = 24
GAP_OPENS      = 25
G1SPAN         = 26
G1LENGTH       = 27
G2SPAN         = 28
G2LENGTH       = 29
INTERPRETATION = 30
G1SEQUENCE     = 31
G2SEQUENCE     = 32

### From postProcessCGPM.py:
FLIP_STRAND_MSG     = "Hit to reverse strand of sequence"
SPLIT_GENE_MSG      = "Possible split gene call on genome"
MISSING_SEGMENT_MSG = "Possible extra or missing domain"
ALTERNATE_START_MSG = "Possible alternate start codon"
OVERLAPPING_HIT_MSG = "Hits appear to overlap"
PARALOG_MSG         = "Could be paralog or gene duplication"
START_CODON_MSG     = "Check start codon on gene from genome"
ATG_CODON_MSG       = "Start codon is not ATG on gene from genome"

QUERY_FILE = open(queryFile,"r")
dataLine = ""
EMPTY = "[]"  #*** For now, annotation fields are empty for protein entries
fLines = QUERY_FILE.read().splitlines()
print "Number of lines in query file: ", len(fLines)

count = 0
for line in fLines:
    DO_SELECT = False
    match = re.search('^#',line)
    if match:
        OUTFILE.write("%s\n" % (line))
    else:
        match = re.search('^\d',line)
        if match:
            fields = line.split('\t')
            dataLine = fields[POS]  # always record the position (1st field in tabbed data)
            (genome,hitType) = fields[GENOME_TYPE].split('_')  # will need to determine which kind of hit this is
            if fields[G1ANNOTATION] != EMPTY or fields[G2ANNOTATION] != EMPTY:  #*** Improve this: was skipping protein records
                #if hitType == "mutual":  # always reported as genome1 hits
                #dataLine = dataLine + "\t" + fields[GENOME_TYPE] + "\t" + fields[G1HEADER] + "\t" + fields[G1ANNOTATION]
                #if hitType == "singular":

                if hitType == "mutual" or hitType == "singular":
                    dataLine = dataLine + "\t" + fields[GENOME_TYPE] + "\t" + fields[G1HEADER] + "\t" + fields[G1CONTIG] + "\t" + fields[G1ANNOTATION] + "\t" + fields[G2HEADER]
                    dataLine = dataLine + "\t" + fields[G2CONTIG] + "\t" + fields[G2ANNOTATION] + "\tG1len=" + fields[G1LENGTH] + "\tG2len=" + fields[G2LENGTH]
                    if FLIP:
                        match = re.search(FLIP_STRAND_MSG,fields[INTERPRETATION])
                        if match:
                            dataLine = dataLine + "\t" + fields[INTERPRETATION]
                            DO_SELECT = True
                    elif SPLIT:
                        match = re.search(SPLIT_GENE_MSG,fields[INTERPRETATION])
                        if match:
                            dataLine = dataLine + "\t" + fields[INTERPRETATION]
                            DO_SELECT = True
                    elif XTRA:
                        match = re.search(MISSING_SEGMENT_MSG,fields[INTERPRETATION])
                        if match:
                            dataLine = dataLine + "\t" + fields[INTERPRETATION]
                            DO_SELECT = True
                    elif ALTERNATE:
                        match = re.search(ALTERNATE_START_MSG,fields[INTERPRETATION])
                        if match:
                            dataLine = dataLine + "\t" + fields[INTERPRETATION]
                            DO_SELECT = True
                    elif OVERLAP:
                        match = re.search(OVERLAPPING_HIT_MSG,fields[INTERPRETATION])
                        if match:
                            dataLine = dataLine + "\t" + fields[INTERPRETATION]
                            DO_SELECT = True
                    elif PARALOG:
                        match = re.search(PARALOG_MSG,fields[INTERPRETATION])
                        if match:
                            dataLine = dataLine + "\t" + fields[INTERPRETATION]
                            DO_SELECT = True
                    elif NOT_ATG:
                        match = re.search(ATG_CODON_MSG,fields[INTERPRETATION])
                        if match:
                            dataLine = dataLine + "\t" + fields[INTERPRETATION]
                            DO_SELECT = True
                    elif ANY:
                        dataLine = dataLine + "\t" + fields[INTERPRETATION]
                        DO_SELECT = True
                if hitType == "loner":
                    if genome == "genome1":
                        if fields[G1ANNOTATION] != EMPTY:  #*** improve this; was skipping protein records
                            DO_SELECT = True 
                            dataLine = dataLine + "\t" + fields[GENOME_TYPE] + "\t" + fields[G1HEADER] + "\t" + fields[G1CONTIG] + "\t" + fields[G1ANNOTATION] + "\tG1len=" + fields[G1LENGTH] 
                    if genome == "genome2":
                        if fields[G2ANNOTATION] != EMPTY:  #*** ditto
                            DO_SELECT = True
                            dataLine = dataLine + "\t" + fields[GENOME_TYPE] + "\t" + fields[G2HEADER] + "\t" + fields[G2CONTIG] + "\t" + fields[G2ANNOTATION] + "\tG2len=" + fields[G2LENGTH]
                if DO_SELECT:
                    OUTFILE.write("%s\n" % (dataLine))
                    count += 1
print "Number of hits in out file: ", count
QUERY_FILE.close()

##### Clean up

if inFile:
    INFILE.close()
OUTFILE.close()
LOGFILE.close()

