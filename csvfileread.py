#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 12:09:48 2017

@author: zwen
"""

import matplotlib.pyplot as plt
import csv
from collections import defaultdict

'''stats on the metadata'''
fname1 = "/Users/grandwor/Desktop/research_stat/sigmetadata.txt"
'''dict to record the properties for each signature'''
metasigset = set()
reasondict = {}
proxexdict = {}
proxintdict = {}
normproxexdict ={}
normproxintdict ={}
numexdict = {}
numintdict = {}
signamedict = {}
signaturedict = {}
describdict={}
describset = set()
sigtypenumberdict = {}
sigtypenamedict = {}
sigtypenumberstat= {}
sigtypenamestat = {}
sigtypenumberset = set()
sigtypesignamedict = {}
sigtypesigname = {}
'''group signatures according to their sigtypename or number'''
sigtypesignumberdic = defaultdict(list)
sigtypenumsignumberdic = defaultdict(list)

'''record the normalized scores to two list for histogram'''
normInthisto = []
normExthisto = []

'''record the normalized score to two dict for each signumber'''
normIntsignumber ={}
normExtsignumber ={}

'''sigtypenumber and normalized proximity dict of list
'''

sigtypenumberExt = defaultdict(list)
sigtypenumberInt = defaultdict(list)

'''lambda function to calculate the normalized proximity score'''
normInt = lambda x: float(x[2])/float(x[4]) if row[2]!="" and row[2]!='None' and row[4]!="" and row[4]!='None'  and float(x[4])>0 else 0
normExt = lambda x: float(x[3])/float(x[5]) if row[3]!="" and row[3]!='None'and row[5]!="" and row[5]!='None'  and float(x[5])>0 else 0


f1 = open(fname1, 'r')
f1csvread = csv.reader(f1, delimiter = '\t')
rowcount=0
for row in f1csvread:
    print("line is ", rowcount)
    if rowcount ==0:
        rowcount+=1
        continue;
    else:
        if(row[3]!="" and row[3]!='None'):
            print("row3 raw",float(row[3]))
        metasigset.add(row[0])
        rowcount +=1
        reasondict[row[0]] = row[1]
        proxexdict[row[0]] =row[2]
        proxintdict[row[0]] =row[3]
        numexdict[row[0]] =row[4]
        numintdict[row[0]] = row[5]
        '''ext = normExt(row)
        inte = normInt(row)
        normproxexdict[row[0]] = ext
        print("normext", ext)
        print("normint", inte)
        normproxintdict[row[0]] = inte
        normInthisto.append(inte)
        normExthisto.append(ext)'''
        
        '''normalize external and internal proximity'''
        if(row[1].isdigit() and float(row[1])>0):
            normproxexdict[row[0]] = 1
        else:
            if(row[2]!="" and row[2]!='None' and row[4]!="" and row[4]!='None' and float(row[4])>0):
                
                normproxexdict[row[0]] = float(row[2])/float(row[4])
            else:
                normproxexdict[row[0]] = 0
        normExthisto.append(normproxexdict[row[0]])
        sigtypenumberExt[row[9]].append(normproxexdict[row[0]])
        normExtsignumber[row[0]] = normproxexdict[row[0]]
        
        if(row[1].isdigit() and float(row[1])>0):
            normproxintdict[row[0]] = 1
        else:
            if(row[3]!="" and row[3]!='None'and row[5]!="" and row[5]!='None' and float(row[5])>0):
                
                normproxintdict[row[0]] = float(row[3])/float(row[5])
            else:            
                normproxintdict[row[0]] =0
        normInthisto.append(normproxintdict[row[0]])
        sigtypenumberInt[row[9]].append(normproxintdict[row[0]])
        normIntsignumber[row[0]] = normproxintdict[row[0]]
        
        '''print("normext", normproxexdict[row[0]])
        print("normint", normproxintdict[row[0]])'''
        
        signamedict[row[0]] = row[6]
        signaturedict[row[0]] = row[7]
        describdict[row[0]] = row[8]
        describset.add(row[8])
        sigtypenumberdict[row[0]]=row[9]
        sigtypenumberset.add(row[9])
        sigtypenamedict[row[0]] =row[10]
        
        if not(sigtypesigname.has_key(row[9])):
            sigtypesigname[row[9]] = row[10]
        
        sigtypesignumberdic[row[10]].append(row[0])
        sigtypenumsignumberdic[row[9]].append(row[0])
        
        if sigtypenumberstat.has_key(row[9]):
            sigtypenumberstat[row[9]]+=1
        else:
            sigtypenumberstat[row[9]]=1
        if sigtypenamestat.has_key(row[10]):
            sigtypenamestat[row[10]] +=1
        else:
            sigtypenamestat[row[10]] =1
f1.close()  
plt.hist(normInthisto)
plt.savefig("/home/zwen/Desktop/research_stat/"+"normInthisto.png")
plt.hist(normExthisto)
plt.savefig("/home/zwen/Desktop/research_stat/"+"normExthisto.png")
len(sigtypenumberset)
for sig in sigtypenumberset:
    plt.hist(sigtypenumberInt[sig])
    plt.hist(sigtypenumberExt[sig])
plt.bar(list(sigtypenumberstat.keys()), sigtypenumberstat.values(), color='g')

lstatforsigpersigtypenumber=[]        
for st in sigtypenumberset:
    lstatforsigpersigtypenumber.append(len(sigtypenumsignumberdic[st]))


plt.hist(lstatforsigpersigtypenumber)
plt.xlabel('signature count per sigtype')
plt.ylabel('frq count')
plt.title("Histogram of Signatures per Sigtype")
plt.savefig("/home/zwen/Desktop/stat/"+"lstatforsigpersigtypenumber.pdf") 
 
 
 
 
 
'''stat on the data'''

fname = "/Users/grandwor/Desktop/research_stat/collapsedSpertus201607to10.txt"
f = open(fname,'r')
'''
sets for the machineid, IPaddress inccategory attached_incidenttype signature, columnname
dict signature-frequency total data
dict signature -fequency for each log


'''
mcIDset = set()
colname = set()
ipset = set()
incTypelib ={}
incCatlib ={}
sigset = set()
sigfreqTotal = {}
siglog = {}
sigfreqlog = {}
sigfreqlogIntscore ={}
sigfreqlogExtscore ={}
sigfreqlogIntscoretimesfreq = {}
sigfreqlogExtscoretimesfreq = {}
isinc = {}
'''siglist to record all the occurrences of signatures for each type'''
siglist ={}
isincstat ={'t':0, 'f':0}
'''machineid-signature type or signature type name'''
mIDsigtypename = defaultdict(set)
mIDsigtypenumber=defaultdict(set)
'''
signatures count across all the data
'''
sigdatacount = {}

'''sigtypenumber-signaturecount'''
sigtypenumbersignaturecount = {}

'''logname with label true and false'''
lognamet = set()
lognamef = set()

'''arountinc'''
aroundinc = {}

'''csv reader'''
fcsvread = csv.reader(f, delimiter='\t')
lognameset =set()
'''row count'''

'''number of logs'''
'''machineID for date'''
mcIDperdate = defaultdict(list)
'''machineID for events'''
mcIDperevents = defaultdict(list)
'''logpermachine'''
numbereventsperlog = []
'''clusdate'''
clusdateset = set()

'''signature logdata'''
logsignature =defaultdict(list)

count = 0
for row in fcsvread:
    print("rowcount is ",count)
    if (count==0 or count==224720 or count==224721 or count==258491 or count==258492 or count==294542) :
        rowlen = len(row)
        print(row)
        for i in range(rowlen):
            colname.add(row[i])
        count +=1
        continue;
    else:
        count+=1
        mcIDset.add(row[0])
        
        if  incCatlib.has_key(row[3]):
            incCatlib[row[3]]+=1
        else:
            incCatlib[row[3]] =1
        
        if  incTypelib.has_key(row[4]):
            incTypelib[row[4]]+=1
        else:
            incTypelib[row[4]] =1
        
        '''generate a dict for each log to record the sig, fre pair'''
        '''name for log dict is the machineid and incdate'''
        '''incident for logdata'''
        clusdate = row[1].split(" ")
        incdate = row[2].split(" ")
        logname = row[0]+clusdate[0]
        numbereventsperlog.append(int(row[6]))
        lognameset.add(logname)
        mcIDperdate[clusdate[0]].append(row[0])
        clusdateset.add(clusdate[0])
        aroundinc[logname] = row[5]
        if(row[5]=='t' and clusdate[0]==incdate[0]):
            isinc[logname] = 't'
            isincstat['t'] +=1
            lognamet.add(logname)
        else:
            isinc[logname] = 'f'
            isincstat['f']+=1
            lognamef.add(logname)
        '''dict for each log signatures'''
        sigfreqlog[logname] = {}
        siglog[logname]=set()
        sigfreqlogIntscore[logname] ={}
        sigfreqlogExtscore[logname] ={}
        sigfreqlogIntscoretimesfreq[logname]={}
        sigfreqlogExtscoretimesfreq[logname]={} 
        '''row[7] has to remove the ()'''
        sigfreq = row[7].replace("(", "")
        sigfreq = sigfreq.replace(";)", "")
        sigfreqset= sigfreq.split(";")
        print(sigfreqset)
        '''put signumber and frequency count to the log library for each log'''
        if(len(sigfreqset)>0):
            for sf in sigfreqset:
                signum= sf.split(",")
                sigset.add(signum[0])
               
                if(count<=5):
                    print(signum[0])
                if(len(signum)>1):
                    ''''print("row count", count)'''
                     
                    sigfreqlog[logname][signum[0]] =signum[1]
                    if(signum[0]!='-1'):
                        mcIDperevents[signum[0]].append(row[0])
                        if sigtypenumbersignaturecount.has_key(sigtypenumberdict[signum[0]]):
                            sigtypenumbersignaturecount[sigtypenumberdict[signum[0]]] +=1
                        else:
                            sigtypenumbersignaturecount[sigtypenumberdict[signum[0]]] =1
                        
                        if sigdatacount.has_key(signum[0]):
                            sigdatacount[signum[0]] +=1
                        else:
                            sigdatacount[signum[0]] = 1
                        mIDsigtypename[row[0]].add(sigtypenamedict[signum[0]])
                        mIDsigtypenumber[row[0]].add(sigtypenumberdict[signum[0]])
                        if(siglist.has_key(sigtypenumberdict[signum[0]])):
                            siglist[sigtypenumberdict[signum[0]]]+=1
                        else:
                            siglist[sigtypenumberdict[signum[0]]] =1
                        
                    '''there is a case where signumber is -1 which is not in the metadata
                    I assigned a internal and external importance 0.1 for now
                    '''
                    if(signum[0]=='-1'):
                        normIntsignumber[signum[0]] = 0.1
                        normExtsignumber[signum[0]] =0.1
                    logsignature[signum[0]].append(logname)
                    siglog[logname].add(signum[0])
                    sigfreqlog[logname][signum[0]] = int(signum[1])   
                    sigfreqlogIntscore[logname][signum[0]] =normIntsignumber[signum[0]]
                    sigfreqlogExtscore[logname][signum[0]] =normExtsignumber[signum[0]]
                    sigfreqlogIntscoretimesfreq[logname][signum[0]] =int(signum[1])*float(normIntsignumber[signum[0]])
                    sigfreqlogExtscoretimesfreq[logname][signum[0]] =int(signum[1])*float(normExtsignumber[signum[0]])
f.close()

'''number of machineid per date and histogram'''
lmachineIDfordate=[]
for date in clusdateset:
    lmachineIDfordate.append(len(mcIDperdate[date]))
    
plt.hist(lmachineIDfordate)
plt.title("Histogram for number of machineid for dates")
plt.xlabel("number of machineIDs")
plt.ylabel("freq count")
plt.savefig("/home/zwen/Desktop/stat/"+"machineIDfordtate.png")
 
'''number of machineid per each event''' 
lmachineIDforevent=[]
for sig in sigset:
    lmachineIDforevent.append(len(mcIDperevents[sig]))
plt.hist(lmachineIDforevent)
plt.title("Histogram for number of machineid for events")
plt.xlabel("number of machineIDs")
plt.ylabel("freq count")
plt.savefig("/home/zwen/Desktop/stat/"+"machineIDforevents.png")
'''
count of machineID - freq
         1 - 21113
         2 - 4007
         3 - 1517
         4 - 1058
         5 - 804
         6 - 600
         7  -439
         8 - 360
         9  -301
         10 -264
         
         

'''
            

for ln in lognameset:
    print("logname and data ",ln)
    print(sigfreqlogIntscoretimesfreq[ln])
    print(sigfreqlogExtscoretimesfreq[ln])
    
    
    
    
'''signature happened only a few times'''
lsiggreatertime = []
for sig in sigdatacount.keys():
    if sigdatacount[sig] >=100:
        lsiggreatertime.append(sig)
    
'''stats on the data about sigtypenumber-signumber pair dict
  stats on the sigtypename-signumber pair dict
'''  
typesignumberstat = {}
typeNumsignumberstat={} 
'''sigset and metasigset only difference in one item -1'''
for sig in sigset:
    if sig == '-1':
        continue;
    if typesignumberstat.has_key(sigtypenamedict[sig]):
        typesignumberstat[sigtypenamedict[sig]] +=1
    else:
        typesignumberstat[sigtypenamedict[sig]] =1
    
    if typeNumsignumberstat.has_key(sigtypenumberdict[sig]):
        typeNumsignumberstat[sigtypenumberdict[sig]] +=1
    else:
        typeNumsignumberstat[sigtypenumberdict[sig]] =1
    
    
'''print the histogram of sigtypenumber and proximity scores'''   
    
statfile = open("/home/zwen/Desktop/statfile.txt",'w') 
    
import sys
'''sys.stdout=statfile'''   
    
for st in sigtypenumberset:
    plt.title("sigtypenumer "+st+" size "+str(sigtypenumberstat[st])+" occurrences "+str(siglist[st]))
    plt.hist(sigtypenumberInt[st])
    plt.xlabel("Normalized Internal Proximity - Sigtypename "+sigtypesigname[st])
    plt.ylabel("Countfrq")
    plt.savefig("/home/zwen/Desktop/stat/"+st+".pdf")
    
    
    
    
for k in sigtypenumberInt.keys():
    sys.stdout.write("len is "+str(len(sigtypenumberInt[k])))
    sys.stdout.flush()
    
for st in sigtypenumberset:
    plt.title("sigtypenumer "+st+" size "+str(sigtypenumberstat[st])+" len of sigtypenumberInt "+str(len(sigtypenumberInt[st]))+" occurrences "+str(siglist[st]))
    plt.hist(sigtypenumberInt[st])
    plt.xlabel("Normalized Internal Proximity - Sigtypename "+sigtypesigname[st])
    plt.ylabel("Countfrq")
    plt.savefig("/home/zwen/Desktop/stat/"+st+".pdf")
    plt.show()

lstatforsigtypenumber = [] 
lstatforsigtypename = [] 
for id in mcIDset:
    lstatforsigtypename.append(len(mIDsigtypename[id]))
    lstatforsigtypenumber.append(len(mIDsigtypenumber[id]))
    
'''draw histogram'''  
plt.hist(lstatforsigtypename)
plt.title("number of type by machineID")
plt.xlabel("number of types")
plt.ylabel("freq count")
plt.savefig("/home/zwen/Desktop/stat/"+"numberoftype_byMachineID.pdf")
plt.show()
'''
number of Type - frequency count
1 - 10402
2 - 11490
3 - 9925
4 - 7847
5 - 2941
6 - 421
7 - 135
8 - 50
9 - 21
10 - 11
11 - 1
12 - 1

'''   
'''
check the machineID with different type of types of signatures
make a data set and check the sparsity?????
'''  
'''
generate a histogram of the sigdatacount
'''
lstatforsigdatacount = []
for sig in sigdatacount.keys():
    lstatforsigdatacount.append(sigdatacount[sig])
'''draw histogram'''  
plt.hist(lstatforsigtypename)
plt.title("Histogram sigdatacount")
plt.xlabel("number of count across data")
plt.ylabel("freq count")
plt.savefig("/home/zwen/Desktop/stat/"+"sigdatacount.pdf")
plt.show()
'''
number of count - freq count
1 - 21113
2 - 4007
3 - 1571
4 - 1058
5 - 804
6 - 600
7 - 439
8 - 360
9 - 301
10 - 264
11 - 243
12 - 204
13 - 184
14 - 163
15 - 147
'''
'''generate histogram for the sigtype - signature count'''
lstatforsigtypenumbersignaturecount = []
for sig in sigtypenumbersignaturecount.keys():
    lstatforsigtypenumbersignaturecount.append(sigtypenumbersignaturecount[sig])
'''draw histogram'''  
plt.hist(lstatforsigtypenumbersignaturecount)
plt.title("Histogram sigtypesignaturecount")
plt.xlabel("number of count across signatures")
plt.ylabel("freq count")
plt.savefig("/home/zwen/Desktop/stat/"+"sigtypenumbersignaturecount.pdf")
plt.show()
    
'''generate data set for learning'''  
'''
1. feature selection,there are 107 categories of signatures, the problem here is 
to reduce the possible signatures and not contain so much sparsity.

   '20': 12942, possible category
 '2000': 6718, might drop
 '2002': 4348,might drop
 '2003': 1170,might drop
 '2006': 49333,possible category??
 '2007': 295,might drop?
 '2008': 229,might frop?
 '2010': 17, might drop
 '2012': 180,might drop?
 '2013': 101,drop
 '2014': 141,drop
 '2016': 133455,might drop?
 '2018': 175,might drop
 '2019': 4604,possible ?
 '2023': 1510, possible
 '2027': 1,drop
 '2029': 27,drop
 '2035': 1253,drop?
 '2038': 28409,drop
 '2040': 177,drop
 '2042': 1060,drop?
 '2046': 117,drop
 '2048': 349,drop
 '2049': 357,drop?
 '21': 40, might drop
 '28': 88207,possible category
 '3003': 2012,possible category
 '3006': 21,might drop
 '3007': 1843,?
 '3008': 219,?
 '3012': 1,drop
 '3013': 130,drop?
 '3022': 597,drop
 '3028': 113,drop
 '3038': 3831,might drop?
 '3042': 1,drop
 '3043': 569,drop
 '3062': 102,drop
 '3064': 170,drop
 '3065': 8,drop
 '3080': 106,drop
 '3093': 1, drop
 '3097': 1736207,possible category
 '3098': 2587547,possible category
 '36': 8451, possible category
 '40': 6082, might drop
 '41': 21909, possible category
 '42': 212458, possible category
 '44': 1369825, possible?
 '45': 101569,possible?
 '5037': 96987,possible category
 '5053': 2393,possible
 '5058': 10,drop
 '5063': 862,drop
 '5064': 27,drop
 '5072': 13881,possible?
 '5091': 23483,drop
 '5095': 1276,drop
 '5097': 13,drop
 '5100': 1,drop
 '5103': 5026,might drop?
 '5104': 1224,might drop?
 '5107': 2962,might drop?
 '5111': 3,drop
 '5121': 203,drop
 '5127': 130,drop
 '5140': 40,drop
 '5143': 765,drop
 '5153': 166,drop
 '5156': 1553,might drop?
 '5160': 6,drop
 '5163': 972,drop
 '5164': 1017,might drop?
 '5167': 253,drop
 '5168': 26641,possible category
 '5171': 3,drop
 '5172': 7505,drop
 '5173': 64,drop
 '5174': 2,drop
 '5176': 377,drop
 '5177': 96,drop
 '5179': 45,drop
 '5181': 9777,possible category
 '5182': 1,drop
 '5185': 23,drop
 '5186': 4,drop
 '5191': 17,drop
 '53': 30192,possible category
 '55': 60, might drop
 '5507': 2006,drop
 '57': 30358, possible category
 '58': 15702, possible?
 '59': 22031, less possible?
 '60': 12287, possible category
 '63': 3725, possible category
 '64': 3620, possible category
 '65': 122, possible?
 '66': 112, possible?
 '67': 473, possible?
 '68': 5,drop
 '69': 2,drop
 '70': 294,might drop?
 '71': 6, might drop?
 '72': 6449, might drop?
 '73': 223,might drop?
 '74': 5, might drop
 '8': 10174 possible
 
 the information above is based on the histogram of each category.

'''  
keepset = set(['20','2023','28','3003','3097','3098','36','41','42','5037','5053','5168','5181','53','57','60','63','64','8'])
possibleset = set(['2006','2019','3007','3008','44','45','5072','58','59''65','66','67'])
mightdropset = set(['2000','2002','2003','2007','2008','2010','2012','2016','2018','21','3006','3038','40','5103','5104', '5107','5156','5164','55','70','71','72','73','74'])
dropset=set(['2013','2014','2027','2029','2035','2038','2040','2042','2046','2048','2049','3012','3013','3022','3028','3042', '3043', '3062', '3064', '3065', '3080', '3093','5058', '5063', '5064','5091', '5095','5097', '5100','5111', '5121','5127', '5140', '5143', '5153','5160', '5163','5167','5171', '5172', '5173', '5174', '5176', '5177', '5179',  '5182', '5185', '5186', '5191','5507','68','69']) 
    
'''then deal with signature in the three sets above differenly'''
'''
1 first route: treat the signatures in the first into 10 categories based on the normalized score or frequency*normalized score
               treat the signature in the mightdropset together, and the signature in the dropset together.  
               
   for the keepset, generate a eleven variables for this category, range from  0 - 1 by 0.1 with 11 category
   k0, k01, k02 - k1
   for the possibleset, generate  6 variables, range from 0 - 1 by 0.2
   p0,p02-p1
   for the mightdropset, generate 3 variables for it range from 0 0.5 and 1
   m0 m05 m1
   for the drop set generate two variables for 0 and 1
   d0 d1
   
   
'''
'''add field titles'''
fieldnames=['logname','aroundinc','label']
for i in range(11):
    fieldnames.append('k'+str(i))
for i in range(0,11,2):
    fieldnames.append('p'+str(i))
for i in range(0,11,5):
    fieldnames.append('m'+str(i))
for i in range(0,11,10):
    fieldnames.append('d'+str(i))
    
dataout1 = defaultdict(dict)
for lg in lognameset:
    
    for i in range(11):
        dataout1[lg]['k'+str(i)] = 0
    for i in range(0,11,2):
        dataout1[lg]['p'+str(i)] = 0
    for i in range(0,11,5):
        dataout1[lg]['m'+str(i)] = 0
    for i in range(0,11,10):
        dataout1[lg]['d'+str(i)] = 0
    dataout1['label'] = 0

g = lambda x : 1 if x=='t' else 0    
for lg in lognameset:
    dataout1[lg]['aroundinc']= g(aroundinc[lg])
    dataout1[lg]['logname'] = lg
    if isinc[lg] == 't':
        dataout1[lg]['label'] = 1
    else:
        dataout1[lg]['label'] = 0
        
    for sig in sigfreqlogIntscore[lg].keys():
        sk = sigfreqlogIntscore[lg][sig]
        if sig!= '-1' and sigtypenumberdict[sig] in keepset:
            if sk == 0:
                dataout1[lg]['k0'] +=1
            if sk>0 and sk<0.1:
                dataout1[lg]['k1'] +=1
            if sk>=0.1 and sk<0.2:
                dataout1[lg]['k2'] +=1
            if sk>=0.2 and sk<0.3:
                dataout1[lg]['k3'] +=1
            if sk>=0.3 and sk<0.4:
                dataout1[lg]['k4'] +=1
            if sk>=0.4 and sk<0.5:
                dataout1[lg]['k5'] +=1
            if sk>=0.5 and sk<0.6:
                dataout1[lg]['k6'] +=1
            if sk>=0.6 and sk<0.7:
                dataout1[lg]['k7'] +=1
            if sk>=0.7 and sk<0.8:
                dataout1[lg]['k8'] +=1
            if sk>=0.8 and sk<0.9:
                dataout1[lg]['k9'] +=1
            if sk>=0.9 and sk<=1:
                dataout1[lg]['k10'] +=1
                
        if sig!= '-1' and sigtypenumberdict[sig] in possibleset:
            if sk == 0:
                dataout1[lg]['p0'] +=1
            if sk>0 and sk<0.2:
                dataout1[lg]['p2'] +=1
            if sk>=0.2 and sk<0.4:
                dataout1[lg]['p4'] +=1
            if sk>=0.4 and sk<0.6:
                dataout1[lg]['p6'] +=1
            if sk>=0.6 and sk<0.8:
                dataout1[lg]['p8'] +=1
            if sk>=0.8 and sk<=1:
                dataout1[lg]['p10'] +=1
                
        if sig!='-1' and sigtypenumberdict[sig] in mightdropset:
            if sk == 0:
                dataout1[lg]['m0'] +=1
            if sk>0 and sk<0.5:
                dataout1[lg]['m5'] +=1
            if sk>=0.5 and sk<=1:
                dataout1[lg]['m10'] +=1
        if sig!='-1' and sigtypenumberdict[sig] in dropset:
            if sk < 0.8:
                dataout1[lg]['d0'] +=1
            if sk>=0.8 and sk<=1:
                dataout1[lg]['d10'] +=1
fopen1 = open("/home/zwen/Desktop/stat/m1.csv",'w')
writer = csv.DictWriter(fopen1, fieldnames=fieldnames)
writer.writeheader()
for lg in lognameset:
    writer.writerow(dataout1[lg])
fopen1.close()



'''
second use the frequency*normInt score 
'''


fieldnames1=['logname','aroundinc','label']
for i in range(11):
    fieldnames1.append('k'+str(i))
for i in range(11):
    fieldnames1.append('p'+str(i))
for i in range(2):
    fieldnames1.append('m'+str(i))
for i in range(2):
    fieldnames1.append('d'+str(i))
    
dataout2 = defaultdict(dict)
for lg in lognameset:
    for i in range(11):
        dataout2[lg]['k'+str(i)] = 0
    for i in range(11):
        dataout2[lg]['p'+str(i)] = 0
    for i in range(2):
        dataout2[lg]['m'+str(i)] = 0
    for i in range(2):
        dataout2[lg]['d'+str(i)] = 0
    dataout2[lg]['label'] = 0
    
  
   

g = lambda x : 1 if x=='t' else 0    
for lg in lognameset:
    dataout2[lg]['aroundinc']= g(aroundinc[lg])
    dataout2[lg]['logname'] = lg
    if isinc[lg] == 't':
        dataout2[lg]['label'] = 1
    else:
        dataout2[lg]['label'] = 0
        
    for sig in sigfreqlogIntscore[lg].keys():
        sk = sigfreqlogIntscoretimesfreq[lg][sig]
        if sig!= '-1' and sigtypenumberdict[sig] in keepset:
            if sk == 0:
                dataout2[lg]['k0'] +=1
            if sk>0 and sk<1:
                dataout2[lg]['k1'] +=1
            if sk>=1 and sk<2:
                dataout2[lg]['k2'] +=1
            if sk>=2 and sk<3:
                dataout2[lg]['k3'] +=1
            if sk>=3 and sk<4:
                dataout2[lg]['k4'] +=1
            if sk>=4 and sk<5:
                dataout2[lg]['k5'] +=1
            if sk>=5 and sk<6:
                dataout2[lg]['k6'] +=1
            if sk>=6 and sk<7:
                dataout2[lg]['k7'] +=1
            if sk>=7 and sk<8:
                dataout2[lg]['k8'] +=1
            if sk>=8 and sk<9:
                dataout2[lg]['k9'] +=1
            if sk>=9:
                dataout2[lg]['k10'] +=1
                
        if sig!= '-1' and sigtypenumberdict[sig] in possibleset:
            if sk == 0:
                dataout2[lg]['p0'] +=1
            if sk>0 and sk<1:
                dataout2[lg]['p1'] +=1
            if sk>=1 and sk<2:
                dataout2[lg]['p2'] +=1
            if sk>=2 and sk<3:
                dataout2[lg]['p3'] +=1
            if sk>=3 and sk<4:
                dataout2[lg]['p4'] +=1
            if sk>=4 and sk<5:
                dataout2[lg]['p5'] +=1
            if sk>=5 and sk<6:
                dataout2[lg]['p6'] +=1
            if sk>=6 and sk<7:
                dataout2[lg]['p7'] +=1
            if sk>=7 and sk<8:
                dataout2[lg]['p8'] +=1
            if sk>=8 and sk<9:
                dataout2[lg]['p9'] +=1
            if sk>=9:
                dataout2[lg]['p10'] +=1
                
        if sig!='-1' and sigtypenumberdict[sig] in mightdropset:
            if sk <=1:
                dataout2[lg]['m0'] +=1
            if sk>1:
                dataout2[lg]['m1'] +=1
            
        if sig!='-1' and sigtypenumberdict[sig] in dropset:
            if sk <= 1:
                dataout2[lg]['d0'] +=1
            if sk>1:
                dataout2[lg]['d1'] +=1
fopen2 = open("/home/zwen/Desktop/stat/m2.csv",'w')
writer = csv.DictWriter(fopen2, fieldnames=fieldnames1)
writer.writeheader()
for lg in lognameset:
    writer.writerow(dataout2[lg])
fopen2.close()

'''data3'''
'''random choose from lognamet and lognamef set individually 10,000 samples without replacement'''
import numpy as np
lognametlist = list(lognamet)
lognameflist = list(lognamef)
'''randomly choose 10,000 from both lognametlist and lognameflist'''
rd_lognametlist = np.random.choice(lognametlist,60000,replace=False)
rd_lognameflist = np.random.choice(lognameflist,60000,replace=False)
rd_logname = []
rd_logname.extend(rd_lognametlist)
rd_logname.extend(rd_lognameflist)
'''
generate a new file with 10000 true label and 10000 false label
'''
fieldnames3=['logname','aroundinc','label']
for i in range(11):
    fieldnames3.append('k'+str(i))
for i in range(0,11,2):
    fieldnames3.append('p'+str(i))
for i in range(0,11,5):
    fieldnames3.append('m'+str(i))
for i in range(0,11,10):
    fieldnames3.append('d'+str(i))
    
dataout3 = defaultdict(dict)
for lg in rd_logname:
    
    for i in range(11):
        dataout3[lg]['k'+str(i)] = 0
    for i in range(0,11,2):
        dataout3[lg]['p'+str(i)] = 0
    for i in range(0,11,5):
        dataout3[lg]['m'+str(i)] = 0
    for i in range(0,11,10):
        dataout3[lg]['d'+str(i)] = 0
    dataout3['label'] = 0

g = lambda x : 1 if x=='t' else 0    
for lg in rd_logname:
    dataout3[lg]['aroundinc']= g(aroundinc[lg])
    dataout3[lg]['logname'] = lg
    if isinc[lg] == 't':
        dataout3[lg]['label'] = 1
    else:
        dataout3[lg]['label'] = 0
        
    for sig in sigfreqlogIntscore[lg].keys():
        sk = sigfreqlogIntscore[lg][sig]
        if sig!= '-1' and sigtypenumberdict[sig] in keepset:
            if sk == 0:
                dataout3[lg]['k0'] +=1
            if sk>0 and sk<0.1:
                dataout3[lg]['k1'] +=1
            if sk>=0.1 and sk<0.2:
                dataout3[lg]['k2'] +=1
            if sk>=0.2 and sk<0.3:
                dataout3[lg]['k3'] +=1
            if sk>=0.3 and sk<0.4:
                dataout3[lg]['k4'] +=1
            if sk>=0.4 and sk<0.5:
                dataout3[lg]['k5'] +=1
            if sk>=0.5 and sk<0.6:
                dataout3[lg]['k6'] +=1
            if sk>=0.6 and sk<0.7:
                dataout3[lg]['k7'] +=1
            if sk>=0.7 and sk<0.8:
                dataout3[lg]['k8'] +=1
            if sk>=0.8 and sk<0.9:
                dataout3[lg]['k9'] +=1
            if sk>=0.9 and sk<=1:
                dataout3[lg]['k10'] +=1
                
        if sig!= '-1' and sigtypenumberdict[sig] in possibleset:
            if sk == 0:
                dataout3[lg]['p0'] +=1
            if sk>0 and sk<0.2:
                dataout3[lg]['p2'] +=1
            if sk>=0.2 and sk<0.4:
                dataout3[lg]['p4'] +=1
            if sk>=0.4 and sk<0.6:
                dataout3[lg]['p6'] +=1
            if sk>=0.6 and sk<0.8:
                dataout3[lg]['p8'] +=1
            if sk>=0.8 and sk<=1:
                dataout3[lg]['p10'] +=1
                
        if sig!='-1' and sigtypenumberdict[sig] in mightdropset:
            if sk == 0:
                dataout3[lg]['m0'] +=1
            if sk>0 and sk<0.5:
                dataout3[lg]['m5'] +=1
            if sk>=0.5 and sk<=1:
                dataout3[lg]['m10'] +=1
        if sig!='-1' and sigtypenumberdict[sig] in dropset:
            if sk < 0.8:
                dataout3[lg]['d0'] +=1
            if sk>=0.8 and sk<=1:
                dataout3[lg]['d10'] +=1
fopen3 = open("/home/zwen/Desktop/stat/rd_m36.csv",'w')
writer = csv.DictWriter(fopen3, fieldnames=fieldnames3)
writer.writeheader()
for lg in rd_logname:
    writer.writerow(dataout3[lg])
fopen3.close()


'''data4'''
'''random choose from lognamet and lognamef set individually 10,000 samples without replacement'''
import numpy as np
lognametlist = list(lognamet)
lognameflist = list(lognamef)
'''randomly choose 10,000 from both lognametlist and lognameflist'''
rd_lognametlist = np.random.choice(lognametlist,10000,replace=False)
rd_lognameflist = np.random.choice(lognameflist,10000,replace=False)
rd_logname = []
rd_logname.extend(rd_lognametlist)
rd_logname.extend(rd_lognameflist)


fieldnames4=['logname','aroundinc','label']
for i in range(11):
    fieldnames4.append('k'+str(i))
for i in range(11):
    fieldnames4.append('p'+str(i))
for i in range(2):
    fieldnames4.append('m'+str(i))
for i in range(2):
    fieldnames4.append('d'+str(i))

dataout4 = defaultdict(dict)
for lg in rd_logname:
    for i in range(11):
        dataout4[lg]['k'+str(i)] = 0
    for i in range(11):
        dataout4[lg]['p'+str(i)] = 0
    for i in range(2):
        dataout4[lg]['m'+str(i)] = 0
    for i in range(2):
        dataout4[lg]['d'+str(i)] = 0
    dataout4[lg]['label'] = 0
    
  
   

g = lambda x : 1 if x=='t' else 0    
for lg in rd_logname:
    dataout4[lg]['aroundinc']= g(aroundinc[lg])
    dataout4[lg]['logname'] = lg
    if isinc[lg] == 't':
        dataout4[lg]['label'] = 1
    else:
        dataout4[lg]['label'] = 0
        
    for sig in sigfreqlogIntscore[lg].keys():
        sk = sigfreqlogIntscoretimesfreq[lg][sig]
        if sig!= '-1' and sigtypenumberdict[sig] in keepset:
            if sk == 0:
                dataout4[lg]['k0'] +=1
            if sk>0 and sk<1:
                dataout4[lg]['k1'] +=1
            if sk>=1 and sk<2:
                dataout4[lg]['k2'] +=1
            if sk>=2 and sk<3:
                dataout4[lg]['k3'] +=1
            if sk>=3 and sk<4:
                dataout4[lg]['k4'] +=1
            if sk>=4 and sk<5:
                dataout4[lg]['k5'] +=1
            if sk>=5 and sk<6:
                dataout4[lg]['k6'] +=1
            if sk>=6 and sk<7:
                dataout4[lg]['k7'] +=1
            if sk>=7 and sk<8:
                dataout4[lg]['k8'] +=1
            if sk>=8 and sk<9:
                dataout4[lg]['k9'] +=1
            if sk>=9:
                dataout4[lg]['k10'] +=1
                
        if sig!= '-1' and sigtypenumberdict[sig] in possibleset:
            if sk == 0:
                dataout4[lg]['p0'] +=1
            if sk>0 and sk<1:
                dataout4[lg]['p1'] +=1
            if sk>=1 and sk<2:
                dataout4[lg]['p2'] +=1
            if sk>=2 and sk<3:
                dataout4[lg]['p3'] +=1
            if sk>=3 and sk<4:
                dataout4[lg]['p4'] +=1
            if sk>=4 and sk<5:
                dataout4[lg]['p5'] +=1
            if sk>=5 and sk<6:
                dataout4[lg]['p6'] +=1
            if sk>=6 and sk<7:
                dataout4[lg]['p7'] +=1
            if sk>=7 and sk<8:
                dataout4[lg]['p8'] +=1
            if sk>=8 and sk<9:
                dataout4[lg]['p9'] +=1
            if sk>=9:
                dataout4[lg]['p10'] +=1
                
        if sig!='-1' and sigtypenumberdict[sig] in mightdropset:
            if sk <=1:
                dataout4[lg]['m0'] +=1
            if sk>1:
                dataout4[lg]['m1'] +=1
            
        if sig!='-1' and sigtypenumberdict[sig] in dropset:
            if sk <= 1:
                dataout4[lg]['d0'] +=1
            if sk>1:
                dataout4[lg]['d1'] +=1
fopen4 = open("/home/zwen/Desktop/stat/rd_m4.csv",'w')
writer = csv.DictWriter(fopen4, fieldnames=fieldnames4)
writer.writeheader()
for lg in rd_logname:
    writer.writerow(dataout4[lg])
fopen4.close()

'''generate data five WHERER ENTRY IS THE LOG(FREQUENCY) +1'''


'''add field titles'''
'''data5 took too long to run'''
fieldnames5=['logname','aroundinc','label']
lsig = []
for sig in sigset:
    fieldnames5.append('x'+sig+'x')
    lsig.append('x'+sig+'x')

dataout5 = {}

fopen5 = open("/home/zwen/Desktop/stat/m5.csv",'w')
writer = csv.DictWriter(fopen5, fieldnames=fieldnames5)
writer.writeheader()

g = lambda x : 1 if x=='t' else 0    
for lg in lognameset:
    dataout5['aroundinc']= g(aroundinc[lg])
    dataout5['logname'] = lg
    if isinc[lg] == 't':
        dataout5['label'] = 1
    else:
        dataout5['label'] = 0
    for sig in lsig:   
        if sig in sigfreqlog[lg].keys():
            sk = sigfreqlog[lg][sig]
            if(sk>0):
                '''+1 FOR THE CASE WHERE SK = 1'''
                dataout5['x'+sig+'x'] = np.log(sk)+1
        else:
            dataout5['x'+sig+'x'] = 0
    writer.writerow(dataout5)

fopen5.close()





'''add field titles'''
'''data6  choose signatures with frequence cross data set >=100
   signature value = log(fre)+1
'''

'''random choose from lognamet and lognamef set individually 6,000 samples without replacement'''
import numpy as np
lognametlist = list(lognamet)
lognameflist = list(lognamef)
'''randomly choose 10,000 from both lognametlist and lognameflist'''
rd_lognametlist = np.random.choice(lognametlist,6000,replace=False)
rd_lognameflist = np.random.choice(lognameflist,6000,replace=False)
rd_logname = []
rd_logname.extend(rd_lognametlist)
rd_logname.extend(rd_lognameflist)

fieldnames6=['logname','aroundinc','label']
lsig=[]
for sig in lsiggreatertime:
    fieldnames6.append('x'+sig+'x')
    lsig.append(sig);
  
        

dataout6 = {}

fopen6 = open("/Users/grandwor/Desktop/research/m8.csv",'w')
writer = csv.DictWriter(fopen6, fieldnames=fieldnames6)
writer.writeheader()

g = lambda x : 1 if x=='t' else 0  
count = 0  
for lg in rd_logname:
    count +=1
    dataout6['aroundinc']= g(aroundinc[lg])
    dataout6['logname'] = lg
    if isinc[lg] == 't':
        dataout6['label'] = 1
    else:
        dataout6['label'] = 0
    for sig in lsig:   
        if sig in sigfreqlog[lg].keys():
            sk = sigfreqlog[lg][sig]
            if(sk>0):
                '''+1 FOR THE CASE WHERE SK = 1'''
                dataout6['x'+sig+'x'] = np.log(sk)+1
        else:
            dataout6['x'+sig+'x'] = 0
    print("row count is ",count)
    writer.writerow(dataout6)

fopen6.close()


'''add field titles'''
'''data7  choose signatures with frequence cross data set >=100
   signature value using tf-idf = freq*(log(N/n+1)) smooth
'''

'''random choose from lognamet and lognamef set individually 10,000 samples without replacement'''
import numpy as np
lognametlist = list(lognamet)
lognameflist = list(lognamef)
'''number of lines of data
   number of signatures across all lines of data sigdatacount
'''
Nline = len(lognameset)

'''randomly choose 10,000 from both lognametlist and lognameflist'''
rd_lognametlist = np.random.choice(lognametlist,6000,replace=False)
rd_lognameflist = np.random.choice(lognameflist,6000,replace=False)
rd_logname = []
rd_logname.extend(rd_lognametlist)
rd_logname.extend(rd_lognameflist)

fieldnames7=['logname','aroundinc','label']
lsig = []
for sig in lsiggreatertime:
    fieldnames7.append('x'+sig+'x')
    lsig.append(sig)
  
        

dataout7 = {}

fopen7 = open("/Users/grandwor/Desktop/research/m9.csv",'w')
writer = csv.DictWriter(fopen7, fieldnames=fieldnames7)
writer.writeheader()

g = lambda x : 1 if x=='t' else 0  
count = 0  
for lg in rd_logname:
    count +=1
    dataout7['aroundinc']= g(aroundinc[lg])
    dataout7['logname'] = lg
    if isinc[lg] == 't':
        dataout7['label'] = 1
    else:
        dataout7['label'] = 0
    for sig in lsig:   
        if sig in sigfreqlog[lg].keys():
            sk = sigfreqlog[lg][sig]
            if(sk>0):
                '''+1 FOR THE CASE WHERE SK = 1'''
                dataout7['x'+sig+'x'] = sk*np.log(Nline/sigdatacount[sig]+1)
        else:
            dataout7['x'+sig+'x'] = 0
    print("row count is ",count)
    writer.writerow(dataout7)

fopen7.close()

'''add field titles'''
'''data10  choose signatures with frequence cross data set >=50
   signature value = log(fre)+1
'''

'''random choose from lognamet and lognamef set individually 6,000 samples without replacement'''
import numpy as np
lognametlist = list(lognamet)
lognameflist = list(lognamef)
'''randomly choose 10,000 from both lognametlist and lognameflist'''
rd_lognametlist = np.random.choice(lognametlist,6000,replace=False)
rd_lognameflist = np.random.choice(lognameflist,6000,replace=False)
rd_logname = []
rd_logname.extend(rd_lognametlist)
rd_logname.extend(rd_lognameflist)

fieldnames6=['logname','aroundinc','label']
lxsigx = []
lsig = []

for sig in lsiggreatertime:
    fieldnames6.append('x'+sig+'x')
    lsig.append(sig)
  
        

dataout6 = {}

fopen6 = open("/Users/grandwor/Desktop/research_stat/m13.csv",'w')
writer = csv.DictWriter(fopen6, fieldnames=fieldnames6)
writer.writeheader()

g = lambda x : 1 if x=='t' else 0  
count = 0  
for lg in rd_logname:
    count +=1
    dataout6['aroundinc']= g(aroundinc[lg])
    dataout6['logname'] = lg
    if isinc[lg] == 't':
        dataout6['label'] = 1
    else:
        dataout6['label'] = 0
    for sig in lsig: 
        xsigx = 'x'+sig+'x'
        if sig in sigfreqlog[lg].keys():
            sk = sigfreqlog[lg][sig]
            if(sk>0):
                '''+1 FOR THE CASE WHERE SK = 1'''
                
                dataout6[xsigx] = np.log(sk)+1
                
        else:
            dataout6[xsigx] = 0
    print("row count is ",count)
    writer.writerow(dataout6)

fopen6.close()


'''add field titles'''
'''data11  choose signatures with frequence cross data set >=50
   signature value using tf-idf = freq*(log(N/n+1)) smooth
'''

'''random choose from lognamet and lognamef set individually 10,000 samples without replacement'''
import numpy as np
lognametlist = list(lognamet)
lognameflist = list(lognamef)
'''number of lines of data
   number of signatures across all lines of data sigdatacount
'''
Nline = len(lognameset)

'''randomly choose 10,000 from both lognametlist and lognameflist'''
rd_lognametlist = np.random.choice(lognametlist,6000,replace=False)
rd_lognameflist = np.random.choice(lognameflist,6000,replace=False)
rd_logname = []
rd_logname.extend(rd_lognametlist)
rd_logname.extend(rd_lognameflist)

fieldnames7=['logname','aroundinc','label']
lxsigx = []
lsig=[]
    
for sig in lsiggreatertime:
    fieldnames7.append('x'+sig+'x')
    lsig.append(sig)
  

dataout7 = {}

fopen7 = open("/Users/grandwor/Desktop/research_stat/m14.csv",'w')
writer = csv.DictWriter(fopen7, fieldnames=fieldnames7)
writer.writeheader()

g = lambda x : 1 if x=='t' else 0  
count = 0  
for lg in rd_logname:
    count +=1
    dataout7['aroundinc']= g(aroundinc[lg])
    dataout7['logname'] = lg
    if isinc[lg] == 't':
        dataout7['label'] = 1
    else:
        dataout7['label'] = 0
    for sig in lsig:   
        if sig in sigfreqlog[lg].keys():
            sk = sigfreqlog[lg][sig]
            if(sk>0):
                '''+1 FOR THE CASE WHERE SK = 1'''
                dataout7['x'+sig+'x'] = (np.log(sk)+1)*np.log(Nline/sigdatacount[sig]+1)
        else:
            dataout7['x'+sig+'x'] = 0
    print("row count is ",count)
    writer.writerow(dataout7)

fopen7.close()


''''''
'''add field titles'''
'''data_m12  choose signatures with frequence cross data set >=50
   signature value = log(fre)+1
'''

'''random choose from lognamet and lognamef set individually 10,000 samples without replacement'''
import numpy as np
lognametlist = list(lognamet)
lognameflist = list(lognamef)
'''randomly choose 10,000 from both lognametlist and lognameflist'''
rd_lognametlist = np.random.choice(lognametlist,10000,replace=False)
rd_lognameflist = np.random.choice(lognameflist,10000,replace=False)
rd_logname = []
rd_logname.extend(rd_lognametlist)
rd_logname.extend(rd_lognameflist)

fieldnames6=['logname','aroundinc','label']

lsig = []
for sig in lsiggreatertime:
    fieldnames6.append('x'+sig+'x')   
    lsig.append(sig)

        

dataout6 = {}

fopen6 = open("/Users/grandwor/Desktop/research_stat/m12.csv",'w')
writer = csv.DictWriter(fopen6, fieldnames=fieldnames6)
writer.writeheader()

g = lambda x : 1 if x=='t' else 0  
count = 0  
for lg in rd_logname:
    count +=1
    dataout6['aroundinc']= g(aroundinc[lg])
    dataout6['logname'] = lg
    if isinc[lg] == 't':
        dataout6['label'] = 1
    else:
        dataout6['label'] = 0
    for sig in lsig:   
        if sig in sigfreqlog[lg].keys():
            sk = sigfreqlog[lg][sig]
            if(sk>0):
                '''+1 FOR THE CASE WHERE SK = 1'''
                dataout6['x'+sig+'x'] = np.log(sk)+1
                print("sig ",sig," lgfre ", dataout6[sig])
        else:
            dataout6['x'+sig+'x'] = 0
    print("row count is ",count)
    writer.writerow(dataout6)

fopen6.close()









'''logistic regression'''
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
data1 = pd.read_csv("/home/zwen/Desktop/stat/m1.csv")
fieldnames1=['logname','aroundinc','label']
for i in range(11):
    fieldnames1.append('k'+str(i))
for i in range(0,11,2):
    fieldnames1.append('p'+str(i))
for i in range(0,11,5):
    fieldnames1.append('m'+str(i))
for i in range(0,11,10):
    fieldnames1.append('d'+str(i))
data1.columns=fieldnames1
data1.head()
'''get the train and test data'''
X= data1.iloc[:,3:].values
y =data1.iloc[:,2].values

X_train,X_test, y_train, y_test =train_test_split(X,y,test_size=.3, random_state=25)
logreg = LogisticRegression()
logreg.fit(X_train,y_train)

'''test'''
y_pred=logreg.predict(X_test)

from sklearn.metrics import confusion_matrix
confusion_matrix=confusion_matrix(y_test,y_pred)
confusion_matrix

print(classification_report(y_test,y_pred))

'''test with SVM'''
from sklearn.svm import SVC
svcrbf=SVC()
svclinear=SVC(kernel='linear')
model=svclinear.fit(X_train,y_train)
y_pred = model.predict(X_test)
from sklearn.metrics import confusion_matrix
confusion_matrix=confusion_matrix(y_test,y_pred)
confusion_matrix

print(classification_report(y_test,y_pred))


'''logistic regression on data2'''

fieldnames2=['logname','aroundinc','label']
for i in range(11):
    fieldnames2.append('k'+str(i))
for i in range(11):
    fieldnames2.append('p'+str(i))
for i in range(2):
    fieldnames2.append('m'+str(i))
for i in range(2):
    fieldnames2.append('d'+str(i))
data2 = pd.read_csv("/home/zwen/Desktop/stat/m2.csv")
data2.columns = fieldnames2
X= data2.iloc[:,3:].values
y =data2.iloc[:,2].values

X_train,X_test, y_train, y_test =train_test_split(X,y,test_size=.3, random_state=25)
logreg = LogisticRegression()
logreg.fit(X_train,y_train)

'''test'''
y_pred=logreg.predict(X_test)

from sklearn.metrics import confusion_matrix

confusion_matrix=confusion_matrix(y_test,y_pred)
confusion_matrix

print(classification_report(y_test,y_pred))

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
data1 = pd.read_csv("/home/zwen/Desktop/stat/m1.csv")
fieldnames1=['logname','aroundinc','label']
for i in range(11):
    fieldnames.append('k'+str(i))
for i in range(0,11,2):
    fieldnames.append('p'+str(i))
for i in range(0,11,5):
    fieldnames.append('m'+str(i))
for i in range(0,11,10):
    fieldnames.append('d'+str(i))
data1.columns=fieldnames1
data1.head()
'''get the train and test data'''
X= data1.iloc[:,3:].values
y =data1.iloc[:,2].values

X_train,X_test, y_train, y_test =train_test_split(X,y,test_size=.3, random_state=25)
logreg = LogisticRegression()
logreg.fit(X_train,y_train)

'''test'''
y_pred=logreg.predict(X_test)

from sklearn.metrics import confusion_matrix
confusion_matrix=confusion_matrix(y_test,y_pred)
confusion_matrix

print(classification_report(y_test,y_pred))

'''test with SVM'''
from sklearn.svm import SVC
model=SVC().fit(X_train,y_train)
y_pred = model.predict(X_test)
from sklearn.metrics import confusion_matrix
confusion_matrix=confusion_matrix(y_test,y_pred)
confusion_matrix

print(classification_report(y_test,y_pred))






'''logistic regression on rd_m3'''
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
data3 = pd.read_csv("/home/zwen/Desktop/stat/rd_m36.csv")
fieldnames3=['logname','aroundinc','label']
for i in range(11):
    fieldnames3.append('k'+str(i))
for i in range(0,11,2):
    fieldnames3.append('p'+str(i))
for i in range(0,11,5):
    fieldnames3.append('m'+str(i))
for i in range(0,11,10):
    fieldnames3.append('d'+str(i))
data3.columns=fieldnames3
data3.head()
'''get the train and test data'''
X= data3.iloc[:,3:].values
y =data3.iloc[:,2].values

X_train,X_test, y_train, y_test =train_test_split(X,y,test_size=.3, random_state=25)
logreg = LogisticRegression()
logreg.fit(X_train,y_train)

'''test'''
y_pred=logreg.predict(X_test)

from sklearn.metrics import confusion_matrix
confusion_matrix=confusion_matrix(y_test,y_pred)
confusion_matrix

print(classification_report(y_test,y_pred))
'''test with SVM'''
from sklearn.svm import SVC
svclinear=SVC(kernel='linear')
model=SVC().fit(X_train,y_train)
modellinear=svclinear.fit(X_train,y_train)
y_pred = model.predict(X_test)
from sklearn.metrics import confusion_matrix
confusion_matrix=confusion_matrix(y_test,y_pred)
confusion_matrix

print(classification_report(y_test,y_pred))




'''analysis on data set rd_m4'''

'''logistic regression on rd_m4'''
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
data4 = pd.read_csv("/home/zwen/Desktop/stat/rd_m4.csv")
fieldnames4=['logname','aroundinc','label']
for i in range(11):
    fieldnames4.append('k'+str(i))
for i in range(11):
    fieldnames4.append('p'+str(i))
for i in range(2):
    fieldnames4.append('m'+str(i))
for i in range(2):
    fieldnames4.append('d'+str(i))
data4.columns=fieldnames4
data4.head()
'''get the train and test data'''
X= data4.iloc[:,3:].values
y =data4.iloc[:,2].values

X_train,X_test, y_train, y_test =train_test_split(X,y,test_size=.3, random_state=25)
logreg = LogisticRegression()
logreg.fit(X_train,y_train)

'''test'''
y_pred=logreg.predict(X_test)

from sklearn.metrics import confusion_matrix
confusion_matrix=confusion_matrix(y_test,y_pred)
confusion_matrix

print(classification_report(y_test,y_pred))
'''test with SVM'''
from sklearn.svm import SVC
svclinear=SVC(kernel='linear')
model=SVC().fit(X_train,y_train)
modellinear=svclinear.fit(X_train,y_train)
y_pred = modellinear.predict(X_test)
from sklearn.metrics import confusion_matrix
confusion_matrix=confusion_matrix(y_test,y_pred)
confusion_matrix

print(classification_report(y_test,y_pred))



'''logistic and svm on data 8
'''
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
data8 = pd.read_csv("/Users/grandwor/Desktop/research/m8.csv")

data8.columns=fieldnames6
data8.head()
'''get the train and test data'''
X= data8.iloc[:,3:].values
y =data8.iloc[:,2].values

X_train,X_test, y_train, y_test =train_test_split(X,y,test_size=.3, random_state=25)
logreg = LogisticRegression()
logreg.fit(X_train,y_train)

'''test'''
y_pred=logreg.predict(X_test)

from sklearn.metrics import confusion_matrix
confusion_matrix=confusion_matrix(y_test,y_pred)
confusion_matrix

print(classification_report(y_test,y_pred))

'''test with SVM'''
from sklearn.svm import SVC
svcrbf=SVC()
svclinear=SVC(kernel='linear')
model=svclinear.fit(X_train,y_train)
y_pred = model.predict(X_test)
from sklearn.metrics import confusion_matrix
confusion_matrix=confusion_matrix(y_test,y_pred)
confusion_matrix

print(classification_report(y_test,y_pred))



'''logistic and SVM on data 9
'''

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
data9 = pd.read_csv("/Users/grandwor/Desktop/research/m9.csv")

data9.columns=fieldnames7
data9.head()
'''get the train and test data'''
X= data9.iloc[:,3:].values
y =data9.iloc[:,2].values

X_train,X_test, y_train, y_test =train_test_split(X,y,test_size=.3, random_state=25)
logreg = LogisticRegression()
logreg.fit(X_train,y_train)

'''test'''
y_pred=logreg.predict(X_test)

from sklearn.metrics import confusion_matrix
confusion_matrix=confusion_matrix(y_test,y_pred)
confusion_matrix

print(classification_report(y_test,y_pred))

'''test with SVM'''
from sklearn.svm import SVC
svcrbf=SVC()
svclinear=SVC(kernel='linear')
model=svclinear.fit(X_train,y_train)
y_pred = model.predict(X_test)
from sklearn.metrics import confusion_matrix
confusion_matrix=confusion_matrix(y_test,y_pred)
confusion_matrix

print(classification_report(y_test,y_pred))


'''logistic and SVM on data 10
'''

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
data10 = pd.read_csv("/Users/grandwor/Desktop/research_stat/m13.csv")

data10.columns=fieldnames6
data10.head()
'''get the train and test data'''
X= data10.iloc[:,3:].values
y =data10.iloc[:,2].values

X_train,X_test, y_train, y_test =train_test_split(X,y,test_size=.3, random_state=25)
logreg = LogisticRegression()
logreg.fit(X_train,y_train)

'''test'''
y_pred=logreg.predict(X_test)

from sklearn.metrics import confusion_matrix
confusion_matrix=confusion_matrix(y_test,y_pred)
confusion_matrix

print(classification_report(y_test,y_pred))

'''test with SVM'''
from sklearn.svm import SVC
svcrbf=SVC()
svclinear=SVC(kernel='rbf')
model=svclinear.fit(X_train,y_train)
y_pred = model.predict(X_test)
from sklearn.metrics import confusion_matrix
confusion_matrix=confusion_matrix(y_test,y_pred)
confusion_matrix

print(classification_report(y_test,y_pred))



'''logistic and SVM on data 11
'''

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
data11 = pd.read_csv("/Users/grandwor/Desktop/research_stat/m14.csv")

data11.columns=fieldnames7
data11.head()
'''get the train and test data'''
X= data11.iloc[:,3:].values
y =data11.iloc[:,2].values

X_train,X_test, y_train, y_test =train_test_split(X,y,test_size=.3, random_state=25)
logreg = LogisticRegression()
logreg.fit(X_train,y_train)

'''test'''
y_pred=logreg.predict(X_test)

from sklearn.metrics import confusion_matrix
confusion_matrix=confusion_matrix(y_test,y_pred)
confusion_matrix

print(classification_report(y_test,y_pred))

'''test with SVM'''
from sklearn.svm import SVC
svcrbf=SVC()
svclinear=SVC(kernel='rbf')
model=svclinear.fit(X_train,y_train)
y_pred = model.predict(X_test)
from sklearn.metrics import confusion_matrix
confusion_matrix=confusion_matrix(y_test,y_pred)
confusion_matrix

print(classification_report(y_test,y_pred))

'''generate the Bayesian structures'''
'''neighbordic'''
'''local importance_ chance in the data set the signatures in logs labelled one'''
localimpcount={}
localnonimpcount={}
for sig in lsiggreatertime:
    localimpcount[sig]=0
    localnonimpcount[sig] = 0
    for lg in logsignature[sig]:
        if lg in lognamet:
            localimpcount[sig] +=1
        if lg in lognamef:
            localnonimpcount[sig]+=1
localimp = {}
for sig in lsiggreatertime:
    k = len(logsignature[sig])
    if k >0:
        localimp[sig] = localimpcount[sig]/k
    else:
        localimp[sig] = 0

'''generate the Bayesian structures'''
'''neighbordic'''
signb = {}
count1 = 0
for sig in lsiggreatertime:
    count1 +=1
    print("Number of sig ", count1)
    signb[sig]={}
    for lg in logsignature[sig]:
        if sig in siglog[lg]:
            for s in siglog[lg]:
                if s in lsiggreatertime:
                    '''check whether the co-neighbor frequency alread caluculate in signb[s][sig]'''
                    '''elif: first time to calculate this neighborhood information'''
                    if s in signb.keys() and s != sig:
                        signb[sig][s] = signb[s][sig]
               
                    elif s in signb[sig].keys():
                        signb[sig][s] +=1
                    else:
                        signb[sig][s] = 1
                        
'''change count to the probability'''
signbprob = {}
sum = {}
for sig in signb.keys():
    sum[sig] = 0
    for s in signb[sig].keys():
        sum[sig] +=signb[sig][s]
for sig in signb.keys():
    signbprob[sig] ={}
    for s in signb[sig].keys():
        signbprob[sig][s] = float(signb[sig][s]/signb[sig][sig])
        
'''collective learning, try to get stable  probabability from its surrounding one-step-away neighbors
weight is calculated in the signbprob, and the normalized proximity score is used as the initial node importance
also use restart value, assign 0.2 for restart and right now I don't know how to normalize
'''  


'''
'''
sigimp1 = {}
'''initiate the sigimp[sig] to be the normalized proximity score'''
for sig in sigset:
    if sig != "-1":
        sigimp1[sig] = normproxintdict[sig]
    else:
        sigimp1[sig] = 0.1
sigimp = {}
'''initiate the sigimp[sig] to be the normalized proximity score'''
for sig in sigset:
    if sig != "-1":
        sigimp[sig] = normproxintdict[sig]
    else:
        sigimp[sig] = 0.1
limit = 0.1;
'''normalization factor'''
nf = 1
count = 0
while(limit>0.1):
    limit = 0 
    count +=1
    for sig in lsiggreatertime: 
        sum = 0
        
        for s in signbprob[sig].keys():
            '''update the importance by the neighbor d importance weighted by the neighbor probability'''
            sum += nf*sigimp[s]*signbprob[sig][s]
        '''print("sig is ", sig,"sigimp", sigimp[sig])'''  
        if sum>1:
            sum = 1
        limit +=abs(sum - sigimp[sig])
        print("limit is ",limit) 
        sigimp[sig] = sum
    print("iterate count", count)
    print("limit is ",limit) 
    
    
def write_report(r1, r2, filename):
        input_file=open(filename, "a")
        for k in r1.keys():
            line = '{}, {} {}'.format(k,r1[k],r2[k])
            print>>input_file, line
filename1 = "/home/zwen/Desktop/stat/sigimpcomparison.txt"
write_report(sigimp,sigimp1,filename1)


    
for sig in sigimp1.keys():
    print("sig is", sig, " difference is imp1 - imp is ",sigimp1[sig] - sigimp[sig])
