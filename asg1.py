# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#CSCI3220 2018-19 First Term Assignment 1

#I declare that the assignment here submitted is original except for source material explicitly acknowledged, and that the same or closely related material has not been previously submitted for another course. I also acknowledge that I am aware of University policy and regulations on honesty in academic work, and of the disciplinary guidelines and procedures applicable to breaches of such policy and regulations, as contained in the following websites.

#University Guideline on Academic Honesty:
#http://www.cuhk.edu.hk/policy/academichonesty/

#Student Name: Nigel Nicholas
#Student ID  : 1155088791
import sys
sys.setrecursionlimit(1500)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#                                   Function Optimum
#          Input:
#         rStart = the index of row where you start ( from string r )
#         sStart = the index of column where you start ( from string s )
#       returns the optimum score for the table[rstart][sstart]
#           IN the process, it will fill in the score table


def optimum(rStart, sStart ):
    # if you've reached the end of the table on either row or column (base case)
    if rStart == len(r) and sStart == len(s):
        score_table[rStart][sStart] = 0
        return 0

    elif rStart == len(r) :
        arrow_table[rStart][sStart].append((rStart, sStart+1))
        score_table[rStart][sStart] = (len(s)-sStart)*indel
        return (len(s)-sStart)*indel
    
    elif sStart == len(s) :
        arrow_table[rStart][sStart].append((rStart+1, sStart))
        score_table[rStart][sStart] = (len(r)-rStart)*indel
        return  (len(r)-rStart)*indel

    # comparing the start character of each string being specified by the index
    # to know whether it's +match (if same) or +mismatch ( if different)

    if r[rStart]==s[sStart]:
        adding = match

    else: 
        adding = mismatch

    # recursive function to reach the base case
    # Diagonal,Vertical, and Horiziontal are variables to contain the corresponding score
    
    if not score_table[rStart+1][sStart+1]:
        diagonal = optimum(rStart+1,sStart+1)
    else:
        diagonal = score_table[rStart+1][sStart+1]
    
    if not score_table[rStart][sStart+1]:
        horizontal = optimum(rStart,sStart+1)
    else:
        horizontal = score_table[rStart][sStart+1]

    if not score_table[rStart+1][sStart]:
        vertical = optimum(rStart+1,sStart)
    else:
        vertical = score_table[rStart+1][sStart]

    
    score = maximum( diagonal+adding, vertical+indel, horizontal+indel, rStart,sStart )
    score_table[rStart][sStart] = score
    
    return score
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
##                                      Fucntion Maximum
#       Input:
#       diagonal,vertical,horizontal = derived from the call function from optimum
#       rStart , sStart = same as previous function has described
#       
#       Returns: the maximum score of either diagonal,vertical, or horizontal
#               In the process, it fills in the arrow_table for traceback later on
        

def maximum(diagonal , vertical , horizontal , rStart , sStart):
    # Find maxScore first
    if  diagonal >= vertical and diagonal >= horizontal:
        maxScore = diagonal
    
    elif vertical >= horizontal and vertical >= diagonal:
        maxScore = vertical
    
    elif horizontal >= diagonal and horizontal >= vertical:
        maxScore = horizontal

    # Use maxScore to put in the table which gives the optimum score

    if maxScore == diagonal:
            arrow_table[rStart][sStart].append( (rStart+1, sStart+1) )

    if maxScore == vertical:
            arrow_table[rStart][sStart].append( (rStart+1, sStart) )

    if maxScore == horizontal:
            arrow_table[rStart][sStart].append( (rStart,sStart+1) )


    return maxScore
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
##                              Function Traceback
#               Input:
#               rStart, sStart = the index at which string r and s starts
#               rStr, sStr = the string to store for printing the alignment later on
#               
#               Use: 
#               To find paths from indext (0,0) to (len(r), len(s)) and print the 2 strings
#                   that gives the best alignment score


def traceback(rStart, sStart, rStr, sStr):

        # base case, where the indexes have reached the corner bottom right
    if rStart == len(r) and sStart == len(s):
        print "\n"+ rStr
        print sStr  
        return 
    
        # traversing recursively from a place to another while adding characters 1 by 1 to
        # new_rStr and new_sStr -> which are the stored local string variable to be printed
        # later on 

    if (rStart, sStart+1) in arrow_table[rStart][sStart]:
            new_rStr = rStr + "_"
            new_sStr = sStr + s[sStart]
            traceback(rStart, sStart+1, new_rStr, new_sStr)
    


    if (rStart+1, sStart+1) in arrow_table[rStart][sStart]:
            new_rStr = rStr + r[rStart]
            new_sStr = sStr + s[sStart]
            traceback(rStart+1, sStart+1, new_rStr, new_sStr)
    

    if (rStart+1, sStart) in arrow_table[rStart][sStart]:
            new_rStr = rStr + r[rStart]
            new_sStr = sStr + "_"
            traceback(rStart+1, sStart, new_rStr, new_sStr)


    return 

def scoretable():
    header = "  "
    for x in s:
        header = header + "  " + x + "  "
    print header    
    print "  " + '-'*5*len(s) 

    for i in range( len(r) ):
        string = str()
        string = r[i] + " "
        for j in range ( len(s) ):
            
            if score_table[i][j] >=0:
                string = string + "| " + str(score_table[i][j]) + " |"
            else:
                string = string + "| " + str(score_table[i][j]) + "|"
        print string


#- - - - - - - - - - - - - - - - - - - MAIN - - - - - - - - - - - - - - - - - - - - - - - - #

# prompts by the question : 
match = input()         # score for a match 
mismatch = input()      # score for a mismatch
indel = input()         # score for indel
r = raw_input()         # first DNA sequence string
s = raw_input()         # second DNA sequence string

# trial
# r = "ATGCGT"
# s = "ACGGCGT"


arrow_table = [ [ []for j in range(len(s)+1) ] for k in range(len(r)+1) ]
score_table = [ [0 for j in range(len(s)+1)] for k in range(len(r)+1)]


maxScore = optimum(0,0)



print str(maxScore)

# next is the traceback: order = horizontal, diagonal, vertical

#rStr and sStr is the one that holds the string for best alignment string
rStr = str()
sStr = str()



traceback(0,0, rStr,sStr)

# uncomment below to see table of score devised
scoretable()
#print arrow_table

# NOTE: TO REDUCE REDUNDANCY WE CAN USE SCORE TABLE TO MAKE SURE IF IT IS FILLED,
# NO NEED TO CHECK ANYMORE
# The base cases for score_table is wrong, because it depends on the indel score, not simply
# -1
# Arrow table should also fill in the base cases

