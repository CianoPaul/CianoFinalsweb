from django.db import models

class Item(models.Model):
	sname = models.CharField(max_length=40)
	fname = models.CharField(max_length=50)
	mname = models.CharField(max_length=50)
	age = models.TextField(default="")
	add = models.TextField(default="")
	contact = models.TextField(default="")
	disease = models.TextField(default="")
	specifydisease = models.TextField(default="")
	plan = models.TextField(default="")
	total = models.TextField(default="")

	def __str__(self):
         return '%s-%s' % (self.sname, self.fname)

class ExercisePlan(models.Model):
	intensity = models.TextField(default="")
	focus = models.TextField(default="")
	
	planID = models.BigAutoField(primary_key=True)
	#customerID = models.ForeignKey(Item, on_delete=models.CASCADE)
	
	
	def __str__(self):
		return self.intensity

class Program(models.Model):
	DietPlan = models.TextField(default="")
	Trainer = models.TextField(default="")
	Duration = models.TextField(default="")
	
	programID = models.BigAutoField(primary_key=True)
	#customerID = models.ForeignKey(Item, on_delete=models.CASCADE)
	#planID = models.ForeignKey(Item, on_delete=models.CASCADE)
	prg_prd = models.ManyToManyField(ExercisePlan)
	
	def __str__(self):
		return self.DietPlan
	
class Products(models.Model):
	protein = models.TextField(default="")
	gymbags = models.TextField(default="")
	mat = models.TextField(default="")
	others = models.TextField(default="")
	Loss = models.TextField(default="")
	locker = models.TextField(default="")
	productID = models.BigAutoField(primary_key=True)
	#customerID = models.ForeignKey(Item, on_delete=models.CASCADE)
	#planID = models.ForeignKey(Item, on_delete=models.CASCADE)
	#programID = models.ForeignKey(Item, on_delete=models.CASCADE)
	program_product = models.ManyToManyField(Program)
	
	def __str__(self):
		return self.protein
	
class Feedback(models.Model):
	review = models.TextField(default="")
	concern = models.TextField(default="")
	complaints = models.TextField(default="")
	
	reviewID = models.TextField(default="",primary_key=True)
	#customerID = models.ForeignKey(Item, on_delete=models.CASCADE)
	#planID = models.ForeignKey(Item, on_delete=models.CASCADE)
	#programID = models.ForeignKey(Item, on_delete=models.CASCADE)
	#productID = models.ForeignKey(Item, on_delete=models.CASCADE)
	review_item = models.ForeignKey(Item, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.reviewID
	
