from django.urls import path
from LLApps.dashboard.views import *

urlpatterns = [
    path('', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('activate/<str:labour_id>/<str:token>/', activate_account, name='activate_account'),
    path('forgot-password/', forgot_password_view, name='forgot_password_view'),
    path('verify_otp_view/', verify_otp_view, name='verify_otp_view'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard_view'),
    path('parties/', parties_view, name='parties_view'),
    path('parties/<uuid:party_id>/', party_tasks_view, name='party_tasks'),
    path('add-new-party/', add_new_party, name='add_new_party'),
    path('edit-party/<uuid:party_id>', edit_party, name='edit_party'),
    path('delete-party/<uuid:party_id>', delete_party, name='delete_party'),
    path('payments/', payments_view, name='payments_view'),
    path('contact/', contact_view, name='contact_view'),
    path('profile/', profile_view, name='profile_view'),
    path('update-profile-view/', update_profile_view, name='update_profile_view'),
    path('some-error-page/', some_error_page, name='some_error_page'),
    path("add_task/<uuid:party_id>/" , add_task , name="add_task"),
    path("tasks_view/" , tasks_view , name="tasks_view"), 
    path('task/delete/<int:task_id>/', delete_task, name='delete_task'),
    path('task/update/<int:task_id>/', update_task, name='update_task'),
    path('labour-read/', labour_read , name='labour_read'),
    path('labour-create/', create_labour_worker , name="labour_create"),
    path('labour-delete/<int:worker_id>', labour_delete , name='labour_delete' ),
    path('labour-update/<int:worker_id>', labour_update , name='labour_update'),
    path('labour-attendance/<int:worker_id>/', mark_attendance, name='mark_attendance'),
    path("salary/generate/<int:worker_id>/", generate_salary, name="generate_salary"),
    path("salary/list/", salary_list, name="salary_list"),
    path("pay-salary/<int:worker_id>/", pay_salary, name="pay_salary"), 
    path("undo-salary/<int:worker_id>/", undo_salary_payment, name="undo_salary_payment"),
]