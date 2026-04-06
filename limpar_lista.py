import re

def limpar():
    try:
        # Lê a lista original
        with open('lista_pihole.txt', 'r', encoding='utf-8') as f_in:
            linhas = f_in.readlines()
        
        dominios = set()
        for linha in linhas:
            # Limpa o protocolo, o www e parâmetros de URL
            limpo = re.sub(r'^(0\.0\.0\.0\s+)?(https?://)?(www\.)?', '', linha.strip())
            dominio = limpo.split('/')[0].split('?')[0].lower()
            
            # Valida se parece um domínio
            if '.' in dominio and len(dominio) > 3:
                dominios.add(dominio)

        # Salva a lista limpa e organizada
        with open('lista_limpa.txt', 'w', encoding='utf-8') as f_out:
            for d in sorted(dominios):
                f_out.write(f"0.0.0.0 {d}\n")
        print("Sucesso: lista_limpa.txt gerada.")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    limpar()
