import yaml

def getQuestion():
    # Read and parse the YAML file
    with open('media/resources/qa.yaml', 'r') as file:
        quiz_data = yaml.load(file, Loader=yaml.FullLoader)

    # Load the result.yaml file (if it exists)
    try:
        with open('media/resources/result.yaml', 'r') as result_file:
            result_data = yaml.load(result_file, Loader=yaml.FullLoader)
    except FileNotFoundError:
        result_data = []

    # Assuming quiz_data structure matches your YAML structure
    questions = quiz_data['data']
    quizName = quiz_data['name']
    date = quiz_data['date']
    starttime = quiz_data['starttime']
    runtime = quiz_data['runtime']
    branch = quiz_data['branch']
    extrainfo = quiz_data['extrainfo']
    maxQuestion = quiz_data['maxQuestion']

    

    sevHigh = []
    sevMedi = []
    sevExtra  = []
    for ques in questions:
        if ques['Severity'] == 'high':
            sevHigh.append(ques)
        elif ques['Severity'] == 'medium':
            sevMedi.append(ques)
        else:
            sevExtra.append(ques)
    
    # print("sevHigh", len(sevHigh), " : ",sevHigh)
    # print("sevMedi", len(sevMedi), " : ",sevMedi)
    # print("sevLow",  len(sevExtra), " : ",sevExtra)

    try:
        lastQuestion = result_data[-1]
        lastresponseTime = lastQuestion['Response_time']
        lastAvgTime = lastQuestion['AvgTimeToAnswer']
        noResultData = False

    except:
        lastresponseTime = 20 #default response Time
        lastAvgTime = 15
        noResultData = True

    print("lastresponseTime: ",lastresponseTime,"lastAvgTime: ", lastAvgTime, "lastQuestion: ", "noResultData: ",noResultData,"\n") 

    setupdata = getSetup_yamldata()
    try:
        if setupdata[0]['high'] is None:
            lastresponseTime, lastAvgTime = 30, 15
    except:
        pass
    
    try:
        if setupdata[0]['medium'] is None:
            lastresponseTime, lastAvgTime = 5, 15
    except:
        pass
    
    current_question = None  # Initialize the current_question variable

    if lastresponseTime >= lastAvgTime: # medium question   
        print("sevMedi")       
        if sevMedi:
            for question in sevMedi:
                question_found = False  # Flag to check if the question was found in 'result_data'
                
                if noResultData:
                    current_question = question
                    break  # Stop searching after finding the first unmatched question

                # Loop through 'result_data' to compare with the current question
                for resData in result_data:
                    if resData['Question'] == question['Question']:
                        question_found = True
                        break  # Question found, no need to continue searching
                
                # If the question was not found in 'result_data', assign it to 'current_question'
                if not question_found:
                    current_question = question
                    break  # Stop searching after finding the first unmatched question

                data = {"medium" : "empty"}
                feedSetupdata(data)

        if current_question:
            print("AvgTimeToAnswer: ",current_question['AvgTimeToAnswer'],"Current Question:",  current_question['Question'])
            return (current_question, questions, quizName, date, starttime, runtime, branch, extrainfo, maxQuestion)

        else:
            print("No unmatched questions found in sevMedi.")

    else: # high question
        print("sevHigh")       
        if sevHigh:
            for question in sevHigh:
                question_found = False  # Flag to check if the question was found in 'result_data'
                
                # Loop through 'result_data' to compare with the current question
                for resData in result_data:
                    if resData['Question'] == question['Question']:
                        question_found = True
                        break  # Question found, no need to continue searching
                
                # If the question was not found in 'result_data', assign it to 'current_question'
                if not question_found:
                    current_question = question
                    break  # Stop searching after finding the first unmatched question

                data = {"high" : "empty"}
                feedSetupdata(data)
                

        if current_question:
            print("AvgTimeToAnswer: ",current_question['AvgTimeToAnswer'],"Current Question:",  current_question['Question'])
            return (current_question, questions, quizName, date, starttime, runtime, branch, extrainfo, maxQuestion)
        else:
            print("No unmatched questions found in sevHigh.")
    



def feedSetupdata(data):
    try:
        with open('media/resources/setup.yaml', 'r') as file:
            result_data = yaml.load(file, Loader=yaml.FullLoader)
    except FileNotFoundError:
        result_data = []
    
    result_data = []

    # Append the result entry to the result_data list
    result_data.append(data)

    with open('media/resources/setup.yaml', 'w') as result_file:
        yaml.dump(result_data, result_file)

def getSetup_yamldata():
    try:
        with open('media/resources/setup.yaml', 'r') as file:
            result_data = yaml.load(file, Loader=yaml.FullLoader)
    except FileNotFoundError:
        result_data = []
    
    if result_data is None:
        result_data = []

    return result_data

def scoreresult():
    try:
        with open('media/resources/result.yaml', 'r') as file:
            result_data = yaml.load(file, Loader=yaml.FullLoader)
    except FileNotFoundError:
        result_data = []
    
    score = 0

    for item in result_data:
        score += item['score']

    return score

