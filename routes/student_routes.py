from fastapi import APIRouter, FastAPI, Response
from models.student_model import Student
from controllers.student_controller import create_student, get_all_students, get_student_by_id, get_students_pagination, update_student, delete_student, search_student

StudentRouter = APIRouter(
    # means every route inside this router automatically starts with /students.
    prefix= '/students',
    tags= ['students']
    # This grps all api under group named students : Organized
)

# BONUS : Search Student by name
@StudentRouter.get('/search')
def search_students(search: str, response: Response):
    return search_student(search, response)

# Bonus : Pagination
@StudentRouter.get('/pagination')
def pagination_route(page: int, limit: int, response: Response):
    return get_students_pagination(page, limit, response)

# create student
@StudentRouter.post('/')
def create_student_route(student: Student, response: Response):
    return create_student(student, response)

# read all students
@StudentRouter.get('/')
def get_all_students_route(response: Response):
    return get_all_students(response)

# read student by id
@StudentRouter.get('/{studentid}')
def get_student_by_id_route(studentid: int, response: Response):
    return get_student_by_id(studentid, response)

# update student by id
@StudentRouter.put('/{studentid}')
def update_student_route(studentid: int, updated_student: Student, response: Response):
    return update_student(studentid, updated_student, response)

# delete student by id
@StudentRouter.delete('/{studentid}')
def delete_student_route(studentid: int, response: Response):
    return delete_student(studentid, response)


