from flask import Flask , jsonify

todo = Flask('__name__')

@todo.route('/student-list')
def students_list():
    students = [
        {
            'id':1,
            'student_name': 'std1',
            'age':20,
            'email':'hello@gmail'
        },
        {
            'id':2,
            'student_name': 'std2',
            'age': 20,
            'email': 'hello1@gmail'
        },
        {
            'id':3,
            'student_name': 'std3',
            'age': 20,
            'email': 'hello2@gmail'
        }
    ]
    return jsonify(students)

@todo.route('/student-list/<int:id>')
def get_student_by_id(id):
    students = [
        {
            'id': 1,
            'student_name': 'std1',
            'age': 20,
            'email': 'hello@email'
        },
        {
            'id': 2,
            'student_name': 'std2',
            'age': 20,
            'email': 'hello12@email'
        },
        {
            'id': 3,
            'student_name': 'std3',
            'age': 20,
            'email': 'hello23@email'
        }
    ]
    student = next((s for s in students if s['id'] == id), None)
    if student:
        return jsonify(student)
    return jsonify({'error': 'Student not found'}), 404

if __name__ == '__main__':
    todo.run(
        host='127.0.0.1',
        port=5010,
        debug=True
    )

