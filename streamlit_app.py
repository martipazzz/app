import streamlit as st

def obtener_recomendacion(materia, horas, metodo):
    recomendaciones = {
        # Matemática
        ("Matemática", "Menos de 1 hora", "Leyendo u Observando"): "Según tus respuestas, te recomendamos:\nEjemplos resueltos: Se observan ejercicios ya resueltos y se sigue el paso a paso para entender el procedimiento. Esta técnica ayuda a visualizar la aplicación de fórmulas y métodos matemáticos.",
        ("Matemática", "Menos de 1 hora", "Escribiendo o Hablando"): "Según tus respuestas, te recomendamos:\nResolver ejercicios básicos: Realizar ejercicios sencillos sobre el tema, enfocándose en comprender cada paso. Escribir cada operación ayuda a reforzar el aprendizaje.",
        ("Matemática", "Menos de 1 hora", "Escuchando"): "Según tus respuestas, te recomendamos:\nVideos explicativos cortos: Escuchar explicaciones en video sin mirar la pantalla y tratar de imaginar los pasos en la mente. Luego, intentar resolver un problema similar basándose en lo que se ha escuchado.",
        ("Matemática", "1-2 horas", "Leyendo u Observando"): "Según tus respuestas, te recomendamos:\nMapas de fórmulas: Se elaboran esquemas con las fórmulas más importantes y sus aplicaciones. Relacionarlas con ejemplos facilita su memorización y uso en ejercicios.",
        ("Matemática", "1-2 horas", "Escribiendo o Hablando"): "Según tus respuestas, te recomendamos:\nExplicar por escrito: Escribir una explicación detallada sobre un problema matemático difícil, describiendo cada paso como si se estuviera enseñando a otra persona. Esto ayuda a estructurar el pensamiento lógico.",
        ("Matemática", "1-2 horas", "Escuchando"): "Según tus respuestas, te recomendamos:\nEscuchar problemas resueltos y visualizar mentalmente: Escuchar la resolución de un problema matemático sin ver la pantalla e intentar imaginar los pasos en la mente. Luego, comprobar si la solución mental coincide con la real.",
        ("Matemática", "2-3 horas", "Leyendo u Observando"): "Según tus respuestas, te recomendamos:\nResolución de problemas aplicados: Trabajar en ejercicios que tengan aplicaciones en la vida real, como cálculos financieros o mediciones. Relacionar los problemas con situaciones prácticas mejora la comprensión.",
        ("Matemática", "2-3 horas", "Escribiendo o Hablando"): "Según tus respuestas, te recomendamos:\nTécnica Pomodoro: Se estudia en ciclos de 25 minutos de concentración, seguidos de 5 minutos de descanso. Después de cuatro ciclos, se toma un descanso más largo. Este método mejora la productividad y el enfoque.",
        ("Matemática", "2-3 horas", "Escuchando"): "ESegún tus respuestas, te recomendamos:\nEstudio en grupo con discusión: Escuchar a otras personas explicando problemas matemáticos y participar en discusiones sobre las soluciones. Esto permite ver diferentes enfoques y aclarar dudas.",
        
        # Lenguaje
        ("Lenguaje", "Menos de 1 hora", "Leyendo u Observando"): "Según tus respuestas, te recomendamos:\nLectura rápida + Resúmenes visuales: Consiste en leer rápidamente un texto sin detenerse en cada palabra, buscando captar la idea principal. Luego, se crean mapas conceptuales, esquemas o dibujos que representen lo más importante del texto. Esto ayuda a procesar la información sin perder tiempo en detalles innecesarios.",
        ("Lenguaje", "Menos de 1 hora", "Escribiendo o Hablando"): "Según tus respuestas, te recomendamos:\nEscritura libre + Resumen corto: Escribir lo que se recuerda sin mirar el texto, tratando de explicarlo con palabras propias. Luego, se hace un pequeño resumen con las ideas clave. Esta técnica fortalece la memoria y mejora la comprensión al obligar al cerebro a estructurar la información.",
        ("Lenguaje", "Menos de 1 hora", "Escuchando"): "Según tus respuestas, te recomendamos:\nAudiolibros + Pódcast: Escuchar un audiolibro o un pódcast sobre el tema mientras se realiza otra actividad como caminar o descansar. Para reforzar la comprensión, se puede intentar resumir en la mente lo más importante de lo escuchado. Usar una velocidad de reproducción más rápida ayuda a mantener la concentración.",
        ("Lenguaje", "1-2 horas", "Leyendo u Observando"): "Según tus respuestas, te recomendamos:\nMétodo SQ3R (Survey, Question, Read, Recite, Review): Se basa en cinco pasos: 1) Explorar el texto por encima para captar la idea general. 2) Formular preguntas sobre el contenido. 3) Leer detenidamente en busca de respuestas. 4) Repetir en voz alta o escribir lo más importante. 5) Revisar y repasar lo aprendido. Este método mejora la comprensión y la retención a largo plazo.",
        ("Lenguaje", "1-2 horas", "Escribiendo o Hablando"): "Según tus respuestas, te recomendamos:\nMétodo Cornell: Consiste en dividir una hoja en tres secciones: una columna estrecha a la izquierda para palabras clave, una columna más ancha a la derecha para notas detalladas y un espacio en la parte inferior para un resumen general. Esta estructura facilita la organización de la información y el repaso posterior.",
        ("Lenguaje", "1-2 horas", "Escuchando"): "Según tus respuestas, te recomendamos:\nEscuchar resúmenes y repetir mentalmente: Buscar resúmenes en formato de audio y escucharlos atentamente. Luego, tratar de repetir mentalmente las ideas clave o explicarlas en voz alta. Esto refuerza la comprensión auditiva y ayuda a fijar la información en la memoria.",
        ("Lenguaje", "2-3 horas", "Leyendo u Observando"): "Según tus respuestas, te recomendamos:\nAnálisis literario + Mapas mentales: Consiste en leer un texto con profundidad, analizando personajes, ideas principales y mensajes del autor. Luego, se usa un mapa mental para conectar conceptos, estableciendo relaciones entre ellos. Esto facilita la comprensión y ayuda a recordar los detalles importantes.",
        ("Lenguaje", "2-3 horas", "Escribiendo o Hablando"): "Según tus respuestas, te recomendamos:\nTécnica Feynman (escribir para entender): Se elige un concepto y se escribe sobre él como si se estuviera explicando a un niño. Se identifican las partes confusas y se vuelve a escribir de forma más clara. Esto ayuda a detectar lagunas en el conocimiento y a mejorar la comprensión.",
        ("Lenguaje", "2-3 horas", "Escuchando"): "Según tus respuestas, te recomendamos:\nClub de lectura o audioclases: Escuchar audioclases sobre el tema o participar en un club de lectura en el que se discuten libros y textos. La interacción con otras personas permite reflexionar sobre lo aprendido y reforzar la comprensión.",
        
        # Historia
        ("Historia", "Menos de 1 hora", "Leyendo u Observando"): "Según tus respuestas, te recomendamos:\nLíneas de tiempo: Se crean esquemas visuales con fechas y eventos clave para entender la secuencia de los acontecimientos históricos.",
        ("Historia", "Menos de 1 hora", "Escribiendo o Hablando"): "Según tus respuestas, te recomendamos:\nResumir con palabras propias: Escribir un resumen breve sin copiar del texto, destacando los eventos más importantes. Esto ayuda a fijar la información en la memoria.",
        ("Historia", "Menos de 1 hora", "Escuchando"): "Según tus respuestas, te recomendamos:\nPódcast de historia: Escuchar narraciones de eventos históricos y tratar de imaginar la escena en la mente. Luego, repasar mentalmente los datos más relevantes.",
        ("Historia", "1-2 horas", "Leyendo u Observando"): "Según tus respuestas, te recomendamos:\nMapas mentales: Relacionar eventos, personajes y causas en un diagrama que permita visualizar cómo se conectan entre sí. Esto ayuda a recordar información con mayor facilidad.",
        ("Historia", "1-2 horas", "Escribiendo o Hablando"): "Según tus respuestas, te recomendamos:\nPreguntas y respuestas escritas: Formular preguntas sobre el tema y tratar de responderlas sin ver el material. Escribir las respuestas fortalece la memoria. ",
        ("Historia", "1-2 horas", "Escuchando"): "Según tus respuestas, te recomendamos:\nDocumentales o audiolibros: Escuchar una narración histórica en audio y luego contar en voz alta lo más importante con palabras propias. ",
        ("Historia", "2-3 horas", "Leyendo u Observando"): "Según tus respuestas, te recomendamos:\nEnsayos y fichas de estudio: Escribir un ensayo comparando distintos eventos históricos y utilizar fichas para recordar datos clave.",
        ("Historia", "2-3 horas", "Escribiendo o Hablando"): "Según tus respuestas, te recomendamos:\nDebates escritos: Escribir sobre un evento como si se estuviera participando en un debate, argumentando diferentes puntos de vista. ",
        ("Historia", "2-3 horas", "Escuchando"): "Según tus respuestas, te recomendamos:\nClases grabadas con reflexión: Escuchar una clase de historia y luego escribir un breve resumen de lo aprendido. ",
        
        # Ciencias
        ("Ciencias", "Menos de 1 hora", "Leyendo u Observando"): "Según tus respuestas, te recomendamos:\nInfografías y diagramas: Observar imágenes explicativas, esquemas y gráficos para comprender conceptos científicos de forma visual. Esto permite captar información rápidamente sin necesidad de leer demasiado.",
        ("Ciencias", "Menos de 1 hora", "Escribiendo o Hablando"): "Según tus respuestas, te recomendamos:\nNotas rápidas con palabras clave: Escribir términos importantes y definiciones cortas para repasarlas varias veces. Subrayar ideas clave y hacer pequeñas explicaciones con ejemplos.",
        ("Ciencias", "Menos de 1 hora", "Escuchando"): "Según tus respuestas, te recomendamos:\nVideos de experimentos: Escuchar la explicación de un experimento sin ver la pantalla e intentar imaginar el proceso. Luego, reflexionar sobre cómo se aplican los conceptos en la vida real.",
        ("Ciencias", "1-2 horas", "Leyendo u Observando"): "Flashcards de términos científicos.",
        ("Ciencias", "1-2 horas", "Escribiendo o Hablando"): "Según tus respuestas, te recomendamos:\nResúmenes y autoevaluación escrita: Escribir resúmenes detallados de cada tema, resaltando fórmulas o teorías importantes. Luego, elaborar preguntas sobre el contenido y responderlas sin mirar el material.",
        ("Ciencias", "1-2 horas", "Escuchando"): "Según tus respuestas, te recomendamos:\nPódcast de ciencia: Escuchar expertos hablando sobre el tema y luego intentar explicarlo con palabras propias. Este método mejora la comprensión auditiva y ayuda a consolidar la información.",
        ("Ciencias", "2-3 horas", "Leyendo u Observando"): "Según tus respuestas, te recomendamos:\nAprendizaje basado en proyectos: Realizar un experimento en casa o investigar un problema científico aplicando el método científico. Se formula una hipótesis, se buscan datos y se documentan los resultados. Esto permite entender conceptos de manera práctica y significativa.",
        ("Ciencias", "2-3 horas", "Escribiendo o Hablando"): "Según tus respuestas, te recomendamos:\nTécnica Feynman (explicar para entender): Elegir un tema científico y escribir sobre él como si se estuviera explicando a alguien sin conocimientos previos. Si hay partes difíciles de explicar, volver a estudiar y simplificar la información. Esto ayuda a detectar lagunas en el conocimiento y a reforzar la comprensión.",
        ("Ciencias", "2-3 horas", "Escuchando"): "Según tus respuestas, te recomendamos:\nClases en audio + Discusión en grupo: Escuchar clases grabadas de profesores o pódcast científicos y luego discutir con compañeros o con un tutor sobre los temas abordados. Explicar lo aprendido en voz alta ayuda a fijar el conocimiento y aclarar dudas.",
    }
    return recomendaciones.get((materia, horas, metodo), "No tenemos una recomendación específica, pero intenta combinar diferentes métodos para mejorar tu estudio.")

def main():
    st.title("Recomendador de Métodos de Estudio 📚")
    
    nombre = st.text_input("Hola, ¿Cuál es tu nombre?")
    
    if nombre:
        st.write(f"¡Bienvenid@ {nombre}! 🎉")
        st.write("Selecciona las opciones para recibir una recomendación de estudio.")

        curso = st.selectbox("¿En qué curso te encuentras?", 
                             ["7° y 8° Básico", "1° y 2° Medio", "3° y 4° Medio"])

        materia = st.selectbox("¿Qué materia quieres estudiar hoy?", 
                               ["Matemática", "Lenguaje", "Historia", "Ciencias"])

        horas = st.selectbox("¿Cuántas horas de estudio puedes dedicarle?", 
                             ["Menos de 1 hora", "1-2 horas", "2-3 horas"])

        metodo = st.selectbox("¿Cómo se te hace más sencillo aprender?", 
                              ["Leyendo u Observando", "Escribiendo o Hablando", "Escuchando"])

        if st.button("Obtener recomendación"):
            recomendacion = obtener_recomendacion(materia, horas, metodo)
            st.subheader("Recomendación:")
            st.write(recomendacion)

if __name__ == "__main__":
    main()
