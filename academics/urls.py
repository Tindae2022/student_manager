from django.urls import path
from .views import year_leader
from academics.views import students
from .views.students import PdfView
from .views import course
from .views import modules
from .views import classes
from .views import semester
from .views import timetable
from .views import lecturers

urlpatterns = [
    path('year_leader/dashboard/', year_leader.dashboard, name='dashboard'),

    path('students/', students.StudentListView.as_view(), name='student_index'),

    path('students/<int:pk>/', students.StudentDetailView.as_view(), name='student_details'),

    path('students/create/', students.StudentCreateView.as_view(), name='student_create'),

    path('students/<int:pk>/update/', students.StudentUpdateView.as_view(), name='student_update'),

    path('students/<int:pk>/delete/', students.StudentDeleteView.as_view(), name='student_delete'),

    path('student-search/', students.StudentSearchView.as_view(), name='student_search'),

    path('students/<int:pk>/send_email/', students.send_email_view, name='send_email'),

    path('students/<int:student_id>/pdf/', PdfView.as_view(), name='pdf_view'),

    path('students/table/', students.StudentTableView.as_view(), name='class_list'),

    path('courses/', course.CourseListView.as_view(), name='course_index'),

    path('courses/create/', course.CourseCreateView.as_view(), name='course_create'),
    path('courses/<int:pk>/update/', course.CourseUpdateView.as_view(), name='course_update'),

    path('courses/<int:pk>/delete/', course.CourseDeleteView.as_view(), name='course_delete'),

    path('modules/', modules.ModuleListView.as_view(), name='module_index'),
    path('modules/create/', modules.ModuleCreateView.as_view(), name='module_create'),

    path('modules/<int:pk>/update/', modules.ModuleUpdateView.as_view(), name='module_update'),

    path('modules/<int:pk>/delete/', modules.ModuleDeleteView.as_view(), name='module_delete'),

    path('modules/search/', modules.ModuleSearchView.as_view(), name='module_search'),

    path('classes/', classes.ClassListView.as_view(), name='class_index'),

    path('classes/create/', classes.ClassCreateView.as_view(), name='class_create'),

    path('classes/success/', classes.class_success, name='class_success'),

    path('classes/<int:pk>/update/', classes.ClassUpdateView.as_view(), name='class_update'),

    path('classes/delete/success/', classes.class_delete, name='class_delete_success'),

    path('classes/<int:pk>/delete/', classes.ClassDeleteView.as_view(), name='class_delete'),

    path('semester/', semester.SemesterListView.as_view(), name='semester_index'),

    path('semester/tableview/', semester.SemesterTableListView.as_view(), name='semester_table'),

    path('semester/register_success', semester.semester_success, name='semester_success'),

    path('semester/<int:pk>/update/', semester.SemesterUpdateView.as_view(), name='semester_update'),

    path('semester/create/', semester.SemesterCreateView.as_view(), name='semester_create'),

    path('semester/<int:pk>/delete/', semester.SemesterDeleteView.as_view(), name='semester_delete'),

    path('semester/delete_success/', semester.semester_delete_success, name='semester_delete_success'),

    path('students/import-csv/', students.ImportCSVView.as_view(), name='import_csv'),

    path('timetable/create/', timetable.TimetableCreateView.as_view(), name='create_timetable'),

    path('classes/<int:pk>/', classes.ClassDetailView.as_view(), name='class_timetable'),

    path('timetable/<int:pk>/update/', timetable.TimetableUpdateView.as_view(), name='update_timetable'),

    path('timetable/success/', timetable.register_success, name='timetable_register_success'),

    path('timetable/<int:pk>/delete/', timetable.TimetableDeleteView.as_view(), name='delete_timetable'),

    path('timetable/delete/', timetable.delete_success, name='timetable_delete_success'),

    path('lecturer/', lecturers.LecturerListView.as_view(), name='lecturer_index'),
    path('lecturer/create/success/', lecturers.LecturerCreateSuccessTemplateView.as_view(),
         name='lecturer_create_success'),

    path('lecturer/<int:pk>/update/', lecturers.LecturerUpdateView.as_view(), name='lecturer_update'),

    path('lecturer/delete/success/', lecturers.LecturerDeleteSuccessTemplateView.as_view(),
         name='lecturer_delete_success'),

    path('lecturer/create/', lecturers.LecturerCreateView.as_view(), name='lecturer_create'),

    path('lecturer/<int:pk>/delete/', lecturers.LecturerDeleteView.as_view(), name='lecturer_delete'),

    path('student/create/success/', students.StudentSuccessTemplateView.as_view(), name='student_create_success'),

    path('student/delete/success/', students.StudentDeleteSuccessTemplateView.as_view(), name='student_delete_success'),

    path('course/create/success/', course.CourseSuccessTemplateView.as_view(), name='course_create_success'),

    path('course/delete/success/', course.CourseDeleteSuccessTemplateView.as_view(), name='course_delete_success'),


]
