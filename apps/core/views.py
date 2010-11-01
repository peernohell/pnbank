# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

@login_required
def index(request):
    """Page de démarrage de l'application"""

    return render_to_response(
        "index.html",
        context_instance = RequestContext(request)
    )

