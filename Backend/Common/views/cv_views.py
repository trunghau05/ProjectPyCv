import json
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from bson import ObjectId
from ..models import CvCreated, User, Skill, Language, Education, Experience, Project

# ----------- Helper serialize -----------
def serialize_cv(cv):
    data = cv.to_mongo().to_dict()
    data["_id"] = str(data["_id"])
    data["us_id"] = str(cv.us_id.id)
    for lst in ["skills","languages","educations","experiences","projects"]:
        data[lst] = [e.to_mongo().to_dict() for e in getattr(cv, lst)]
        for obj in data[lst]:
            if "_id" in obj:
                obj["_id"] = str(obj["_id"])
    return data

# ----------- CV Views -----------
@method_decorator(csrf_exempt, name='dispatch')
class CvListCreate(View):
    def get(self, request):
        cvs = CvCreated.objects()
        data = [serialize_cv(cv) for cv in cvs]
        return JsonResponse(data, safe=False)

    def post(self, request):
        body = json.loads(request.body)
        user = User.objects.get(id=body["user_id"])
        cv = CvCreated(
            us_id=user,
            title=body.get("title"),
            skills=[Skill(**sk) for sk in body.get("skills", [])],
            languages=[Language(**lg) for lg in body.get("languages", [])],
            educations=[Education(**ed) for ed in body.get("educations", [])],
            experiences=[Experience(**ex) for ex in body.get("experiences", [])],
            projects=[Project(**pj) for pj in body.get("projects", [])],
        )
        cv.save()
        return JsonResponse(serialize_cv(cv))

@method_decorator(csrf_exempt, name='dispatch')
class CvDetail(View):
    def get_cv(self, cv_id):
        try:
            return CvCreated.objects.get(id=cv_id)
        except CvCreated.DoesNotExist:
            return None

    def get(self, request, cv_id):
        cv = self.get_cv(cv_id)
        if not cv:
            return HttpResponse(status=404)
        return JsonResponse(serialize_cv(cv))

    def put(self, request, cv_id):
        cv = self.get_cv(cv_id)
        if not cv:
            return HttpResponse(status=404)

        body = json.loads(request.body)
        cv.title = body.get("title", cv.title)
        if "skills" in body:
            cv.skills = [Skill(**sk) for sk in body["skills"]]
        if "languages" in body:
            cv.languages = [Language(**lg) for lg in body["languages"]]
        if "educations" in body:
            cv.educations = [Education(**ed) for ed in body["educations"]]
        if "experiences" in body:
            cv.experiences = [Experience(**ex) for ex in body["experiences"]]
        if "projects" in body:
            cv.projects = [Project(**pj) for pj in body["projects"]]

        cv.save()
        return JsonResponse(serialize_cv(cv))

    def delete(self, request, cv_id):
        cv = self.get_cv(cv_id)
        if not cv:
            return HttpResponse(status=404)
        cv.delete()
        return HttpResponse(status=204)
