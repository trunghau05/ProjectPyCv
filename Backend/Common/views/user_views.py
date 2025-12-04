import json
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from bson import ObjectId
from ..models import User, Skill, Language, Education, Experience, Project

# ----------- Helper serialize -----------
def serialize_user(user):
    data = user.to_mongo().to_dict()
    data["_id"] = str(data["_id"])
    for lst in ["skills","languages","educations","experiences","projects"]:
        data[lst] = [e.to_mongo().to_dict() for e in getattr(user, lst)]
        for obj in data[lst]:
            if "_id" in obj:
                obj["_id"] = str(obj["_id"])
    return data

# ----------- User Views -----------
@method_decorator(csrf_exempt, name='dispatch')
class UserListCreate(View):
    def get(self, request):
        users = User.objects()
        data = [serialize_user(u) for u in users]
        return JsonResponse(data, safe=False)

    def post(self, request):
        body = json.loads(request.body)
        user = User(
            name=body.get("name"),
            img=body.get("img"),
            role=body.get("role"),
            email=body.get("email"),
            phone=body.get("phone"),
            birth=body.get("birth"),
            address=body.get("address"),
            about=body.get("about"),
        )

        # Embedded docs
        for sk in body.get("skills", []):
            user.skills.append(Skill(**sk))
        for lg in body.get("languages", []):
            user.languages.append(Language(**lg))
        for ed in body.get("educations", []):
            user.educations.append(Education(**ed))
        for ex in body.get("experiences", []):
            user.experiences.append(Experience(**ex))
        for pj in body.get("projects", []):
            user.projects.append(Project(**pj))

        user.save()
        return JsonResponse(serialize_user(user))

@method_decorator(csrf_exempt, name='dispatch')
class UserDetail(View):
    def get_user(self, _id):
        try:
            return User.objects.get(id=_id)
        except User.DoesNotExist:
            return None

    def get(self, request, _id):
        user = self.get_user(_id)
        if not user:
            return HttpResponse(status=404)
        return JsonResponse(serialize_user(user))

    def put(self, request, _id):
        user = self.get_user(_id)
        if not user:
            return HttpResponse(status=404)

        body = json.loads(request.body)
        for k, v in body.items():
            if k in ["skills","languages","educations","experiences","projects"]:
                continue
            setattr(user, k, v)

        if "skills" in body:
            user.skills = [Skill(**sk) for sk in body["skills"]]
        if "languages" in body:
            user.languages = [Language(**lg) for lg in body["languages"]]
        if "educations" in body:
            user.educations = [Education(**ed) for ed in body["educations"]]
        if "experiences" in body:
            user.experiences = [Experience(**ex) for ex in body["experiences"]]
        if "projects" in body:
            user.projects = [Project(**pj) for pj in body["projects"]]

        user.save()
        return JsonResponse(serialize_user(user))

    def delete(self, request, _id):
        user = self.get_user(_id)
        if not user:
            return HttpResponse(status=404)
        user.delete()
        return HttpResponse(status=204)
