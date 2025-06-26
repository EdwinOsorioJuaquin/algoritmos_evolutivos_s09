import random
import tkinter as tk
from tkinter import ttk, messagebox

class TorneoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Algoritmo de Selección por Torneo Genético")
        self.root.geometry("900x650")
        self.root.configure(bg='#f0f8ff')
        
        # Configurar paleta de colores
        self.colores = {
            'fondo': '#f0f8ff',
            'fondo_titulo': '#4682b4',
            'texto_titulo': 'white',
            'fondo_frame': '#e6f2ff',
            'participante': '#5f9ea0',
            'ganador': '#2e8b57',
            'perdedor': '#cd5c5c',
            'boton': '#6495ed',
            'boton_hover': '#4169e1',
            'texto_boton': 'white',
            'vs_color': '#9932cc'
        }
        
        # Datos iniciales
        self.individuos = {
            "A": 85,
            "B": 45,
            "C": 70,
            "D": 20,
            "E": 60,
            "F": 90
        }
        
        self.ganadores = []
        self.current_torneo = 0
        
        # Configurar estilo
        self.setup_style()
        
        # Crear interfaz
        self.create_widgets()
    
    def setup_style(self):
        """Configura los estilos visuales con colores"""
        style = ttk.Style()
        
        # Configurar tema
        style.theme_use('clam')
        
        # Estilos personalizados
        style.configure('Titulo.TLabel', 
                      font=('Helvetica', 18, 'bold'),
                      background=self.colores['fondo_titulo'],
                      foreground=self.colores['texto_titulo'],
                      padding=10)
        
        style.configure('Subtitulo.TLabel', 
                      font=('Helvetica', 12, 'italic'),
                      background=self.colores['fondo'],
                      foreground='#333333')
        
        style.configure('Participante.TLabel', 
                      font=('Helvetica', 11, 'bold'),
                      background=self.colores['fondo_frame'],
                      foreground=self.colores['participante'])
        
        style.configure('Ganador.TLabel', 
                      font=('Helvetica', 12, 'bold'),
                      background=self.colores['fondo_frame'],
                      foreground=self.colores['ganador'])
        
        style.configure('Perdedor.TLabel', 
                      font=('Helvetica', 11),
                      background=self.colores['fondo_frame'],
                      foreground=self.colores['perdedor'])
        
        style.configure('TButton', 
                      font=('Helvetica', 10, 'bold'),
                      background=self.colores['boton'],
                      foreground=self.colores['texto_boton'],
                      borderwidth=1)
        
        style.map('TButton',
                background=[('active', self.colores['boton_hover'])])
        
        style.configure('TFrame', background=self.colores['fondo'])
        style.configure('TLabelframe', background=self.colores['fondo_frame'], borderwidth=2)
        style.configure('TLabelframe.Label', background=self.colores['fondo_frame'])
    
    def create_widgets(self):
        """Crea todos los elementos de la interfaz"""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título con color
        titulo_frame = ttk.Frame(main_frame, style='Titulo.TFrame')
        titulo_frame.grid(row=0, column=0, columnspan=3, sticky='ew', pady=(0, 15))
        
        ttk.Label(titulo_frame, 
                 text="🏆 SELECCIÓN POR TORNEO GENÉTICO 🏆", 
                 style='Titulo.TLabel').pack(fill=tk.X)
        
        # Panel de configuración
        config_frame = ttk.LabelFrame(main_frame, text="⚙️ Configuración", padding=15)
        config_frame.grid(row=1, column=0, sticky='nsew', padx=5, pady=5, ipadx=10, ipady=5)
        
        ttk.Label(config_frame, 
                 text="Número de torneos:",
                 style='Participante.TLabel').grid(row=0, column=0, padx=5)
        
        self.num_torneos = tk.IntVar(value=3)
        ttk.Spinbox(config_frame, 
                   from_=1, to=10, 
                   textvariable=self.num_torneos, 
                   width=5,
                   font=('Helvetica', 10)).grid(row=0, column=1, padx=5)
        
        start_btn = ttk.Button(config_frame, 
                             text="🎯 Iniciar Torneos", 
                             command=self.iniciar_torneos)
        start_btn.grid(row=0, column=2, padx=10)
        
        # Panel de participantes
        part_frame = ttk.LabelFrame(main_frame, text="👥 Participantes", padding=15)
        part_frame.grid(row=2, column=0, sticky='nsew', padx=5, pady=5, ipadx=10, ipady=5)
        
        # Crear una tabla visual para los participantes
        ttk.Label(part_frame, 
                 text="Individuo", 
                 style='Participante.TLabel').grid(row=0, column=0, padx=10, pady=2)
        ttk.Label(part_frame, 
                 text="Fitness", 
                 style='Participante.TLabel').grid(row=0, column=1, padx=10, pady=2)
        
        row = 1
        for ind, fit in self.individuos.items():
            ttk.Label(part_frame, 
                     text=f"{ind}", 
                     style='Participante.TLabel').grid(row=row, column=0, sticky='w', padx=10)
            ttk.Label(part_frame, 
                     text=f"{fit}", 
                     style='Participante.TLabel').grid(row=row, column=1, sticky='w', padx=10)
            row += 1
        
        # Panel del torneo actual
        self.torneo_frame = ttk.LabelFrame(main_frame, text="⚔️ Torneo Actual", padding=20)
        self.torneo_frame.grid(row=1, column=1, rowspan=2, sticky='nsew', padx=5, pady=5, ipadx=10, ipady=5)
        
        self.torneo_label = ttk.Label(self.torneo_frame, 
                                    text="Presione 'Iniciar Torneos' para comenzar", 
                                    style='Subtitulo.TLabel')
        self.torneo_label.pack(pady=10)
        
        # Contenedor para los participantes del torneo
        self.participantes_frame = ttk.Frame(self.torneo_frame)
        self.participantes_frame.pack(pady=10)
        
        self.part1_frame = ttk.Frame(self.participantes_frame)
        self.part1_frame.pack(side=tk.LEFT, padx=20)
        
        self.part1_label = ttk.Label(self.part1_frame, text="", style='Participante.TLabel')
        self.part1_label.pack()
        
        self.vs_label = ttk.Label(self.participantes_frame, 
                                 text="", 
                                 font=('Helvetica', 24, 'bold'),
                                 foreground=self.colores['vs_color'])
        self.vs_label.pack(side=tk.LEFT, padx=10)
        
        self.part2_frame = ttk.Frame(self.participantes_frame)
        self.part2_frame.pack(side=tk.LEFT, padx=20)
        
        self.part2_label = ttk.Label(self.part2_frame, text="", style='Participante.TLabel')
        self.part2_label.pack()
        
        # Separador
        ttk.Separator(self.torneo_frame, orient='horizontal').pack(fill=tk.X, pady=15)
        
        # Ganador
        self.ganador_frame = ttk.Frame(self.torneo_frame)
        self.ganador_frame.pack()
        
        ttk.Label(self.ganador_frame, 
                 text="Ganador:", 
                 style='Participante.TLabel').pack(side=tk.LEFT)
        
        self.ganador_label = ttk.Label(self.ganador_frame, 
                                     text="", 
                                     style='Ganador.TLabel')
        self.ganador_label.pack(side=tk.LEFT, padx=10)
        
        # Botón siguiente
        self.next_button = ttk.Button(self.torneo_frame, 
                                    text="▶️ Siguiente Torneo", 
                                    command=self.siguiente_torneo, 
                                    state=tk.DISABLED)
        self.next_button.pack(pady=15)
        
        # Panel de resultados
        self.resultados_frame = ttk.LabelFrame(main_frame, text="📊 Resultados", padding=15)
        self.resultados_frame.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=5, pady=5, ipadx=10, ipady=5)
        
        # Añadir scrollbar
        scrollbar = ttk.Scrollbar(self.resultados_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.resultados_text = tk.Text(self.resultados_frame, 
                                     height=8, 
                                     wrap=tk.WORD,
                                     font=('Helvetica', 10),
                                     yscrollcommand=scrollbar.set)
        self.resultados_text.pack(fill=tk.BOTH, expand=True)
        
        scrollbar.config(command=self.resultados_text.yview)
        
        # Configurar tags para colores en el texto
        self.resultados_text.tag_config('ganador', foreground=self.colores['ganador'])
        self.resultados_text.tag_config('perdedor', foreground=self.colores['perdedor'])
        self.resultados_text.tag_config('titulo', font=('Helvetica', 11, 'bold'))
        
        self.resultados_text.insert(tk.END, "Resultados de los torneos:\n", 'titulo')
        self.resultados_text.config(state=tk.DISABLED)
        
        # Configurar pesos de filas/columnas
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(3, weight=1)
    
    def iniciar_torneos(self):
        """Inicia el proceso de torneos"""
        self.ganadores = []
        self.current_torneo = 0
        self.resultados_text.config(state=tk.NORMAL)
        self.resultados_text.delete(1.0, tk.END)
        self.resultados_text.insert(tk.END, "⚡ Iniciando torneos...\n\n", 'titulo')
        self.resultados_text.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)
        self.siguiente_torneo()
    
    def siguiente_torneo(self):
        """Realiza el siguiente torneo"""
        if self.current_torneo >= self.num_torneos.get():
            messagebox.showinfo("🏁 Fin del Torneo", "¡Todos los torneos han sido completados!")
            self.next_button.config(state=tk.DISABLED)
            return
        
        self.current_torneo += 1
        self.torneo_label.config(text=f"Torneo {self.current_torneo} de {self.num_torneos.get()}")
        
        # Seleccionar dos individuos aleatorios
        participantes = random.sample(list(self.individuos.items()), 2)
        ind1, fit1 = participantes[0]
        ind2, fit2 = participantes[1]
        
        # Mostrar participantes
        self.part1_label.config(text=f"Individuo {ind1}\nFitness: {fit1}")
        self.part2_label.config(text=f"Individuo {ind2}\nFitness: {fit2}")
        self.vs_label.config(text="VS")
        
        # Determinar ganador
        if fit1 > fit2:
            ganador = ind1
            perdedor = ind2
        elif fit2 > fit1:
            ganador = ind2
            perdedor = ind1
        else:
            ganador = random.choice([ind1, ind2])
            perdedor = ind1 if ganador == ind2 else ind2
        
        # Resaltar ganador y perdedor
        self.part1_label.config(style='Ganador.TLabel' if ganador == ind1 else 'Perdedor.TLabel')
        self.part2_label.config(style='Ganador.TLabel' if ganador == ind2 else 'Perdedor.TLabel')
        
        self.ganadores.append(ganador)
        self.ganador_label.config(text=f"{ganador}")
        
        # Actualizar resultados
        self.resultados_text.config(state=tk.NORMAL)
        
        self.resultados_text.insert(tk.END, f"Torneo {self.current_torneo}:\n")
        self.resultados_text.insert(tk.END, f"  {ind1}({fit1}) vs {ind2}({fit2}) → ", 'titulo')
        self.resultados_text.insert(tk.END, f"Ganador: {ganador}\n\n", 'ganador')
        
        self.resultados_text.see(tk.END)
        self.resultados_text.config(state=tk.DISABLED)
        
        # Deshabilitar botón si es el último torneo
        if self.current_torneo == self.num_torneos.get():
            self.next_button.config(state=tk.DISABLED)
            self.resultados_text.config(state=tk.NORMAL)
            self.resultados_text.insert(tk.END, "✨ Proceso completado!\n", 'titulo')
            self.resultados_text.insert(tk.END, f"🏆 Ganadores finales: {', '.join(self.ganadores)}\n", 'ganador')
            self.resultados_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = TorneoApp(root)
    root.mainloop()