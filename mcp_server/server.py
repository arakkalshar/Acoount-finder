import os
import logging
from fastmcp import FastMCP
from mcp_server.tools.fetch_jobs import fetch_jobs
from mcp_server.tools.sync_pipeline import save_job, update_status, list_pipeline

logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))
log = logging.getLogger("acc-mcp")

mcp = FastMCP("acc-mcp")

@mcp.tool()
def fetch_jobs_tool(role: str = "", location: str = "", keyword: str = "") -> list:
    """Return internship listings filtered by role, location, or keyword."""
    log.info(f"fetch_jobs role={role!r} location={location!r} keyword={keyword!r}")
    return fetch_jobs(role=role, location=location, keyword=keyword)

@mcp.tool()
def save_job_tool(job_id: str) -> dict:
    """Save a job to the internship pipeline by job ID."""
    log.info(f"save_job {job_id!r}")
    return save_job(job_id)

@mcp.tool()
def update_status_tool(job_id: str, status: str) -> dict:
    """Update the application status of a saved job."""
    log.info(f"update_status {job_id!r} {status!r}")
    return update_status(job_id, status)

@mcp.tool()
def list_pipeline_tool() -> list:
    """List all jobs in the internship pipeline."""
    log.info("list_pipeline called")
    return list_pipeline()

if __name__ == "__main__":
    log.info("Starting ACC MCP server")
    mcp.run(transport="sse")
