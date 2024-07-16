articulos = ["el", "la", "los", "las", "un", "una", "unos", "unas"]
nombres = ["niño", "niños", "niña", "niñas", "persona", "personas", "amigo", "amigos", "amiga", "amigas", "músico", "peleador", "peleadora", "comediante", "dibujante", "diseñador", "diseñadora", "bailarín", "bailarina", "corredor", "corredora"]
verbos = ["juega", "jugará", "jugó", "jugarán", "jugaron", "jugando", "jugar", "juegan", "baila", "bailará", "bailó", "bailarán", "bailaron", "bailando", "bailar", "bailan", "pelea", "peleará", "peleó", "pelearán", "pelearon", "peleando", "pelear", "pelean", "vuela", "volará", "voló", "volarán", "volaron", "volando", "volar", "vuelan", "cantinflea", "cantinfleará", "cantinfleó", "cantinflearán", "cantinflearon", "cantinfleando", "cantinflear", "cantinflean", "discute", "discutirá", "discutió", "discutirán", "discutieron", "discutiendo", "discutir", "discuten", "colorea", "coloreará", "coloreó", "colorearán", "colorearon", "coloreando", "colorear", "colorean", "canta", "cantará", "cantó", "cantarán", "cantaron", "cantando", "cantar", "cantan", "viaja", "viajará", "viajó", "viajarán", "viajaron", "viajando", "viajar", "viajan", "patea", "pateará", "pateó", "patearán", "patearon", "pateando", "patear", "patean", "come", "comerá", "comió", "comerán", "comieron", "comiendo", "comer", "comen"]
complementos = ["alegre", "feliz", "enojado", "cansado", "incansable", "callado", "mal", "bien"]

def encontrar_mas_cercana(palabra, lista_palabras):
    return min(lista_palabras, key=lambda p: sum(1 for a, b in zip(palabra, p) if a != b) + abs(len(palabra) - len(p))) if lista_palabras else palabra

def corregir_frase(frase):
    palabras = frase.lower().split()
    if not (4 <= len(palabras) <= 5):
        return "Ingrese una frase de exactamente cuatro o cinco palabras."
    
    roles = [articulos, nombres, verbos, complementos]
    corregidas = [encontrar_mas_cercana(palabras[i], roles[i]) for i in range(4)]
    
    nombre = corregidas[1]
    es_plural = nombre.endswith("s")
    es_femenino = nombre.endswith("a") or nombre.endswith("as")
    
    if es_plural:
        corregidas[0] = "los" if corregidas[0] in ["el", "un"] else "las"
        corregidas[2] = corregidas[2][:-1] + "n" if not corregidas[2].endswith("n") and corregidas[2][-1] != "r" else corregidas[2]
        complementos_plural = [c for c in complementos if c.endswith("s")]
        corregidas[3] = encontrar_mas_cercana(corregidas[3], complementos_plural) if complementos_plural else corregidas[3]
    else:
        corregidas[0] = "el" if not es_femenino else "la"
        corregidas[2] = corregidas[2][:-1] if corregidas[2].endswith("n") and corregidas[2][-1] != "r" else corregidas[2]
        complementos_singular = [c for c in complementos if not c.endswith("s")]
        corregidas[3] = encontrar_mas_cercana(corregidas[3], complementos_singular) if complementos_singular else corregidas[3]
    
    return f"La frase corregida es: '{' '.join(corregidas)}'"

def main():
    while True:
        frase = input("Ingrese una frase de cuatro o cinco palabras o 'salir' para terminar: ")
        if frase.lower() == 'salir':
            break
        print(corregir_frase(frase))

if __name__ == "__main__":
    main()
