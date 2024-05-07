#  i have created this file - GTA
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import QuizQuestion, UserResponse, QuizHistory, QuizResult
import time
import yaml
from utils import getQuestion, scoreresult
from .models import AdminQuestion, Question



def emptyResult_yaml():
    try:
        with open('media/resources/result.yaml', 'r') as file:
            result_data = yaml.load(file, Loader=yaml.FullLoader)
    except FileNotFoundError:
        result_data = []

    result_data = []

    with open('media/resources/result.yaml', 'w') as result_file:
        yaml.dump(result_data, result_file)

# Create your views here.
def reset_quiz(request):
    # Reset the current_question_index to 0
    request.session['current_question_index'] = 0
    emptyResult_yaml()
    return redirect('quiz')


def quiz(request):
    if request.method == 'GET':

        result = getQuestion()  # Assuming getQuestion() returns a tuple or iterable

        if result is not None:
            current_question, questions, quizName, date, starttime, runtime, branch, extrainfo, maxQuestion = result
            # Now you can use the unpacked variables
        else:
            current_question, questions, quizName, date, starttime, runtime, branch, extrainfo, maxQuestion = "1", [1,2,3], "Error", 2030, 10,4,"EXTC", "all the best !!!" , 10

        
        # Get the current question index from the session
        current_question_index = request.session.get('current_question_index', 0)

        # Check if all questions have been answered
        if current_question_index >= maxQuestion:
            # Redirect to a thank you or summary page
            return redirect('quiz_completed')

        # Store the start time for the timer in the session
        request.session['start_time'] = time.time()

        parse = {
            'question': current_question,
            'question_index': current_question_index + 1,
            'total_questions': len(questions),

            'quizName': quizName,
            'date': date,
            'starttime': str(starttime) + " PM",
            'endtime': str(runtime + starttime) + " PM",
            'branch': branch,
            'maxQuestion': maxQuestion,
        }

        return render(request, 'quiz.html', parse)


# ----------------------------------------------------------------------------------
    elif request.method == 'POST':
        # Handle user's answer submission
        current_question_index = request.session.get('current_question_index', 0)
        current_question_index += 1  # Move to the next question
        request.session['current_question_index'] = current_question_index

        # Calculate response time
        start_time = request.session.get('start_time', 0)
        response_time = int(time.time() - start_time)

        # Save the result in result.yaml
        question = request.POST.get('question')
        user_answer = request.POST.get('user_answer')
        answer = request.POST.get('answer')
        severity = request.POST.get('severity')
        marks = request.POST.get('marks')
        avgTimeToAnswer = request.POST.get('avgTimeToAnswer')
        
        if answer == user_answer:
            score = int(marks)
        else:
            score = 0
        
        result_entry = {
            'Question': question,
            'Answer': answer,
            'User_answer': user_answer,
            'Severity': severity,
            'Marks': marks,
            'AvgTimeToAnswer': int(avgTimeToAnswer),
            'Response_time': response_time,
            'score':  score,
        }

        # Load existing data from 'result.yaml' or create an empty list if the file doesn't exist
        try:
            with open('media/resources/result.yaml', 'r') as file:
                result_data = yaml.load(file, Loader=yaml.FullLoader)
        except FileNotFoundError:
            result_data = []

        if result_data is None:
            result_data = []

        # Append the result entry to the result_data list
        result_data.append(result_entry)

        with open('media/resources/result.yaml', 'w') as result_file:
            yaml.dump(result_data, result_file)

        return redirect('quiz')
    


    # return HttpResponse('Teamzeffort    |      index Page')
def quiz_completed(request):
    # return HttpResponse('Teamzeffort    |      quiz_completed Page')
    
    parse = {
        'username'  : "GTA Pawar",
        'userscore' : scoreresult(),
    }
    return render(request,'result.html', parse)

def index(request):
    return HttpResponse('Teamzeffort    |      index Page')
    # return render(request,'quiz.html')

def result(request):
    return HttpResponse('Teamzeffort    |      result Page')
    # return render(request,'result.html')



def head_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        languages = request.POST.get('languages')
        date = request.POST.get('date')
        starttime = request.POST.get('starttime')
        runtime = request.POST.get('runtime')
        branch = request.POST.get('branch')
        extrainfo = request.POST.get('extrainfo')
        maxQuestion = request.POST.get('maxQuestion')

        # Print the data on the terminal
        print(f"Name: {name}")
        print(f"Languages: {languages}")
        print(f"Date: {date}")
        print(f"Start Time: {starttime}")
        print(f"Runtime: {runtime}")
        print(f"Branch: {branch}")
        print(f"Extra Info: {extrainfo}")
        print(f"Max Questions: {maxQuestion}")

        # Create an AdminQuestion instance and save it to the database
        admin_question = AdminQuestion(
            name=name,
            languages=languages,
            date=date,
            starttime=starttime,
            runtime=runtime,
            branch=branch,
            extrainfo=extrainfo,
            maxQuestion=maxQuestion
        )
        admin_question.save()

        # Process and save the individual questions as needed
        # Example:
        question = Question(
            admin_question=admin_question,
            Question="Sample Question",
            Answer="Sample Answer",
            Hint="Sample Hint",
            Option1="Option 1",
            Option2="Option 2",
            Option3="Option 3",
            Option4="Option 4",
            Severity="medium",
            AvgTimeToAnswer=15,
            Marks=1
        )
        question.save()

        return redirect('question_form')  # Redirect to a success page or another URL

    return render(request, 'head_form.html')

def question_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        languages = request.POST.get('languages')
        date = request.POST.get('date')
        starttime = request.POST.get('starttime')
        runtime = request.POST.get('runtime')
        branch = request.POST.get('branch')
        extrainfo = request.POST.get('extrainfo')
        maxQuestion = request.POST.get('maxQuestion')

        # Print the data on the terminal
        print(f"Name: {name}")
        print(f"Languages: {languages}")
        print(f"Date: {date}")
        print(f"Start Time: {starttime}")
        print(f"Runtime: {runtime}")
        print(f"Branch: {branch}")
        print(f"Extra Info: {extrainfo}")
        print(f"Max Questions: {maxQuestion}")

        # Create an AdminQuestion instance and save it to the database
        admin_question = AdminQuestion(
            name=name,
            languages=languages,
            date=date,
            starttime=starttime,
            runtime=runtime,
            branch=branch,
            extrainfo=extrainfo,
            maxQuestion=maxQuestion
        )
        admin_question.save()

        # Process and save the individual questions as needed
        # Example:
        question = Question(
            admin_question=admin_question,
            Question="Sample Question",
            Answer="Sample Answer",
            Hint="Sample Hint",
            Option1="Option 1",
            Option2="Option 2",
            Option3="Option 3",
            Option4="Option 4",
            Severity="medium",
            AvgTimeToAnswer=15,
            Marks=1
        )
        question.save()

        return redirect('success')

def success(request):
    return render(request, 'success.html')




# ---------------------------------------------------------------------------------




# def contact(request):
#     coreMem = Contact.objects.filter(mem_tag="core")
#     teamMem = Contact.objects.filter(mem_tag="team")
#     # print(f"coreMem: {coreMem} \n teamMem: {teamMem}")

#     return render(request, 'tze/contact.html', {'core':coreMem,'team':teamMem })

# def productView(request, myslug):
#     # Fetch the product using the id
#     product = Product.objects.filter(slug=myslug)
#     prodCat = product[0].category
#     # print(prodCat)
#     recproduct = Product.objects.filter(category=prodCat)
#     # print(recproduct)

#     # randomObjects = random.sample(recproduct, 2)
#     randomObjects = random.sample(list(recproduct), 2)


#     return render(request, 'tze/prodView.html', {'product':product[0],'recprod':randomObjects })


# def index(request):
#     return HttpResponse('Teamzeffort    |      index Page')
