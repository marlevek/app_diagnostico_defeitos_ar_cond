import sqlite3

# Função para criar o banco de dados e a tabela
def criar_banco():
    conn = sqlite3.connect('diagnosticos.db')
    cursor = conn.cursor()
    
    # Remover a tabela existente
    cursor.execute('''DROP TABLE IF EXISTS diagnosticos''')
    
    # Criar a tabela se não existir
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS diagnosticos(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       problema TEXT,
                       "possiveis_causas" TEXT,
                       teste TEXT
                   )
                   
                   ''')
    
    # Inserir múltiplas causas para o mesmo problema
    cursor.executemany(''' 
                   INSERT INTO diagnosticos (problema, "possiveis_causas", teste)
                   VALUES (?, ?, ?)
                   ''', [
        ('compressor não liga', 'Falta de gás refrigerante', 'Verifique a pressão do gás refrigerante.'),
        ('compressor não liga', 'Excesso de gás refrigerante', 'Verifique a pressão do gás refrigerante.'),
        ('compressor não liga', 'Baixa ou alta tensão da rede elétrica', 'Verifique a tensão'),
        ('compressor não liga', 'Compressor travado ou trancado', 'Verifique se está chegando energia no compressor.'),
        ('compressor não liga', 'Ligação elétrica incorreta ou fios rompidos', 'Verifique a fiação. Teste a continuidadee dos fios.'),
        ('compressor não liga', 'Módulo IPM com defeito', 'Verifique a resistência e a continuidade dos componentes.'),
        
        ('Ventiladores não funcionam', 'Cabo elétrico desconectado ou com mau contato', 'Verifique o cabo elétrico'),
        ('Ventiladores não funcionam', 'Motor do ventilador defeituoso', 'Faça a ligação direta do ventilador, se não funcionar troque o mesmo'),
        ('Ventiladores não funcionam', 'Capacitor defeituoso', 'Verifique o capacitor'),
        ('Ventiladores não funcionam', 'Placa de comando com defeito', 'Verifique a placa'),
        ('Ventiladores não funcionam', 'Hélice ou turbina solta ou travada', 'Verifique e fixe-a corretamente'),
        ('Ventiladores não funcionam', 'Ligação elétrica incorreta ou fios rompidos', 'Verifique a fiação. Teste a continuidadee dos fios.'),
        
        ('Ar não gela', 'Cabo PP interrompido', 'Teste a ligação'),
        ('Ar não gela', 'Compressor travado', 'Teste o compressor'),
        ('Ar não gela', 'Compressor não comprime', 'Teste o compressor'),
        ('Ar não gela', 'Falta de gás', 'Verifique a pressão e se há vazamento'),
        ('Ar não gela', 'Filtros de ar entupidos', 'Verifique os filtros'),
        
        ('Compressor não funciona em aquecimento', 'Solenóide da válvula reversora com defeito', 'Teste a solenóide da válvula'),
        ('Compressor não funciona em aquecimento', 'Válvula reversora defeituosa ou travada', 'Teste a válvula'),
        ('Compressor não funciona em aquecimento', 'Termostato/sensor de degelo aberto', 'Verifique o sensor'),
        ('Compressor não funciona em aquecimento', 'Placa interna ou externa com defeito', 'Verifique a placa'),
        
        ('Evaporador bloqueado com gelo', 'Obstrução do tubo capilar ou no filtro secador', 'Limpar os componentes com nitrogênio ou substitua os componentes.'),
        ('Evaporador bloqueado com gelo', 'Vazamento de gás', 'Verifique a pressão do sistema e se há vazamentos.'),
        ('Evaporador bloqueado com gelo', 'Pouco fluxo de ar', 'Verifique: se a turbina está lenta; se o evaporador e os filtros estão muito sujos.'),
        ('Evaporador bloqueado com gelo', 'Condensadora ligada direto', 'Verifique se o relé da placa do evaporador está travado (através de continuidade)'),
        
        ('Compressor fica pouco tempo ligado', 'Obstrução da descarga de ar', 'Desobstrua a descarga de ar da unidade'),
        ('Compressor fica pouco tempo ligado', 'Compressor com defeito', 'Teste o compressor'),
        ('Compressor fica pouco tempo ligado', 'Dispositivo de expansão com gelo ou obstruído', 'Remova a carga de gás, passe nitrogênio ou substitua a peça'),
        ('Compressor fica pouco tempo ligado', 'Danos na válvula reversora ou válvula travda', 'Verifique a válvula.'),
        
        ('Compressor não desliga', 'Ajuste no controle muito alto (aquecimento) ou muito baixo (resfriamento)', 'Modifique o ajuste no controle remoto'),
        ('Compressor não desliga', 'Ventilador defeituoso ou não funciona', 'Verifique a circulação de ar na condensadora e teste o ventilador'),
        ('Compressor não desliga', 'Carga insuficiente de gás', 'Verificar vazamentos de gás'),
        ('Compressor não desliga', 'Aparelho subdimensionado', 'Calcule a carga térmica do ambiente.'),
        
        ('Ar condicionado não desliga', 'Carga de gás deficiente', 'Verifique a pressão e se há vazamentos.'),
        ('Ar condicionado não desliga', 'Evaporador bloqueado/sujo', 'Verifique se há obsturção no evaporador'),
        ('Ar condicionado não desliga', 'Condensador bloqueado/sujo', 'Verifique o condensador'),
        ('Ar condicionado não desliga', 'Sensor ambiente com defeito', 'Teste o sensor'),
        
        ('Linha de sucção congelando', 'Excesso de gás', 'Verifique a pressão'),
        ('Linha de sucção congelando', 'Válvula de expansão/tubo capilar com defeito', 'Teste o dispositivo de expansão'),
        ('Linha de sucção congelando', 'Evaporador bloqueado/sujo', 'Verifique o estado do evaporador'),
        ('Linha de sucção congelando', 'Ventilador do evaporador com defeito', 'Tete o ventilador.'),  
        
        ('Linha de líquido congelando', 'Falta de gás', 'Verifique a pressão e se há vazamentos.'),
        ('Linha de líquido congelando', 'Obstrução na linha de líquido', 'Limpar o tubo capilar com nitrogênio ou substituir a peça.'),
        ('Linha de líquido congelando', 'Defeito no condensador', 'Verifique o funcionamento do condensador'),
        ('Linha de líquido congelando', 'Falha no dispositivo de expansão', 'Verifique o dispositivo, troque se necessário.'),

])
    
    # Confirmar as mudanças
    conn.commit()
    conn.close()
    
    print('Banco de dados criado e dados inseridos com sucesso')
    

# Executar a função para criar o banco de dados e inserir as causas
if __name__ == "__main__":
    criar_banco()
