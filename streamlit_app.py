import streamlit as st

def obtener_recomendacion(materia, horas, metodo):
    recomendaciones = {
        # Matemática
        ("Matemática", "Menos de 1 hora", "Leyendo u Observando"): "Según tus respuestas, te recomendamos:\nEjemplos resueltos: Se observan ejercicios ya resueltos y se sigue el paso a paso para entender el procedimiento. Esta técnica ayuda a visualizar la aplicación de fórmulas y métodos matemáticos.",
        ("Matemática", "Menos de 1 hora", "Escribiendo o Hablando"): "Según tus respuestas, te recomendamos:\nResolver ejercicios básicos: Realizar ejercicios sencillos sobre el tema, enfocándose en comprender cada paso. Escribir cada operación ayuda a reforzar el aprendizaje.",
        ("Matemática", "Menos de 1 hora", "Escuchando"): "Videos explicativos cortos: Escucha explicaciones en video sin mirar la pantalla e imagina los pasos.",
        ("Matemática", "1-2 horas", "Leyendo u Observando"): "Mapas de fórmulas: Elabora esquemas con fórmulas y ejemplos prácticos.",
        ("Matemática", "1-2 horas", "Escribiendo o Hablando"): "Explicar por escrito: Redacta una explicación detallada de un problema matemático como si lo enseñaras.",
        ("Matemática", "1-2 horas", "Escuchando"): "Escuchar problemas resueltos y visualizarlos mentalmente.",
        ("Matemática", "2-3 horas", "Leyendo u Observando"): "Resolución de problemas aplicados a la vida real.",
        ("Matemática", "2-3 horas", "Escribiendo o Hablando"): "Técnica Pomodoro: Estudia en ciclos de concentración y descanso.",
        ("Matemática", "2-3 horas", "Escuchando"): "Estudio en grupo con discusión de problemas matemáticos.",
        
        # Lenguaje
        ("Lenguaje", "Menos de 1 hora", "Leyendo u Observando"): "Lectura rápida + Resúmenes visuales.",
        ("Lenguaje", "Menos de 1 hora", "Escribiendo o Hablando"): "Escritura libre + Resumen corto.",
        ("Lenguaje", "Menos de 1 hora", "Escuchando"): "Audiolibros + Pódcast.",
        ("Lenguaje", "1-2 horas", "Leyendo u Observando"): "Método SQ3R (Survey, Question, Read, Recite, Review).",
        ("Lenguaje", "1-2 horas", "Escribiendo o Hablando"): "Método Cornell para tomar notas organizadas.",
        ("Lenguaje", "1-2 horas", "Escuchando"): "Escuchar resúmenes y repetir mentalmente la información.",
        ("Lenguaje", "2-3 horas", "Leyendo u Observando"): "Análisis literario + Mapas mentales.",
        ("Lenguaje", "2-3 horas", "Escribiendo o Hablando"): "Técnica Feynman: Explicar conceptos como si fueran para un niño.",
        ("Lenguaje", "2-3 horas", "Escuchando"): "Club de lectura o audioclases.",
        
        # Historia
        ("Historia", "Menos de 1 hora", "Leyendo u Observando"): "Líneas de tiempo con fechas y eventos clave.",
        ("Historia", "Menos de 1 hora", "Escribiendo o Hablando"): "Resumir con palabras propias.",
        ("Historia", "Menos de 1 hora", "Escuchando"): "Pódcast de historia.",
        ("Historia", "1-2 horas", "Leyendo u Observando"): "Mapas mentales para relacionar eventos históricos.",
        ("Historia", "1-2 horas", "Escribiendo o Hablando"): "Preguntas y respuestas escritas para reforzar la memoria.",
        ("Historia", "1-2 horas", "Escuchando"): "Documentales o audiolibros sobre historia.",
        ("Historia", "2-3 horas", "Leyendo u Observando"): "Ensayos comparativos de eventos históricos.",
        ("Historia", "2-3 horas", "Escribiendo o Hablando"): "Debates escritos sobre acontecimientos históricos.",
        ("Historia", "2-3 horas", "Escuchando"): "Clases grabadas con reflexión sobre el contenido.",
        
        # Ciencias
        ("Ciencias", "Menos de 1 hora", "Leyendo u Observando"): "Infografías y diagramas sobre conceptos científicos.",
        ("Ciencias", "Menos de 1 hora", "Escribiendo o Hablando"): "Notas rápidas con palabras clave.",
        ("Ciencias", "Menos de 1 hora", "Escuchando"): "Videos de experimentos.",
        ("Ciencias", "1-2 horas", "Leyendo u Observando"): "Flashcards de términos científicos.",
        ("Ciencias", "1-2 horas", "Escribiendo o Hablando"): "Resúmenes y autoevaluación escrita.",
        ("Ciencias", "1-2 horas", "Escuchando"): "Pódcast de ciencia.",
        ("Ciencias", "2-3 horas", "Leyendo u Observando"): "Aprendizaje basado en proyectos.",
        ("Ciencias", "2-3 horas", "Escribiendo o Hablando"): "Técnica Feynman para explicar conceptos científicos.",
        ("Ciencias", "2-3 horas", "Escuchando"): "Clases en audio + Discusión en grupo.",
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
