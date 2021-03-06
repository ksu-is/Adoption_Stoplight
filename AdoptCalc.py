import turtle
wn = turtle.Screen()
wn.title("Adoption Stoplight")
wn.bgcolor("black")

#Draw a box
pen = turtle.Turtle()
pen.color ("yellow")
pen.speed('fastest')
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(-300,300)
pen.pendown()
pen.fd(240)
pen.rt(90)
pen.fd(560)
pen.rt(90)
pen.fd(240)
pen.rt(90)
pen.fd(560)


#Red Light

red_light= turtle.Turtle()
red_light.shape("circle")
red_light.speed('fastest')
red_light.shapesize(8,8,8)
red_light.color("grey")
red_light.penup()
red_light.goto(-180,200)

#Yellow Light
yellow_light= turtle.Turtle()
yellow_light.shape("circle")
yellow_light.shapesize(8,8,8)
yellow_light.speed('fastest')
yellow_light.color("grey")
yellow_light.penup()
yellow_light.goto(-180,20)

#Green Light
green_light= turtle.Turtle()
green_light.shape("circle")
green_light.shapesize(8,8,8)
green_light.speed('fastest')
green_light.color("grey")
green_light.penup()
green_light.goto(-180,-160)


#About the animal
screen = turtle.Screen()


animal_name = screen.textinput("How Adoptable?","What is the animal's name?")
animal_type = screen.textinput("How Adoptable?","Is the animal a cat or a dog?")
animal_solid = screen.textinput("How Adoptable?","Is this animal a solid color? (Yes or No)")
animal_color = screen.textinput("How Adoptable?","Does this animal have black on it? (Yes or No)")
animal_age = int(screen.textinput("How Adoptable?","What is the animal's age in months?"))

points = 0

#Cat
if animal_type.lower() == "cat":
#Special Breed
    cat_special = screen.textinput("How Adoptable?","Is this a normal cat breed? (Yes or No)")
    if cat_special.lower() == "yes":
        points = points + 1
    elif cat_special.lower() == "no":
        points = points - 2
    else:
        print("So sorry! I didn't get that")
#Cat colors
    if animal_solid.lower() == "yes":
        if animal_color.lower() == "yes":
            points = points + 3
        elif animal_color.lower() == "no":
            points = points - 1
        else:
            print("Sorry, something went wrong. Please try again.")
    elif animal_solid.lower() == "no":
        if animal_color.lower() == "yes":
            points = points + 2
        elif animal_color.lower() == "no":
            points = points + 1
        else:
            print("Sorry, something went wrong. Try again.")
    else: 
        print("Sorry, I didn't get that")
#Cat Age
    if animal_age < 12:
        print("Green - this animal will have no problem getting adopted!")
    elif animal_age >= 12 and animal_age < 36:
        points = points + 1
    elif animal_age >=36 and animal_age < 60:
        points = points + 2
    elif animal_age >= 60 and animal_age < 96:
         points = points + 3
    elif animal_age > 96:
         points = points + 4
    else:
        print("Sorry, something went wrong")


    
#Dog
elif animal_type.lower() == "dog":
    bully_breed = screen.textinput("How Adoptable?","Is this a bully breed dog? (Yes/No)")
#Dog breed
    if bully_breed.lower() == "yes":
        points = points + 3
    elif bully_breed.lower() == "no":
        toy_breed = screen.textinput("How Adoptable?","Is this a toy breed dog?")
        if toy_breed.lower() == "yes":
            points = points - 1
        elif toy_breed.lower() == "no":
            pass
        else:
            pass
    else:
        print("Sorry, I didn't get that. Please try again")
#Dog Colors
    if animal_solid.lower() == "yes":
        if animal_color.lower() == "yes":
            points = points + 3
        elif animal_color.lower() == "no":
            points = points - 1
        else:
            print("Sorry, something went wrong. Please try again.")
    elif animal_solid.lower() == "no":
        if animal_color.lower() == "yes":
            points = points + 2
        elif animal_color.lower() == "no":
            points = points + 1
        else:
            print("Sorry, something went wrong. Try again.")
    else: 
        print("Sorry, I didn't get that")
#Dog Age
    if animal_age < 12:
        print("Green - this animal will have no problem getting adopted!")
    elif animal_age >= 12 and animal_age < 36:
        points = points + 1
    elif animal_age >=36 and animal_age < 60:
        points = points + 2
    elif animal_age >= 60 and animal_age < 96:
         points = points + 3
    elif animal_age > 96:
         points = points + 4
    else:
        print("Sorry, something went wrong")
    

#Total Points
text_turtle= turtle.Turtle()
text_turtle.color("white")
text_turtle.hideturtle()
if animal_type.lower() == "cat" or "dog":
    if points < 4:
        green_light.color("green")
        text_turtle.write(animal_name + " will have no \n problem being adopted!", font=("Arial",32,"normal"))
    elif points >= 4 and points < 6:
        yellow_light.color("yellow")
        text_turtle.write(animal_name + " may need some \n help to be adopted", font=("Arial",32,"normal"))
    elif points >= 6:
        red_light.color("red")
        text_turtle.write(animal_name + " will definitely \n need help being adopted \n - consider discounting \n adoption fee right away!", font=("Arial",32,"normal"))
    else:
        pass
else:
    pass



wn.mainloop()
