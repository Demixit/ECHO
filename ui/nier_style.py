"""
Nier Automata themed UI components
"""
import tkinter as tk
from tkinter import ttk


class NierStyle:
    """Styling class for Nier Automata themed interface"""
    
    # Nier Automata color palette
    COLORS = {
        'background': '#1a1a1a',      # Dark background
        'panel': '#2d2d2d',           # Panel background
        'accent': '#d70022',          # Red accent (Nier's signature)
        'text_primary': '#ffffff',    # White text
        'text_secondary': '#b0b0b0',  # Gray text
        'input_field': '#3a3a3a',     # Input field
    }
    
    @staticmethod
    def configure_theme(root):
        """Configure the Nier Automata theme for tkinter application"""
        style = ttk.Style()
        
        # Configure colors
        root.configure(bg=NierStyle.COLORS['background'])
        
        # Configure style for various widgets
        style.configure('TFrame', background=NierStyle.COLORS['background'])
        style.configure('TLabel', 
                       background=NierStyle.COLORS['background'],
                       foreground=NierStyle.COLORS['text_primary'])
        style.configure('TButton',
                       background=NierStyle.COLORS['accent'],
                       foreground=NierStyle.COLORS['text_primary'],
                       borderwidth=0)
        style.map('TButton',
                 background=[('active', '#ff0033')],
                 foreground=[('active', '#ffffff')])
        
        style.configure('TEntry',
                       fieldbackground=NierStyle.COLORS['input_field'],
                       foreground=NierStyle.COLORS['text_primary'],
                       borderwidth=1,
                       relief='flat')
        
        return style


class NierMainWindow:
    """Main window with Nier Automata styling"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("E76 - AI Companion")
        self.root.geometry("800x600")
        self.style = NierStyle.configure_theme(self.root)
        
        # Set window icon if available
        # self.root.iconbitmap('assets/icon.ico')  # Optional
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface elements"""
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = ttk.Label(main_frame, text="E76 - AI Companion", font=("Arial", 24, "bold"))
        title_label.pack(pady=(0, 20))
        
        # Model selection area
        model_frame = ttk.Frame(main_frame)
        model_frame.pack(fill=tk.X, pady=10)
        
        model_label = ttk.Label(model_frame, text="Select AI Model:", font=("Arial", 12))
        model_label.pack(anchor=tk.W)
        
        self.model_var = tk.StringVar()
        self.model_dropdown = ttk.Combobox(model_frame, textvariable=self.model_var, state="readonly")
        self.model_dropdown.pack(fill=tk.X, pady=5)
        
        # Chat display area
        chat_frame = ttk.Frame(main_frame)
        chat_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Chat history
        self.chat_history = tk.Text(chat_frame, 
                                   bg=NierStyle.COLORS['panel'], 
                                   fg=NierStyle.COLORS['text_primary'],
                                   wrap=tk.WORD,
                                   state=tk.DISABLED)
        self.chat_history.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
        
        # Scrollbar for chat
        scrollbar = ttk.Scrollbar(chat_frame, command=self.chat_history.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_history.config(yscrollcommand=scrollbar.set)
        
        # Input area
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=10)
        
        self.user_input = ttk.Entry(input_frame, font=("Arial", 12))
        self.user_input.pack(fill=tk.X, side=tk.LEFT, expand=True, padx=(0, 10))
        self.user_input.bind("<Return>", self.send_message)
        
        send_button = ttk.Button(input_frame, text="Send", command=self.send_message)
        send_button.pack(side=tk.RIGHT)
    
    def send_message(self, event=None):
        """Handle sending a message"""
        message = self.user_input.get()
        if message.strip():
            self.add_message_to_chat("You: " + message)
            self.user_input.delete(0, tk.END)
            # Here would be the logic to get AI response
    
    def add_message_to_chat(self, message):
        """Add a message to the chat history"""
        self.chat_history.config(state=tk.NORMAL)
        self.chat_history.insert(tk.END, message + "\n")
        self.chat_history.see(tk.END)
        self.chat_history.config(state=tk.DISABLED)
    
    def run(self):
        """Start the main loop"""
        self.root.mainloop()