

from flask import Flask, jsonify, request
from app.utils import get_principal_info_from_headers, format_assignments_response, format_teachers_response, format_assignment_response
import db  # Assuming you have a db module

app = Flask(__name__)

@app.route('/principal/assignments', methods=['GET'])
def get_principal_assignments():
    principal_info = get_principal_info_from_headers(request.headers)
    assignments = db.get_principal_assignments(principal_info['user_id'])
    response_data = format_assignments_response(assignments)
    return jsonify({'data': response_data})

@app.route('/principal/teachers', methods=['GET'])
def get_all_teachers():
    principal_info = get_principal_info_from_headers(request.headers)
    teachers = db.get_all_teachers()
    response_data = format_teachers_response(teachers)
    return jsonify({'data': response_data})

@app.route('/principal/assignments/grade', methods=['POST'])
def grade_or_regrade_assignment():
    principal_info = get_principal_info_from_headers(request.headers)
    payload = request.get_json()
    assignment_id = payload.get('id')
    grade = payload.get('grade')
    graded_assignment = db.grade_or_regrade_assignment(assignment_id, grade)
    response_data = format_assignment_response(graded_assignment)
    return jsonify({'data': response_data})

if __name__ == '__main__':
    app.run(debug=True)
