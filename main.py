html = """
<html>
    <h1> Hallo, ich bin Marwin!
    </h1>
    <body>
        <h2> &Uuml;ber mich: </h2>
        <p>
        Das ist meine eigene Website
        </p>
        <h2> Was ich machen m&ouml;chte: </h2>
    <p>
        Vielleicht launche ich hier mein eigenes GPT-Model...
        </p>
    </body>
</html>

"""

print(html)

# Write HTML String to file.html
with open("index.html", "w") as file:
    file.write(html)