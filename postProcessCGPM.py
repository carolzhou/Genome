#!/usr/bin/env python

###################################################################
#
# postProcessCGPM.py
#
# This program post-processes the output file produced by code
# compareGeneProfiles_main.py, "compareGeneProfiles_main.report".
# The output of postProcessCGPM.py is a report specifying the 
# following:
#    * gene matches
#    * potential split gene calls
#    * potential overlapping genes or alternative start sites
#    * possible missing fractions of genes
#    * possible missed gene calls
#    * possible missed matching genes (loner similarity by annotation)
#    * paralogs
#    * triplets (geneA -- relationship -- geneB) 
#
# Input parameters, format specifications, and default values:
# Files:
#    genome sequence files (in multi-fasta format; -g1 and -g2)
#    input report file generated by compareGeneProfiles_main.py
#
# Output: postProcessCGPM.report, containing report as described above
#
# Programmer:  Carol L. Ecale Zhou 
# Last update:  22 March 2014
#
###################################################################
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
import fastaSequence

##### FILES

LOGFILE = open("./postProcessCGPM.log","w")
today = os.popen('date')
LOGFILE.write("%s\n" % (today.read()))
REPORT_FILE = "./postProcessCGPM.report" 

##########################################################################
##### PATTERNS

p_fasta   = re.compile('\.(fasta)|(fna)|(fas)|(fnt)|(fa)')
p_report  = re.compile('\.report')
p_comment = re.compile('^#')

########################################################################
##### DECLARATIONS 

##### CONSTANTS
 
HELP_STRING = "This program post-processes a report file, called compareGeneProfiles.report, produced by code,\ncompareGeneProfiles_main.py. The output of postProcessCGPM.py is a report specifying the following:\n   * gene matches\n   * potential split gene calls\n   * potential overlapping genes or alternative start sites\n   * possible missing fractions of genes\n   * possible missed matching genes\n   * possible missing gene calls\n   * possible missed matching genes (loner similarity by annotation)\n   * paralogs\n   * triplets (geneA -- relationship -- geneB)\nNote: some feature are under construction."
 
USAGE_STRING = "Usage:  postProcessCGPM.py <g1_gene_file.fa> <g2_gene_file.fa> <compareGeneProfiles_main.report>\nOr, postProcessCGPM.py -g1 <g1_gene_file.fa> -g2 <g2_gene_file.fa> -r <reportFile.report>\nType: postProcessCGPM.py help, for more information>" 

INPUT_STRING = "You may enter parameters interactively (via prompt) by typing: compareGeneProfiles_main.py -interactive\n"   

ACCEPTABLE_ARG_COUNT = (2,4,7) # 2 if "help", "input", or "interactive" 

#DEBUG = True
#DEBUG = False

##### VARIABLES

# Fill these in later for user-defined parameters
parameters = { # defaults as indicated
    "COVERAGE_DIFF"           : 20,
    "NEARLY_FULL"             : 98,
    "START_DIFF"              : 20,
    "SIMILAR_GENOMES"         : True 
}

files = { # User's input files go here
"geneFile1"     : "",
"geneFile2"     : "",
"inReportFile"  : "",
"outReportFile" : "postProcessCGPM.report"
}

fileError = False    # assume all is ok until proven otherwise

##### DATA STRUCTURES


##### FUNCTIONS ##############################################################

# Function GetArguments

def GetArguments(parameters,files):
    # get Files
    sys.stdout.write("Please enter the filename for genome #1 gene fasta sequences:")
    files["geneFile1"] = sys.stdin.readline().rstrip()
    sys.stdout.write("Genome #2 gene fasta sequence filename:")
    files["geneFile2"] = sys.stdin.readline().rstrip()
    sys.stdout.write("Please enter the report from compareGeneProfiles_main.py:")
    files["inReportFile"] = sys.stdin.readline().rstrip()
    GET_PARAMS = False
    sys.stdout.write("Do you want to accept all defaults? enter y/n  ")
    decision = sys.stdin.readline().rstrip()
    if decision.lower() == "n" or decision.lower() == "no":
        GET_PARAMS = True 
    # get Parameters
    if GET_PARAMS:
        pass

################################################################################
# Get command-line arguments
################################################################################

argCount = len(sys.argv)
if argCount in ACCEPTABLE_ARG_COUNT:
    match = re.search("help", sys.argv[1].lower())
    if match:
        print HELP_STRING
        print USAGE_STRING
        LOGFILE.close(); exit(0)
    match = re.search("input", sys.argv[1].lower())
    if match:
        print INPUT_STRING
        LOGFILE.close(); exit(0)
    match = re.search("interactive", sys.argv[1].lower())
    if match:
        GetArguments(parameters,files)
    elif argCount == 4:  # arguments must be in order
        files["geneFile1"] = sys.argv[1]
        files["geneFile2"] = sys.argv[2]
        files["inReportFile"] = sys.argv[3]
    elif argCount == 7:  # arguments follow argument identifier
        for i in range(argCount):
            if sys.argv[i] == "-g1":
                files["geneFile1"] = sys.argv[i+1]; next
            if sys.argv[i] == "-g2":
                files["geneFile2"] = sys.argv[i+1]; next
            if sys.argv[i] == "-r":
                files["inReportFile"] = sys.argv[i+1]; next
    else:
        print USAGE_STRING
        LOGFILE.close(); exit(0)
else:
    print USAGE_STRING
    LOGFILE.write("%s\n" % ("Incorrect number of command-line arguments provided"))
    LOGFILE.close(); exit(0)

# Check files
match = re.search(p_fasta, files["geneFile1"])
if not match:
    fileError = True
match = re.search(p_fasta, files["geneFile2"])
if not match:
    fileError = True
match = re.search(p_report, files["inReportFile"])
if not match:
    fileError = True
if fileError:
    print "Check the formats of your input files:"
    print "    Gene fasta file #1:     ", files["geneFile1"]
    print "    Gene fasta file #2:     ", files["geneFile2"]
    print "    Report file:            ", files["inReportFile"]
    print USAGE_STRING
    LOGFILE.close(); exit(0)

# Open files
try:
    GENE_FILE1 = open(files["geneFile1"],"r")
except IOError as e:
    fileError = True
    print e
try:
    GENE_FILE2 = open(files["geneFile2"],"r")
except IOError as e:
    fileError = True
    print e
try:
    IN_REPORT_FILE = open(files["inReportFile"],"r")
except IOError as e:
    fileError = True
    print e
if fileError:
    LOGFILE.close(); exit(0)

# Record to log and keep in touch with user
LOGFILE.write("%s" % ("Parameters are: \n"))
LOGFILE.write("%s%s%s" % ("gene file #1: ",files["geneFile1"],"\n"))
LOGFILE.write("%s%s%s" % ("gene file #2: ",files["geneFile2"],"\n"))
LOGFILE.write("%s%s%s" % ("report file:  ",files["inReportFile"],"\n"))

REPORT_FILE = open(files["outReportFile"],"w")  
REPORT_FILE.write("%s%s%s" % ("#gene file #1: ",files["geneFile1"],"\n"))
REPORT_FILE.write("%s%s%s" % ("#gene file #2: ",files["geneFile2"],"\n"))

print "Parameters are:"
print "Gene file #1:", files["geneFile1"]
print "Gene file #2:", files["geneFile2"]
print "Input report file: ", files["inReportFile"]
print "Output report file: ", files["outReportFile"]
print "Parameters:"
keys = list(parameters); keys.sort()
for key in keys:
    print key, "is", parameters[key]

#########################################################################
# Construct multi-fasta objects for geneFile1 and geneFile2 data sets

fLines = GENE_FILE1.read().splitlines() # read lines into list, removing newlines
geneSet1 = fastaSequence.multiFasta()   # create multi-fasta object
geneSet1.addFastas(fLines,"nt")         # load it up!
GENE_FILE1.close()

fLines = GENE_FILE2.read().splitlines() # same for genome #2's genes
geneSet2 = fastaSequence.multiFasta()
geneSet2.addFastas(fLines,"nt")
GENE_FILE2.close()

#########################################################################
# Create nested array(list) data structure for inReportFile data

blastResults = []  # holds a list of dataLines
dataLine     = []  # holds a single blast result and additional data

# dataLine fields are as follows (0-23 taken from class blastAnalysis, method mergeAll):
# Fields for hitLine (0-19):
# 0: sortPostion                               - used below to sort all hitLines relative to genome 1
# 1: genome_hitType - "genome1"|"genome2" + "_" + "mutual"|"singular"|"loner"
# 2-5: qStart,qEnd,sStart,sEnd                 - query/subject start/end values from blast output
# 6-7: identity,evalue                         - from blast output
# 8: "query"|"subject"|"loner"
# 9: g1header                                  - header of genome 1 sequence
# 10: g1contig
# 11: annotations                              - annotations attached to query sequence
# 12-14: g1Start_onGenome,g1End_onGenome,g1Strand - genome1 gene/protein start/end
# 15: "query"|"subject"|"loner"
# 16: g2header                                 - header of genome2 sequence
# 17: g2contig
# 18: g2annotations                            - annotations attached to subject sequence
# 19-21: g2start_onGenome,g2end_onGenome,g2strand - subject gene/protein start/end on its genome
# 22: G1coverage                               - genome1's gene/protein coverage in blast hit
# 23: G2coverage                               - genome2's gene/protein coverage in blast hit
# 24: alignmentLength                          - reported by blast
# 25: gapopens                                 - reported by blast
# 26: g1span                                   - calculated
# 27: g1length                                 - calculated
# 28: g2span                                   - calculated
# 29: g2length                                 - calculated

# Messages to be inserted in comments field of data line
FLIP_STRAND_MSG = "Hit to reverse strand of sequence" 
SPLIT_GENE_MSG  = "Possible split gene call on genome"  
MISSING_SEGMENT_MSG = "Possible extra or missing domain"
ALTERNATE_START_MSG = "Possible alternate start codon"
OVERLAPPING_HIT_MSG = "Hits appear to overlap"
PARALOG_MSG         = "Could be paralog or gene duplication"
START_CODON_MSG     = "Check start codon on gene from genome"
ATG_CODON_MSG       = "Start codon is not ATG on gene from genome"

# Columns and their contents; all but ones at end exist in input report file 
# For readability, field numbers are set as constants:
SORT_POSITION      = 0
GENOME_HITTYPE     = 1
Q_START            = 2 
Q_END              = 3
S_START            = 4 
S_END              = 5 
IDENTITY           = 6 
EVALUE             = 7 
G1_HIT_TYPE        = 8 
G1_HEADER          = 9 
G1_CONTIG          = 10
G1_ANNOTATIONS     = 11   
G1_START_ON_GENOME = 12
G1_END_ON_GENOME   = 13
G1_STRAND          = 14
G2_HIT_TYPE        = 15
G2_HEADER          = 16
G2_CONTIG          = 17
G2_ANNOTATIONS     = 18
G2_START_ON_GENOME = 19
G2_END_ON_GENOME   = 20
G2_STRAND          = 21 
G1_COVERAGE        = 22
G2_COVERAGE        = 23
ALIGNMENT_LENGTH   = 24
GAP_OPENS          = 25
G1_SPAN            = 26
G1_LENGTH          = 27
G2_SPAN            = 28
G2_LENGTH          = 29
ALERT_LIST         = 30  # list of detected items of note and anomalies
G1_SEQUENCE        = 31  # fill this in if possible alternate start site(s)
G2_SEQUENCE        = 32  # ditto

#########################################################################
# Identify anomalous matches

prevDataList = []
prevG1cds = ""
prevG2cds = ""
prevG1start = 0
prevG1end   = 0
prevG2start = 0
prevG2end   = 0
prevQstart  = 0
prevSstart  = 0
prevQend    = 0
prevSend    = 0
alertList = []
alertString = ""
FLIPPED = False
PREVIOUS_FLIPPED = False

# if SIMILAR_GENOMES:  # assume closely related for now; 
IN_REPORT_FILE = open(files["inReportFile"],"r")
fLines = IN_REPORT_FILE.read().splitlines()
IN_REPORT_FILE.close()
#REPORT_FILE = open(files["outReportFile"],"w")  #*** already opened up at top
today = os.popen('date')
REPORT_FILE.write("%s%s%s" % ("#Post-processing of compareGeneProfiles.report on ", today.read(), "\n"))

for line in fLines:
    commentLine = re.search(p_comment, line)
    if commentLine or line == "":
        REPORT_FILE.write("%s%s" % (line,"\n"))
    else:
        # Set up a whole bunch of variables
        dataList = line.split('\t')
        dataList.append(""); dataList.append(""); dataList.append("") # make room for more data
        (genome,hitType) = dataList[GENOME_HITTYPE].split('_')  
        G1headerFields = dataList[G1_HEADER].split('/')
        G2headerFields = dataList[G2_HEADER].split('/')
        G1cds = G1headerFields[0]
        G2cds = G2headerFields[0] 
        if G1cds:
            G1start = int(dataList[G1_START_ON_GENOME])
            G1end   = int(dataList[G1_END_ON_GENOME])
        else:
            G1start = 0
            G1end   = 0
        if G2cds:
            G2start = int(dataList[G2_START_ON_GENOME])
            G2end   = int(dataList[G2_END_ON_GENOME])
        else:
            G2start = 0
            G2end   = 0
        G1distance = G1start - prevG1end  # measures distance between successive gene calls
        G2distance = G2start - prevG2end  # if real close, then might be split gene call
        if dataList[G1_COVERAGE]:
            G1coverage = int(dataList[G1_COVERAGE])
        else:
            G1coverage = 0
        if dataList[G2_COVERAGE]:
            G2coverage = int(dataList[G2_COVERAGE])
        else:
            G2coverage = 0
        if dataList[GAP_OPENS]:
            gapOpens   = int(dataList[GAP_OPENS])

        # Detect missing/added segments between matched genes, hits to reverse strand, and possible adjacent paralogs
        if hitType == "mutual" or hitType == "singular": 
            Qstart = int(dataList[Q_START])
            Qend   = int(dataList[Q_END])
            Sstart = int(dataList[S_START])
            Send   = int(dataList[S_END])
            if G1coverage < 0 or G2coverage < 0: # if coverage computes to negative, then hit was in reverse orientation 
                alertList.append("a)" + FLIP_STRAND_MSG)
                FLIPPED = True 
            if (gapOpens == 0 or gapOpens == 1) and abs(G1coverage - G2coverage) > parameters["COVERAGE_DIFF"]: # one seq may be missing a domain
                alertList.append("b)" + MISSING_SEGMENT_MSG) 
            if G1cds == prevG1cds:
                alertList.append("c)" + PARALOG_MSG + " on genome 2") # if same gene occurs twice, then possible paralogs on other genome...
            if G2cds == prevG2cds:                                       # ...or could be (more likely) split gene (catch below)
                alertList.append("d)" + PARALOG_MSG + " on genome 1")

            # Detect possible alternate start sites; PREVIOUS_FLIPPED gets set below, based on FLIPPED outcome
            if not PREVIOUS_FLIPPED:  # when previous hit was to reverse orientation, coverage goes negative, so calculation below is not meaningful
                if G1coverage >= parameters["NEARLY_FULL"] and (100 - G2coverage) >= parameters["COVERAGE_DIFF"]: # could exist alternate start codon 
                    if genome == "genome1":  # genome 2 gene is the subject
                        if abs(Sstart - prevSend) <= parameters["START_DIFF"]:  
                            alertList.append("e)" + ALTERNATE_START_MSG + " on genome 2") 
                            fasta = geneSet2.matchHeader(dataList[G2_HEADER])
                            ATGsequence = fasta.highlightAllStartCodons()
                            dataList[G2_SEQUENCE] = ATGsequence
                            #print "Sort loc is", dataList[0], "abs diff Sstart minus prevSend is", Sstart, "-", prevSend, "is", abs(Sstart - prevSend)
                    elif genome == "genome2":  # genome 2 gene is the query (#***???)
                        if abs(Qstart - prevQend) <= parameters["START_DIFF"]:
                            alertList.append("f)" + ALTERNATE_START_MSG + " on genome 2")
                            fasta = geneSet2.matchHeader(dataList[G2_HEADER])
                            ATGsequence = fasta.highlightAllStartCodons()
                            dataList[G2_SEQUENCE] = ATGsequence
                if G2coverage >= parameters["NEARLY_FULL"] and (100 - G1coverage) >= parameters["COVERAGE_DIFF"]: # could exist alternate start codon
                    if genome == "genome2":  # genome1 gene is the subject 
                        if abs(Sstart - prevSend) <= parameters["START_DIFF"]:  # genome1 gene is the subject
                            alertList.append("g)" + ALTERNATE_START_MSG + " on genome 1")
                            fasta = geneSet1.matchHeader(dataList[G1_HEADER])
                            ATGsequence = fasta.highlightAllStartCodons()
                            dataList[G1_SEQUENCE] = ATGsequence
                    elif genome == "genome1":  # genome 2 gene is the subject (#***???)
                        if abs(Qstart - prevQend) <= parameters["START_DIFF"]:
                            alertList.append("h)" + ALTERNATE_START_MSG + " on genome 1")
                            fasta = geneSet1.matchHeader(dataList[G1_HEADER])
                            ATGsequence = fasta.highlightAllStartCodons()
                            dataList[G1_SEQUENCE] = ATGsequence

            if G1distance == 0 or G1distance == 3:  # gene call could be split (0|1 codon apart)
                alertList.append("i)" + SPLIT_GENE_MSG + "1") 
                fasta = geneSet1.matchHeader(dataList[G1_HEADER])
                if fasta.getStartCodon().lower() != "atg":
                    alertList.append("k)" + ATG_CODON_MSG + "1") 
                sequence = fasta.highlightAllStartCodons()
                dataList[G1_SEQUENCE] = sequence
                startType = fasta.verifyProkaryoticStartCodon()
                alertList.append("m)" + START_CODON_MSG + "1, type is: " + startType)
            if G2distance == 0 or G2distance == 3:
                alertList.append("j)" + SPLIT_GENE_MSG + "2")
                fasta = geneSet2.matchHeader(dataList[G2_HEADER])
                if fasta.getStartCodon().lower() != "atg":
                    alertList.append("l)" + ATG_CODON_MSG + "2") 
                sequence = fasta.highlightAllStartCodons()
                dataList[G2_SEQUENCE] = sequence
                startType = fasta.verifyProkaryoticStartCodon()
                alertList.append("n)" + START_CODON_MSG + "2, type is: " + startType)
            prevQstart = Qstart
            prevQend   = Qend
            prevSstart = Sstart
            prevSend   = Send

        if hitType == "loner":
            if G1cds == prevG1cds:  # genome1_loner
                alertList.append("o)" + SPLIT_GENE_MSG + " on genome 1")
                #***  This section of code has redundancy due to confusion regarding set1 vs. set2
                fasta1 = geneSet1.matchHeader(dataList[G1_HEADER])
                fasta2 = geneSet2.matchHeader(dataList[G1_HEADER])
                fasta3 = geneSet1.matchHeader(dataList[G2_HEADER])
                fasta4 = geneSet2.matchHeader(dataList[G2_HEADER])
                if fasta1:
                    dataList[G1_SEQUENCE] = fasta1.sequence
                    startType = fasta1.verifyProkaryoticStartCodon()
                elif fasta2:
                    dataList[G1_SEQUENCE] = fasta2.sequence
                    startType = fasta2.verifyProkaryoticStartCodon()
                elif fasta3:
                    dataList[G2_SEQUENCE] = fasta3.sequence
                    startType = fasta3.verifyProkaryoticStartCodon()
                elif fasta4:
                    dataList[G2_SEQUENCE] = fasta4.sequence
                    startType = fasta4.verifyProkaryoticStartCodon()
                else:
                    dataList[G1_SEQUENCE] = "no sequence found"
                    startType = "unknown"
                alertList.append("q)" + START_CODON_MSG + "1, type is: " + startType)
            if G2cds == prevG2cds:  # genome2_loner
                alertList.append("p)" + SPLIT_GENE_MSG + " on genome 2")
                #***  This section of code has redundancy due to confusion regarding set1 vs. set2
                fasta1 = geneSet1.matchHeader(dataList[G1_HEADER])
                fasta2 = geneSet2.matchHeader(dataList[G1_HEADER])
                fasta3 = geneSet1.matchHeader(dataList[G2_HEADER])
                fasta4 = geneSet2.matchHeader(dataList[G2_HEADER])
                if fasta1:
                    dataList[G1_SEQUENCE] = fasta1.sequence
                    startType = fasta1.verifyProkaryoticStartCodon()
                elif fasta2:
                    dataList[G1_SEQUENCE] = fasta2.sequence
                    startType = fasta2.verifyProkaryoticStartCodon()
                elif fasta3:
                    dataList[G2_SEQUENCE] = fasta3.sequence
                    startType = fasta3.verifyProkaryoticStartCodon()
                elif fasta4:
                    dataList[G2_SEQUENCE] = fasta4.sequence
                    startType = fasta4.verifyProkaryoticStartCodon()
                else:
                    dataList[G2_SEQUENCE] = "no sequence found"
                    startType = "unknown"
                alertList.append("r)" + START_CODON_MSG + "2, type is: " + startType)

        prevDataList = dataList
        prevG1cds   = G1cds
        prevG2cds   = G2cds
        prevG1start = G1start
        prevG1end   = G1end
        prevG2start = G2start
        prevG2end   = G2end
        PREVIOUS_FLIPPED = FLIPPED
        FLIPPED = False

        # write newly annotated data line to output report file
        for alert in alertList:
            alertString = alertString + "; " + alert 
        alertString = alertString.lstrip(';')
        dataList[ALERT_LIST] = alertString
        for data in dataList:
            REPORT_FILE.write("%s%s" % (data,"\t"))
        REPORT_FILE.write("%s" % ("\n"))
        alertList = []  # reset
        alertString = ""

REPORT_FILE.close() 
LOGFILE.close()
