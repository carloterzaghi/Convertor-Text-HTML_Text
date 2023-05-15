import os

dic_caracteres = {
    "Á": "&Aacute;",
    "á": "&aacute;",
    "À": "&Agrave;",
    "à": "&agrave;",
    "Ã": "&Atilde;",
    "ã": "&atilde;",
    "Â": "&Acirc;",
    "â": "&acirc;",
    "Ä": "&Auml;",
    "ä": "&auml;",
    "Å": "&Aring;",
    "å": "&aring;",
    "É": "&Eacute;",
    "é": "&eacute;",
    "È": "&Egrave;",
    "è": "&egrave;",
    "Ê": "&Ecirc;",
    "ê": "&ecirc;",
    "Ë": "&Euml;",
    "ë": "&euml;",
    "Í": "&Iacute;",
    "í": "&iacute;",
    "Ì": "&Igrave;",
    "ì": "&igrave;",
    "Î": "&Icirc;",
    "î": "&icirc;",
    "Ï": "&Iuml;",
    "ï": "&iuml;",
    "Ó": "&Oacute;",
    "ó": "&oacute;",
    "Ò": "&Ograve;",
    "ò": "&ograve;",
    "Ô": "&Ocirc;",
    "ô": "&ocirc;",
    "Ö": "&Ouml;",
    "ö": "&ouml;",
    "Õ": "&Otilde;",
    "õ": "&otilde;",
    "Ú": "&Uacute;",
    "ú": "&uacute;",
    "Ù": "&Ugrave;",
    "ù": "&ugrave;",
    "Û": "&Ucirc;",
    "û": "&ucirc;",
    "Ü": "&Uuml;",
    "ü": "&uuml;",
    "Ç": "&Ccedil;",
    "ç": "&ccedil;",
    "Ñ": "&Ntilde;",
    "ñ": "&ntilde;",
    "Ø": "&Oslash;",
    "ø": "&oslash;",
    "Þ": "&THORN;",
    "þ": "&thorn;",
    "ß": "&szlig;",
}

while True:
    os.system('cls')
    text = input("Texto normal: ")

    new_text = ""
    for i in text:
        if i in dic_caracteres.keys():
            new_text += dic_caracteres[i]
        else:
            new_text += i
    os.system('cls')
    print("Texto enviado:\n\n"+text)
    print("\n\n============================================\n\nTexto HTML:\n\n" + new_text + "\n\n\n")
    continuar = input("Continuar: ")
    if continuar == "n": break
