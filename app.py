from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def start():
    wynik1 = None
    wynik2 = None
    podsumowanie = None

    if request.method == "POST":
        wiek = int(request.form["wiek"])
        sen = int(request.form["sen"])
        stres = int(request.form["stres"])

        if sen < 6 or stres > 7:
            wynik1 = "Zły stan zdrowia"
        elif sen < 7 or stres > 5:
            wynik1 = "Średni stan zdrowia"
        else:
            wynik1 = "Dobry stan zdrowia"

        punkty = 0

        if sen >= 7:
            punkty += 2
        elif sen >= 6:
            punkty += 1

        if stres <= 3:
            punkty += 2
        elif stres <= 6:
            punkty += 1

        if wiek < 40:
            punkty += 1

        if punkty >= 4:
            wynik2 = f"Dobry stan zdrowia (wynik: {punkty})"
        elif punkty >= 2:
            wynik2 = f"Średni stan zdrowia (wynik: {punkty})"
        else:
            wynik2 = f"Zły stan zdrowia (wynik: {punkty})"

        if "Dobry" in wynik1 and "Dobry" in wynik2:
            podsumowanie = "Twój styl życia wygląda na zdrowy."
        elif "Zły" in wynik1 and "Zły" in wynik2:
            podsumowanie = "Warto zwrócić uwagę na sen i poziom stresu."
        else:
            podsumowanie = "Wyniki są mieszane – możliwa poprawa nawyków."

    return render_template(
        "index.html",
        wynik1=wynik1,
        wynik2=wynik2,
        podsumowanie=podsumowanie
    )

if __name__ == "__main__":
    print("""
▒▒▒▒▒█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
▒▒▒▒▒█░▒▒▒▒▒▒▒▓▒▒▓▒▒▒▒▒▒▒░█
▒▒▒▒▒█░▒▒▓▒▒▒▒▒▒▒▒▒▄▄▒▓▒▒░█░▄▄
▄▀▀▄▄█░▒▒▒▒▒▒▓▒▒▒▒█░░▀▄▄▄▄▄▀░░█
█░░░░█░▒▒▒▒▒▒▒▒▒▒▒█░░░░░░░░░░░█
▒▀▀▄▄█░▒▒▒▒▓▒▒▒▓▒█░░░█▒░░░░█▒░░█
▒▒▒▒▒█░▒▓▒▒▒▒▓▒▒▒█░░░░░░░▀░░░░░█
▒▒▒▄▄█░▒▒▒▓▒▒▒▒▒▒▒█░░█▄▄█▄▄█░░█
▒▒▒█░░░█▄▄▄▄▄▄▄▄▄▄█░█▄▄▄▄▄▄▄▄▄█
▒▒▒█▄▄█░░█▄▄█░░░░░░█▄▄█░░█▄▄█
    """)
    app.run(debug=True)