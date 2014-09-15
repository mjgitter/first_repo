from django.shortcuts import render, redirect
import uuid
from requests import Request

def github_connect(request):
    state = uuid.uuid4().hex
    request.session['github_auth_state'] = state
    params = {
        'client_id': '123asd45678a12345678',
        'scope': 'user:email, repo',
        'state': state
    }

    github_auth_url = 'https://github.com/login/oauth/authorize'
    r = Request('GET', url=github_auth_url, params=params).prepare()
    return redirect(r.url)