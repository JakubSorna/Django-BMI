from django.shortcuts import render

def BMI(request):
	if request.method == "POST":
		try:
			float(request.POST["weight"])
			float(request.POST["height"])
		except:
			error = "Wrong values."
			return render(request, "main/BMI.html", dict(error=error))

		height = float(request.POST["height"])/100
		result = round(float(request.POST["weight"])/height**2,1)
		BMI = f"Your BMI is {result}"
		return render(request, "main/BMI.html",{"BMI":BMI})
	else:
		return render(request, "main/BMI.html")



# Create your views here.
