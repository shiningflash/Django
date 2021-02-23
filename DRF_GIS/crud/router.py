from rest_framework import routers

from student.viewsets import StudentViewset

router = routers.DefaultRouter()
router.register('student', StudentViewset)