import subprocess, os, sys
sys.stdout.reconfigure(encoding='utf-8')

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
provas_dir = r"C:\Users\Ruan Gomes\Downloads\Meruoca\provas"

conversoes = [
    ('PROVA_REAL_INBRASP_2026_IPAPORANGA.html', 'PROVA_REAL_INBRASP_2026_IPAPORANGA.pdf'),
    ('PROVA_OFICIAL_SIMULADO_01_INBRASP.html', 'SIMULADO_01_CAMARA_MERUOCA.pdf'),
    ('CADERNO_ESSENCIAL_OURO_89Q.html', 'CADERNO_ESSENCIAL_OURO_89Q.pdf'),
    ('CADERNO_PROVAO_RESGATE_137Q.html', 'CADERNO_PROVAO_RESGATE_137Q.pdf'),
    ('CADERNO_QUESTOES_SEMANA_05_DIA_01_28_09_2026.html', 'CADERNO_HOJE_SEMANA_05_DIA_01.pdf'),
    ('CADERNO_REFORCO_PORTUGUES_SINTAXE_PERIODO_40Q.html', 'CADERNO_REFORCO_PORTUGUES_40Q.pdf'),
    ('PROVA_02_CAMARA_PIRES_FERREIRA_INBRASP.html', 'SIMULADO_02_CAMARA_PIRES_FERREIRA.pdf'),
    ('PROVA_03_CAMARA_IPAPORANGA_INBRASP.html', 'SIMULADO_03_CAMARA_IPAPORANGA.pdf'),
    ('PROVA_04_CAMARA_HIDROLANDIA_INBRASP.html', 'SIMULADO_04_CAMARA_HIDROLANDIA.pdf'),
    ('PROVA_05_CAMARA_PEDRA_BRANCA_INBRASP.html', 'SIMULADO_05_CAMARA_PEDRA_BRANCA.pdf')
]

for src, dst in conversoes:
    src_file = os.path.join(provas_dir, src)
    dst_file = os.path.join(provas_dir, dst)
    if os.path.exists(src_file):
        normalized_url = "file:///" + src_file.replace("\\", "/")
        cmd = [
            edge_path,
            "--headless=new",
            "--disable-gpu",
            "--run-all-compositor-stages-before-draw",
            f"--print-to-pdf={dst_file}",
            normalized_url
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if os.path.exists(dst_file):
            size_kb = os.path.getsize(dst_file) / 1024
            print(f"[OK] {dst} ({size_kb:.1f} KB)")
        else:
            print(f"[FALHA] {dst}")

print("\nTodas as conversões para PDF concluídas com sucesso!")
