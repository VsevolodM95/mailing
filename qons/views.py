from django.shortcuts import render, get_object_or_404, render_to_response
from qons.models import Qon, Quest, Answer
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django import forms
from django.core.mail import send_mail

def detail(request, father_id):
    return HttpResponse("You're looking at poll %s." % father_id)

def index(request):
    latest_poll_list = Qon.objects.all()
    return render_to_response('qons/index.html', {'form':form})

def vote(request, qon_id):
    p = get_object_or_404(Qon, pk=qon_id)
    info = ""
    if request.method == "POST":
        try:
	    for q in p.quest_set.all():
	        answer = request.POST['quest-'+str(q.id)]
		a = Answer()		
		a.qs = q		
		a.answer = answer
            	a.save()
		info = info+str(q.id)+". "+q.question+"\n"+"--> "+answer+"\n\n"
	    send_mail('Subscription has been cancelled', 'A user has refused from subscription. His answers on questions are next:\n\n'+info, 'lordmilten95@gmail.com', ['lordmilten95@gmail.com'])
	    return HttpResponseRedirect(reverse('qons:results', args=(p.id,)))
        except (KeyError, Quest.DoesNotExist):
            return render(request, 'qons/detail.html', {
              'qon': p,
              'error_message': "You didn't select a choice.",
            })
    else:
       # return HttpResponseRedirect(reverse('qons:results', args=(p.id,)))
        return render(request, 'qons/detail.html', {
            'qon': p,
        })

def results(request, qon_id):
    qon = get_object_or_404(Qon, pk=qon_id)
    return render(request, 'qons/results.html', {'qon': qon})

#smtpd
