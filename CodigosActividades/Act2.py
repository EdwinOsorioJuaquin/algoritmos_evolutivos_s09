import tkinter as tk
from tkinter import ttk, messagebox

class OXApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Algoritmo de Cruce OX")
        self.root.geometry("950x650")
        self.root.configure(bg='#f5f5f5')
        
        # Configurar paleta de colores
        self.colores = {
            'fondo': '#f5f5f5',
            'titulo': '#3f51b5',
            'subtitulo': '#2196f3',
            'padre1': '#4caf50',
            'padre2': '#ff5722',
            'hijo': '#9c27b0',
            'segmento': '#ffeb3b',
            'texto': '#212121',
            'borde': '#bdbdbd'
        }
        
        # Datos iniciales
        self.padre_1 = [1, 2, 3, 4, 5, 6, 7, 8]
        self.padre_2 = [8, 7, 6, 5, 4, 3, 2, 1]
        self.inicio_cruce = 3
        self.fin_cruce = 6
        
        # Configurar estilo
        self.setup_style()
        
        # Crear interfaz
        self.create_widgets()
        
        # Ejecutar cruce inicial
        self.ejecutar_cruce()
    
    def setup_style(self):
        """Configura los estilos visuales"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Estilos personalizados
        style.configure('Titulo.TLabel', 
                       font=('Roboto', 16, 'bold'),
                       foreground='white',
                       background=self.colores['titulo'],
                       padding=10)
        
        style.configure('Subtitulo.TLabel', 
                      font=('Roboto', 12, 'bold'),
                      foreground=self.colores['subtitulo'])
        
        style.configure('Gen.TLabel', 
                      font=('Roboto', 14, 'bold'),
                      padding=10,
                      relief='solid',
                      borderwidth=1)
        
        style.configure('GenPadre1.TLabel',
                      background='white',
                      foreground=self.colores['padre1'])
        
        style.configure('GenPadre2.TLabel',
                      background='white',
                      foreground=self.colores['padre2'])
        
        style.configure('GenHijo.TLabel',
                      background='white',
                      foreground=self.colores['hijo'])
        
        style.configure('Segmento.TLabel',
                      background=self.colores['segmento'],
                      font=('Roboto', 14, 'bold'))
        
        style.configure('TButton',
                      font=('Roboto', 10, 'bold'),
                      padding=6)
        
        style.map('TButton',
                 background=[('active', '#e0e0e0')])
    
    def create_widgets(self):
        """Crea todos los elementos de la interfaz"""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="15")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        ttk.Label(main_frame, 
                 text="Algoritmo de Cruce OX (Order Crossover)", 
                 style='Titulo.TLabel').grid(row=0, column=0, columnspan=3, sticky='ew', pady=(0, 15))
        
        # Panel de configuración
        config_frame = ttk.LabelFrame(main_frame, text="Configuración", padding=10)
        config_frame.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
        
        ttk.Label(config_frame, text="Padre 1:").grid(row=0, column=0, padx=5, pady=5)
        self.padre1_entry = ttk.Entry(config_frame, width=30)
        self.padre1_entry.grid(row=0, column=1, padx=5, pady=5)
        self.padre1_entry.insert(0, ",".join(map(str, self.padre_1)))
        
        ttk.Label(config_frame, text="Padre 2:").grid(row=1, column=0, padx=5, pady=5)
        self.padre2_entry = ttk.Entry(config_frame, width=30)
        self.padre2_entry.grid(row=1, column=1, padx=5, pady=5)
        self.padre2_entry.insert(0, ",".join(map(str, self.padre_2)))
        
        ttk.Label(config_frame, text="Inicio segmento:").grid(row=2, column=0, padx=5, pady=5)
        self.inicio_entry = ttk.Spinbox(config_frame, from_=0, to=len(self.padre_1)-1, width=5)
        self.inicio_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        self.inicio_entry.set(self.inicio_cruce)
        
        ttk.Label(config_frame, text="Fin segmento:").grid(row=3, column=0, padx=5, pady=5)
        self.fin_entry = ttk.Spinbox(config_frame, from_=1, to=len(self.padre_1), width=5)
        self.fin_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')
        self.fin_entry.set(self.fin_cruce)
        
        ttk.Button(config_frame, 
                  text="Ejecutar Cruce", 
                  command=self.ejecutar_cruce).grid(row=4, column=0, columnspan=2, pady=10)
        
        # Panel de visualización
        vis_frame = ttk.Frame(main_frame)
        vis_frame.grid(row=2, column=0, sticky='nsew', padx=5, pady=5)
        
        # Visualización del Padre 1
        ttk.Label(vis_frame, text="Padre 1", style='Subtitulo.TLabel').grid(row=0, column=0, pady=(0, 10))
        self.padre1_frame = ttk.Frame(vis_frame)
        self.padre1_frame.grid(row=1, column=0)
        
        # Visualización del Padre 2
        ttk.Label(vis_frame, text="Padre 2", style='Subtitulo.TLabel').grid(row=0, column=1, pady=(0, 10))
        self.padre2_frame = ttk.Frame(vis_frame)
        self.padre2_frame.grid(row=1, column=1)
        
        # Visualización del Hijo
        ttk.Label(vis_frame, text="Hijo", style='Subtitulo.TLabel').grid(row=0, column=2, pady=(0, 10))
        self.hijo_frame = ttk.Frame(vis_frame)
        self.hijo_frame.grid(row=1, column=2)
        
        # Panel de explicación
        expl_frame = ttk.LabelFrame(main_frame, text="Proceso de Cruce OX", padding=15)
        expl_frame.grid(row=1, column=1, rowspan=2, sticky='nsew', padx=5, pady=5)
        
        self.expl_text = tk.Text(expl_frame, wrap=tk.WORD, height=15, width=40,
                               font=('Roboto', 10), padx=10, pady=10)
        self.expl_text.pack(fill=tk.BOTH, expand=True)
        
        # Configurar scrollbar
        scrollbar = ttk.Scrollbar(expl_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.expl_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.expl_text.yview)
        
        # Configurar pesos de filas/columnas
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=2)
        main_frame.rowconfigure(2, weight=1)
    
    def ejecutar_cruce(self):
        """Ejecuta el algoritmo de cruce OX y actualiza la visualización"""
        try:
            # Obtener valores de entrada
            self.padre_1 = list(map(int, self.padre1_entry.get().split(',')))
            self.padre_2 = list(map(int, self.padre2_entry.get().split(',')))
            self.inicio_cruce = int(self.inicio_entry.get())
            self.fin_cruce = int(self.fin_entry.get())
            
            # Validar entradas
            if len(self.padre_1) != len(self.padre_2):
                raise ValueError("Los padres deben tener la misma longitud")
            
            if self.inicio_cruce >= self.fin_cruce:
                raise ValueError("El inicio del segmento debe ser menor que el fin")
            
            if self.fin_cruce > len(self.padre_1):
                raise ValueError("El fin del segmento excede la longitud de los padres")
            
            # Paso 1: Copiar el segmento del Padre 2 al Hijo 1
            hijo_1 = [-1] * len(self.padre_1)
            hijo_1[self.inicio_cruce:self.fin_cruce] = self.padre_2[self.inicio_cruce:self.fin_cruce]
            
            # Crear el mapeo entre los genes intercambiados
            mapeo = {}
            for i in range(self.inicio_cruce, self.fin_cruce):
                mapeo[self.padre_1[i]] = self.padre_2[i]
                mapeo[self.padre_2[i]] = self.padre_1[i]
            
            # Paso 2: Completar el resto del hijo con los genes del Padre 1
            for i in range(len(self.padre_1)):
                if self.inicio_cruce <= i < self.fin_cruce:
                    continue  # Saltar el segmento de cruce
                
                gen = self.padre_1[i]
                
                # Resolver conflictos
                while gen in hijo_1[self.inicio_cruce:self.fin_cruce]:
                    gen = mapeo[gen]
                
                hijo_1[i] = gen
            
            # Actualizar visualización
            self.actualizar_visualizacion(self.padre_1, self.padre_2, hijo_1)
            
            # Actualizar explicación
            self.actualizar_explicacion(hijo_1, mapeo)
            
        except Exception as e:
            messagebox.showerror("Error", f"Entrada inválida: {str(e)}")
    
    def actualizar_visualizacion(self, padre1, padre2, hijo):
        """Actualiza la visualización gráfica de los cromosomas"""
        # Limpiar frames anteriores
        for widget in self.padre1_frame.winfo_children():
            widget.destroy()
        
        for widget in self.padre2_frame.winfo_children():
            widget.destroy()
        
        for widget in self.hijo_frame.winfo_children():
            widget.destroy()
        
        # Mostrar Padre 1
        for i, gen in enumerate(padre1):
            style = 'Gen.TLabel'
            if self.inicio_cruce <= i < self.fin_cruce:
                style = 'Segmento.TLabel'
            
            lbl = ttk.Label(self.padre1_frame, text=str(gen), style=style)
            lbl.grid(row=0, column=i, padx=2)
        
        # Mostrar Padre 2
        for i, gen in enumerate(padre2):
            style = 'Gen.TLabel'
            if self.inicio_cruce <= i < self.fin_cruce:
                style = 'Segmento.TLabel'
            
            lbl = ttk.Label(self.padre2_frame, text=str(gen), style=style)
            lbl.grid(row=0, column=i, padx=2)
        
        # Mostrar Hijo
        for i, gen in enumerate(hijo):
            style = 'GenHijo.TLabel'
            if self.inicio_cruce <= i < self.fin_cruce:
                style = 'Segmento.TLabel'
            
            lbl = ttk.Label(self.hijo_frame, text=str(gen), style=style)
            lbl.grid(row=0, column=i, padx=2)
    
    def actualizar_explicacion(self, hijo, mapeo):
        """Actualiza el panel de explicación del proceso"""
        self.expl_text.config(state=tk.NORMAL)
        self.expl_text.delete(1.0, tk.END)
        
        # Paso 1
        self.expl_text.insert(tk.END, "Paso 1: Copiar segmento del Padre 2 al Hijo\n", 'bold')
        self.expl_text.insert(tk.END, 
                            f"Se copian los genes del Padre 2 en las posiciones {self.inicio_cruce} a {self.fin_cruce-1}:\n")
        self.expl_text.insert(tk.END, f"Segmento copiado: {self.padre_2[self.inicio_cruce:self.fin_cruce]}\n\n")
        
        # Mapeo
        self.expl_text.insert(tk.END, "Mapeo de genes intercambiados:\n", 'bold')
        for k, v in mapeo.items():
            self.expl_text.insert(tk.END, f"{k} ↔ {v}\n")
        self.expl_text.insert(tk.END, "\n")
        
        # Paso 2
        self.expl_text.insert(tk.END, "Paso 2: Completar con genes del Padre 1\n", 'bold')
        self.expl_text.insert(tk.END, "Para cada posición fuera del segmento:\n")
        self.expl_text.insert(tk.END, "1. Tomar el gen del Padre 1\n")
        self.expl_text.insert(tk.END, "2. Si el gen ya está en el segmento copiado, usar el mapeo\n")
        self.expl_text.insert(tk.END, "3. Repetir hasta encontrar un gen no presente\n\n")
        
        # Resultado final
        self.expl_text.insert(tk.END, "Resultado final del cruce OX:\n", 'bold')
        self.expl_text.insert(tk.END, f"{hijo}\n")
        
        # Configurar tags para formato
        self.expl_text.tag_config('bold', font=('Roboto', 10, 'bold'))
        
        self.expl_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = OXApp(root)
    root.mainloop()