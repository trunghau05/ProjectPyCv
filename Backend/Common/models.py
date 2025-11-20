from mongoengine import *
from datetime import datetime

connect(
    db='pycv_db',
    host='localhost',
    port=27017
)

# ======================= USER =======================
class User(Document):
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    fullname = StringField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)


# ======================= PROFILE =======================
class Profile(Document):
    user = ReferenceField(User, required=True, reverse_delete_rule=CASCADE)
    
    headline = StringField()                # Ví dụ: "Fullstack Developer"
    phone = StringField()
    address = StringField()
    birthday = StringField()
    about_me = StringField()                # mô tả bản thân

    created_at = DateTimeField(default=datetime.utcnow)


# ======================= SKILL =======================
class Skill(Document):
    user = ReferenceField(User, required=True, reverse_delete_rule=CASCADE)
    name = StringField(required=True)            # VD: Python, Angular
    level = IntField(min_value=1, max_value=5)   # 1–5 hoặc 20–100 tùy template


# ======================= LANGUAGE =======================
class Language(Document):
    user = ReferenceField(User, required=True, reverse_delete_rule=CASCADE)
    name = StringField(required=True)            # VD: English
    level = StringField()                        # VD: "B1", "Fluent", "Native"


# ======================= EDUCATION =======================
class Education(Document):
    user = ReferenceField(User, required=True, reverse_delete_rule=CASCADE)
    
    school = StringField(required=True)
    degree = StringField(required=True)           # "Bachelor", "Engineer"
    major = StringField(required=True)
    
    start_year = IntField()
    end_year = IntField()


# ======================= EXPERIENCE =======================
class Experience(Document):
    user = ReferenceField(User, required=True, reverse_delete_rule=CASCADE)
    
    company = StringField(required=True)
    position = StringField(required=True)
    description = StringField()
    
    start_date = StringField()
    end_date = StringField()


# ======================= PROJECT =======================
class Project(Document):
    user = ReferenceField(User, required=True, reverse_delete_rule=CASCADE)
    
    title = StringField(required=True)
    role = StringField()
    description = StringField()
    technologies = ListField(StringField())


# ======================= CV TEMPLATE =======================
class CVTemplate(Document):
    title = StringField(required=True)
    thumbnail = StringField()  # link ảnh mẫu
    json_structure = DictField()  # cấu trúc bố cục template
    is_public = BooleanField(default=True)


# ======================= CV (USER CREATED) =======================
class CurriculumVitae(Document):
    user = ReferenceField(User, required=True, reverse_delete_rule=CASCADE)
    template = ReferenceField(CVTemplate, required=True)
    
    profile = ReferenceField(Profile)
    skills = ListField(ReferenceField(Skill))
    languages = ListField(ReferenceField(Language))
    educations = ListField(ReferenceField(Education))
    experiences = ListField(ReferenceField(Experience))
    projects = ListField(ReferenceField(Project))
    
    title = StringField(required=True)              # CV Backend Developer
    created_at = DateTimeField(default=datetime.utcnow)
