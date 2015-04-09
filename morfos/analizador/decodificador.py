def decodificador(codigoEagle):
	codigo = codigoEagle.lower()
	codigoDecodificado = ""

	#print(codigo)
	
	#Adjetivos
	if(codigo[0] == 'a'):
		codigoDecodificado = "Adjetivo"
		if(codigo[1] == 'q'):
			codigoDecodificado = codigoDecodificado + ", Calificativo"
		if(codigo[1] == 'o'):
			codigoDecodificado = codigoDecodificado + ", Ordinal"
		if(codigo[2] == 'a'):
			codigoDecodificado = codigoDecodificado + ", Aumentativo"
		if(codigo[2] == 'd'):
				codigoDecodificado = codigoDecodificado + ", Disminutivo"                            
		if(codigo[2] == 'c'):
				codigoDecodificado = codigoDecodificado + ", Comparativo"
		if(codigo[2] == 's'):
				codigoDecodificado = codigoDecodificado + ", Superlativo"
		if(codigo[3] == 'm'):
				codigoDecodificado = codigoDecodificado + ", Másculino"
		if(codigo[3] == 'f'):
				codigoDecodificado = codigoDecodificado + ", Femenino"                                
		if(codigo[3] == 'c'):
				codigoDecodificado = codigoDecodificado + ", Común"
		if(codigo[4] == 's'):
				codigoDecodificado = codigoDecodificado + ", Singular"
		if(codigo[4] == 'p'):
				codigoDecodificado = codigoDecodificado + ", Plural"
		if(codigo[4] == 'n'):
				codigoDecodificado = codigoDecodificado + ", Invariable" 
		if(codigo[5] == 'p'):
				codigoDecodificado = codigoDecodificado + ", Participio"
	
	#Adverbios
	if(codigo[0] == 'r'):
		codigoDecodificado = "Adverbio"
		if(codigo[1] == 'g'):
			codigoDecodificado = codigoDecodificado + ", General"
		if(codigo[1] == 'n'):
			codigoDecodificado = codigoDecodificado + ", Negativo"
	
	#Determinantes
	if(codigo[0] == 'd'):
		codigoDecodificado = "Determinante"
		if(codigo[1] == 'd'):
			codigoDecodificado = codigoDecodificado + ", Demostrativo"
		if(codigo[1] == 'p'):
			codigoDecodificado = codigoDecodificado + ", Posesivo"
		if(codigo[1] == 't'):
			codigoDecodificado = codigoDecodificado + ", Interrogativo"
		if(codigo[1] == 'e'):
			codigoDecodificado = codigoDecodificado + ", Exclamativo"
		if(codigo[1] == 'i'):
			codigoDecodificado = codigoDecodificado + ", Indefinido"
		if(codigo[1] == 'a'):
			codigoDecodificado = codigoDecodificado + ", Artículo"
		if(codigo[2] == '1'):
			codigoDecodificado = codigoDecodificado + ", Primera Persona"
		if(codigo[2] == '2'):
			codigoDecodificado = codigoDecodificado + ", Segunda Persona"
		if(codigo[2] == '3'):
			codigoDecodificado = codigoDecodificado + ", Tercera Persona"
		if(codigo[3] == 'm'):
			codigoDecodificado = codigoDecodificado + ", Masculino"
		if(codigo[3] == 'f'):
			codigoDecodificado = codigoDecodificado + ", Femenino"
		if(codigo[3] == 'c'):
			codigoDecodificado = codigoDecodificado + ", Común"
		if(codigo[3] == 'n'):
			codigoDecodificado = codigoDecodificado + ", Neutro"
		if(codigo[4] == 's'):
			codigoDecodificado = codigoDecodificado + ", Singular"
		if(codigo[4] == 'p'):
			codigoDecodificado = codigoDecodificado + ", Plural"
		if(codigo[4] == 'n'):
			codigoDecodificado = codigoDecodificado + ", Invariable"
		if(codigo[5] == 's'):
			codigoDecodificado = codigoDecodificado + ", Singular"
		if(codigo[5] == 'p'):
			codigoDecodificado = codigoDecodificado + ", Plural"
	
	#Nombres
	if(codigo[0] == 'n'):
		codigoDecodificado = "Nombre"
		if(codigo[1] == 'c'):
			codigoDecodificado = codigoDecodificado + ", Común"
		if(codigo[1] == 'p'):
			codigoDecodificado = codigoDecodificado + ", Propio"
		if(codigo[2] == 'm'):
			codigoDecodificado = codigoDecodificado + ", Masculino"
		if(codigo[2] == 'f'):
			codigoDecodificado = codigoDecodificado + ", Femenino"
		if(codigo[2] == 'c'):
			codigoDecodificado = codigoDecodificado + ", Común"
		if(codigo[3] == 's'):
			codigoDecodificado = codigoDecodificado + ", Singular"
		if(codigo[3] == 'p'):
			codigoDecodificado = codigoDecodificado + ", Plural"
		if(codigo[3] == 'n'):
			codigoDecodificado = codigoDecodificado + ", Invariable"
		if(codigo[5] == 's' and codigo[6] == 'p'):
			codigoDecodificado = codigoDecodificado + ", Persona"
		if(codigo[5] == 'g' and codigo[6] == '0'):
			codigoDecodificado = codigoDecodificado + ", Lugar"
		if(codigo[5] == 'o' and codigo[6] == '0'):
			codigoDecodificado = codigoDecodificado + ", Organización"
		if(codigo[5] == 'v' and codigo[6] == '0'):
			codigoDecodificado = codigoDecodificado + ", Otros"
		if(codigo[6] == 'a'):
			codigoDecodificado = codigoDecodificado + ", Aumentativo"
		if(codigo[6] == 'd'):
			codigoDecodificado = codigoDecodificado + ", Disminutivo"
	
	#Verbos
	if(codigo[0] == 'v'):
		codigoDecodificado = "Verbo"
		if(codigo[1] == 'm'):
			codigoDecodificado = codigoDecodificado + ", Principal"
		if(codigo[1] == 'a'):
			codigoDecodificado = codigoDecodificado + ", Auxiliar"
		if(codigo[1] == 's'):
			codigoDecodificado = codigoDecodificado + ", Semiauxiliar"
		if(codigo[2] == 'i'):
			codigoDecodificado = codigoDecodificado + ", Indicativo"
		if(codigo[2] == 's'):
			codigoDecodificado = codigoDecodificado + ", Subjuntivo"
		if(codigo[2] == 'm'):
			codigoDecodificado = codigoDecodificado + ", Imperativo"
		if(codigo[2] == 'n'):
			codigoDecodificado = codigoDecodificado + ", Infinitivo"
		if(codigo[2] == 'g'):
			codigoDecodificado = codigoDecodificado + ", Gerundio"
		if(codigo[2] == 'p'):
			codigoDecodificado = codigoDecodificado + ", Participio"
		if(codigo[3] == 'p'):
			codigoDecodificado = codigoDecodificado + ", Presente"
		if(codigo[3] == 'i'):
			codigoDecodificado = codigoDecodificado + ", Imperfecto"
		if(codigo[3] == 'f'):
			codigoDecodificado = codigoDecodificado + ", Futuro"
		if(codigo[3] == 's'):
			codigoDecodificado = codigoDecodificado + ", Pasado"
		if(codigo[3] == 'c'):
			codigoDecodificado = codigoDecodificado + ", Condicional"
		if(codigo[4] == '1'):
			codigoDecodificado = codigoDecodificado + ", Primera Persona"
		if(codigo[4] == '2'):
			codigoDecodificado = codigoDecodificado + ", Segunda Persona"
		if(codigo[4] == '3'):
			codigoDecodificado = codigoDecodificado + ", Tercera Persona"
		if(codigo[5] == 's'):
			codigoDecodificado = codigoDecodificado + ", Singular"
		if(codigo[5] == 'p'):
			codigoDecodificado = codigoDecodificado + ", Plural"
		if(codigo[6] == 'm'):
			codigoDecodificado = codigoDecodificado + ", Masculino"
		if(codigo[6] == 'f'):
			codigoDecodificado = codigoDecodificado + ", Femenino"
	
	#Pronombres
	if(codigo[0] == 'p'):
		codigoDecodificado = "Pronombre"
		if(codigo[1] == 'p'):
			codigoDecodificado = codigoDecodificado + ", Personal"
		if(codigo[1] == 'd'):
			codigoDecodificado = codigoDecodificado + ", Demostrativo"
		if(codigo[1] == 'x'):
			codigoDecodificado = codigoDecodificado + ", Posesivo"
		if(codigo[1] == 'i'):
			codigoDecodificado = codigoDecodificado + ", Indefinido"
		if(codigo[1] == 't'):
			codigoDecodificado = codigoDecodificado + ", Interrogativo"
		if(codigo[1] == 'r'):
			codigoDecodificado = codigoDecodificado + ", Relativo"
		if(codigo[1] == 'e'):
			codigoDecodificado = codigoDecodificado + ", Exclamativo"
		if(codigo[2] == '1'):
			codigoDecodificado = codigoDecodificado + ", Primera Persona"
		if(codigo[2] == '2'):
			codigoDecodificado = codigoDecodificado + ", Segunda Persona"
		if(codigo[2] == '3'):
			codigoDecodificado = codigoDecodificado + ", Tercera Persona"
		if(codigo[3] == 'm'):
			codigoDecodificado = codigoDecodificado + ", Masculino"
		if(codigo[3] == 'f'):
			codigoDecodificado = codigoDecodificado + ", Femenino"
		if(codigo[3] == 'c'):
			codigoDecodificado = codigoDecodificado + ", Común"
		if(codigo[3] == 'n'):
			codigoDecodificado = codigoDecodificado + ", Neutro"
		if(codigo[4] == 's'):
			codigoDecodificado = codigoDecodificado + ", Singular"
		if(codigo[4] == 'p'):
			codigoDecodificado = codigoDecodificado + ", Plural"
		if(codigo[4] == 'n'):
			codigoDecodificado = codigoDecodificado + ", Impersonal Invariable"
		if(codigo[5] == 'n'):
			codigoDecodificado = codigoDecodificado + ", Nominativo"
		if(codigo[5] == 'a'):
			codigoDecodificado = codigoDecodificado + ", Acusativo"
		if(codigo[5] == 'd'):
			codigoDecodificado = codigoDecodificado + ", Dativo"
		if(codigo[5] == 'o'):
			codigoDecodificado = codigoDecodificado + ", Oblicuo"
		if(codigo[6] == 's'):
			codigoDecodificado = codigoDecodificado + ", Singular"
		if(codigo[6] == 'p'):
			codigoDecodificado = codigoDecodificado + ", Plural"
		if(codigo[7] == 'p'):
			codigoDecodificado = codigoDecodificado + ", Polite"
			
	#Conjunciones
	if(codigo[0] == 'c'):
		codigoDecodificado = "Conjunción"
		if(codigo[1] == 'c'):
			codigoDecodificado = codigoDecodificado + ", Coordinada"
		if(codigo[1] == 's'):	
			codigoDecodificado = codigoDecodificado + ", Subordinada"
    
	#Interjecciones
	if(codigo[0] == 'i'):
		codigoDecodificado = "Interjección"
	
	#Preposiciones
	if(codigo[0] == 's'):
		codigoDecodificado = "Adposición"
		if(codigo[1] == 'p'):
			codigoDecodificado = codigoDecodificado + ", Preposición"
		if(codigo[2] == 's'):	
			codigoDecodificado = codigoDecodificado + ", Simple"
		if(codigo[2] == 'c'):	
			codigoDecodificado = codigoDecodificado + ", Contraída"
		if(codigo[3] == 'm'):	
			codigoDecodificado = codigoDecodificado + ", Masculino"
		if(codigo[2] == 's'):	
			codigoDecodificado = codigoDecodificado + ", Singular"
	
	#Puntuación
	if(codigo[0] == 'f'):
		codigoDecodificado = "Puntuación"
	
	#Numerales
	if(codigo[0] == 'z'):
		codigoDecodificado = "Cifra"
		if (len(codigo) > 1):
			if(codigo[1] == 'd'):
				codigoDecodificado = "Partitivo"
			if(codigo[1] == 'm'):
				codigoDecodificado = "Moneda"
			if(codigo[1] == 'p'):
				codigoDecodificado = "Porcentaje"
			if(codigo[1] == 'u'):
				codigoDecodificado = "Unidad"
	
	#Fechas y Horas
	if(codigo[0] == 'w'):
		codigoDecodificado = "Fecha/Hora"

	#print(codigoDecodificado)
	
	return codigoDecodificado
"""	
decodificador("AqCmSp")
decodificador("W")
decodificador("Zu")
decodificador("PX2NS0P0")
decodificador("DI0MP0")
decodificador("VSSP1P0")
decodificador("Zd")
"""