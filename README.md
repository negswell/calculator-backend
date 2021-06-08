# calculator-backend

#Approach

Create simple get request routes or end points for different types of mathematical calculations that need to be performed.For simple operations like addition, subtraction , multiplication,division, i used the eval function to evaluate the entire expression string. For the power of a number operation had to parse ^ to ** to make it syntactically correct in python in order to eval it. For the other complex functions, i simply used the math library to make it easy to perform the complex calculations.The server runs on gunicorn in production , as it gives better performance than inbuilt python servers. The reason to choose fast api is that it makes it easy to develop API's and has one of the best performances in production environment among python frameworks.

#Assumptions 

Used the math library to perform complex math operations.

#Asymptotic Analysis 

X to power y or x**y is O(n)

Factorial of n : O(N!)

eval used in calcualte route is O(n*n) where n is length of the string.
can be optimized to O(n) if parsing for character '^' is done in the frontend.


#Improvemnts 

Create response and result models using pedantic.

