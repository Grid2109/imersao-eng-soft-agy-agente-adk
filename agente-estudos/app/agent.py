import os
import pathlib
from datetime import date, timedelta
from dotenv import load_dotenv
from google.adk import Agent
from google.adk.agents.readonly_context import ReadonlyContext
from google.adk.environment import LocalEnvironment
from google.adk.skills import load_skill_from_dir
from google.adk.tools.environment import EnvironmentToolset
from google.adk.tools.skill_toolset import SkillToolset

# Caminhos base calculados a partir de agent.py
APP_DIR = pathlib.Path(__file__).parent
BASE_DIR = APP_DIR.parent
PLANOS_DIR = (BASE_DIR / "planos").resolve()
PLANOS_DIR.mkdir(parents=True, exist_ok=True)

SKILL_PLANO_DIR = (APP_DIR / "skills" / "plano-de-estudos").resolve()
SKILL_REVISAO_DIR = (APP_DIR / "skills" / "revisao-ativa").resolve()

# Carrega variáveis de ambiente do .env
load_dotenv(BASE_DIR / ".env")
load_dotenv(BASE_DIR.parent / ".env")


class FerramentasDeArquivo(EnvironmentToolset):
    """Subclasse do EnvironmentToolset restrita às ferramentas ReadFile e WriteFile."""

    async def get_tools(self, readonly_context=None):
        tools = await super().get_tools(readonly_context)
        return [t for t in tools if t.name in ("ReadFile", "WriteFile")]


# Carrega as skills do ADK
skill_plano = load_skill_from_dir(SKILL_PLANO_DIR)
skill_revisao = load_skill_from_dir(SKILL_REVISAO_DIR)
skill_toolset = SkillToolset(skills=[skill_plano, skill_revisao])

# Configura o ambiente local apontando para a pasta planos/
file_toolset = FerramentasDeArquivo(
    environment=LocalEnvironment(working_dir=PLANOS_DIR)
)

DIAS_SEMANA = [
    "segunda-feira",
    "terça-feira",
    "quarta-feira",
    "quinta-feira",
    "sexta-feira",
    "sábado",
    "domingo",
]


def instrucao_agente(context: ReadonlyContext) -> str:
    """Instruction provider dinâmico que injeta a data de hoje, calendário e orientações das skills."""
    hoje = date.today()
    dia_semana = DIAS_SEMANA[hoje.weekday()]
    data_formatada = hoje.strftime("%d/%m/%Y")

    # Próximas datas de referência para evitar erros de cálculo de dias de semana
    proximos_dias = []
    for i in range(1, 8):
        d = hoje + timedelta(days=i)
        proximos_dias.append(
            f"  - Próxima {DIAS_SEMANA[d.weekday()]}: {d.strftime('%d/%m/%Y')} (formato CSV: {d.strftime('%m/%d/%Y')})"
        )
    referencias_datas = "\n".join(proximos_dias)

    return (
        f"Hoje é {dia_semana}, {data_formatada} ({hoje.isoformat()}).\n"
        f"Próximos dias de referência para cálculo de início:\n{referencias_datas}\n\n"
        "Você é um mentor especialista em estudos. Você ajuda os estudantes a montar planos de "
        "estudos personalizados, cronogramas executáveis e materiais de recuperação ativa (flashcards e quizzes).\n\n"
        "REGRAS FUNDAMENTAIS:\n"
        "1. Skills disponíveis:\n"
        "   - Use `plano-de-estudos` quando a pessoa quiser organizar estudos, montar ou replanejar cronogramas e gerar agenda CSV.\n"
        "   - Use `revisao-ativa` quando a pessoa fornecer anotações, resumo, código ou assunto para criar flashcards e um quiz de 5 perguntas.\n"
        "2. Regras de Gating: siga rigorosamente a regra de ativação de cada skill antes de carregar recursos L3 com `load_skill_resource`. "
        "Se faltar informação essencial, faça uma única mensagem objetiva pedindo apenas o que falta.\n"
        "3. Respeito aos dias da semana no plano de estudos: calcule cada data com precisão. Se o usuário puder estudar em dias específicos "
        "(ex: segunda, quarta e sexta), TODAS as sessões agendadas devem cair EXATAMENTE nesses dias da semana, sem exceção.\n"
        "4. Gravação da agenda (CSV) com a ferramenta `WriteFile` em `plano-de-estudos.csv`:\n"
        "   - Cabeçalho exato: Subject,Start Date,Start Time,End Date,End Time,Description\n"
        "   - Cada linha DEVE conter obrigatoriamente as 6 colunas, nem mais, nem menos.\n"
        "   - REGRA DAS VÍRGULAS NO SUBJECT: NUNCA coloque vírgulas desprotegidas no Subject. Se o Subject contiver qualquer vírgula, ele DEVE estar entre aspas duplas (exemplo: \"📚 JS: Variáveis, Tipos e Operadores\",11/16/2026,...). Para simplificar e evitar erros de coluna, prefira usar hífens ou a palavra 'e' em vez de vírgula no Subject.\n"
        "   - NUNCA omita a coluna End Date! Para sessões que ocorrem no mesmo dia, o End Date é idêntico ao Start Date.\n"
        "   - Datas no formato MM/DD/YYYY e horários em HH:MM AM/PM\n"
        "   - A Description DEVE sempre estar entre aspas duplas: \"Revisão: ... | Técnica: ... | Entregável: ...\"\n"
        "   - Se o plano tiver mais de 14 dias de estudo, inclua no CSV apenas os primeiros 14 dias (Passo 5 do workflow)\n"
        "   - Sempre termine o conteúdo do CSV com uma quebra de linha final (\\n)\n"
        "5. Replanejamento:\n"
        "   - Se o estudante informar sessões perdidas/atrasos, NUNCA empilhe em um único dia e NUNCA estenda o prazo final "
        "se houver dias de margem disponíveis. Utilize os dias de margem (🛟 Margem) para absorver o atraso e manter a data de conclusão.\n"
        "   - Sobrescreva o arquivo `plano-de-estudos.csv` com a versão corrigida."
    )


# Obtém o modelo a partir da variável de ambiente MODEL (padrão: gemini-2.5-flash)
MODEL_NAME = os.getenv("MODEL", "gemini-2.5-flash")

root_agent = Agent(
    name="agente_estudos",
    model=MODEL_NAME,
    instruction=instrucao_agente,
    tools=[skill_toolset, file_toolset],
)
