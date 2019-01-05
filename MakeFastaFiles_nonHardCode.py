#COMMAND LINE TO RUN THIS PROGRAM IN COMMAND PROMTN (RUN IT FROM ANYWHERE)
#MakeFastaFiles_nonHardCode.py
#-i C:\\Users\s433088\AppData\Local\Programs\Python\Python36-32\Codes_bere_lap\Cluster_Unclustered_Count_0_with_trimmed_sequences_45-69bp__single_target_sheets.csv
#-o C:\\Users\s433088\AppData\Local\Programs\Python\Python36-32\Codes_bere_lap\Cluster_Unclustered_Count_0_with_trimmed_sequences_45-69bp__single_target_sheets.fasta
#-u 11
# -s seqIndex
# -t trimmedSeq

#COMMAND LINE TO RUN THIS PROGRAM IN LAPTOP AT HOME TO RUN INDIVIDUAL TARGETS (THIS MUST BE RUN AS A BATCH FILE)

#MakeFastaFiles_nonHardCode.py
#-i C:\\Users\MHS\Documents\PhD\Thesis\official_data_set\preliminary_workflow\Split_cluster_unclustered\998897.csv
#-o C:\\Users\MHS\Documents\PhD\Thesis\official_data_set\preliminary_workflow\FastaFiles_Split_cluster_unclustered\998897_fasta.csv
#-u 6
#-s 0
#-t 2

#ALL
#MakeFastaFiles_nonHardCode.py -i C:\\Users\MHS\Documents\PhD\Thesis\official_data_set\preliminary_workflow\Split_cluster_unclustered\998897.csv -o C:\\Users\MHS\Documents\PhD\Thesis\official_data_set\preliminary_workflow\FastaFiles_Split_cluster_unclustered\998897_fasta.csv -u 6 -s 0 -t 2
import sys, getopt

def main(argv):
    
    InputCSVFileName = ""
    OutputFASTAFile = ""
    SeqID_index = 0
    TrimmedSequence_index = 0
    rowWhereDataStarts = ""
    OutputRows = ""
    

    try:
        opts, args = getopt.getopt(argv,"i:o:u:s:t:",["inCSVfile=","outFASTAFile=","rowWhereDataStarts=","SeqID_index=","TrimmedSequence_index="])
    except getopt.GetoptError:
      print ('MakeFastaFiles.py -i <CSVFile> -o <OutputFastaFile> -u <rowWhereDataStarts> -s <SeqID_index> -t <TrimmedSequence_index>')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
         print ('MakeFastaFiles.py -i <CSVFile> -o <OutputFastaFile> -u <rowWhereDataStarts> -s <SeqID_index> -t <TrimmedSequence_index>')
         sys.exit()
        elif opt in ("-i", "--inCSVfile"):
            InputCSVFileName = arg
        elif opt in ("-o", "--outFASTAFile"):
            OutputFASTAFile = arg
        elif opt in ("-u", "--rowWhereDataStarts"):
            rowWhereDataStarts = arg
            
        elif opt in ("-s", "--SeqID_index"):
            SeqID_index = int(arg)
        elif opt in ("-t", "--TrimmedSequence_index"):
            TrimmedSequence_index = int(arg)
    

    #make variables

    inputFile = open(InputCSVFileName)
    OutputFile = open(OutputFASTAFile,'a')
        


    #Read throuh and skip header row

    for c in range(0, int(rowWhereDataStarts)):
        HeaderTemp = inputFile.readline()

    #Reading through the rows and breaking at the end of the data

    tempstring = "temp"
    while tempstring:
        tempstring = inputFile.readline()
        if tempstring == "":
            break
        templine = tempstring.splitlines()
        x = templine[0]
        rowlist = x.split(",")
        SeqID = rowlist[SeqID_index]
        TrimmedSequence = rowlist[TrimmedSequence_index]
        OutputRows = ">" + SeqID + '\n' + TrimmedSequence + '\n'
        OutputFile.write(OutputRows)

    inputFile.close()
    OutputFile.close()


 
if __name__ == "__main__":
    main(sys.argv[1:])
