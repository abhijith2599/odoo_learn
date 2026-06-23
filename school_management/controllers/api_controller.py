# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class SchoolApiController(http.Controller):

    @http.route('/api/school/auth', type='json', auth='none', methods=['POST'], csrf=False)
    def authenticate(self, db, login, password, **kwargs):
        try:
            request.session.authenticate(db, {'login': login, 'password': password, 'type': 'password'})
            return {
                'status': 'success',
                'session_id': request.session.sid,
                'uid': request.session.uid
            }
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

    @http.route('/api/school/student/<int:student_id>', type='http', auth='user', methods=['GET'], csrf=False)
    def get_student(self, student_id, **kwargs):
        student = request.env['school.student'].sudo().browse(student_id)
        if not student.exists():
            return request.make_response(
                json.dumps({'error': 'Student not found'}),
                headers=[('Content-Type', 'application/json')],
                status=404
            )
        
        data = {
            'id': student.id,
            'name': student.name,
            'roll_number': student.roll_number,
            'state': student.state,
            'class': student.class_id.name if student.class_id else None,
            'company': student.company_id.name if student.company_id else None
        }
        return request.make_response(
            json.dumps(data),
            headers=[('Content-Type', 'application/json')]
        )

    @http.route('/api/school/student/<int:student_id>/attendance', type='json', auth='user', methods=['POST'], csrf=False)
    def mark_attendance(self, student_id, **kwargs):
        student = request.env['school.student'].sudo().browse(student_id)
        if not student.exists():
            return {'status': 'error', 'message': 'Student not found'}
        
        # Log attendance in chatter
        student.message_post(body="Attendance marked via REST API.")
        return {'status': 'success', 'message': f'Attendance marked for {student.name}'}
