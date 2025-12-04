# -*- coding: utf-8 -*-
from mongoengine import connect
from models import *

# =================== KẾT NỐI MONGO ===================
# Nếu MongoDB có username/password, dùng:
# connect(db="PyCV_DB", username="user", password="pass", host="localhost", port=27017)

# =================== USER ===================
user = User(
    email="hau@example.com",
    password="123456",
    fullname="Nguyễn Trung Hậu",
).save()


# =================== PROFILE ===================
profile = Profile(
    user=user,
    headline="Fullstack Developer",
    phone="0123 456 789",
    address="Hồ Chí Minh",
    birthday="2004-10-10",
    about_me="Sinh viên IT, yêu thích lập trình web và AI."
).save()


# =================== SKILLS ===================
skill_python = Skill(user=user, name="Python", level=5).save()
skill_js = Skill(user=user, name="JavaScript", level=4).save()
skill_angular = Skill(user=user, name="Angular", level=4).save()


# =================== LANGUAGE ===================
lang_en = Language(user=user, name="English", level="Fluent").save()
lang_vi = Language(user=user, name="Vietnamese", level="Native").save()


# =================== EDUCATION ===================
edu1 = Education(
    user=user,
    school="Đại học Công nghệ Thông tin",
    degree="Bachelor",
    major="Computer Science",
    start_year=2022,
    end_year=2026,
).save()


# =================== EXPERIENCE ===================
exp1 = Experience(
    user=user,
    company="FPT Software",
    position="Intern Backend Developer",
    description="Phát triển API bằng Python và FastAPI.",
    start_date="2024-06",
    end_date="2024-12",
).save()


# =================== PROJECT ===================
pj1 = Project(
    user=user,
    title="PonPlan - App quản lý tài chính",
    role="Fullstack Developer",
    description="Quản lý chi tiêu, dashboard, Firebase + Django API.",
    technologies=["Angular", "Ionic", "Django", "Firebase"],
).save()

pj2 = Project(
    user=user,
    title="Checkers Game",
    role="Frontend & AI Developer",
    description="Trò chơi cờ đam, AI dùng minimax alpha-beta.",
    technologies=["HTML", "JS", "FastAPI", "Python"],
).save()


# =================== TEMPLATE ===================
template1 = CVTemplate(
    title="Modern Blue",
    thumbnail="/static/templates/modern-blue.png",
    json_structure={
        "layout": "two-column",
        "color": "#0066ff",
        "sections": ["profile", "skills", "experience", "education", "projects"]
    }
).save()


# =================== CREATE CV ===================
cv = CurriculumVitae(
    user=user,
    template=template1,
    profile=profile,
    skills=[skill_python, skill_js, skill_angular],
    languages=[lang_en, lang_vi],
    educations=[edu1],
    experiences=[exp1],
    projects=[pj1, pj2],
    title="CV Fullstack Developer - Nguyễn Trung Hậu"
).save()

# =================== PRINT KHÔNG LỖI UNICODE ===================
print("Dữ liệu mẫu đã được tạo!".encode("utf-8").decode("utf-8"))
