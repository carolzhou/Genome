##############################################
# Module: blastAnalysis.py
# Programmer:  Carol L. Ecale Zhou
# Date of last update:  16 July 2013
#
# Module comprising data structures and methods for blasting the genes and proteins
#    of two genome objects and comparing the gene profiles and the nt and aa levels.
#
# Classes and methods: 
#     hit 
#         printAll
#         printAll2file
#     hitList
#         append
#         printAll
#         printAll2file
#     homology
#         reportStats
#         printAll
#         printAll2file
#         mergeAll
#     paralog
#         printAll
#         printAll2file
#     blast
#         identifyLoners
#         identifyParalogs
#         compareHits
#         recordHits
#         printHits
#         printHits2file
#         makeBlastDB
#         performBlast
#
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

import string
import fastaSequence
import genomeSequence
import annotation
import re, os, copy
import operator
from itertools import groupby   # used in mergeAll method # changed sort method 16july2013

# Default values used if user- or program-defined defaults not provided
GENE_MATCH_IDENTITY_DEFAULT = 95
GENE_MATCH_COVERAGE_DEFAULT = 95
GENE_SIMILARITY_IDENTITY_DEFAULT = 60
GENE_SIMILARITY_COVERAGE_DEFAULT = 75
DOMAIN_MATCH_IDENTITY_DEFAULT = 95
DOMAIN_MATCH_COVERAGE_DEFAULT = 45
DOMAIN_SIMILARITY_IDENTITY_DEFAULT = 60
DOMAIN_SIMILARITY_COVERAGE_DEFAULT = 45
PARALOG_MATCH_IDENTITY_DEFAULT = 95
PARALOG_MATCH_COVERAGE_DEFAULT = 95
PARALOG_SIMILARITY_IDENTITY_DEFAULT = 60
PARALOG_SIMILARITY_COVERAGE_DEFAULT = 75
PARALOG_DOMAIN_MATCH_IDENTITY_DEFAULT = 95
PARALOG_DOMAIN_MATCH_COVERAGE_DEFAULT = 45
PARALOG_DOMAIN_SIMILARITY_IDENTITY_DEFAULT = 60
PARALOG_DOMAIN_SIMILARITY_COVERAGE_DEFAULT = 45
PROTEIN_MATCH_IDENTITY_DEFAULT = 95
PROTEIN_MATCH_COVERAGE_DEFAULT = 95
PROTEIN_SIMILARITY_IDENTITY_DEFAULT = 60
PROTEIN_SIMILARITY_COVERAGE_DEFAULT = 75
PROTEIN_DOMAIN_MATCH_IDENTITY_DEFAULT = 95
PROTEIN_DOMAIN_MATCH_COVERAGE_DEFAULT = 45
PROTEIN_DOMAIN_SIMILARITY_IDENTITY_DEFAULT = 60
PROTEIN_DOMAIN_SIMILARITY_COVERAGE_DEFAULT = 45
PROTEIN_PARALOG_MATCH_IDENTITY_DEFAULT = 95
PROTEIN_PARALOG_MATCH_COVERAGE_DEFAULT = 95
PROTEIN_PARALOG_SIMILARITY_IDENTITY_DEFAULT = 60 
PROTEIN_PARALOG_SIMILARITY_COVERAGE_DEFAULT = 75
PROTEIN_PARALOG_DOMAIN_MATCH_IDENTITY_DEFAULT = 95
PROTEIN_PARALOG_DOMAIN_MATCH_COVERAGE_DEFAULT = 45
PROTEIN_PARALOG_DOMAIN_SIMILARITY_IDENTITY_DEFAULT = 60
PROTEIN_PARALOG_DOMAIN_SIMILARITY_COVERAGE_DEFAULT = 45

p_comment = re.compile('^#')

##############################################################################################
class hit(object):
   
    def __init__(self):
        self.queryHeader     = ""
        self.subjectHeader   = ""
        self.identity        = ""
        self.alignmentLength = 0
        self.mismatches      = None
        self.gapopens        = None
        self.queryStart      = 0
        self.queryEnd        = 0
        self.subjectStart    = 0
        self.subjectEnd      = 0
        self.evalue          = 0
        self.bitscore        = 0
        self.queryCoverage   = 0  # calculate later, when we get q/s lengths
        self.subjectCoverage = 0
        self.hitType         = "unknown"  # fill in with "mutual best", "singular best"

    def computeCoverage(self,queryLength,subjectLength):
        errorCode = [] # for debug
        if queryLength == 0 or subjectLength == 0:
            errorCode.append(1) 
            return errorCode
        qLen = float(queryLength)
        sLen = float(subjectLength)
        qSpan = float(int(self.queryEnd) - int(self.queryStart) + 1)
        sSpan = float(int(self.subjectEnd) - int(self.subjectStart) + 1)
        self.queryCoverage = int(round(100*qSpan/qLen))
        self.subjectCoverage = int(round(100*sSpan/sLen))
        return (self.queryCoverage,self.subjectCoverage) 

    def printAll(self):
        print "query:", self.queryHeader
        print "subject:", self.subjectHeader
        print "hit type:", self.hitType
        print "identity:", self.identity
        print "alignment length:", self.alignmentLength
        print "mismatches:", self.mismatches
        print "gapopens:", self.gapopens
        print "query start/end:", self.queryStart, "/", self.queryEnd
        print "subject start/end:", self.subjectStart, "/", self.subjectEnd
        print "evalue:", self.evalue
        print "bitscore:", self.bitscore
        print "query/subject coverage:", self.queryCoverage, "/", self.subjectCoverage

    def printAll2file(self,FILE_HANDLE):
        FILE_HANDLE.write("%s%s%s" % ("query:",self.queryHeader,"\n"))
        FILE_HANDLE.write("%s%s%s" % ("subject:",self.subjectHeader,"\n"))
        FILE_HANDLE.write("%s%s%s" % ("hit type:",self.hitType,"\n"))
        FILE_HANDLE.write("%s%s%s" % ("identity:",self.identity,"\n"))
        FILE_HANDLE.write("%s%s%s" % ("alignment length:",self.alignmentLength,"\n"))
        FILE_HANDLE.write("%s%s%s" % ("mismatches:",self.mismatches,"\n"))
        FILE_HANDLE.write("%s%s%s" % ("gapopens:",self.gapopens,"\n"))
        FILE_HANDLE.write("%s%s%s%s%s" % ("query start/end:",self.queryStart,"/",self.queryEnd,"\n"))
        FILE_HANDLE.write("%s%s%s%s%s" % ("subject start/end:",self.subjectStart,"/",self.subjectEnd,"\n"))
        FILE_HANDLE.write("%s%s%s" % ("evalue:",self.evalue,"\n"))
        FILE_HANDLE.write("%s%s%s" % ("bitscore:",self.bitscore,"\n"))
        FILE_HANDLE.write("%s%s%s%s%s" % ("query/subject coverage:",self.queryCoverage,"/",self.subjectCoverage,"\n"))

###########################################################################################################
class hitList(object): # Holds output from a blast run plus meta-data about the run

    def __init__(self):
        self.blastHits = []  # list of hit objects
        self.type = "unknown"  # "mutual best", "singular", "loner", "paralog"
        self.identityCutoff = "unknown" 
        self.evalueCutoff   = "unknown" 

    def append(self,newHit):
        self.blastHits.append(newHit)

    def printAll(self):
        for hit in self.blastHits:
            hit.printAll()

    def printAll2file(self,FILE_HANDLE):
        for hit in self.blastHits:
            hit.printAll2file(FILE_HANDLE)

###########################################################################################################
class homology(object):  # holds comparative information between 2 gene/protein sets
    
    def __init__(self):
        self.mutualBestHits = { #*** CHECK WHETHER THE VALUES SHOULD BE TYPE "None" (can Python accept user-defined type?) 
            "set1" : [],   # NOTE: using literal list of hit objects here; python doesn't like my user-defined type
            "set2" : []    # type list of hit objects 
        }
        self.singularHits = {
            "set1" : [],   # type list of hit objects 
            "set2" : []    # type list of hit objects 
        } 
        self.loners = {
            "set1" : [],   # type FastaSequence
            "set2" : []    # type FastaSequence
        }

    def computeCoverage(self,seqList1,seqList2):  # NEEDS TESTING 
        # This method fills in fields hit.queryCoverage and hit.subjectCoverage
        seqLength1 = {}
        seqLength2 = {}
        for seq in seqList1:
            seqLength1[seqList1.header] = len(seqList1.sequence)
        for seq in seqList2:
            seqLength2[seqList2.header] = len(seqList2.sequence)
        for hit in self.mutualBestHits["set1"]:
            hit.computeCoverage(seqLength1[hit.queryHeader],seqLength2[hit.subjectHeader])
        for hit in self.mutualBestHits["set2"]:
            hit.computeCoverage(seqLength2[hit.queryHeader],seqLength1[hit.subjectHeader])
        for hit in self.singularHits["set1"]:
            hit.computeCoverage(seqLength1[hit.queryHeader],seqLength2[hit.subjectHeader])
        for hit in self.singluarHits["set2"]:
            hit.computeCoverage(seqLength2[hit.queryHeader],seqLength1[hit.subjectHeader])

    def mergeAll(self,seqList1,seqList2):  
        # This method merges all of the hit types (plus loners) for both genomes.
        # First, a list is constructed 
        # comprising the reference genome's genes and their mutual best and singular
        # hits to the other genome's genes; this list includes genome 1's loners.
        # Then, genome 2's singular hits are added, with reference location based
        # on the reference genome--thus, according to the start positions of the
        # subject (gene in reference genome that was hit by genome 2's gene). Then
        # this combined list is sorted by genome 1's gene start positions.
        # Genome 2's loners are then merged in by fitting them in between the closest
        # (mutual or singular) hits (i.e., subject start) to reference genome genes.
        # Note that there may not be a single uniquely best location to place genome 
        # 2's loners, but a reasonably good position is found using this approach.

        errorCode      = [] # for debugging
        mergeList      = [] # array/list of hits and loners for gene/protein set1 (i.e., seqList1)
        hitLine        = [] # array if items to be appended to mergeList

        #########################################################################################
        # Fields for hitLine (0-19):
        # 0: sortPostion                               - used below to sort all hitLines relative to genome 1
        # 1: genome_hitType - "genome1"|"genome2" + "_" + "mutual"|"singular"|"loner"
        # 2-5: qStart,qEnd,sStart,sEnd                 - query/subject start/end values from blast output 
        # 6-7: identity,evalue                         - from blast output
        # 8: "query"|"subject"|"loner"                 - role in blast hit, or if no hit was found 
        # 9: g1header                                  - header of query sequence
        # 10: g1 query sequence contig (ie, parent sequence of gene)  #*** new
        # 11: g1annotations                             - annotations attached to query sequence
        # 12-14: g1Start_onGenome,g1End_onGenome,g1Strand - gene/protein start/end on its genome
        # 15: "query"|"subject"|"loner"
        # 16: g2header                                 - header of subject sequence
        # 17: g2 subject sequence contig (ie, parent sequence of gene) #*** new
        # 18: g2annotations                            - annotations attached to subject sequence
        # 19-21: g2Start_onGenome,g2sEnd_onGenome,g2Strand - subject gene/protein start/end on its genome
        # 22: G1coverage                               - genome1's gene/protein coverage in blast hit
        # 23: G2coverage                               - genome2's gene/protein coverage in blast hit
        # 24: alignmentLength                          - reported by blast
        # 25: gapopens                                 - reported by blast
        # 26: g1segment                                - span within blast alignment
        # 27: g1length                                 - length of g1 gene
        # 28: g2segment                                - span within blast alignment
        # 29: g2length                                 - length of g2 gene
        #########################################################################################

        # Fields for hitLine (0-32):
        SORT_POSITION      = 0
        GENOME_HIT_TYPE    = 1
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
 
        #########################################################################################

        ##### Set up data structures for quick access to annotations and sequence lengths
        #seqAnnot1  = {}   # key = header, value = annotations, for genome1 genes/proteins
        #seqAnnot2  = {}   # ditto, for genome2
        #seqLength1 = {}   # key = header, value = length of sequence for genome1 genes/proteins
        #seqLength2 = {}   # ditto, for genome2
        #seqContig1 = {}   # key = header, value = parent sequence (ie, contig name) for genome1 gene

        ##### Set up data structures for quick access to annotations and sequence lengths
        seqAnnot1  = {}   # key = header, value = annotations, for genome1 genes/proteins
        seqAnnot2  = {}   # ditto, for genome2
        seqLength1 = {}   # key = header, value = length of sequence for genome1 genes/proteins
        seqLength2 = {}   # ditto, for genome2
        seqContig1 = {}   # key = header, value = parent sequence (ie, contig name) for genome1 gene
        seqContig2 = {}   # ditto, for genome2

        annotations = []
        for seq in seqList1.fastaList:
            aList = list(seq.annotationList)
            for annot in aList:
                annotations.append(list(annot.annotationList))
            seqAnnot1[seq.header] = list(annotations) 
            annotations = []  # reset
            seqLength1[seq.header] = len(seq.sequence)
            seqContig1[seq.header] = seq.parentSequence
        for seq in seqList2.fastaList:
            aList = list(seq.annotationList)
            for annot in aList:
                annotations.append(list(annot.annotationList))
            seqAnnot2[seq.header] = list(annotations)
            annotations = []  # reset 
            seqLength2[seq.header] = len(seq.sequence)
            seqContig2[seq.header] = seq.parentSequence

        # Create lists to hold different categories of hits and loners 
        quickMutual1   = []
        quickSingular1 = []
        quickLoner1    = []
        quickSingular2 = []
        quickLoner2    = [] 

        # Capture mutual Best Hits for Genome 1   #*** CONTINUE HERE
        for hit in self.mutualBestHits["set1"]:  
            (qLocusTag,qStrand,qStart,qEnd,junk) = hit.queryHeader.split('/') #*** should split to list then pull data by index
            (sLocusTag,sStrand,sStart,sEnd,junk) = hit.subjectHeader.split('/')
            qAnnotations = seqAnnot1[hit.queryHeader]
            sAnnotations = seqAnnot2[hit.subjectHeader]
            g1segment    = int(hit.queryEnd)   - int(hit.queryStart) + 1
            g2segment    = int(hit.subjectEnd) - int(hit.subjectStart) + 1
            g1length     = seqLength1[hit.queryHeader]
            g2length     = seqLength2[hit.subjectHeader]
            g1Contig     = seqContig1[hit.queryHeader]
            g2Contig     = seqContig2[hit.subjectHeader]
            (g1coverage,g2coverage) = hit.computeCoverage(g1length,g2length)
            sortPosition = qStart   # start position of query gene/protein, relative to genome1
            hitLine = [sortPosition,"genome1_mutual",hit.queryStart,hit.queryEnd,hit.subjectStart,hit.subjectEnd,hit.identity,hit.evalue,"query",hit.queryHeader,g1Contig,qAnnotations,qStart,qEnd,qStrand,"subject",hit.subjectHeader,g2Contig,sAnnotations,sStart,sEnd,sStrand,g1coverage,g2coverage,hit.alignmentLength,hit.gapopens,g1segment,g1length,g2segment,g2length]
            quickMutual1.append(hitLine)

        # Capture singular Best Hits for Genome 1
        for hit in self.singularHits["set1"]:
            (qLocusTag,qStrand,qStart,qEnd,junk) = hit.queryHeader.split('/')
            (sLocusTag,sStrand,sStart,sEnd,junk) = hit.subjectHeader.split('/')
            qAnnotations = seqAnnot1[hit.queryHeader]
            sAnnotations = seqAnnot2[hit.subjectHeader]
            g1segment    = int(hit.queryEnd) - int(hit.queryStart) + 1
            g2segment    = int(hit.subjectEnd) - int(hit.subjectStart) + 1
            g1length     = seqLength1[hit.queryHeader]
            g2length     = seqLength2[hit.subjectHeader]
            g1Contig     = seqContig1[hit.queryHeader]
            g2Contig     = seqContig2[hit.subjectHeader]
            (g1coverage,g2coverage) = hit.computeCoverage(g1length,g2length)
            sortPosition = qStart     # start position of query gene/protein, relative to genome1
            hitLine = [sortPosition,"genome1_singular",hit.queryStart,hit.queryEnd,hit.subjectStart,hit.subjectEnd,hit.identity,hit.evalue,"query",hit.queryHeader,g1Contig,qAnnotations,qStart,qEnd,qStrand,"subject",hit.subjectHeader,g2Contig,sAnnotations,sStart,sEnd,sStrand,g1coverage,g2coverage,hit.alignmentLength,hit.gapopens,g1segment,g1length,g2segment,g2length]
            quickSingular1.append(hitLine)

        # Capture loners for Genome 1
        for seq in self.loners["set1"]:
            annotations = seqAnnot1[seq.header] 
            g1Contig    = seqContig1[seq.header]
            (locusTag,strand,start,end,junk) = seq.header.split('/')
            sortPosition = start             # no hit, actually; reference position is gene/protein start on genome 1
            hitLine = [sortPosition,"genome1_loner","","","","","","","loner",seq.header,g1Contig,annotations,start,end,strand,"","","","","","","","","","","","","","",""] 
            quickLoner1.append(hitLine)

        # Load hits & loners for genome 1 (i.e., reference genome's genes/proteins) into merge list 
        for hitLine in quickMutual1:
            mergeList.append(hitLine)
        for hitLine in quickSingular1:
            mergeList.append(hitLine)
        for loner in quickLoner1:
            mergeList.append(loner)

        # Prepare to insert genome2's singular hits and loners to mergeList
        # First, capture genome2's singular hits and loners in 'hitList' format 

        # Capture singular hits for genome2
        for hit in self.singularHits["set2"]:
            sAnnotations = seqAnnot1[hit.subjectHeader]  #*** Double check this for accuracy
            qAnnotations = seqAnnot2[hit.queryHeader]    #*** Double check this for accuracy
            g1segment    = int(hit.subjectEnd) - int(hit.subjectStart) + 1
            g2segment    = int(hit.queryEnd)   - int(hit.queryStart) + 1
            g1length     = seqLength1[hit.subjectHeader]
            g2length     = seqLength2[hit.queryHeader]
            g1Contig     = seqContig1[hit.subjectHeader]
            g2Contig     = seqContig2[hit.queryHeader]
            (g2coverage,g1coverage) = hit.computeCoverage(g2length,g1length)
            (qLocusTag,qStrand,qStart,qEnd,junk) = hit.queryHeader.split('/')
            (sLocusTag,sStrand,sStart,sEnd,junk) = hit.subjectHeader.split('/')
            sortPosition = sStart  # relative to genome1 (the subject)
            hitLine = [sortPosition,"genome2_singular",hit.queryStart,hit.queryEnd,hit.subjectStart,hit.subjectEnd,hit.identity,hit.evalue,"subject",hit.subjectHeader,g1Contig,sAnnotations,sStart,sEnd,sStrand,"query",hit.queryHeader,g2Contig,qAnnotations,qStart,qEnd,qStrand,g1coverage,g2coverage,hit.alignmentLength,hit.gapopens,g1segment,g1length,g2segment,g2length]
            quickSingular2.append(hitLine) 

        # Capture loners for genome 2, but note that there is no hit, so no reference to genome 1
        for seq in self.loners["set2"]:
            annotations = seqAnnot2[seq.header]
            g2Contig    = seqContig2[seq.header]
            (locusTag,strand,start,end,junk) = seq.header.split('/')
            hitLine = ["0","genome2_loner","","","","","","","","","","","","","","loner",seq.header,g2Contig,annotations,start,end,strand,"","","","","","","",""]
            quickLoner2.append(hitLine) 

        # Append genome2's singular hits to mergeList and sort mergeList
        for hitLine in quickSingular2:
            mergeList.append(hitLine)
        g1contig_position = lambda x: (x[G1_CONTIG], int(x[SORT_POSITION]))
        mergeList.sort(key=g1contig_position)

        # Find a suitable location for each genome2 loner (place according to cds number along genome 2) #*** Try, but maybe better to lump at top
        for loner in quickLoner2:
            lonerIndex = 0  # will place loner at front of mergeList unless a better location is found (see below)
            lonerContig     = loner[G2_CONTIG]
            lonerHeader     = loner[G2_HEADER]
            lonerHeaderList = lonerHeader.split('/')
            lonerCDSlist    = lonerHeaderList[0].split('cds') 
            lonerCDSnumber  = lonerCDSlist[1] 
            # Identify location for genome2's loner after line containing that genome's previous cds number
            for hitLine in mergeList: 
                if lonerContig == hitLine[G2_CONTIG]: # look for location within same contig on genome 2
                    g2Header     = hitLine[G2_HEADER]
                    g2HeaderList = g2Header.split('/')
                    g2CDSlist    = g2HeaderList[0].split('cds') 
                    g2CDSnumber  = g2CDSlist[1] 
                    # CDSs should be (pretty much) in order, based on having been sorted (above)
                    if int(lonerCDSnumber) > int(g2CDSnumber):  
                        # find index of this g2 data line in mergeList...
                        lonerIndex = mergeList.index(hitLine) + 1   #  place loner just after 
                        break  # found where to insert
            # Lastly, add genome2's loner to mergeList at position lonerIndex
            mergeList.insert(lonerIndex,loner)

        # Create a header for the mergeList; Make deep copy (new memory) of mergeList and return it
        headerLine = ["#sortPos","genome_type","qStart","qEnd","sStart","sEnd","identity","evalue","Q|S|Loner","G1header","G1contig","G1annotations","G1geneStart","G1geneEnd","G1strand","Q|S|Loner","G2header","G2contig","G2annotations","G2geneStart","G2geneEnd","G2strand","G1coverage","G2coverage","alignmentLength","gapOpens","g1span","g1length","g2span","g2length"]
        mergeList.insert(0,headerLine)
        newMergeList = copy.deepcopy(mergeList)  #*** ? Pretty sure dynamic memory is needed
        return newMergeList  

    def reportStats(self):
        statsList = []
        set1mutuals = len(self.mutualBestHits["set1"])
        set2mutuals = len(self.mutualBestHits["set2"])
        set1singulars = len(self.singularHits["set1"])
        set2singulars = len(self.singularHits["set2"])
        set1loners = len(self.loners["set1"])
        set2loners = len(self.loners["set2"])

        print "Set 1 mutual best hits:", set1mutuals
        print "Set 2 mutual best hits:", set2mutuals
        print "Set 1 singular hits:", set1singulars
        print "Set 2 singular hits:", set2singulars
        print "Set 1 loners:", set1loners
        print "Set 2 loners:", set2loners 

        statsList.append("Set 1 mutual best hits: " + str(set1mutuals))
        statsList.append("Set 2 mutual best hits: " + str(set2mutuals))
        statsList.append("Set 1 singular hits: " + str(set1singulars))
        statsList.append("Set 2 singular hits:" + str(set2singulars))
        statsList.append("Set 1 loners: " + str(set1loners))
        statsList.append("Set 2 loners: " + str(set2loners))
        return statsList

    def printAll(self):
        print "List of mutual best hits for set 1:"
        for hit in self.mutualBestHits["set1"]:   #*** Test if it works to say, "self.mutualBestHits["set1"].printAll()"
            hit.printAll()
        print "End list of mutual best hits for set 1."
        print "List of mutual best hits for set 2:"
        for hit in self.mutualBestHits["set2"]:
            hit.printAll()
        print "End of list of mutual best hits for set 2."
        print "List of singular best hits for set 1:"
        for hit in self.singularHits["set1"]:
            hit.printAll()
        print "End of list of singular best hits for set 1."
        print "List of singular best hits for set 2:"
        for hit in self.singularHits["set2"]:
            hit.printAll()
        print "End of list of singular best hits for set 2."
        print "List of loners for set 1:"
        for seq in self.loners["set1"]:
            seq.printAll()
        print "End of list of loners for set 1."
        print "List of loners for set 2:"
        for seq in self.loners["set2"]:
            seq.printAll()
        print "End of list of loners for set 2."

    def printAll2file(self,FILE_HANDLE): 
        FILE_HANDLE.write("%s" % ("List of mutual best hits for set 1:\n"))
        for hit in self.mutualBestHits["set1"]:   
            hit.printAll2file(FILE_HANDLE)
        FILE_HANDLE.write("%s" % ("End list of mutual best hits for set 1.\n"))
        FILE_HANDLE.write("%s" % ("List of mutual best hits for set 2:\n"))
        for hit in self.mutualBestHits["set2"]:
            hit.printAll2file(FILE_HANDLE)
        FILE_HANDLE.write("%s" % ("End of list of mutual best hits for set 2.\n"))
        FILE_HANDLE.write("%s" % ("List of singular best hits for set 1:\n"))
        for hit in self.singularHits["set1"]:
            hit.printAll2file(FILE_HANDLE)
        FILE_HANDLE.write("%s" % ("End of list of singular best hits for set 1.\n"))
        FILE_HANDLE.write("%s" % ("List of singular best hits for set 2:\n"))
        for hit in self.singularHits["set2"]:
            hit.printAll2file(FILE_HANDLE)
        FILE_HANDLE.write("%s" % ("End of list of singular best hits for set 2.\n"))
        FILE_HANDLE.write("%s" % ("List of loners for set 1:\n"))
        for seq in self.loners["set1"]:
            seq.printAll2file(FILE_HANDLE)
        FILE_HANDLE.write("%s" % ("End of list of loners for set 1.\n"))
        FILE_HANDLE.write("%s" % ("List of loners for set 2:\n"))
        for seq in self.loners["set2"]:
            seq.printAll2file(FILE_HANDLE)
        FILE_HANDLE.write("%s" % ("End of list of loners for set 2.\n"))

###########################################################################################################
class paralog(object):  #
    def __init__(self):
        self.header = ""      # header of paralog's fasta sequence
        self.blastHit = None  # hit object that links this paralog

    def printAll(self):
        print "Paralogs information:"
        print "header:", self.header
        print "blast hit:"
        self.blastHit.printAll()

    def printAll2file(self,FILE_HANDLE):
        FILE_HANDLE.write("%s" % ("Paralogs information:\n"))
        FILE_HANDLE.write("%s%s%s" % ("header:",self.header,"\n"))
        FILE_HANDLE.write("%s" % ("blast hit:\n"))
        self.blastHit.printAll2file(FILE_HANDLE)
        
###########################################################################################################
class blast(object):

    # Class blast creates blast databases and performs blast between 2 fasta sets and compares results

    def __init__(self):
        self.blastHits = hitList()  # List of hit objects w/associated data 
        self.blastHit = hit()
        self.paralogT = paralog()   # paralog template
        self.homologs = homology()

    def identifyLoners(self,kvargs):  # kvargs contains 2 sequence lists and a homology object
        if "seqList1" in kvargs.keys():       # a multi-fasta object
            seqList1 = kvargs["seqList1"]
        else:
            return False
        if "seqList2" in kvargs.keys():       # a multi-fasta object
            seqList2 = kvargs["seqList2"]
        else:
            return False
        if "comparedHits" in kvargs.keys():   # a homology object
            comparedHits = kvargs["comparedHits"]
        else:
            return False

        mutualHitList1   = comparedHits.mutualBestHits["set1"]
        mutualHitList2   = comparedHits.mutualBestHits["set2"]
        singularHitList1 = comparedHits.singularHits["set1"]
        singularHitList2 = comparedHits.singularHits["set2"]
        lonerList1       = comparedHits.loners["set1"]
        lonerList2       = comparedHits.loners["set2"]

        hadahit = False
        for seq in seqList1.fastaList:
            for hit in mutualHitList1:  
                if seq.header == hit.queryHeader:
                    hadahit = True
            for hit in singularHitList1:
                if seq.header == hit.queryHeader:
                    hadahit = True 
            if not hadahit:
                lonerList1.append(seq)
            hadahit = False  # reset

        hadahit = False
        for seq in seqList2.fastaList:
            for hit in mutualHitList2:
                if seq.header == hit.queryHeader:
                    hadahit = True
            for hit in singularHitList2:
                if seq.header == hit.queryHeader:
                    hadahit = True
            if not hadahit:
                lonerList2.append(seq)
            hadahit = False  # reset
        return comparedHits   # returns a homology object
 
    def identifyParalogs(self,inList1,inList2,kvargs):
        paralogCount = 0
        if "type" in kvargs.keys():
            mType = kvargs["type"]
        if mType.lower() == "gene":
            if "paralogMatchIdentity" in kvargs.keys():
                identity = kvargs["paralogMatchIdentity"]
            else:
                identity = PARALOG_MATCH_IDENTITY_DEFAULT
            if "paralogMatchCoverage" in kvargs.keys():
                coverage = kvargs["paralogMatchCoverage"]
            else:
                coverage = PARALOG_MATCH_IDENTITY_DEFAULT
        elif mType.lower() == "protein":
            if "proteinParalogMatchIdentity" in kvargs.keys():
                identity = kvargs["proteinParalogMatchIdentity"]
            else:
                identity = PROTEIN_PARALOG_MATCH_IDENTITY_DEFAULT
            if "proteinParalogMatchCoverage" in kvargs.keys():
                coverage = kvargs["proteinParalogMatchCoverage"]
            else:
                coverage = PROTEIN_PARALOG_MATCH_IDENTITY_DEFAULT
        else:
            return False

        # For each sequence, record any qualifying hits to other sequences in the genome 
        for seq in inList1.fastaList:
            for nextHit in inList2.blastHits:  # check if it's a hit of seq against non-self seq
                if seq.header == nextHit.queryHeader and nextHit.queryHeader != nextHit.subjectHeader:
                    if nextHit.identity >= identity:  # check hit quality
                        newParalog = copy.deepcopy(self.paralogT) # replicate the paralog template
                        newParalog.header = nextHit.subjectHeader
                        newParalog.blastHit = nextHit
                        seq.paralogList.append(newParalog) # add to list of paralogs for this sequence object
                        paralogCount += 1 
        return paralogCount 

    def compareHits(self,inList1,inList2,kvargs): # Compare hits between 2 gene/protein sets
        newComparison = copy.deepcopy(self.homologs)
        errorCode = []  # for debug
        if "type" in kvargs.keys():
            mType = kvargs["type"]
        if mType.lower() == "gene":
            if "geneMatchIdentity" in kvargs.keys():
                identity = kvargs["geneMatchIdentity"]
            else:
                identity = GENE_MATCH_IDENTITY_DEFAULT
            if "geneMatchCoverage" in kvargs.keys():
                coverage = kvargs["geneMatchCoverage"]
            else:
                coverage = GENE_MATCH_COVERAGE_DEFAULT
        elif mType.lower() == "protein":
            if "proteinMatchIdentity" in kvargs.keys():
                identity = kvargs["proteinMatchIdentity"]
            else:
                identity = PROTEIN_MATCH_IDENTITY_DEFAULT
            if "proteinMatchCoverage" in kvargs.keys():
                coverage = kvargs["proteinMatchCoverage"]
            else:
                coverage = PROTEIN_MATCH_COVERAGE_DEFAULT
        else:
            errorCode.append(1)

        # Compare hits between 2 input hitList objects 
        for hit1 in inList1.blastHits:
            for hit2 in inList2.blastHits: 
                if hit1.subjectHeader == hit2.queryHeader and hit2.subjectHeader == hit1.queryHeader:
                    newComparison.mutualBestHits["set1"].append(hit1)
                    newComparison.mutualBestHits["set2"].append(hit2)
                    hit1.hitType = "mutual best"
                    hit2.hitType = "mutual best"
                elif hit1.subjectHeader == hit2.queryHeader:  # hit1's top (but not mutual)
                    newComparison.singularHits["set1"].append(hit1)
                    hit1.hitType = "singular best"
                elif hit2.subjectHeader == hit1.queryHeader:  # hit2's top (but not mutual)
                    newComparison.singularHits["set2"].append(hit2)
                    hit2.hitType = "singlular best"
        if errorCode:
            print "Method compareHits errorCode:", errorCode
        return newComparison

    def recordHits(self,filename):
        HIT_FILE = open(filename,"r")
        newHitList = copy.deepcopy(self.blastHits) 
        fLines = HIT_FILE.read().splitlines()  # read lines into list, removing newlines
        for line in fLines:
            match = re.search(p_comment, line)
            if not match:
                fields = line.split('\t')
                newHit = copy.deepcopy(self.blastHit)
                newHit.queryHeader     = fields[0]
                newHit.subjectHeader   = fields[1]
                newHit.identity        = fields[2]
                newHit.alignmentLength = fields[3]
                newHit.mismatches      = fields[4]
                newHit.gapopens        = fields[5]
                newHit.queryStart      = fields[6]
                newHit.queryEnd        = fields[7]
                newHit.subjectStart    = fields[8]
                newHit.subjectEnd      = fields[9]
                newHit.evalue          = fields[10]
                newHit.bitscore        = fields[11]
                newHitList.append(newHit)
        HIT_FILE.close()
        return(newHitList)

    def printHits(self,hitList):
        hitList.printAll()

    def printHits2file(self,hitList,FILE_HANDLE):
        hitList.printAll2file(FILE_HANDLE)

    def makeBlastDB(self,kvargs):  # Create blastDBs for contigs, genes, proteins
        if "dbType" in kvargs.keys():
            databaseType = kvargs["dbType"].lower()
        else:
            databaseType = "nucl"
        if "filename" in kvargs.keys():
            filename = kvargs["filename"]
        else:
            return False
        if databaseType == "nucl" or databaseType == "nt" or databaseType == "dna":
            command = "makeblastdb -in " + filename + " -dbtype nucl -logfile " + filename + ".blastdb1_nucl_log"
        elif databaseType == "prot" or databaseType == "aa" or databaseType == "protein":
            command = "makeblastdb -in " + filename + " -dbtype prot -logfile " + filename + ".blastdb1_prot_log"
        else:
            return False
        myResult = os.system(command)
        return myResult

    def performBlast(self,kvargs):
        command = ""
        errorList = []

        # Gather parameters for blast
        if "query" in kvargs.keys():        # The sequences being blasted
            query = kvargs["query"]
        else:
            errorList.append(1) 
        if "subject" in kvargs.keys():      # The database that is being blasted against
            subject = kvargs["subject"]
        else:
            errorList.append(2)
        if "mtype" in kvargs.keys():
            mtype = kvargs["mtype"]
        else:
            errorList.append(3) 
        if "evalue" in kvargs.keys():
            evalue = str(kvargs["evalue"])
        else:
            evalue = str(0.01)              # default
        if "identity" in kvargs.keys():
            identity = str(kvargs["identity"])
        else:
            identity = str(50)              # default
        if "scoreEdge" in kvargs.keys():    # Best hit score edge
            scoreEdge = str(kvargs["scoreEdge"])
        else:
            scoreEdge = str(0.05)           # default
        if "maxTargetSeqs" in kvargs.keys():
            maxTargetSeqs = str(kvargs["maxTargetSeqs"])
        else:
            maxTargetSeqs = str(1)          # default
        if "overhang" in kvargs.keys():     # Blast hit overhang
            overhang = str(kvargs["overhang"])
        else:
            overhang = str(0.25)            # default
        if "outputFormat" in kvargs.keys():
            outputFormat = str(kvargs["outputFormat"])
        else:
            outputFormat = str(7)           # tabbed list by default
        if "outfile" in kvargs.keys():
            outfile = kvargs["outfile"]
        else:
            errorList.append(4)

        # Blast
        if mtype == "nucl" or mtype == "nt" or mtype == "gene" or mtype == "nucleotide":
            command = "blastn -query " + query + " -out " + outfile + " -task blastn -db " + subject + \
                " -evalue " + evalue + " -best_hit_score_edge " + scoreEdge + " -best_hit_overhang " + \
                overhang + " -outfmt " + outputFormat + " -perc_identity " + identity + \
                " -max_target_seqs " + maxTargetSeqs 
        elif mtype == "prot" or mtype == "aa" or mtype == "protein":
            command = "blastp -query " + query + " -out " + outfile + " -task blastp -db " + subject + \
                " -evalue " + evalue + " -best_hit_score_edge " + scoreEdge + " -best_hit_overhang " + \
                overhang + " -outfmt " + outputFormat + " -max_target_seqs " + maxTargetSeqs
        else:
            errorList.append(10)
        result = os.system(command)
        errorList.append(result)
 
        return errorList 
  
