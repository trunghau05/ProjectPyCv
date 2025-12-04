from mongoengine import *
from datetime import datetime

connect(
    db='pycv_db',
    host='mongodb+srv://tintuc_db:tintuc_db@tintuc.dsywlmm.mongodb.net/',
)


# ======================================================
# =============  EMBEDDED MODELS  ======================
# (nằm trong User – embedded, không tạo collection riêng)
# ======================================================

class Skill(EmbeddedDocument):
    sk_id = StringField()
    name = StringField(required=True)
    level = IntField(min_value=0, max_value=100)   # %, ví dụ 80


class Language(EmbeddedDocument):
    lg_id = StringField()
    name = StringField(required=True)              # English
    level = StringField()                          # B1 / Native / Fluent


class Education(EmbeddedDocument):
    ed_id = StringField()
    school = StringField(required=True)
    branch = StringField()
    start_year = IntField()
    end_year = IntField()


class Experience(EmbeddedDocument):
    ex_id = StringField()
    company = StringField(required=True)
    position = StringField(required=True)
    description = StringField()
    start_date = StringField()
    end_date = StringField()


class Project(EmbeddedDocument):
    pj_id = StringField()
    title = StringField(required=True)
    role = StringField()
    description = StringField()
    technologies = ListField(StringField())


# ======================================================
# ======================= USER =========================
# (User chứa toàn bộ thông tin con – embedded list)
# ======================================================

class User(Document):
    name = StringField(required=True)
    img = StringField()
    role = StringField()
    email = StringField(required=True)
    phone = StringField()
    birth = StringField()
    address = StringField()
    about = StringField()

    # Embedded array
    skills = EmbeddedDocumentListField(Skill)
    languages = EmbeddedDocumentListField(Language)
    educations = EmbeddedDocumentListField(Education)
    experiences = EmbeddedDocumentListField(Experience)
    projects = EmbeddedDocumentListField(Project)

    meta = {"collection": "users"}



# ======================================================
# ======================= CV CREATED ===================
# (CV do user tạo – liên kết bằng reference)
# ======================================================

class CvCreated(Document):
    us_id = ReferenceField(User, required=True)

    skills = EmbeddedDocumentListField(Skill)
    languages = EmbeddedDocumentListField(Language)
    educations = EmbeddedDocumentListField(Education)
    experiences = EmbeddedDocumentListField(Experience)
    projects = EmbeddedDocumentListField(Project)

    title = StringField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)

    meta = {"collection": "cv_created"}

