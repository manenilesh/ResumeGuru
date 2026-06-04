from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Resume

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

@login_required
def create_resume_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        summary = request.POST.get("summary")
        skills = request.POST.get("skills")
        experience = request.POST.get("experience")
        education = request.POST.get("education")
        projects = request.POST.get("projects")
        template = request.POST.get("template")

        resume = Resume.objects.create(
            user=request.user,
            title=title,
            full_name=full_name,
            email=email,
            phone=phone,
            address=address,
            summary=summary,
            skills=skills,
            experience=experience,
            education=education,
            projects=projects,
            template=template
        )

        return redirect("view_resume", resume_id=resume.id)

    return render(request, "resumes/create_resume.html")


@login_required
def my_library_view(request):
    resumes = Resume.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "resumes/my_library.html", {
        "resumes": resumes
    })


@login_required
def view_resume_view(request, resume_id):
    resume = get_object_or_404(
        Resume,
        id=resume_id,
        user=request.user
    )

    return render(request, "resumes/view_resume.html", {
        "resume": resume
    })


def resume_samples_view(request):
    return render(request, "resumes/samples.html")


@login_required
def resume_samples_view(request):
    return render(request, "resumes/samples.html")

def resume_templates_view(request):
    return render(request, "resumes/templates.html")


@login_required
def download_resume_pdf(request, resume_id):
    resume = get_object_or_404(
        Resume,
        id=resume_id,
        user=request.user
    )

    template = get_template("resumes/resume_pdf.html")

    html = template.render({
        "resume": resume
    })

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="{resume.title}.pdf"'

    pisa_status = pisa.CreatePDF(
        html,
        dest=response
    )

    if pisa_status.err:
        return HttpResponse("PDF generation failed")

    return response