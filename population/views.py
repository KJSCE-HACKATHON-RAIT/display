from django.shortcuts import render


def home(requests):
    context = {}
    context['current_data'] = [1,5,6]

    #ML


    context['predicted_data'] = [2,12,8]
    return render(requests,'population.html',context)

