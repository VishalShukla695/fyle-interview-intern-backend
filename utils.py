# app/utils.py

def get_principal_info_from_headers(headers):
    principal_info = headers.get('X-Principal')
    return principal_info

def format_assignments_response(assignments):
    formatted_assignments = []
    for assignment in assignments:
        formatted_assignment = {
            "content": assignment.content,
            "created_at": str(assignment.created_at),
            "grade": assignment.grade,
            "id": assignment.id,
            "state": assignment.state,
            "student_id": assignment.student_id,
            "teacher_id": assignment.teacher_id,
            "updated_at": str(assignment.updated_at)
        }
        formatted_assignments.append(formatted_assignment)
    return formatted_assignments

def format_teachers_response(teachers):
    formatted_teachers = []
    for teacher in teachers:
        formatted_teacher = {
            "created_at": str(teacher.created_at),
            "id": teacher.id,
            "updated_at": str(teacher.updated_at),
            "user_id": teacher.user_id
        }
        formatted_teachers.append(formatted_teacher)
    return formatted_teachers

def format_assignment_response(assignment):
    formatted_assignment = {
        "content": assignment.content,
        "created_at": str(assignment.created_at),
        "grade": assignment.grade,
        "id": assignment.id,
        "state": assignment.state,
        "student_id": assignment.student_id,
        "teacher_id": assignment.teacher_id,
        "updated_at": str(assignment.updated_at)
    }
    return formatted_assignment
