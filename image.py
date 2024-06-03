import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Definindo as localizações das ilhas
class Imagem:
    def inicial(self):
        ilhas = {
            "Ilha dos Piratas": (1, 1),
            "Ilha Misteriosa": (2, 2),
            "Ilha do Vulcão": (3, 1),
            "Ilha das Sombras": (4, 2),
            "Ilha Encantada": (5, 1),
            "Ilha Perdida": (6, 1.5),
            "Ilha do Tesouro": (7, 2)
        }

        caminhos = [
            ("Ilha dos Piratas", "Ilha Misteriosa", 'A'),
            ("Ilha Misteriosa", "Ilha das Sombras", 'A'),
            ("Ilha Perdida", "Ilha do Tesouro", 'A'),
            ("Ilha das Sombras", "Ilha do Tesouro", 'A'),
            ("Ilha do Vulcão", "Ilha Perdida", 'A'),
            ("Ilha Encantada", "Ilha do Tesouro", 'A'),
            ("Ilha dos Piratas", "Ilha do Vulcão", 'B'),
            ("Ilha do Vulcão", "Ilha Encantada", 'B'),
            ("Ilha Misteriosa", "Ilha Encantada", 'B'),
            ("Ilha Encantada", "Ilha Misteriosa", 'B'),
            ("Ilha Perdida", "Ilha do Vulcão", 'B'),
            ("Ilha das Sombras", "Ilha dos Piratas", 'B'),
            
        ]

        fig, ax = plt.subplots()

        # Desenhando as ilhas
        for ilha, (x, y) in ilhas.items():
            ax.plot(x, y, 'o', label=ilha)
            ax.text(x, y+0.1, ilha, ha='center')

            # Definindo o caminho correto para ser destacado
            caminho_correto = [
                ("Ilha dos Piratas", "Ilha Misteriosa", 'A'),
                ("Ilha Misteriosa", "Ilha Encantada", 'B'),
                ("Ilha Encantada", "Ilha do Tesouro", 'A'),
            ]

        # Desenhando todos os caminhos de forma mais sutil
        for origem, destino, escolha in caminhos:
            x_origem, y_origem = ilhas[origem]
            x_destino, y_destino = ilhas[destino]
            ax.annotate("", xy=(x_destino, y_destino), xycoords='data',
                        xytext=(x_origem, y_origem), textcoords='data',
                        arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="lightgrey"))

        # Destacando o caminho correto
        for origem, destino, escolha in caminho_correto:
            x_origem, y_origem = ilhas[origem]
            x_destino, y_destino = ilhas[destino]
            ax.annotate("", xy=(x_destino, y_destino), xycoords='data',
                        xytext=(x_origem, y_origem), textcoords='data',
                        arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="red"))
            meio_x = (x_origem + x_destino) / 2
            meio_y = (y_origem + y_destino) / 2
            ax.text(meio_x, meio_y, escolha, ha='right', color="red")

        # Configurando a visualização
        ax.set_xlim(0, 8)
        ax.set_ylim(0, 3)
        plt.legend()
        plt.show()
