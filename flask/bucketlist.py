
class Bucketlist():

	Bucketlists=[]


	def __init__(self,post=None,description=None,owner=None):
		self.post=post
		self.description=description
		self.owner=owner
	def create(self,post, description, owner):
		if description!=''and post!='':
			data = {}
			data['post'] = post
			data['description']=description
			data['owner']=owner
			self.Bucketlists.append(data)
			
			return 1
			
		else:
			return 2
	def delete(self,post,description):
		for i in self.Bucketlists:
			self.Bucketlists.pop(i)		
			return True
		else:
			return False			