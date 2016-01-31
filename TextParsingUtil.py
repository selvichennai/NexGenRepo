import re
from nltk.corpus import stopwords
import pandas


#------------------------------------------
#Function:cleanhtml
#Params: raw_html --> raw string from which HTML tags need to be removed
#Comment: Use this function to clean your string from HTML tags
#-------------------------------------------
def cleanhtml(raw_html):

    cleanr =re.compile('<.*?>')

    cleantext = re.sub(cleanr,'', raw_html)

    return cleantext


#------------------------------------------
#Function: CleanNonAscii
#Params: tobeCleanedText --> String from which all numbers and special chars need to be removed
#Comment: Use this function to remove all sepcial chatrs and in particular non-ascii chars
#-------------------------------------------
def CleanNonAscii(tobeCleanedText):
    
    cleanText = re.sub("[^a-zA-Z]",           # The pattern to search for
           " ",                   # The pattern to replace it with
           tobeCleanedText)
    
    return cleanText


#------------------------------------------
#Function: RemoveStopWordsInternal
#Params:  tobeCleanedString --> string from which you want the stopwords to be removed
#Comment: Use this function to remove all stopwords from your string. Note that this is an internal function
#-------------------------------------------
def RemoveStopWordsInternal(tobeCleanedString):
    prunedList = []
    
    # TODO: Need to fix the bug with nltk.download(). Then we can remove this array
    stopwordLookup = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
                        'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
                        'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
                        'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
                        'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
                        'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
                        'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
                        'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
                        'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
                        'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
                        'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
                        'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
                            
    wordsinInputString = [word.lower() for word in tobeCleanedString.split()]
    
    #stopWordList = set(stopwords.words('english'))
    stopWordList = set(stopwordLookup)
    
    return [cleanWord for cleanWord in wordsinInputString if cleanWord not in stopwordLookup]

 
    
 #------------------------------------------
#Function: RemoveStopWordsInternal
#Params:  listOfReviews --> list of strings from which you want the stopwords to be removed
#Comment: Use this function to remove all stopwords from your string. Note that this is an external function.
#-------------------------------------------    
def RemoveStopWords(listOfReviews):
    
    cleanedList = map(RemoveStopWordsInternal, listOfReviews)
    
    return list(cleanedList)

#------------------------------------------
#Function: ReadCSVFile
#Params:fileName
#Comment: This function reads a tsv file
#------------------------------------------- 

def ReadCSVFile(fileName):
    
    return pandas.read_csv(fileName, sep='\t', quoting=3,header=0)
    
    
