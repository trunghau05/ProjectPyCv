# # common/views.py
# # -*- coding: utf-8 -*-
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from mongoengine import connect
# from Common.models import *

# # =================== KẾT NỐI MONGO ===================
# # Nếu MongoDB có username/password, dùng:
# # connect(db="PyCV_DB", username="user", password="pass", host="localhost", port=27017)


# @csrf_exempt
# def seed_cv_data(request):
#     """
#     API POST nội bộ để tạo dữ liệu mẫu CV
#     """
#     try:
#         # =================== USER ===================
#         user = User(
#             email="hau@example.com",
#             password="123456",
#             fullname="Nguyễn Trung Hậu",
#         ).save()

#         # =================== PROFILE ===================
#         profile = Profile(
#             user=user,
#             headline="Fullstack Developer",
#             phone="0123 456 789",
#             address="Hồ Chí Minh",
#             birthday="2004-10-10",
#             about_me="Sinh viên IT, yêu thích lập trình web và AI."
#         ).save()

#         # =================== SKILLS ===================
#         skill_python = Skill(user=user, name="Python", level=5).save()
#         skill_js = Skill(user=user, name="JavaScript", level=4).save()
#         skill_angular = Skill(user=user, name="Angular", level=4).save()

#         # =================== LANGUAGE ===================
#         lang_en = Language(user=user, name="English", level="Fluent").save()
#         lang_vi = Language(user=user, name="Vietnamese", level="Native").save()

#         # =================== EDUCATION ===================
#         edu1 = Education(
#             user=user,
#             school="Đại học Công nghệ Thông tin",
#             degree="Bachelor",
#             major="Computer Science",
#             start_year=2022,
#             end_year=2026,
#         ).save()

#         # =================== EXPERIENCE ===================
#         exp1 = Experience(
#             user=user,
#             company="FPT Software",
#             position="Intern Backend Developer",
#             description="Phát triển API bằng Python và FastAPI.",
#             start_date="2024-06",
#             end_date="2024-12",
#         ).save()

#         # =================== PROJECT ===================
#         pj1 = Project(
#             user=user,
#             title="PonPlan - App quản lý tài chính",
#             role="Fullstack Developer",
#             description="Quản lý chi tiêu, dashboard, Firebase + Django API.",
#             technologies=["Angular", "Ionic", "Django", "Firebase"],
#         ).save()

#         pj2 = Project(
#             user=user,
#             title="Checkers Game",
#             role="Frontend & AI Developer",
#             description="Trò chơi cờ đam, AI dùng minimax alpha-beta.",
#             technologies=["HTML", "JS", "FastAPI", "Python"],
#         ).save()

#         # =================== TEMPLATE ===================
#         template1 = CVTemplate(
#             title="Modern Blue",
#             thumbnail="/static/templates/modern-blue.png",
#             json_structure={
#                 "layout": "two-column",
#                 "color": "#0066ff",
#                 "sections": ["profile", "skills", "experience", "education", "projects"]
#             }
#         ).save()

#         # =================== CREATE CV ===================
#         cv = CurriculumVitae(
#             user=user,
#             template=template1,
#             profile=profile,
#             skills=[skill_python, skill_js, skill_angular],
#             languages=[lang_en, lang_vi],
#             educations=[edu1],
#             experiences=[exp1],
#             projects=[pj1, pj2],
#             title="CV Fullstack Developer - Nguyễn Trung Hậu"
#         ).save()

#         return JsonResponse({
#             "status": "success",
#             "message": "Dữ liệu mẫu đã được tạo!",
#             "user_id": str(user.id),
#             "cv_id": str(cv.id)
#         })

#     except Exception as e:
#         return JsonResponse({"status": "error", "message": str(e)})

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from mongoengine.errors import DoesNotExist, ValidationError
from .models import *

# ================= CREATE CV =================
@csrf_exempt
def create_cv(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_id = data.get("user_id")
            template_id = data.get("template_id")
            title = data.get("title")

            # Lấy đối tượng User và Template
            user = User.objects.get(id=user_id)
            template = CVTemplate.objects.get(id=template_id)

            # Tạo CV mới
            cv = CurriculumVitae(
                user=user,
                template=template,
                title=title,
                # có thể thêm các trường reference khác nếu muốn
            )
            cv.save()

            return JsonResponse({"status": "success", "cv_id": str(cv.id)}, status=201)

        except DoesNotExist:
            return JsonResponse({"status": "error", "message": "User or Template not found"}, status=404)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid method"}, status=405)


# ================= UPDATE CV =================
@csrf_exempt
def update_cv(request, cv_id):
    if request.method == "PUT":
        try:
            cv = CurriculumVitae.objects.get(id=cv_id)
            data = json.loads(request.body)

            # Chỉ update những trường có trong request
            if "title" in data:
                cv.title = data["title"]
            if "template_id" in data:
                template = CVTemplate.objects.get(id=data["template_id"])
                cv.template = template
            if "profile_id" in data:
                profile = Profile.objects.get(id=data["profile_id"])
                cv.profile = profile

            # Update các list reference (skills, languages...) nếu có
            if "skills" in data:  # list of skill_ids
                cv.skills = [Skill.objects.get(id=sid) for sid in data["skills"]]
            if "languages" in data:
                cv.languages = [Language.objects.get(id=lid) for lid in data["languages"]]
            if "educations" in data:
                cv.educations = [Education.objects.get(id=eid) for eid in data["educations"]]
            if "experiences" in data:
                cv.experiences = [Experience.objects.get(id=eid) for eid in data["experiences"]]
            if "projects" in data:
                cv.projects = [Project.objects.get(id=pid) for pid in data["projects"]]

            cv.save()
            return JsonResponse({"status": "success", "cv_id": str(cv.id)})

        except DoesNotExist:
            return JsonResponse({"status": "error", "message": "CV or related object not found"}, status=404)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid method"}, status=405)


# ================= DELETE CV =================
@csrf_exempt
def delete_cv(request, cv_id):
    if request.method == "DELETE":
        try:
            cv = CurriculumVitae.objects.get(id=cv_id)
            cv.delete()
            return JsonResponse({"status": "success", "message": "CV deleted"})
        except DoesNotExist:
            return JsonResponse({"status": "error", "message": "CV not found"}, status=404)
    return JsonResponse({"status": "error", "message": "Invalid method"}, status=405)


# ================= GET CV BY USER =================
def get_cvs_by_user(request, user_id):
    if request.method == "GET":
        try:
            cvs = CurriculumVitae.objects(user=user_id)
            data = []
            for cv in cvs:
                data.append({
                    "cv_id": str(cv.id),
                    "title": cv.title,
                    "template": str(cv.template.id),
                    "created_at": cv.created_at.isoformat()
                })
            return JsonResponse({"status": "success", "cvs": data})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid method"}, status=405)


# ================= GET CV DETAIL =================
def get_cv_detail(request, cv_id):
    if request.method == "GET":
        try:
            cv = CurriculumVitae.objects.get(id=cv_id)
            data = {
                "cv_id": str(cv.id),
                "title": cv.title,
                "user": str(cv.user.id),
                "template": str(cv.template.id),
                "profile": str(cv.profile.id) if cv.profile else None,
                "skills": [str(s.id) for s in cv.skills],
                "languages": [str(l.id) for l in cv.languages],
                "educations": [str(e.id) for e in cv.educations],
                "experiences": [str(e.id) for e in cv.experiences],
                "projects": [str(p.id) for p in cv.projects],
                "created_at": cv.created_at.isoformat()
            }
            return JsonResponse({"status": "success", "cv": data})
        except DoesNotExist:
            return JsonResponse({"status": "error", "message": "CV not found"}, status=404)
    return JsonResponse({"status": "error", "message": "Invalid method"}, status=405)
