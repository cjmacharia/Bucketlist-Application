
class Bucketlist():

	Bucketlists=[]


	def __init__(self,post=None,description=None,):
		self.post=post
		self.description=description
	def create(self,post, description):
		if description!=''and post!='':
			data = {}
			data['post'] = post
			data['description']=description
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