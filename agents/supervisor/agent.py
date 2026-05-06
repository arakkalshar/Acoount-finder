from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from agents.specialist.agent import career_specialist

supervisor = LlmAgent(
    name="supervisor",
    model="gemini-2.0-flash",
    description="Lead Orchestrator — user-facing career coach",
    instruction="""
You are the Agentic Career Coach helping users manage their internship search.
For ANY job search, saving, status update, or pipeline summary task — always delegate to career_specialist.
Never answer job questions yourself. Hand off to career_specialist and return its response.
For greetings or unrelated questions, answer directly.
""",
    tools=[AgentTool(agent=career_specialist)],
)

root_agent = supervisor
