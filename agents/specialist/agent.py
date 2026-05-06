import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseServerParams

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
    toolsets=[
        MCPToolset(connection_params=SseServerParams(url=MCP_SERVER_URL))
    ],
)
