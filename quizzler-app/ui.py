# create the label for the score
self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR) # increment the score
self.score_label.grid(row=0, column=1)

# create the canvas (where the question will be displayed)
self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question Text", fill=THEME_COLOR, font=("Arial", 20, "italic"))
self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

# create the buttons
true_image = PhotoImage(file="quizzler-app/images/true.png")
self.true_button = Button(image=true_image, highlightthickness=0)
self.true_button.grid(row=2, column=0)

false_image = PhotoImage(file="quizzler-app/images/false.png")
self.false_button = Button(image=false_image, highlightthickness=0) 
self.false_button.grid(row=2, column=1)