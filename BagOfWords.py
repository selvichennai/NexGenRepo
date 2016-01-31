from TextParsingUtil import *

# read the TSV file
rawInput = ReadCSVFile("./ModelDataFiles/unlabeledTrainData.tsv")

rawInputReview = rawInput['review'].values.tolist()

# clean non-ascii and HTML tags
cleanedRawInput = map( lambda rawReviewLine : CleanNonAscii(cleanhtml(rawReviewLine)), rawInputReview)

#remove stopwords. The return is a list of list. Each element in the parent list has a list of words in a sentence 
cleanedInputForAnalysis = RemoveStopWords(list(cleanedRawInput)) 

# add scoring functions to it to find frequent words and creat a training set

                                                                       

