from django.shortcuts import render


def home(requests):
    if requests.method == "POST":
        print(requests.post.get('img'))
    return render(requests,'population.html',{})

