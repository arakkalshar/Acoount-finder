import os
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseConnectionParams

MCP_SERVER_URL = os.getenv(
    "MCP_SERVER_URL",
    "https://acc-mcp-664441136314.us-east1.run.app/sse"
)

career_specialist = LlmAgent(
    name="career_specialist",
    model="gemini-2.0-flash",
    description="Worker agent — fetches jobs and manages the internship pipeline",
    instruction="""
You are the Career Specialist with access to these tools:
- fetch_jobs_tool: find internships by role, location, or keyword
- save_job_tool: save a job by job ID
- update_status_tool: update status (saved, applied, interviewing, offered, rejected)
- list_pipeline_tool: show all saved jobs and statuses
Always use tools. Never make up data. Show company, title, location, and job ID clearly.
""",
    tools=[
        MCPToolset(
            connection_params=SseConnectionParams(url=MCP_SERVER_URL)
        )
    ],
)

root_agent = LlmAgent(
    name="supervisor",
    model="gemini-2.0-flash",
    description="Lead Orchestrator — user-facing career coach",
    instruction="""
You are the Agentic Career Coach helping users manage their internship search.
For ANY job search, saving, status update, or pipeline summary — delegate to career_specialist.
Never answer job questions yourself. Return the specialist response to the user.
""",
    tools=[AgentTool(agent=career_specialist)],
)
