weight = float(input("Enter your weight:"))
height = float(input("Enter your height:"))

height = (height / 100) ** 2

body_mass_index = round(weight / height, 1)

if body_mass_index >= 40:
    print("Your body mass index is", body_mass_index, "You are too fat, go to GYM!")
elif 35 <= body_mass_index < 40:
    print("Your body mass index is", body_mass_index, "You are fat enough, go to GYM!")
elif 30 <= body_mass_index < 35:
    print("Your body mass index is", body_mass_index, "You are fat, go to GYM!")
elif 25 <= body_mass_index < 30:
    print("Your body mass index is", body_mass_index, "You are almost okay, eat less!")
elif 18.5 <= body_mass_index < 25:
    print("Your body mass index is", body_mass_index, "You are okay!")
elif body_mass_index < 18.5:
    print("Your body mass index is", body_mass_index, "EAT MORE, STUPID BITCH!")
