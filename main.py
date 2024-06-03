from image import Imagem

class ExploradorIlhasInterativo:
    def __init__(self, transicoes, dicas, caminho_correto):
        self.transicoes = transicoes
        self.dicas = dicas
        self.caminho_correto = caminho_correto
        self.caminho_atual = []
        self.senha_atual = ""
        self.caminho_correto_digito = ['A', 'B', 'A']
        self.senha_correta = "123"

    def mostrar_senha_atual(self, etapa, escolha_certa):
        # Gera um dígito para a senha
        parte_senha = self.senha_correta[etapa] if escolha_certa else str((int(self.senha_correta[etapa]) + 5) % 10)
        self.senha_atual += parte_senha
        print(f"\n🔑 Você encontrou um dígito da senha: {parte_senha}\n")

    def explorar_ilhas(self):
        ilha_atual = "Ilha dos Piratas"
        etapa = 0

        while True:
            print(f"🌴 Você está na {ilha_atual}. \n\n Dica para a próxima ilha: {self.dicas.get(ilha_atual, 'Exploração é a chave!')}")
            print("\n\nOpções de navegação:")
            for navio, destino in self.transicoes.get(ilha_atual, {}).items():
                print(f"  Navio {navio}: para {destino}")
            escolha = input("\nEscolha o navio (A/B): ").strip().upper()


            if escolha not in self.transicoes.get(ilha_atual, {}):
                print("\n⚠️ Opção inválida. Vamos tentar isso de novo.\n")
                continue

            if escolha not in self.caminho_correto_digito[etapa]:
                print("\n🔑 Você encontrou um dígito da senha: 2\n")
                self.senha_atual += "2"
            else:
                escolha_certa = escolha == self.caminho_correto[etapa] if etapa < len(self.caminho_correto) else False
                self.mostrar_senha_atual(etapa, escolha_certa)
            
            ilha_atual = self.transicoes[ilha_atual][escolha]
            self.caminho_atual.append(ilha_atual)
            etapa += 1

            if etapa >= len(self.senha_correta):
                print(f"\n🏴‍☠️ Bem-vindo à Ilha do Tesouro!\n")
                break

        print(f"Senha coletada: {self.senha_atual}")
        senha_usuario = input("Digite a senha para desbloquear o tesouro: ")
        if senha_usuario == self.senha_atual and self.caminho_atual == self.caminho_correto:
            print("\n🎉 Parabéns, você desbloqueou o tesouro e venceu o jogo!\n")
            Imagem().inicial()
        else:
            print("\n❌ A senha está incorreta. Parece que você seguiu o caminho errado em algum momento.\n")



if __name__ == "__main__":
    transicoes = {
        "Ilha dos Piratas": {"A": "Ilha Misteriosa", "B": "Ilha do Vulcão"},
        "Ilha Misteriosa": {"A": "Ilha das Sombras", "B": "Ilha Encantada"},
        "Ilha do Vulcão": {"A": "Ilha das Sombras", "B": "Ilha Encantada"},
        "Ilha das Sombras": {"A": "Ilha do Tesouro"},
        "Ilha Encantada": {"A": "Ilha do Tesouro"},
    }

    dicas = {
        "Ilha dos Piratas": "Uma névoa densa esconde segredos antigos e tesouros esquecidos.",
        "Ilha Misteriosa": "Este lugar mágico é conhecido por sua beleza encantadora.",
        "Ilha do Vulcão": "Este lugar mágico é conhecido por sua beleza encantadora.",
        "Ilha Encantada": "Você está quase lá! O tesouro está muito perto.",
        "Ilha das Sombras": "Você está quase lá! O tesouro está muito perto.",
    }

    caminho_correto = ['Ilha Misteriosa', 'Ilha Encantada', 'Ilha do Tesouro']

    explorador = ExploradorIlhasInterativo(transicoes, dicas, caminho_correto)
    explorador.explorar_ilhas()
