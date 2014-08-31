from django.shortcuts import render_to_response

from docker_jenkins_slave.forms import DockerfileRequestForm


def home(request):
    form = DockerfileRequestForm()
    return render_to_response("index.html", {'form': form})
