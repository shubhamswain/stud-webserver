import string
import poplib
from django.contrib.auth import get_user_model
MyUser = get_user_model()
class WebmailBackend(object):
	def authenticate(self, webmail=None, password=None, server=None):
		try:
			#print "Yes1"
			serv = poplib.POP3_SSL(server, 995)
			serv.user(webmail)
			if('+OK'):
				serv.pass_(password)
				if('+OK Logged in.'):
					try:
						user = MyUser.objects.get(webmail=webmail)
					except:
						user = MyUser.objects.create_user(webmail=webmail)
						user.save()
					#print "Yes2"	
					return user
				else:
					#print "Yes3"
					return None	
			else:
				return None		     
		except poplib.error_proto:
			return None	
		
	def get_user(self, user_id):
		try:
			return MyUser.objects.get(pk=user_id)
		except MyUser.DoesNotExist:
			return None
