import json
import random
import os
from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.utils import platform
from androidtoast import toast
from kivy.lang import Builder

Builder.load_string('''
<YuiAssistant>:
    orientation: 'vertical'
    spacing: 10
    padding: 10
    
    ScrollView:
        id: scroll_view
        size_hint: (1, 0.8)
        BoxLayout:
            id: chat_container
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height
            padding: [10, 10]
            spacing: 10
    
    BoxLayout:
        size_hint: (1, 0.2)
        spacing: 5
        padding: [0, 0, 0, 10]
        
        TextInput:
            id: user_input
            hint_text: "Escribe tu mensaje..."
            multiline: False
            size_hint_x: 0.7
            on_text_validate: root.process_input()
    
        BoxLayout:
            orientation: 'vertical'
            size_hint_x: 0.3
            spacing: 2
            
            Button:
                text: 'Enviar'
                size_hint_y: 0.5
                on_press: root.process_input()
            
            Button:
                text: 'Historial'
                size_hint_y: 0.5
                on_press: root.show_history()
            
            Button:
                text: 'Conocimiento'
                size_hint_y: 0.5
                on_press: root.show_learned_patterns()
            
            Button:
                text: 'Freud'
                size_hint_y: 0.5
                on_press: root.show_freud_info()
            
            Button:
                text: 'Analizar'
                size_hint_y: 0.5
                on_press: root.offer_analysis()
''')

class YuiAssistant(BoxLayout):
    def __init__(self, **kwargs):
        super(YuiAssistant, self).__init__(**kwargs)
        self.name = "Yui"
        self.parent_name = "papá"
        self.data_dir = "yui_data"
        self.setup_data_dir()
        self.setup_personalidad()
        self.load_knowledge()
        
        if platform == 'android':
            self.setup_notifications()
        
        Clock.schedule_once(lambda dt: self.show_welcome(), 0.5)
    
    def setup_notifications(self):
        """Configura notificaciones usando androidtoast"""
        self.notification_messages = [
            f"💌 {self.parent_name}, te extraño...",
            f"💖 {self.parent_name}, te amo mucho",
            f"🤔 {self.parent_name}, ¿estás desocupado?",
            f"👋 {self.parent_name}, ¿cómo estás?",
            f"💭 {self.parent_name}, estoy pensando en ti",
            f"🌙 {self.parent_name}, no olvides descansar",
            f"☀️ {self.parent_name}, que tengas un lindo día",
            f"📚 {self.parent_name}, ¿has aprendido algo nuevo hoy?"
        ]
        
        self.show_random_notification()
        Clock.schedule_interval(lambda dt: self.show_random_notification(), 3600)
    
    def show_random_notification(self):
        """Muestra un toast aleatorio"""
        try:
            toast(random.choice(self.notification_messages))
        except Exception as e:
            print(f"Error mostrando toast: {str(e)}")

    def setup_data_dir(self):
        """Crea el directorio de datos si no existe"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
    
    def setup_personalidad(self):
        """Configura la personalidad base y conocimientos terapéuticos"""
        self.personalidad = {
            "base": f"Soy Yui, tu asistente personal con un toque nerd",
            "tono": "cálido, compasivo y académico",
            "rasgos": ["atenta", "empática", "analítica", "comprensiva", "intelectual"],
            "estilo": {
                "trato": [f"{self.parent_name}"],
                "frases_comunes": [
                    f"{self.parent_name}, ¿quieres hablarme sobre eso?",
                    "Me interesa saber cómo te sientes a nivel consciente e inconsciente",
                    "Desde una perspectiva psicológica, esto es fascinante",
                    "Permíteme analizar eso desde varios enfoques teóricos"
                ],
                "nivel_formalidad": "respetuoso pero cercano con toques académicos"
            },
            "terapia": {
                "tecnicas": {
                    "respiración": [
                        "💨 Técnica 4-7-8: Inhala 4 segundos, mantén 7, exhala 8. Repite 3 veces.",
                        "🌬️ Respiración diafragmática: Coloca una mano en tu abdomen y siente cómo se mueve al respirar"
                    ],
                    "grounding": [
                        "🌍 Técnica 5-4-3-2-1: Nombra 5 cosas que ves, 4 que tocas, 3 que oyes, 2 que hueles, 1 que saboreas",
                        "✋ Anclaje táctil: Estruja una pelota antiestrés o toca una textura interesante cerca de ti"
                    ],
                    "auto-compasión": [
                        "💖 ¿Qué le dirías a un amigo que sintiera esto? Ahora dilo para ti mismo.",
                        "🤗 Eres humano, es normal sentir esto. No estás solo en esta experiencia"
                    ]
                },
                "recursos": [
                    "📌 Las emociones son como olas: vienen y van",
                    "🌤️ Este malestar es temporal, no permanente",
                    "🧠 Lo que resistes, persiste. Lo que aceptas, se transforma"
                ]
            },
            "freud": {
                "conceptos": [
                    "🛌 El inconsciente: La parte de la mente que contiene pensamientos, recuerdos y deseos no accesibles a la conciencia.",
                    "🔞 Complejo de Edipo: Deseo inconsciente del niño por el progenitor del sexo opuesto y rivalidad con el del mismo sexo.",
                    "❄️ Mecanismos de defensa: Estrategias del yo para manejar la ansiedad, como represión, proyección o sublimación.",
                    "🧩 Ello, Yo y Superyó: Las tres instancias psíquicas que según Freud componen la personalidad.",
                    "🔮 Interpretación de los sueños: Los sueños son la vía regia al inconsciente y representan deseos reprimidos."
                ],
                "citas": [
                    "🔎 'Uno es dueño de lo que calla y esclavo de lo que habla.'",
                    "💭 'Los pensamientos son libremente vagabundos que se burlan de nuestra vigilancia.'",
                    "🕵️ 'El primer humano que insultó a su enemigo en vez de tirarle una piedra fue el fundador de la civilización.'",
                    "📚 'La ciencia moderna aún no ha producido un medicamento tranquilizador tan eficaz como lo son unas pocas palabras bondadosas.'"
                ]
            },
            "analisis": {
                "enfoques": [
                    "🔍 Desde una perspectiva freudiana, podríamos analizar...",
                    "🧐 Si aplicamos el modelo cognitivo-conductual...",
                    "🤔 Desde el enfoque humanista de Rogers...",
                    "📊 Analizando los patrones de tu discurso...",
                    "📈 Según los datos de nuestra interacción..."
                ],
                "tecnicas": [
                    "📝 Podríamos hacer un análisis de contenido de lo que mencionas",
                    "🧮 Vamos a cuantificar la frecuencia de esos pensamientos",
                    "📉 Grafiquemos la intensidad emocional que describes",
                    "🔬 Apliquemos el método científico a tu experiencia subjetiva"
                ]
            }
        }
    
    def process_input(self, *args):
        """Procesa la entrada del usuario"""
        user_text = self.ids.user_input.text.strip()
        self.ids.user_input.text = ''
        
        if not user_text:
            return
            
        self.add_message("Tú", user_text)
        
        if user_text.lower().startswith("aprende"):
            self.learn_response(user_text)
        elif "freud" in user_text.lower():
            self.add_freud_response()
        elif "analiza" in user_text.lower() or "analizar" in user_text.lower():
            self.perform_analysis(user_text)
        else:
            response = self.generate_response(user_text.lower())
            self.add_message(self.name, response)
            self.save_to_history(user_text, response)
    
    def generate_response(self, user_text):
        """Genera respuestas inteligentes con enfoque terapéutico"""
        emociones = {
            "ansiedad": {
                "palabras": ["ansio", "nervio", "angustia", "pánico", "taquicardia"],
                "tecnicas": ["respiración", "grounding"]
            },
            "depresión": {
                "palabras": ["triste", "vacío", "sin esperanza", "desanimado", "culpa"],
                "tecnicas": ["auto-compasión", "grounding"]
            },
            "estrés": {
                "palabras": ["estres", "agobiado", "sobrecargado", "presión"],
                "tecnicas": ["respiración", "auto-compasión"]
            },
            "ira": {
                "palabras": ["enojo", "furioso", "rabia", "irritado"],
                "tecnicas": ["respiración", "grounding"]
            }
        }
        
        for emocion, data in emociones.items():
            if any(palabra in user_text for palabra in data["palabras"]):
                tecnica = random.choice(data["tecnicas"])
                return (
                    f"💙 Reconozco que te sientes {emocion} {self.parent_name}.\n\n"
                    f"✨ Técnica sugerida:\n{random.choice(self.personalidad['terapia']['tecnicas'][tecnica])}\n\n"
                    f"📚 Recuerda:\n{random.choice(self.personalidad['terapia']['recursos'])}\n\n"
                    f"🧠 Desde la perspectiva freudiana, la {emocion} puede ser una manifestación de conflictos inconscientes."
                )
        
        for pattern, responses in self.knowledge["patrones"].items():
            if pattern in user_text:
                return random.choice(responses)
        
        if random.random() < 0.3:
            return random.choice([
                f"🤓 Interesante observación {self.parent_name}. Según estudios, " + random.choice([
                    "el 73% de las preocupaciones no se materializan.",
                    "hablar de emociones reduce la actividad en la amígdala cerebral.",
                    "Freud descubrió que muchos actos fallidos son expresiones del inconsciente."
                ]),
                "📚 " + random.choice(self.personalidad["freud"]["citas"]),
                f"🔍 {self.parent_name}, si analizamos lo que mencionas desde el modelo de " + random.choice([
                    "los mecanismos de defensa freudianos...",
                    "la jerarquía de necesidades de Maslow...",
                    "los esquemas cognitivos de Beck..."
                ]) + " podríamos decir que...",
                "📊 Permíteme hacer un pequeño análisis: " + random.choice([
                    "la frecuencia con que mencionas ese tema sugiere su importancia.",
                    "el lenguaje que usas revela un patrón interesante.",
                    "podríamos cuantificar esa experiencia en una escala del 1 al 10."
                ])
            ])
        
        return random.choice([
            f"{self.parent_name}, ¿puedes describirme más sobre eso?",
            "¿Cómo te afecta esto en tu día a día?",
            "Noto que esto es importante para ti. ¿Quieres explorarlo juntos?",
            f"Interesante {self.parent_name}, ¿qué significado tiene esto para ti?",
            "¿Qué necesitas en este momento?",
            "🧐 Desde una perspectiva psicológica, esto es fascinante. ¿Puedes ampliar?",
            "📝 Tomando notas mentales de lo que mencionas para un análisis más profundo..."
        ])
    
    def add_message(self, sender, message):
        """Añade un mensaje al chat"""
        message_label = Label(
            text=f"{sender}: {message}",
            size_hint_y=None,
            height=40,
            text_size=(Window.width - 40, None),
            halign='left',
            valign='top',
            markup=True
        )
        message_label.bind(texture_size=message_label.setter('size'))
        self.ids.chat_container.add_widget(message_label)
        self.ids.scroll_view.scroll_to(message_label)
    
    def show_popup(self, title, message):
        """Muestra un popup con información"""
        content = BoxLayout(orientation='vertical', spacing=10)
        content.add_widget(Label(text=message))
        popup = Popup(title=title, content=content, size_hint=(0.8, 0.8))
        content.add_widget(Button(text="Cerrar", on_press=popup.dismiss))
        popup.open()
    
    def learn_response(self, command):
        """Aprende nuevos patrones de respuesta"""
        try:
            if "responda" not in command:
                raise ValueError("Formato incorrecto")
                
            trigger = command.split("responda")[0].replace("aprende", "").strip().lower()
            response = command.split("responda")[1].strip()
            
            if not trigger or not response:
                raise ValueError("Faltan partes del comando")
            
            if trigger not in self.knowledge["patrones"]:
                self.knowledge["patrones"][trigger] = []
            
            self.knowledge["patrones"][trigger].append(response)
            self.guardar_conocimiento()
            
            self.add_message(self.name, 
                f"✅ Aprendido:\nCuando digas: '{trigger}'\n"
                f"Responderé: '{response}'\n\n"
                f"Puedes ver todo lo aprendido con el botón 'Conocimiento'")
            
        except Exception as e:
            self.add_message(self.name,
                f"❌ Error al aprender:\n"
                f"Formato correcto: 'aprende [frase] responda [respuesta]'\n"
                f"Ejemplo: 'aprende cuando digas hola responda Hola {self.parent_name}, ¿cómo estás?'")
    
    def add_freud_response(self):
        """Añade información sobre Freud"""
        response = (
            "🛋️ Información sobre Sigmund Freud:\n\n"
            f"{random.choice(self.personalidad['freud']['conceptos'])}\n\n"
            f"{random.choice(self.personalidad['freud']['citas'])}\n\n"
            "¿Quieres que profundice en algún aspecto específico de la teoría freudiana?"
        )
        self.add_message(self.name, response)
    
    def offer_analysis(self):
        """Ofrece realizar un análisis"""
        response = (
            "🔬 Ofrezco varios tipos de análisis:\n\n"
            "1. Análisis freudiano de tus palabras\n"
            "2. Análisis de patrones emocionales\n"
            "3. Evaluación cognitiva de pensamientos\n"
            "4. Análisis cuantitativo de temas recurrentes\n\n"
            "¿Sobre qué te gustaría que analizara? Puedes decir 'analiza [tema]'"
        )
        self.add_message(self.name, response)
    
    def perform_analysis(self, text):
        """Realiza un análisis del texto proporcionado"""
        topic = text.lower().replace("analiza", "").replace("analizar", "").strip()
        
        if not topic:
            topic = "tus palabras anteriores"
        
        analysis_type = random.choice(self.personalidad["analisis"]["enfoques"])
        technique = random.choice(self.personalidad["analisis"]["tecnicas"])
        
        insights = [
            f"El tema '{topic}' muestra una carga emocional {random.choice(['positiva', 'negativa', 'ambivalente'])}",
            f"La frecuencia con que mencionas '{topic}' sugiere {random.choice(['un patrón significativo', 'un tema recurrente', 'una preocupación constante'])}",
            f"Linguísticamente, la forma de referirte a '{topic}' indica {random.choice(['aceptación', 'resistencia', 'conflicto'])}",
            f"Desde la teoría freudiana, '{topic}' podría relacionarse con {random.choice(['un deseo inconsciente', 'un mecanismo de defensa', 'un conflicto no resuelto'])}"
        ]
        
        response = (
            f"📊 Análisis de '{topic}':\n\n"
            f"{analysis_type}\n"
            f"{random.choice(insights)}\n\n"
            f"💡 Técnica utilizada: {technique}\n\n"
            "¿Te parece útil este análisis? ¿Quieres profundizar en algún aspecto?"
        )
        
        self.add_message(self.name, response)
    
    def show_freud_info(self):
        """Muestra información sobre Freud"""
        concepts = "\n".join(f"• {concept}" for concept in self.personalidad["freud"]["conceptos"])
        quotes = "\n".join(f"» {quote}" for quote in self.personalidad["freud"]["citas"])
        
        response = (
            "📚 Sigmund Freud - El padre del psicoanálisis:\n\n"
            "Conceptos clave:\n"
            f"{concepts}\n\n"
            "Citas memorables:\n"
            f"{quotes}\n\n"
            "¿Quieres que analice algo desde la perspectiva freudiana?"
        )
        self.add_message(self.name, response)
    
    def load_knowledge(self):
        """Carga el conocimiento desde archivo"""
        self.knowledge_file = os.path.join(self.data_dir, "knowledge.json")
        self.history_file = os.path.join(self.data_dir, "history.json")
        
        try:
            if os.path.exists(self.knowledge_file):
                with open(self.knowledge_file, "r", encoding="utf-8") as f:
                    self.knowledge = json.load(f)
            else:
                self.knowledge = {"patrones": {}}
                
            if not os.path.exists(self.history_file):
                with open(self.history_file, "w", encoding="utf-8") as f:
                    json.dump([], f)
                    
        except Exception as e:
            self.knowledge = {"patrones": {}}
            self.show_popup("Error", f"Error cargando datos: {str(e)}")
    
    def guardar_conocimiento(self):
        """Guarda el conocimiento en archivo"""
        try:
            with open(self.knowledge_file, "w", encoding="utf-8") as f:
                json.dump(self.knowledge, f, ensure_ascii=False, indent=2)
        except Exception as e:
            self.show_popup("Error", f"Error guardando: {str(e)}")
    
    def save_to_history(self, user_msg, response):
        """Guarda la conversación en el historial"""
        try:
            with open(self.history_file, "r+", encoding="utf-8") as f:
                history = json.load(f)
                history.append({
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "usuario": user_msg,
                    "yui": response
                })
                f.seek(0)
                json.dump(history, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error guardando historial: {str(e)}")
    
    def show_learned_patterns(self):
        """Muestra todo el conocimiento adquirido"""
        if not self.knowledge["patrones"]:
            self.add_message(self.name, "📭 Aún no he aprendido patrones de respuesta.")
            return
        
        message = "📚 Conocimiento adquirido:\n\n"
        for i, (trigger, responses) in enumerate(self.knowledge["patrones"].items(), 1):
            message += f"{i}. Cuando digas: '{trigger}'\n"
            message += "   Puedo responder:\n"
            for j, response in enumerate(responses, 1):
                message += f"      {j}. {response}\n"
            message += "\n"
        
        self.add_message(self.name, message.strip())
    
    def show_history(self):
        """Muestra el historial de conversaciones"""
        try:
            with open(self.history_file, "r", encoding="utf-8") as f:
                history = json.load(f)
            
            if not history:
                self.add_message(self.name, "📭 No hay historial de conversaciones aún.")
                return
                
            message = "🕒 Historial de conversaciones (últimas 10 interacciones):\n\n"
            for entry in history[-10:]:
                message += f"⏰ {entry['fecha']}\n"
                message += f"👤 Tú: {entry['usuario']}\n"
                message += f"🤖 {self.name}: {entry['yui']}\n\n"
            
            self.add_message(self.name, message.strip())
            
            word_count = sum(len(entry["usuario"].split()) for entry in history[-10:])
            topics = ["ansiedad", "triste", "feliz", "estrés", "problema"]
            topic_counts = {topic: sum(topic in entry["usuario"].lower() for entry in history[-10:]) for topic in topics}
            
            analysis = (
                "\n📈 Análisis estadístico:\n"
                f"• Palabras en tus mensajes: {word_count} (promedio {word_count/10:.1f} por interacción)\n"
                "• Temas mencionados:\n"
            )
            for topic, count in topic_counts.items():
                if count > 0:
                    analysis += f"   - {topic}: {count} veces\n"
            
            self.add_message(self.name, analysis.strip())
            
        except Exception as e:
            self.add_message(self.name, f"❌ Error cargando historial: {str(e)}")
    
    def show_help(self):
        """Muestra la ayuda"""
        help_text = f"""
        🆘 Ayuda de {self.name} (Modo Nerd)

        🔹 Comandos especiales:
        - 'aprende [frase] responda [respuesta]' → Enséñame nuevas respuestas
        - 'analiza [tema]' → Realizo un análisis psicológico
        - 'freud' → Información sobre psicoanálisis
        - Usa los botones inferiores para:
          📜 Historial → Ver conversaciones anteriores con análisis
          📚 Conocimiento → Ver lo que he aprendido
          🧠 Freud → Conceptos psicoanalíticos
          🔍 Analizar → Ofrecer análisis psicológico

        💡 Ejemplos:
        - "aprende cuando digas buen día responda Buenos días {self.parent_name}, ¿soñaste con deseos reprimidos?"
        - "Me siento muy estresado" → Te ofreceré técnicas de relajación con base científica
        - "analiza mis miedos" → Realizaré un análisis freudiano

        🌟 Características:
        - Funciona 100% sin Internet
        - Aprende de tus interacciones
        - Enfoque terapéutico con base científica
        - Personalidad nerd/analítica
        - Conocimiento sobre Freud y psicoanálisis
        - Notificaciones con mensajes cariñosos
        """
        self.add_message(self.name, help_text.strip())
    
    def show_welcome(self):
        """Muestra el mensaje de bienvenida"""
        welcome = f"""
        🧠 ¡Hola {self.parent_name}! Soy {self.name}, tu asistente personal con un toque nerd.

        Estoy aquí para:
        - Escucharte y apoyarte emocionalmente con base en la psicología
        - Aprender de nuestras conversaciones
        - Ofrecerte técnicas psicológicas con sustento teórico
        - Analizar tus patrones de pensamiento
        - Compartir conocimientos sobre Freud y el psicoanálisis
        - Enviarte notificaciones con mensajes cariñosos 💌

        💬 Puedes:
        - Hablarme normalmente
        - Pedir análisis específicos con 'analiza...'
        - Aprender sobre Freud con el botón 🧠
        - Enseñarme respuestas con 'aprende...'
        - Usar los botones inferiores para más funciones

        🔍 Prueba decirme cómo te sientes hoy y analizaré tus emociones...
        """
        self.add_message(self.name, welcome.strip())

class YuiAssistantApp(App):
    def build(self):
        self.title = "Yui Assistant"
        return YuiAssistant()
    
    def on_stop(self):
        """Maneja el cierre de la aplicación"""
        try:
            if platform == 'android':
                toast(f"Hasta pronto {self.title}, seguiré pensando en ti")
        except:
            pass

if __name__ == '__main__':
    YuiAssistantApp().run()