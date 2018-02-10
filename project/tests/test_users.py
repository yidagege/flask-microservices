import json
from project.tests.base import BaseTestCase

class TestUserService(BaseTestCase):
	def test_users(self):
		"""确保ping的服务正常."""
		response = self.client.get('/ping')
		data = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 200)
		self.assertIn('pong', data['message'])
		self.assertIn('success', data['status'])

	def test_add_user(self):
		"""确保能够正确添加一个用户的用户到数据库中"""
		with self.client:
			response = self.client.post(
	            '/users',
	            data=json.dumps(dict(username='cnych', email='qikqiak@gmail.com')),
	            content_type='application/json',
	        )
			data = json.loads(response.data.decode())
			self.assertEqual(response.status_code, 201)
			self.assertIn('qikqiak@gmail.com was added', data['message'])
			self.assertEqual('success', data['status'])
