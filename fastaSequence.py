#############################################################
# Module: fastaSequence.py
# Programmer: Carol L. Ecale Zhou
# Data of last update:  9 July 2013
# Module containing classes and methods for representing a multi-fasta sequence and associated methods
# Classes and methods: 
#     fasta
#         enterGeneData
#         assignType
#         assignHeader
#         removeEMBOSSpostfix
#         removeTerminalAsterisk
#         getHeader
#         getShortHeader
#         getTruncHeader
#         assignSequence
#         consolidate
#         getSequenceLength
#         getSubsequence
#         reverseComplement
#         addAnnotation
#         getStartCodon
#         highlightAllStartCodons
#         printFasta
#         printFasta2file
#         printAll
#         printAll2file
#         splitToList
#         getAnnotationlist
#         printAnnotation
#         printAnnotations2file
#     multiFasta   
#         reportStats
#         reportParalogs
#         addFasta
#         addFastas
#         addAnnotation
#         deleteFasta
#         printMultiFasta
#         printAll
#         printAll2file
#         renumber
#         matchHeader
#         removeEMBOSSpostfix
#         removeTerminalAsterisk        
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
import annotation
import re
from Bio import SeqIO  #*** BioPython is on mpath but not yet on mpath-dev, as of 16jan2014 - cez

p_extra = re.compile('(\s)|([0-9])|(\*)') # characters often included in sequence text 
p_header = re.compile('^>')
p_comment = re.compile('^#')
p_up2space = re.compile('^\S*')   # find 1st instance of everything that's not white space (check this)
p_startCodon = re.compile('atg')  # standard start codon sequence (recall: storing sequence as lower case)

#######################################################################################

class fasta(object):

    # Class fasta represents any kind of fasta sequence. User can specify a parent sequence,
    # comprising a header, for identifying a child relationship: eg, gene has a contig parent.
    # Fasta header is stored as text only, without the conventional '>'.
    # Get and print methods return header with the initial '>' symbol.
    # There is a need for 2 headers (header and fullHeader) because...
    # the header may be truncated after the first white space; the fullHeader is
    # the entire header string provided by the user. (Note: RAST truncates header after space)
    # Sequence can be entered as a list of lines or as continuous sequence in a single string.
    # Sequence can be converted back & forth between lines vs. single string.

    def __init__(self):
        self.header = ""         # full header
        self.truncHeader = ""    # truncated after N (self.truncation) characters
        self.shortHeader = ""    # truncated after 1st space (consistent w/RAST) 
        self.compoundHeader = "" # full header with parentSequence (eg, contig name) appended
        self.name = "none"
        self.sequence = ""       # store sequence as continuous lower-case string, sans numbers, white space
        self.type = "unknown"    # "nt" or "aa"; not "gene" or "dna" or the like
        self.parentSequence = "" # eg, for gene, the contig that the gene is on
        self.order = 0           # order in multi-fasta list
        self.truncation = 20     # number of characters (N) in header to retain, by default
        self.annotationList = [] # list of annotationRecord objects 
        self.paralogList = []    # list of paralog objects (header + blast hit)
        self.startCodonCount = 0 # calculated possible start codons in forward strand (for genes)
        self.codonStartLocs = [] # start positions of 'atg' sequences (for genes)
        self.nrHeader = ""       # "combined" header from NR database sequence entry
        self.nrGInumber = ""     # NCBI gi identifier

    def queryNRsequence(self,gi,nrLocation):  # Specific to NR; any other database has different format 
        # Given an NCBI gi identifier and the dir/file of an NR database, pull the sequence from NR database
        if gi != "" and int(gi) > 0: 
            giString = "gi\|" + gi + "\|"
        else:
            print "problem with gi"
            return(0)
        for record in SeqIO.parse(nrLocation,"fasta"):
            match = re.findall(giString,record.id)
            if match:
                self.assignHeader(record.id)
                self.assignSequence(str(record.seq))

    def enterGeneData(self,geneData): #*** should create a gene class, which "inherits" fasta
        if isinstance(geneData,dict): #*** should pass **kvargs and check for keys
            self.assignHeader(geneData["header"])
            self.name           = geneData["name"]
            self.sequence       = geneData["sequence"]
            self.type           = geneData["type"]
            self.parentSequence = geneData["parentSequence"]
            self.order          = geneData["order"]

    def assignType(self,type):
        if type.lower() == "nt" or type.lower() == "aa":
            self.type = type.lower()
        else:
            self.type = "unknown"

    def assignHeader(self,hdr):   # Remove symbols and spaces, which may cause problems for open-source codes
        cleanHeader = hdr.lstrip('>') # Remove '>' symbol if present; store header text onlya
        cleanHeader = re.sub(' ', '_', cleanHeader)
        cleanHeader = re.sub('[();:?.]','',cleanHeader)
        self.header = cleanHeader
        self.truncHeader = self.header[0:self.truncation]
        match = p_up2space.match(self.header)
        if match:
            self.shortHeader = match.group()
        else:
            self.shortHeader = self.truncHeader
        self.compoundHeader = self.header
        if self.parentSequence:
            self.compoundHeader = self.compountHeader + '_' + self.parentSequence

    def removeEMBOSSpostfix(self):  # Remove the pesky "_1" that EMBOSS adds
        self.assignHeader(self.header.rstrip("_1 "))

    def removeTerminalAsterisk(self):
        self.sequence = self.sequence.rstrip("* ")

    def getHeader(self):
        return ('>' + self.header)  # Add '>' symbol
 
    def getCompoundHeader(self):  # parentSequence (e.g., contig name) is appended to header 
        return ('>' + self.compoundHeader) 

    def getShortHeader(self):  #
        return ('>' + self.shortHeader) 

    def getTruncHeader(self):
        return ('>' + self.truncHeader) # 

    def assignSequence(self,seq):      # Input is single string or a list of strings
        if isinstance(seq,str):
            self.sequence = seq.lower()
            self.consolidate()         # Remove white spaces & numbers, if present
            return True
        elif isinstance(seq,list):
            self.sequence = ''.join(seq.lower())
            self.consolidate()         # Remove white space and collapse
            return True
        else:
            seqType = type(seq)
            print "seq is type", seqType
            return False

    def getStartCodon(self):
        if self.sequence != "":
            return self.sequence[0:3]
        else:
            return False 

    def verifyProkaryoticStartCodon(self):
        if self.sequence != "":
            testCodon = self.sequence[0:3].lower()
            if testCodon == "atg":
                return "common"
            elif testCodon == "gtg" or testCodon == "ttg":
                return "alternate"
            elif testCodon == "att" or testCodon == "ctg":
                return "rare"
            else:
                return "incorrect"

    def highlightAllStartCodons(self):
        codonStarts = []
        seqList = list(self.sequence)
        codonsHighlighted = ""
        if self.sequence != "":
            codonStarts = [m.start() for m in re.finditer('atg',self.sequence)]
            self.startCodonCount = len(codonStarts)
            for start in codonStarts:
                seqList[start] = seqList[start].upper()
                seqList[start+1] = seqList[start+1].upper()
                seqList[start+2] = seqList[start+2].upper()
            codonsHighlighted = ''.join(seqList)
            self.codonStartLocs = codonStarts
        return codonsHighlighted 

    def consolidate(self): # Remove white space and collapse sequence
        self.sequence = p_extra.sub('',self.sequence) # 

    def getSequenceLength(self):
        return (len(self.sequence))     # Report how long the sequence is

    def getSubsequence(self,start,end): # Recall: string position numbering starts with 0!
        return (self.sequence[int(start):int(end)])

    def reverseComplement(self):
        if self.type.lower() == "nt":
            complements = string.maketrans('acgtrymkbdhvACGTRYMKBDHV','tgcayrkmvhdbTGCAYRKMVHDB')
            revCompl = self.sequence.translate(complements)[::-1]
            self.sequence = revCompl
            return True
        return False

    def addAnnotation(self,newAnnot):
            self.annotationList.append(newAnnot)

    def printFasta(self):
        hdr = self.getHeader()
        seq = self.sequence
        print hdr
        print seq

    def printFasta2file(self,FILE_HANDLE,headerType="short"):
        if headerType.lower() == "compound":
            hdr = self.getCompoundHeader()
        elif headerType.lower() == "full":
            hdr = self.getHeader()
        elif headerType.lower() == "truncated":
            hdr = self.getTruncHeader()
        elif headerType.lower() == "short":
            hdr = self.getShortHeader()
        else:
            hdr = self.getShortHeader()
        seq = self.sequence
        FILE_HANDLE.write("%s%s" % (hdr,"\n"))
        FILE_HANDLE.write("%s%s" % (seq,"\n"))

    def printFasta2file_case(self,FILE_HANDLE,case,headerType="short"):
        if headerType.lower() == "compound":
            hdr = self.getCompoundHeader()
        elif headerType.lower() == "full":
            hdr = self.getHeader()
        elif headerType.lower() == "truncated":
            hdr = self.getTruncHeader()
        elif headerType.lower() == "short":
            hdr = self.getShortHeader()
        else:
            hdr = self.getShortHeader()
        seq = self.sequence
        if case.lower() == "upper":
            seq = seq.upper()
        FILE_HANDLE.write("%s%s" % (hdr,"\n"))
        FILE_HANDLE.write("%s%s" % (seq,"\n"))

    def printAll(self):  # Dump everything: useful for testing  
        count = 0 
        print "CompoundHeader:", self.compoundHeader
        print "Header:", self.header
        print "ShortHeader:", self.shortHeader
        print "TruncHeader:", self.truncHeader
        print "Type:", self.type
        print "Order in list:", self.order
        print "Sequence length is:", self.getSequenceLength()
        if (self.annotationList):
            count += 1
            print "Annotation Set No.", count, ":"
            self.printAnnotations()
        print "Sequence:", self.sequence

    def printAll2file(self,FILE_HANDLE):  # Dump everything: useful for testing  
        count = 0 
        FILE_HANDLE.write("%s%s%s" % ("Header:",self.header,"\n"))
        FILE_HANDLE.write("%s%s%s" % ("ShortHeader:",self.shortHeader,"\n"))
        FILE_HANDLE.write("%s%s%s" % ("TruncHeader:",self.truncHeader,"\n"))
        FILE_HANDLE.write("%s%s%s" % ("Type:",self.type,"\n"))
        FILE_HANDLE.write("%s%s%s" % ("Order in list:",self.order,"\n"))
        FILE_HANDLE.write("%s%s%s" % ("Sequence length is:",self.getSequenceLength(),"\n"))
        if (self.annotationList):
            count += 1
            FILE_HANDLE.write("%s%s%s" % ("Annotation Set No.",count,":\n"))
            self.printAnnotations2file(FILE_HANDLE)
        FILE_HANDLE.write("%s%s%s" % ("Sequence:",self.sequence,"\n"))

    def splitToList(self,lineLength):  # Returns a list of sequence lines
        nextLine = ""
        sequenceList = []
        numberList = list(xrange(0,len(self.sequence),lineLength))
        for number in numberList:
            nextSegment = self.sequence[int(number):int(number+lineLength)]
            sequenceList.append(nextSegment)
        return(sequenceList)
 
    def getAnnotationList(self):
        return self.annotationList

    def printAnnotations(self):
        for annot in self.annotationList:
            annot.printAnnotationRecord()

    def printAnnotations2file(self,FILE_HANDLE):
        for annot in self.annotationList:
            annot.printAnnotationRecord2file(FILE_HANDLE)

#####################################################################################
 
class multiFasta(object): 
 
    # Class multiFasta is essentially a list of fasta objects.
    # Usage: Draft or finished genome; set of genes or proteins
    # The class keeps track of the order in which the fasta object occur in the list.
    # The order is needed so that it can be re-ordered based on, for example,
    # ...shifting the start position on the genome.

    def __init__(self):
        self.fastaList = []  # list of fasta objects
        self.annotationList = []
        self.filename = "unknown"

    def reportStats(self):
        stats = []
        print "Sequence from file name:", self.filename
        stats.append("Sequence from file name:" + self.filename)
        print "Number of fasta sequences:", len(self.fastaList)
        stats.append("Number of fasta sequence:" + str(len(self.fastaList)))
        print "Number of annotations:", len(self.annotationList)
        stats.append("Number of annotations:" + str(len(self.annotationList)))
        print "Annotations:", self.annotationList
        print "No. of fasta sequences with paralogs:", self.countParalogs() 
        stats.append("No. of fasta sequence with paralogs: " + str(self.countParalogs()))
        return stats

    def countParalogs(self):  # count no. of fastas that have paralogs (not total paralog hits)
        count = 0
        for fasta in self.fastaList:
           if fasta.paralogList:
               count += 1 
        return count

    def addFasta(self,newFa):
        newFa.order = len(self.fastaList) + 1
        self.fastaList.append(newFa)

    def addFastas(self,lines,mtype): # Given multi-fasta file read into line set, create multi-fasta object
        sequence = ""
        numberAdded = 0
        if lines:
            header = lines[0] # capture 1st header (should be first line in lineSet!)
            lines.pop(0)
            for line in lines:
                match = re.search(p_header, line) # detect start of a new fasta
                if match:
                    newFasta = fasta()            # create new object
                    newFasta.assignHeader(header)
                    newFasta.assignSequence(sequence)
                    newFasta.assignType(mtype)
                    self.addFasta(newFasta)
                    numberAdded += 1              # no. of fasta objects added so far from lines
                    sequence = ""                 # reset
                    header = line                 # capture next header
                    continue
                sequence += line
            newFasta = fasta()
            newFasta.assignHeader(header)
            newFasta.assignSequence(sequence)
            newFasta.assignType(mtype)
            self.addFasta(newFasta)
            numberAdded += 1
        return numberAdded

    def addAnnotation(self,newAnnot):
        self.annotationList.append(newAnnot)

    def deleteFasta(self,oldFasta):
        for fa in self.fastaList:
            if fa == oldFasta:
                self.fastaList.remove(fa)
                return True
        return False

    def printMultiFasta(self):
        for fa in self.fastaList:
            fa.printFasta()

    def printMultiFasta2file(self,FILE_HANDLE):
        for fa in self.fastaList:
            fa.printFasta2file(FILE_HANDLE)

    def printMultiFasta2file_case(self,FILE_HANDLE,case):
        for fa in self.fastaList:
            fa.printFasta2file_case(FILE_HANDLE,case)

    def printAll(self):
        count = 0
        print "Number of fastas:", len(self.fastaList)
        for fa in self.fastaList:
            count += 1
            print "*****List item no.", count, ":"
            fa.printAll()
            print "\n"

    def printAll2file(self,FILE_HANDLE):
        count = 0
        FILE_HANDLE.write("%s%s%s" % ("Number of fastas:",len(self.fastaList),"\n"))
        for fa in self.fastaList:
            count += 1
            FILE_HANDLE.write("%s%s%s" % ("*****List item no.",count,":\n"))
            fa.printAll2file(FILE_HANDLE)
            FILE_HANDLE.write("%s" % ("\n"))

    def renumber(self):  # If any fasta object was deleted, then renumber to close gaps in ordering
        newOrder = 0     # Caution:  this will re-order fasta objects in sequence!
        for fa in self.fastaList:
            newOrder += 1
            fa.order = newOrder 

    def matchHeader(self,hdr):
        for fa in self.fastaList:
            if fa.header == hdr:
                return fa
        return False

    def removeEMBOSSpostfix(self):  # remove pesky '_1' that EMBOSS adds to translated sequence
        for prot in self.fastaList:
            prot.removeEMBOSSpostfix()

    def removeTerminalAsterisk(self):  # remove '*' that EMBOSS adds to end of protein translation 
        for prot in self.fastaList:
            prot.removeTerminalAsterisk()
