from django.shortcuts import render

from docker_jenkins_slave.forms import DockerfileRequestForm


def home(request):
    form = DockerfileRequestForm()
    return render(request, "index.html", {'form': form})
