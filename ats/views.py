from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def ats_score_view(request):
    score = None

    if request.method == "POST":
        resume_text = request.POST.get("resume_text", "")
        job_description = request.POST.get("job_description", "")

        resume_words = set(resume_text.lower().split())
        job_words = set(job_description.lower().split())

        if len(job_words) > 0:
            matched_words = resume_words.intersection(job_words)
            score = int((len(matched_words) / len(job_words)) * 100)
        else:
            score = 0

    return render(request, "ats/ats_score.html", {
        "score": score
    })