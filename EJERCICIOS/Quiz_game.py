questions = ("¿Cuál es la capital de Francia?",
             "¿Cuál es la capital de España?",
             "¿Cuál es la capital de Italia?",
             "¿Cuál es la capital de Alemania?",
             "¿Cuál es la capital de Portugal?")


options = (("A. París", "B. Londres", "C.Berlín", "D. Roma",),
            ("A. Madrid", "B. Barcelona", "C. Valencia", "D. Sevilla",),
            ("A. Milán", "B. Roma", "C. Nápoles", "D. Turín",),
            ("A. Múnich", "B. Berlín", "C. Hamburgo", "D. Frankfurt",),
            ("A. Lisboa", "B. Oporto", "C. Faro", "D. Coimbra",))   


answers =  ("A", "A", "B", "B", "A")
guesses  = []
score = 0

question_number = 0

for question in questions:
    print("-------------------------")
    print(question)
    for i in options[question_number]:
        print(i)
    guess = input("Ingrese su respuesta (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_number]:
        score += 1
        print("¡Correcto!")
    else:
        print("Incorrecto.")
        print(f"La respuesta correcta es: {answers[question_number]}")
    question_number += 1

print("-------------------------")
print("Resultados finales")
print("-------------------------")
print("Respuestas correctas: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("Tus respuestas: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
score  =  int( score / len(questions) * 100)
print(f"Tu puntuación es: {score}%")