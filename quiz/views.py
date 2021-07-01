from django.shortcuts import render
from .models import Question
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.


# def get_response(request):
#     # si il y a des données postées
#     if request.method == "POST":
#         # alors on crée le formulaire (+ .save() pour enregistrer)
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             # rediriger ici vers les résultats et importer redirect au lieu de hhtpresponseredirect
#             return HttpResponseRedirect("/thanks/")
#     else:
#         form = QuestionForm()
#     return render(request, 'quiz/index.html', {'form': form})


# comparaison de la réponse

lst = []
anslist = []
reponses = Question.objects.all()


for i in reponses:
    anslist.append(i.reponse)


def welcome(request):
    lst.clear()
    return render(request, 'quiz/welcome.html')


def quiz(request):
    bobiquestions = Question.objects.all().order_by('id')
    paginator = Paginator(bobiquestions, 1)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        questions = paginator.page(page)
    except(EmptyPage, InvalidPage):
        questions = paginator.page(paginator.num_pages)

    return render(request, 'quiz/quiz.html', {'bobiquestions': bobiquestions, 'questions': questions})


def result(request):

    score = 0
    bonnes_reponses = len(anslist)
    for lol in range(len(lst)):
        if lst[lol] == anslist[lol]:
            score += 1
    return render(request, 'quiz/result.html', {'score': score, 'bonnes_reponses': bonnes_reponses})


def saveans(request):
    # la str 'ans' vient du fichier js et permet de ne pas rafraichir la page
    ans = request.GET['ans']
    lst.append(ans)
