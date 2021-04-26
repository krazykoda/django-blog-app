from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

# Create your tests here.
class BlogTest(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(
			username= "tester",
			email="test@test.com",
			password="testpassword"
		)

		self.post = Post.objects.create(
			title="Blog test",
			body="we are testing",
			author=self.user
		)


		self.comment = Comment.objects.create(
			author=self.user,
			body="Comment test",
			post=self.post
		)

	def test_post_content(self):
		self.assertEqual(f"{self.post.title}", "Blog test")
		self.assertEqual(f"{self.post.body}", "we are testing")
		self.assertEqual(f"{self.post.author}", "tester")


	def test_comment_content(self):
		self.assertEqual(f"{self.comment.author}", "tester")
		self.assertEqual(f"{self.comment.body}", "Comment test")
		self.assertEqual(f"{self.comment.post}", "Blog test")



	def test_post_list(self):
		response = self.client.get("/blogs/")
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Blog test")
		self.assertContains(response, "we are testing")


	def test_post_details(self):
		response = self.client.get('/blogs/1')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Blog test")
		self.assertContains(response, "Comment test")
		self.assertTemplateUsed(response, 'detail.html')