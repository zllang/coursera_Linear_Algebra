voting_data = list(open("voting_record_dump109.txt"))

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    _dict = dict()
    for line in voting_data:
        _item = line.split(" ")
        _dict[_item[0]] = [int(ele) for ele in _item[3:]]
    return _dict

## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
 #   from vec import Vec
 #   from dictutil import list2dict
    from vecutil import list2vec
    #list_a = voting_data[sen_a]
    #dict_a = list2dict(list_a)
    vec_a = list2vec(voting_dict[sen_a]) #Vec(set(dict_a.keys()),dict_a)
    #list_b = voting_data[sen_b]
    #dict_b = list2dict(list_b)
    vec_b = list2vec(voting_dict[sen_b]) #Vec(set(dict_b.keys()),dict_b)
    return vec_a*vec_b


## Task 3

def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    result = 0
    result_name = ''
    for sen_name  in voting_dict.keys():
        if(sen_name != sen):
            tmp = policy_compare(sen,sen_name,voting_dict)
            if(tmp > result or result_name ==''):
                result = tmp
                result_name = sen_name    
    return result_name
    

## Task 4

def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
    result = 0
    result_name = ''
    for sen_name  in voting_dict.keys():
        if(sen_name != sen):
            tmp = policy_compare(sen,sen_name,voting_dict)
            if(tmp < result or result_name ==''):
                result = tmp
                result_name = sen_name    
    return result_name
    
    

## Task 5

most_like_chafee    = most_similar('Chafee',create_voting_dict())
least_like_santorum = least_similar('Santorum',create_voting_dict()) 



# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    from vecutil import list2vec
    _sum = 0
    vec0 = list2vec(voting_dict[sen])
    for sen_name in sen_set:
        vec1 = list2vec(voting_dict[sen_name])
        _sum += vec0 * vec1
    return _sum/len(sen_set)

def max_average_Democrat():
    _other_set = set()
    _democrat_set = set()
    for line in voting_data:
        _item = line.split(" ")
        if(_item[1]=="D"):
            _democrat_set.add(_item[0]) #_democrat_dict[_item[0]] = [int(ele) for ele in _item[3:]]
        else:
            _other_set.add(_item[0]) #_other_dict[_item[0]] = [int(ele) for ele in _item[3:]]
    max_average = 0
    max_sen_name = ''
    _voting_dict = create_voting_dict()
    for sen_name in _other_set:
        cur_average = find_average_similarity(sen_name,_democrat_set,_voting_dict)
        if(cur_average>max_average or max_sen_name==''):
            max_average = cur_average
            max_sen_name = sen_name
    return max_sen_name


most_average_Democrat = max_average_Democrat() # give the last name (or code that computes the last name)


# Task 7

def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
    return 0

average_Democrat_record = '...' # (give the vector)


# Task 8

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    return ('...', '')

