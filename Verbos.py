def correccion_verbo(verbo):
    verbos_espanol = [
        "abandonar", "abrir", "abrazar", "aburrir", "acampar", "aceptar", "aclarar", "acompañar", "aconsejar", "acordar",
        "actuar", "adivinar", "admirar", "admitir", "adoptar", "adorar", "advertir", "afeitar", "agarrar", "agradecer",
        "agrandar", "agravar", "agregar", "aguantar", "ahorrar", "alcanzar", "alegrar", "alimentar", "aliviar", "alquilar",
        "amar", "amenazar", "andar", "anunciar", "apagar", "aparecer", "aplaudir", "aplicar", "apoyar", "aprender",
        "apretar", "aprovechar", "arreglar", "arriesgar", "asistir", "asustar", "atacar", "atender", "atraer", "atrever",
        "aumentar", "ayudar", "bailar", "bajar", "barrer", "beber", "bendecir", "borrar", "buscar", "caer", "calentar",
        "callar", "calmar", "cambiar", "caminar", "cancelar", "cantar", "cargar", "casar", "castigar", "cazar", "ceder",
        "cenar", "cerrar", "charlar", "chocar", "cobrar", "cocinar", "coger", "colaborar", "colocar", "comer", "compartir",
        "comprar", "comprender", "comunicar", "conducir", "conocer", "conseguir", "consentir", "construir", "contar",
        "contestar", "continuar", "contratar", "contribuir", "convencer", "convertir", "correr", "cortar", "coser",
        "costar", "crear", "crecer", "creer", "cruzar", "cuidar", "cumplir", "dar", "decidir", "decir", "declarar",
        "decorar", "dedicar", "dejar", "demostrar", "denunciar", "depender", "derrotar", "desayunar", "descansar",
        "describir", "desear", "desempeñar", "deshacer", "despedir", "despertar", "destruir", "detener", "detestar",
        "devolver", "dibujar", "dirigir", "discutir", "disfrutar", "divertir", "dividir", "doblar", "doler", "dormir",
        "duchar", "dudar", "echar", "elegir", "empezar", "empujar", "encantar", "encender", "encontrar", "enfermar",
        "engañar", "enojar", "enseñar", "entender", "entrar", "enviar", "equivocar", "escapar", "escoger", "escribir",
        "escuchar", "esforzar", "esperar", "esquiar", "establecer", "estar", "estudiar", "evitar", "examinar", "exigir",
        "existir", "explicar", "explorar", "expresar", "extender", "faltar", "felicitar", "fijar", "firmar", "follar",
        "formar", "fregar", "fumar", "ganar", "gastar", "gemir", "girar", "gobernar", "golpear", "gritar", "guardar",
        "gustar", "haber", "hablar", "hallar", "hacer", "herir", "huir", "iluminar", "imaginar", "impedir", "importar",
        "incluir", "indicar", "informar", "insistir", "intentar", "interesar", "introducir", "invitar", "ir", "jugar",
        "juntar", "jurar", "juzgar", "lavar", "leer", "levantar", "limpiar", "llamar", "llegar", "llenar", "llevar",
        "llorar", "lograr", "luchar", "madrugar", "mandar", "mantener", "marcar", "matar", "mecer", "medir", "mejorar",
        "mentir", "merecer", "meter", "mirar", "modificar", "moler", "molestar", "montar", "morder", "morir", "mostrar",
        "mover", "nadar", "nacer", "necesitar", "negar", "negociar", "notar", "obedecer", "obligar", "observar", "obtener",
        "ocupar", "ofrecer", "oir", "olvidar", "operar", "opinar", "ordenar", "organizar", "pagar", "parar", "parecer",
        "partir", "pasar", "pasear", "pedir", "pelear", "pensar", "perder", "perdonar", "permitir", "perseguir", "persuadir",
        "pesar", "pintar", "pisar", "platicar", "practicar", "predecir", "preparar", "presentar", "prestar", "probar",
        "producir", "proteger", "proveer", "publicar", "quemar", "quitar", "realizar", "recibir", "recoger", "recomendar",
        "reconocer", "recordar", "recorrer", "reducir", "reflexionar", "regalar", "regar", "registrar", "relajar", "reparar",
        "repetir", "resolver", "respetar", "respirar", "responder", "restaurar", "resultar", "revelar", "revisar", "rezar",
        "robar", "romper", "saber", "sacar", "saltar", "saludar", "salvar", "sanar", "satisfacer", "seguir", "sentar",
        "sentir", "separar", "servir", "significar", "silenciar", "simbolizar", "situar", "soñar", "someter", "sonreir",
        "soplar", "soportar", "sorprender", "subir", "sufrir", "sugerir", "superar", "suponer", "suspender", "sustituir",
        "tapar", "temer", "tender", "terminar", "tirar", "tocar", "tomar", "trabajar", "traducir", "traer", "tratar", "unir",
        "usar", "utilizar", "vaciar", "valer", "vender", "venir", "ver", "viajar", "visitar", "vivir", "volar", "volver",
        "votar", "zumbar"
    ]

    for v in verbos_espanol:
        if verbo.endswith('ando') and v[:-2] + 'ar' == verbo[:-4] + 'ar':
            return v
        elif verbo.endswith('iendo') and v[:-2] + 'er' == verbo[:-4] + 'er':
            return v
        elif verbo.endswith('iendo') and v[:-2] + 'ir' == verbo[:-4] + 'ir':
            return v
        elif verbo.endswith('ado') and v[:-2] + 'ar' == verbo[:-3] + 'ar':
            return v
        elif verbo.endswith('ido') and v[:-2] + 'er' == verbo[:-3] + 'er':
            return v
        elif verbo.endswith('ido') and v[:-2] + 'ir' == verbo[:-3] + 'ir':
            return v
    return None

cadena = input("Cadena: ")
print("Frase original:", cadena)
palabras = cadena.split()
verbos_encontrados = []

for palabra in palabras:
    if palabra.endswith(('ando', 'iendo', 'ado', 'ido', 'endo')):
        verbo_infinitivo = correccion_verbo(palabra)
        if verbo_infinitivo:
            verbos_encontrados.append((palabra, verbo_infinitivo))

if verbos_encontrados:
    for gerundio_participio, infinitivo in verbos_encontrados:
        print(f"'{gerundio_participio}' se convierte en '{infinitivo}'")
else:
    print("No se encontraron verbos en gerundio o participio.")
